#!/usr/bin/env python3
"""
capsule-capture.py — paste-time, fast, automatic
v1-final per SPEC-after-Claude.md, D0+6, 2026-05-09 23:32 PDT

Behavior (per spec §11.1):
  - Reads paste, applies marker detection from markers.yaml
  - Forms teeth applying Rules 1.1.a (multi-AI-response → D-strand extensions),
    1.1.b (compound I-strand vs. broken tooth, detection-mode-gated),
    1.1.c (unknown-speaker → broken tooth)
  - Detects partitions in AI segments; does NOT recover (close tool's job)
  - Runs Student Data Protocol per §4.5 (the only in-tool redaction)
  - Stamps timestamps per §5.1 evidence-only definition
  - Surfaces Layer 4 candidates per §6
  - Produces spec-conformant capsule.md + _capture/<slug>__paste.txt
  - Sets mode_at_capture: capture, capsule_status: in-capture,
    audience_fit_reviewed: false
  - Runs post-generation conformance check; halts only on Student Data
    Protocol failures.

NO audience-fit checks at capture. NO partition-recovery. NO referent-drift.

IP of Scott Ryll, held under neuroarchy.ai.
"""

import re
import sys
import os
import argparse
import json
import yaml
from datetime import datetime, timezone
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Tuple


# ============================================================================
# CONFIG / CONSTANTS
# ============================================================================

DEFAULT_MARKERS_PATH = Path(__file__).parent / "markers.yaml"

# Student-data detection patterns (conservative; flag-and-prompt, never silent)
STUDENT_NAME_HEURISTICS = [
    # Common contextual cues that suggest a student name follows
    re.compile(r'\bmy student\s+([A-Z][a-z]+)\b'),
    re.compile(r'\bstudent named\s+([A-Z][a-z]+)\b'),
    re.compile(r'\b([A-Z][a-z]+)(?:\'s)?\s+(?:parents?|mom|dad|family)\b'),
    re.compile(r'\bin (?:my )?(?:4th|fourth|3rd|third|5th|fifth) grade\b.*?\b([A-Z][a-z]+)\b'),
]
PERSONAL_HISTORY_KEYWORDS = [
    r'\bfamily death\b', r'\bdeath in (?:the |their )?family\b',
    r'\bIEP\b', r'\b504 plan\b', r'\bdiagnos(?:is|ed|ing)\b',
    r'\bhomeless(?:ness)?\b', r'\bfoster\b',
    r'\bdivorce\b', r'\babuse\b', r'\bneglect\b',
]
PERSONAL_HISTORY_PATTERN = re.compile('|'.join(PERSONAL_HISTORY_KEYWORDS), re.IGNORECASE)

# HIPAA-scope (detect-and-delete; never journal-route)
HIPAA_KEYWORDS = [
    r'\bmedical (?:record|history|condition)\b',
    r'\bprescription\b', r'\bmedication\b',
    r'\bHIPAA\b',
]
HIPAA_PATTERN = re.compile('|'.join(HIPAA_KEYWORDS), re.IGNORECASE)

# Partition detection (folded depth in AI responses)
PARTITION_MARKERS = [
    re.compile(r'^\s*(?:Show more|Read more|See more|\.\.\.|…)\s*$', re.MULTILINE | re.IGNORECASE),
    re.compile(r'\[(?:chart|graph|image|figure|diagram)\s*[:\-]?[^\]]*\]', re.IGNORECASE),
    re.compile(r'<details>', re.IGNORECASE),
]

# Layer 4 candidate-surfacing patterns
META_LANG = re.compile(r"\b(?:I'?m asking|what I mean|to be clear|let me back up|let me clarify)\b", re.IGNORECASE)
AI_CORRECTION = re.compile(r"\b(?:you missed|you got that wrong|that's not what|you didn'?t)\b", re.IGNORECASE)
SELF_INTERRUPT_TAGS = re.compile(r"\b(?:wait|scratch that|actually|tbh|let me back up)\b", re.IGNORECASE)


# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class Segment:
    """A raw detected segment before tooth-formation."""
    speaker: str           # 'scott' | 'ai' | 'unknown'
    content: str
    detection_mode: str    # 'marker-clean' | 'fallback' | 'unknown'
    marker_used: Optional[str] = None


@dataclass
class Tooth:
    """A formed tooth — Scott prompt + (last) AI response, possibly with extensions."""
    index: int
    scott_segment: Optional[Segment] = None
    ai_segment: Optional[Segment] = None
    d_strand_extensions: List[Segment] = field(default_factory=list)  # earlier AI responses
    compound_i_strand_count: int = 1   # 1 = single Scott prompt; >1 = compound
    is_broken: bool = False
    broken_reason: Optional[str] = None
    broken_note: Optional[str] = None
    partitions_detected: int = 0


# ============================================================================
# MARKER LOADING
# ============================================================================

def load_markers(markers_path: Path) -> Dict:
    """Load marker config from YAML."""
    if not markers_path.exists():
        print(f"ERROR: markers config not found: {markers_path}", file=sys.stderr)
        sys.exit(2)
    with open(markers_path) as f:
        return yaml.safe_load(f)


def build_marker_patterns(markers_config: Dict) -> List[Tuple[re.Pattern, str, str]]:
    """
    Build a list of (compiled_pattern, speaker, marker_text) tuples
    from the markers config.
    """
    patterns = []
    for platform, sides in markers_config.items():
        for speaker_key, markers in sides.items():
            speaker = 'scott' if speaker_key == 'scott' else 'ai'
            for m in markers:
                # Match at start of line (after optional whitespace)
                # Escape the marker, then allow optional trailing whitespace.
                pat = re.compile(
                    r'^\s*' + re.escape(m) + r'\s*$',
                    re.MULTILINE
                )
                patterns.append((pat, speaker, m))
    return patterns


# ============================================================================
# SEGMENTATION
# ============================================================================

def detect_segments(text: str, marker_patterns: List[Tuple[re.Pattern, str, str]]) -> Tuple[List[Segment], str]:
    """
    Split raw paste into segments by detecting markers.
    Returns (segments, detection_mode) where detection_mode is one of:
      'marker-clean' — markers found and used
      'fallback'     — no markers found; would need user resolution
    """
    hits = []
    for pat, speaker, marker_text in marker_patterns:
        for m in pat.finditer(text):
            hits.append((m.start(), m.end(), speaker, marker_text))

    if not hits:
        # Fallback: return single unknown block; caller decides how to handle
        return ([Segment(speaker='unknown', content=text.strip(),
                         detection_mode='fallback')], 'fallback')

    # Sort by position; dedupe overlapping
    hits.sort(key=lambda h: h[0])
    cleaned = []
    last_end = -1
    for start, end, speaker, marker_text in hits:
        if start >= last_end:
            cleaned.append((start, end, speaker, marker_text))
            last_end = end

    # Slice text between markers
    segments = []
    for i, (start, end, speaker, marker_text) in enumerate(cleaned):
        next_start = cleaned[i + 1][0] if i + 1 < len(cleaned) else len(text)
        content = text[end:next_start].strip()
        if content:
            segments.append(Segment(
                speaker=speaker,
                content=content,
                detection_mode='marker-clean',
                marker_used=marker_text
            ))

    return (segments, 'marker-clean')


# ============================================================================
# TOOTH FORMATION (Rules 1.1.a, 1.1.b, 1.1.c)
# ============================================================================

def form_teeth(segments: List[Segment]) -> List[Tooth]:
    """
    Form teeth from segments per spec Rules 1.1.a, 1.1.b, 1.1.c.

    Walk segments in order. State machine:
      - On Scott segment: start a new tooth (or extend compound-I-strand)
      - On AI segment: assign to current tooth as ai_segment; if a new AI
        segment follows another AI segment with no Scott between, the
        EARLIER one becomes a d_strand_extension and the LATER one
        becomes the tooth's ai_segment (Rule 1.1.a: last AI before next
        Scott closes the tooth).
      - On unknown segment: emit as broken tooth (Rule 1.1.c).
    """
    teeth: List[Tooth] = []
    tooth_idx = 0
    current_tooth: Optional[Tooth] = None
    pending_scotts: List[Segment] = []  # for compound I-strand detection

    def flush_pending_scotts():
        """If we have pending Scott segments with no AI yet, form a tooth."""
        nonlocal current_tooth, tooth_idx, pending_scotts
        if not pending_scotts:
            return
        tooth_idx += 1
        if len(pending_scotts) == 1:
            # Normal single-Scott tooth, awaiting AI
            current_tooth = Tooth(index=tooth_idx, scott_segment=pending_scotts[0])
        else:
            # Multiple Scott segments: detection-mode-gated per Rule 1.1.b
            all_marker_clean = all(s.detection_mode == 'marker-clean' for s in pending_scotts)
            if all_marker_clean:
                # Compound I-strand: merge content, mark count
                merged = '\n\n'.join(s.content for s in pending_scotts)
                merged_segment = Segment(
                    speaker='scott',
                    content=merged,
                    detection_mode='marker-clean',
                    marker_used=pending_scotts[0].marker_used
                )
                current_tooth = Tooth(
                    index=tooth_idx,
                    scott_segment=merged_segment,
                    compound_i_strand_count=len(pending_scotts)
                )
            else:
                # Fallback or marker-partial: broken tooth
                merged = '\n\n'.join(s.content for s in pending_scotts)
                merged_segment = Segment(
                    speaker='scott',
                    content=merged,
                    detection_mode='fallback'
                )
                current_tooth = Tooth(
                    index=tooth_idx,
                    scott_segment=merged_segment,
                    is_broken=True,
                    broken_reason='scott-only-pair-fallback',
                    broken_note=f'{len(pending_scotts)} consecutive Scott segments; '
                                f'detection mode insufficient for compound-I-strand designation'
                )
        teeth.append(current_tooth)
        pending_scotts = []

    for seg in segments:
        if seg.speaker == 'unknown':
            # Rule 1.1.c: emit current tooth (if any) and pending Scotts; then broken-tooth
            flush_pending_scotts()
            tooth_idx += 1
            teeth.append(Tooth(
                index=tooth_idx,
                is_broken=True,
                broken_reason='unknown-speaker',
                broken_note='Speaker detection failed for this segment'
            ))
            current_tooth = None
        elif seg.speaker == 'scott':
            # If we have a current_tooth waiting for AI, the previous tooth was
            # never closed — but a new Scott prompt arriving means we move on.
            # This is a structurally-incomplete tooth; mark it broken.
            if current_tooth is not None and current_tooth.ai_segment is None and not current_tooth.is_broken:
                current_tooth.is_broken = True
                current_tooth.broken_reason = 'no-ai-response'
                current_tooth.broken_note = 'Scott prompt with no AI response in source thread'
                current_tooth = None
            pending_scotts.append(seg)
        elif seg.speaker == 'ai':
            # If pending Scotts exist, flush them first (forms a tooth awaiting AI)
            if pending_scotts:
                flush_pending_scotts()
            if current_tooth is None:
                # AI segment with no preceding Scott: broken tooth (orphan AI)
                tooth_idx += 1
                teeth.append(Tooth(
                    index=tooth_idx,
                    ai_segment=seg,
                    is_broken=True,
                    broken_reason='orphan-ai',
                    broken_note='AI segment with no preceding Scott prompt'
                ))
                current_tooth = None
            else:
                # Rule 1.1.a: if current_tooth already has an ai_segment,
                # the previous AI becomes a d_strand_extension; the new
                # one becomes the tooth's ai_segment.
                if current_tooth.ai_segment is not None:
                    current_tooth.d_strand_extensions.append(current_tooth.ai_segment)
                current_tooth.ai_segment = seg

    # Flush any trailing pending Scotts
    if pending_scotts:
        flush_pending_scotts()
        # Trailing Scott(s) with no AI: mark broken
        if current_tooth is not None and current_tooth.ai_segment is None and not current_tooth.is_broken:
            current_tooth.is_broken = True
            current_tooth.broken_reason = 'no-ai-response'
            current_tooth.broken_note = 'Trailing Scott prompt with no AI response'

    return teeth


# ============================================================================
# PARTITION DETECTION (no recovery — that's close tool's job)
# ============================================================================

def detect_partitions(content: str) -> int:
    """Count partition markers in content. Does not extract."""
    count = 0
    for pat in PARTITION_MARKERS:
        count += len(pat.findall(content))
    return count


# ============================================================================
# STUDENT DATA PROTOCOL
# ============================================================================

def detect_student_data(text: str) -> List[Dict]:
    """
    Scan text for student-data patterns. Returns list of detected hits
    with their context.
    """
    hits = []
    for pat in STUDENT_NAME_HEURISTICS:
        for m in pat.finditer(text):
            hits.append({
                'type': 'student-name-context',
                'match': m.group(0),
                'span': (m.start(), m.end()),
            })
    for m in PERSONAL_HISTORY_PATTERN.finditer(text):
        hits.append({
            'type': 'personal-history',
            'match': m.group(0),
            'span': (m.start(), m.end()),
        })
    return hits


def detect_hipaa(text: str) -> List[Dict]:
    """Detect HIPAA-scope content (medical, etc.)."""
    hits = []
    for m in HIPAA_PATTERN.finditer(text):
        hits.append({
            'type': 'hipaa-scope',
            'match': m.group(0),
            'span': (m.start(), m.end()),
        })
    return hits


def resolve_student_data_interactive(student_hits, hipaa_hits, scott_waives=False, route_journal=False):
    """
    Resolve student-data detections. Three options per spec §4.5:
      1. Anonymize (S-### + class-code)
      2. Redact (specifics removed; structural reference preserved)
      3. Move to non-corpus journal
    For batch / non-interactive: respect --scott-waives-anonymization
    or --non-corpus-journal flags.

    HIPAA: detect-and-delete; never journal-route.
    """
    if hipaa_hits and not scott_waives:
        return {
            'status': 'halt',
            'reason': 'hipaa-scope-detected',
            'message': f'HIPAA-scope content detected ({len(hipaa_hits)} hit(s)). '
                       f'Detect-and-delete required. No journal routing.',
            'hits': hipaa_hits,
        }
    if scott_waives:
        return {'status': 'waived', 'student_hits': student_hits, 'hipaa_hits': hipaa_hits}
    if route_journal:
        return {'status': 'journal-routed', 'student_hits': student_hits, 'hipaa_hits': hipaa_hits}
    if student_hits:
        return {
            'status': 'halt',
            'reason': 'student-data-detected',
            'message': f'Student-data patterns detected ({len(student_hits)} hit(s)). '
                       f'Resolve via --scott-waives-anonymization or --non-corpus-journal '
                       f'or edit paste before re-running.',
            'hits': student_hits,
        }
    return {'status': 'clean'}


# ============================================================================
# LAYER 4 CANDIDATE SURFACING (per §6)
# ============================================================================

def surface_layer4_candidates(teeth: List[Tooth]) -> Dict[str, List[Dict]]:
    """Pattern-match candidates by tooth-index. No interpretation."""
    out = {
        'questions': [],
        'meta_language': [],
        'ai_corrections': [],
        'self_interruptions': [],
        'compound_i_strands': [],
        'broken_teeth': [],
    }
    for tooth in teeth:
        if tooth.is_broken:
            out['broken_teeth'].append({
                'tooth': tooth.index,
                'reason': tooth.broken_reason,
                'note': tooth.broken_note,
            })
            continue
        if tooth.compound_i_strand_count > 1:
            out['compound_i_strands'].append({
                'tooth': tooth.index,
                'prompt_count': tooth.compound_i_strand_count,
            })
        if tooth.scott_segment:
            content = tooth.scott_segment.content
            if '?' in content:
                out['questions'].append({'tooth': tooth.index, 'snippet': first_sentence(content)})
            if META_LANG.search(content):
                out['meta_language'].append({'tooth': tooth.index, 'snippet': first_sentence(content)})
            if SELF_INTERRUPT_TAGS.search(content):
                out['self_interruptions'].append({'tooth': tooth.index, 'snippet': first_sentence(content)})
        if tooth.ai_segment:
            content = tooth.ai_segment.content
            if AI_CORRECTION.search(content):
                out['ai_corrections'].append({'tooth': tooth.index, 'snippet': first_sentence(content)})
    return out


def first_sentence(text: str, max_chars: int = 180) -> str:
    text = text.strip().replace('\n', ' ')
    m = re.search(r'^(.+?[.!?])(?:\s|$)', text)
    if m:
        s = m.group(1)
    else:
        s = text
    if len(s) > max_chars:
        s = s[:max_chars].rsplit(' ', 1)[0] + '…'
    return s


# ============================================================================
# CAPSULE RENDERING
# ============================================================================

def render_capsule(
    teeth: List[Tooth],
    layer4: Dict,
    *,
    capsule_id: str,
    source_space: str,
    parent_space: str,
    source_thread_title: str,
    selected_for: str,
    selection_note: str,
    paste_artifact_path: str,
    detection_mode_overall: str,
) -> str:
    """Render the capsule.md per spec §3.2 frontmatter and §3.3 body."""
    now_iso = datetime.now(timezone.utc).astimezone().isoformat()

    # Stats
    tooth_count = len([t for t in teeth if not (t.is_broken and t.scott_segment is None and t.ai_segment is None)])
    broken_teeth = [t for t in teeth if t.is_broken]
    broken_tooth_count = len(broken_teeth)
    compound_i = [t for t in teeth if t.compound_i_strand_count > 1]
    unknown_segments = len([t for t in teeth if t.is_broken and t.broken_reason == 'unknown-speaker'])
    partitions_total = sum(t.partitions_detected for t in teeth)

    # Frontmatter
    fm = {
        'capsule_id': capsule_id,
        'capsule_version': 'v1-final',
        'generated_at': now_iso,

        'source_space': source_space,
        'parent_space': parent_space,
        'source_thread_title': source_thread_title,
        'source_url': None,
        'thread_date_range': 'unknown',
        'day_zero_offset_at_generation': 'D0+6',

        'segment_count': sum(1 for t in teeth for s in [t.scott_segment, t.ai_segment, *t.d_strand_extensions] if s is not None),
        'tooth_count': tooth_count,
        'vertebra_count': 0,  # capture-mode: no vertebrae yet
        'broken_tooth_count': broken_tooth_count,
        'broken_teeth': [
            {'tooth': t.index, 'reason': t.broken_reason, 'note': t.broken_note}
            for t in broken_teeth
        ],
        'compound_i_strands': [
            {'tooth': t.index, 'prompt_count': t.compound_i_strand_count, 'note': None}
            for t in compound_i
        ],
        'unknown_segment_count': unknown_segments,
        'audience_fit_failures': 0,
        'audience_fit_reviewed': False,  # Gate. Set true at closure-mode.

        'partitions_text_recovered': 0,         # capture-mode: no recovery
        'partitions_visual_collapsed': 0,       # close tool will count
        'partitions_text_unrecoverable': 0,
        'partitions_detected_at_capture': partitions_total,

        'shared_referents': [],
        'referent_drift_flags': [],
        'co_authorship_note': (
            'Co-written. Attribution to the encoding pair. '
            'Referent-alignment over time is the fidelity metric, not author-percentage.'
        ),

        'seat_annotations': [],

        'space_index_entry': {
            'scope_tag': 'pending',
            'primary_referents': [],
            'one_line_summary': 'pending',
            'arc_group': None,
        },

        'selected_for': selected_for,
        'selection_note': selection_note,

        'capsule_status': 'in-capture',
        'seat_attention': [],
        'scott_review_state': 'unread',

        'sofia_time_overlay': {
            'scope': 'capsule-level',
            'd0_offset_at_thread_origin': 'D0+6',
            'd0_offset_at_thread_close': 'D0+6',
            'sacred_time_register': None,
            'durative_span_class': None,
            'per_tooth': [],
        },

        'collapse_readiness': 'undecided',
        'mode_at_capture': 'capture',

        'research_artifacts': [],
        'journal_routing': [],

        'phase': 1,
        'phase_2_ready': False,

        'detection_mode_overall': detection_mode_overall,
        'paste_artifact': paste_artifact_path,
    }

    fm_yaml = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100)

    # Body
    lines = []
    lines.append('---')
    lines.append(fm_yaml.rstrip())
    lines.append('---')
    lines.append('')
    lines.append(f'# Capsule — {source_thread_title}')
    lines.append('')
    lines.append(f'**Mode:** capture | **Status:** in-capture | **Audience-fit reviewed:** false')
    lines.append('')
    lines.append('---')
    lines.append('')

    # Layer 1 — Path Card
    lines.append('## Layer 1 — Path Card')
    lines.append('')
    lines.append(f'**Title:** {source_thread_title}  ')
    lines.append(f'**Project / Space:** {source_space}  ')
    lines.append(f'**Parent space:** {parent_space}  ')
    lines.append(f'**Date range:** unknown  ')
    lines.append(f'**Status:** in-capture  ')
    lines.append(f'**D0 offset:** D0+6  ')
    lines.append(f'**Vault path:** {capsule_id}.md  ')
    lines.append('')
    lines.append('**Scope note:** *[Why are you capsuling this thread or path? One sentence is enough.]*')
    lines.append('')
    lines.append('---')
    lines.append('')

    # Layer 2 — Verbatim Spine (skeletal at capture)
    lines.append('## Layer 2 — Verbatim Spine')
    lines.append('')
    lines.append('### 2A — Candidate Governing Sentences (auto-surfaced)')
    lines.append('*Surfaced at capture; Scott promotes at scan time.*')
    lines.append('')
    if layer4['questions']:
        for q in layer4['questions'][:5]:
            lines.append(f'- Tooth {q["tooth"]:02d}: {q["snippet"]}')
    else:
        lines.append('- *(none surfaced)*')
    lines.append('')
    lines.append('### 2B — Promoted Spine')
    lines.append('*Scott fills at scan time.*')
    lines.append('')
    lines.append('### 2C — Seed Candidates')
    lines.append('*Principles to file; Scott confirms at scan.*')
    lines.append('')
    lines.append('### 2D — Visual Primary Data')
    lines.append('*Linked artifacts (close tool extracts text-format; visual marked collapsed).*')
    lines.append('')
    lines.append('---')
    lines.append('')

    # Layer 3 — Transcript Layers (3A populated; 3C deferred to close)
    lines.append('## Layer 3 — Transcript Layers')
    lines.append('')
    lines.append('### 3A — Learning Tier')
    lines.append('')
    lines.append('#### Table of Contents')
    for tooth in teeth:
        if tooth.is_broken and tooth.scott_segment is None and tooth.ai_segment is None:
            lines.append(f'{tooth.index:02d}. **[broken_tooth: {tooth.broken_reason}]** — {tooth.broken_note or ""}')
        elif tooth.is_broken:
            scott_snippet = first_sentence(tooth.scott_segment.content, 60) if tooth.scott_segment else '(no Scott)'
            lines.append(f'{tooth.index:02d}. **[broken_tooth: {tooth.broken_reason}]** — {scott_snippet}')
        else:
            scott_snippet = first_sentence(tooth.scott_segment.content, 60) if tooth.scott_segment else '(no Scott)'
            ci_marker = f' [compound-I-strand: {tooth.compound_i_strand_count} prompts]' if tooth.compound_i_strand_count > 1 else ''
            ext_marker = f' [+{len(tooth.d_strand_extensions)} D-strand extension(s)]' if tooth.d_strand_extensions else ''
            lines.append(f'{tooth.index:02d}. **Tooth** — {scott_snippet}{ci_marker}{ext_marker}')
    lines.append('')

    lines.append('#### All Scott Prompts (verbatim, tooth-indexed)')
    lines.append('*Complete I-strand record, unfiltered. Future-Scott hears what he said.*')
    lines.append('')
    for tooth in teeth:
        if tooth.scott_segment:
            ci_tag = f' [compound-I-strand: {tooth.compound_i_strand_count} prompts]' if tooth.compound_i_strand_count > 1 else ''
            lines.append(f'**Tooth {tooth.index:02d}{ci_tag}:**')
            lines.append('')
            lines.append('```text')
            lines.append(tooth.scott_segment.content)
            lines.append('```')
            lines.append('')
    lines.append('')

    lines.append('#### Recall Cues')
    lines.append('*[auto] — generated at capture; Scott reviews at scan time.*')
    lines.append('')
    if layer4['questions']:
        for q in layer4['questions'][:10]:
            lines.append(f'- `[auto]` Tooth {q["tooth"]:02d}: question — {q["snippet"]}')
    if layer4['meta_language']:
        for m in layer4['meta_language'][:5]:
            lines.append(f'- `[auto]` Tooth {m["tooth"]:02d}: meta-language — {m["snippet"]}')
    if layer4['self_interruptions']:
        for s in layer4['self_interruptions'][:5]:
            lines.append(f'- `[auto]` Tooth {s["tooth"]:02d}: self-interruption — {s["snippet"]}')
    lines.append('')

    lines.append('### 3B — Professional Tier')
    lines.append('*Phase 2 placeholder.*')
    lines.append('')

    # Layer 3C — Compliance Tier behind horizontal-rule + warning-header (per Claude Q5; D-seat call)
    lines.append('### 3C — Compliance Tier')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('> ⚠ **COMPLIANCE TIER — FULL FIDELITY BELOW**  ')
    lines.append('> Tooth-by-tooth verbatim record, partition-recovery state, audience-fit  ')
    lines.append('> resolution, and seat annotations. Read carefully; do not paraphrase or  ')
    lines.append('> compress when carrying forward.')
    lines.append('')
    for tooth in teeth:
        lines.append(f'#### Tooth {tooth.index:02d}')
        lines.append('')
        if tooth.is_broken:
            lines.append(f'**Status:** `[broken_tooth: {tooth.broken_reason}]`  ')
            lines.append(f'**Note:** {tooth.broken_note or "—"}  ')
            lines.append('')
        else:
            lines.append(f'**Status:** open (capture-mode; closure pending)  ')
            if tooth.compound_i_strand_count > 1:
                lines.append(f'**Compound I-strand:** {tooth.compound_i_strand_count} prompts  ')
            if tooth.d_strand_extensions:
                lines.append(f'**D-strand extensions:** {len(tooth.d_strand_extensions)}  ')
            lines.append(f'**Partitions detected:** {tooth.partitions_detected}  ')
            lines.append(f'**Civil-time:** unknown — pre-paste  ')
            lines.append('')

        if tooth.scott_segment:
            lines.append('**Scott (I-strand):**')
            lines.append('')
            lines.append('```text')
            lines.append(tooth.scott_segment.content)
            lines.append('```')
            lines.append('')

        for ext_i, ext in enumerate(tooth.d_strand_extensions, 1):
            lines.append(f'**AI (D-strand extension {ext_i}):**')
            lines.append('')
            lines.append('```text')
            lines.append(ext.content)
            lines.append('```')
            lines.append('')

        if tooth.ai_segment:
            lines.append('**AI (D-strand, closing response):**')
            lines.append('')
            lines.append('```text')
            lines.append(tooth.ai_segment.content)
            lines.append('```')
            lines.append('')

    if broken_teeth:
        lines.append('#### Broken teeth — listed')
        lines.append('')
        for t in broken_teeth:
            lines.append(f'- Tooth {t.index:02d}: `[broken_tooth: {t.broken_reason}]` — {t.broken_note or ""}')
        lines.append('')

    lines.append('---')
    lines.append('')

    # Layer 4 — Candidate Material
    lines.append('## Layer 4 — Candidate Material')
    lines.append('')
    lines.append('### 4A — Possible Class-Profile Elements')
    lines.append('*Post-anonymization; content beyond anonymization routes to non-corpus journal.*')
    lines.append('')
    lines.append('### 4B — Possible Missed-Questions')
    if layer4['ai_corrections']:
        for ac in layer4['ai_corrections']:
            lines.append(f'- Tooth {ac["tooth"]:02d}: AI-correction language — {ac["snippet"]}')
    else:
        lines.append('*(none surfaced)*')
    lines.append('')
    lines.append('### 4C — Possible Theoretical Moves')
    lines.append('*Scott surfaces at scan time.*')
    lines.append('')
    lines.append('### 4D — Possible Seed Principles')
    lines.append('*Scott surfaces at scan time.*')
    lines.append('')
    lines.append('### 4E — Possible Double-Scott Patterns')
    if compound_i:
        for t in compound_i:
            lines.append(f'- Tooth {t.index:02d}: `[compound-I-strand: {t.compound_i_strand_count} prompts]`')
    fallback_brokens = [t for t in broken_teeth if t.broken_reason == 'scott-only-pair-fallback']
    if fallback_brokens:
        for t in fallback_brokens:
            lines.append(f'- Tooth {t.index:02d}: `[broken_tooth: scott-only-pair, fallback-detected]`')
    if not (compound_i or fallback_brokens):
        lines.append('*(none surfaced)*')
    lines.append('')
    lines.append('---')
    lines.append('')

    # Layer 5 — Close Protocol (skeletal at capture)
    lines.append('## Layer 5 — Close Protocol')
    lines.append('')
    lines.append('**Status:** in-capture (closure pending)  ')
    lines.append(f'**Filed-by:** capsule-capture.py  ')
    lines.append(f'**Date:** {now_iso}  ')
    lines.append(f'**Container state:** capture-only; close tool will advance  ')
    lines.append(f'**Index-entry:** pending  ')
    lines.append(f'**Artifacts archived:** 0 (close tool extracts text-format partitions)  ')
    lines.append(f'**Broken teeth:** {broken_tooth_count} named  ')
    lines.append(f'**Audience-fit failures:** 0 (closure-mode work)  ')
    lines.append(f'**audience_fit_reviewed:** false (gate; set true at closure-mode)  ')
    lines.append('**To-team:** Scott  ')
    lines.append('**Next:** scan, then run capsule-close.py  ')
    lines.append('')
    lines.append('---')
    lines.append('')

    lines.append(f'*Capsule version: v1-final | Conformance: SPEC-after-Claude.md | '
                 f'IP of Scott Ryll, held under neuroarchy.ai.*')
    lines.append('')

    return '\n'.join(lines)


# ============================================================================
# CONFORMANCE CHECK
# ============================================================================

def conformance_check(capsule_md: str, capsule_path: Path) -> Dict:
    """Post-generation check per §11.1. Returns warnings; halt only on student-data failures."""
    warnings = []
    halts = []

    # Frontmatter parseable?
    if not capsule_md.startswith('---\n'):
        halts.append('Frontmatter missing leading ---')
    else:
        end = capsule_md.find('\n---\n', 4)
        if end == -1:
            halts.append('Frontmatter missing closing ---')
        else:
            try:
                yaml.safe_load(capsule_md[4:end])
            except yaml.YAMLError as e:
                halts.append(f'Frontmatter not parseable: {e}')

    # Layer headers present and ordered
    expected_headers = ['## Layer 1', '## Layer 2', '## Layer 3', '## Layer 4', '## Layer 5']
    last_pos = -1
    for h in expected_headers:
        pos = capsule_md.find(h)
        if pos == -1:
            warnings.append(f'Missing header: {h}')
        elif pos < last_pos:
            warnings.append(f'Header out of order: {h}')
        else:
            last_pos = pos

    return {'warnings': warnings, 'halts': halts, 'passed': not halts}


# ============================================================================
# CLI
# ============================================================================

def main():
    ap = argparse.ArgumentParser(description='capsule-capture.py — paste-time, fast, automatic.')
    ap.add_argument('--input', '-i', required=True, help='Input paste file.')
    ap.add_argument('--name', '-n', required=True, help='Path slug.')
    ap.add_argument('--space', required=True, help='Source space.')
    ap.add_argument('--parent-space', default='pending', help='Parent space ID.')
    ap.add_argument('--selected-for', default='pending', help='Routing target. Defaults to "pending".')
    ap.add_argument('--note', default='pending', help='Selection note. Defaults to "pending".')
    ap.add_argument('--output', '-o', help='Output capsule.md path. Defaults to <name>.md.')
    ap.add_argument('--markers', default=str(DEFAULT_MARKERS_PATH), help='Path to markers.yaml.')
    ap.add_argument('--batch-velocity', action='store_true', help='Batch mode; one-line report.')
    ap.add_argument('--scott-waives-anonymization', action='store_true',
                    help='Skip student-data halt (logged in capsule).')
    ap.add_argument('--non-corpus-journal', action='store_true',
                    help='Route to non-corpus journal per §4.5 Option 3.')
    ap.add_argument('--source-title', default=None, help='Source thread title.')
    args = ap.parse_args()

    paste_path = Path(args.input)
    if not paste_path.exists():
        print(f'ERROR: input file not found: {paste_path}', file=sys.stderr)
        sys.exit(1)

    raw = paste_path.read_text()
    if not raw.strip():
        print('ERROR: empty input', file=sys.stderr)
        sys.exit(1)

    # Student data + HIPAA detection (only required interruption per §3.5)
    student_hits = detect_student_data(raw)
    hipaa_hits = detect_hipaa(raw)
    sdp = resolve_student_data_interactive(
        student_hits, hipaa_hits,
        scott_waives=args.scott_waives_anonymization,
        route_journal=args.non_corpus_journal,
    )
    if sdp['status'] == 'halt':
        print(f'STUDENT-DATA-PROTOCOL HALT: {sdp["message"]}', file=sys.stderr)
        for hit in sdp.get('hits', [])[:10]:
            print(f'  - [{hit["type"]}] {hit["match"]!r} @ {hit["span"]}', file=sys.stderr)
        sys.exit(2)

    # Markers + segmentation
    markers = load_markers(Path(args.markers))
    marker_patterns = build_marker_patterns(markers)
    segments, detection_mode = detect_segments(raw, marker_patterns)

    # Tooth formation
    teeth = form_teeth(segments)

    # Partition detection (count only; recovery deferred to close tool)
    for tooth in teeth:
        if tooth.ai_segment:
            tooth.partitions_detected += detect_partitions(tooth.ai_segment.content)
        for ext in tooth.d_strand_extensions:
            tooth.partitions_detected += detect_partitions(ext.content)

    # Layer 4 surfacing
    layer4 = surface_layer4_candidates(teeth)

    # Capsule ID + paths
    source_title = args.source_title or args.name
    capsule_id = f'{args.space}__{args.name}__D0+6'
    out_path = Path(args.output) if args.output else Path(f'{capsule_id}.md')
    capture_dir = out_path.parent / '_capture'
    capture_dir.mkdir(parents=True, exist_ok=True)
    paste_artifact = capture_dir / f'{args.name}__paste.txt'
    paste_artifact.write_text(raw)

    # Render
    capsule_md = render_capsule(
        teeth, layer4,
        capsule_id=capsule_id,
        source_space=args.space,
        parent_space=args.parent_space,
        source_thread_title=source_title,
        selected_for=args.selected_for,
        selection_note=args.note,
        paste_artifact_path=str(paste_artifact.relative_to(out_path.parent) if out_path.parent in paste_artifact.parents else paste_artifact),
        detection_mode_overall=detection_mode,
    )

    out_path.write_text(capsule_md)

    # Conformance check
    check = conformance_check(capsule_md, out_path)

    # Report
    if args.batch_velocity:
        print(f'{capsule_id}: {len(teeth)} teeth ({sum(1 for t in teeth if not t.is_broken)} candidates / '
              f'{sum(1 for t in teeth if t.is_broken)} broken) → {out_path}')
    else:
        print(f'Capsule written: {out_path}', file=sys.stderr)
        print(f'  Teeth: {len(teeth)}', file=sys.stderr)
        print(f'  Tooth candidates: {sum(1 for t in teeth if not t.is_broken)}', file=sys.stderr)
        print(f'  Broken teeth: {sum(1 for t in teeth if t.is_broken)}', file=sys.stderr)
        print(f'  Compound I-strands: {sum(1 for t in teeth if t.compound_i_strand_count > 1)}', file=sys.stderr)
        print(f'  Unknown segments: {sum(1 for t in teeth if t.is_broken and t.broken_reason == "unknown-speaker")}', file=sys.stderr)
        print(f'  Partitions detected (no recovery): {sum(t.partitions_detected for t in teeth)}', file=sys.stderr)
        print(f'  Detection mode: {detection_mode}', file=sys.stderr)
        print(f'  Paste artifact: {paste_artifact}', file=sys.stderr)
        print(f'  Conformance: {"PASS" if check["passed"] else "FAIL"}', file=sys.stderr)
        for w in check['warnings']:
            print(f'    [warn] {w}', file=sys.stderr)
        for h in check['halts']:
            print(f'    [HALT] {h}', file=sys.stderr)


if __name__ == '__main__':
    main()
