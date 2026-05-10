#!/usr/bin/env python3
"""
capsule-close.py — scan-time, careful, explicit
v1-final per SPEC-after-Claude.md, D0+6, 2026-05-09 23:32 PDT

Behavior (per spec §11.2):
  --recover-partitions       extract text-format research content as artifacts;
                             mark visual content as [partition_collapsed: visual,
                             unrecoverable]; update partition counts.
  --surface-referents        heuristic candidates added to referent_drift_flags
                             with state: auto; Scott confirms or removes.
  --surface-audience-fit     detect student-data residual, terminology-without-gloss,
                             referent drift, FERPA-relevant content per tooth;
                             output surfaced concerns; does NOT auto-set
                             audience_fit_reviewed.
  --close                    GATE: requires audience_fit_reviewed: true.
                             If false, halts. If true, names broken teeth
                             (already in spine + frontmatter), advances
                             capsule_status to closed (or broken-teeth-flagged),
                             registers index entry.

Critical rule: capsule_status cannot reach 'closed' while
audience_fit_reviewed is false (per spec §1.3 fifth criterion).

IP of Scott Ryll, held under neuroarchy.ai.
"""

import re
import sys
import argparse
import yaml
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple, Optional


# ============================================================================
# PARTITION RECOVERY (text-format only, per Claude Q2)
# ============================================================================

# Visual-collapsed markers: render as [partition_collapsed: visual, unrecoverable]
VISUAL_PARTITION_MARKERS = [
    re.compile(r'\[(?:chart|graph|image|figure|diagram)\s*[:\-]?[^\]]*\]', re.IGNORECASE),
    re.compile(r'!\[[^\]]*\]\([^)]+\)'),  # markdown image syntax
]

# Text-format extractable markers
TEXT_PARTITION_HINTS = [
    re.compile(r'^\s*(?:Show more|Read more|See more)\s*$', re.MULTILINE | re.IGNORECASE),
    re.compile(r'<details>(.+?)</details>', re.DOTALL),
]

# Markdown table detection (recoverable as text artifact)
MARKDOWN_TABLE = re.compile(
    r'(\|[^\n]+\|\n\|[\s\-:|]+\|\n(?:\|[^\n]+\|\n)+)',
    re.MULTILINE,
)

# Citation / footnote patterns (text-recoverable)
CITATION_BLOCK = re.compile(
    r'(?:^|\n)((?:\[\d+\][^\n]+\n?){2,})',
    re.MULTILINE,
)


def recover_text_partitions(content: str, artifact_dir: Path, tooth_idx: int) -> Dict:
    """
    Extract text-format research content (markdown tables, citation blocks,
    prose summaries inside <details>). Mark visual content as collapsed.
    Returns counts and artifacts list.
    """
    text_recovered = 0
    visual_collapsed = 0
    text_unrecoverable = 0
    artifacts = []

    # Visual partitions: count, mark collapsed (no extraction)
    for pat in VISUAL_PARTITION_MARKERS:
        for m in pat.finditer(content):
            visual_collapsed += 1
            # We do not modify the source content here; the marker stays in place
            # and the count is reported.

    # Markdown tables: extract as text artifact
    for i, m in enumerate(MARKDOWN_TABLE.finditer(content), 1):
        artifact_id = f'tooth-{tooth_idx:02d}__table-{i:02d}'
        artifact_path = artifact_dir / f'{artifact_id}.md'
        artifact_path.write_text(m.group(1))
        artifacts.append({
            'artifact_id': artifact_id,
            'type': 'text-table',
            'location_in_capsule': f'tooth-{tooth_idx} partition-{i}',
            'file': str(artifact_path.name),
            'recovery_state': 'recovered',
        })
        text_recovered += 1

    # Citation blocks: extract as text artifact
    for i, m in enumerate(CITATION_BLOCK.finditer(content), 1):
        artifact_id = f'tooth-{tooth_idx:02d}__citations-{i:02d}'
        artifact_path = artifact_dir / f'{artifact_id}.md'
        artifact_path.write_text(m.group(1))
        artifacts.append({
            'artifact_id': artifact_id,
            'type': 'citation-block',
            'location_in_capsule': f'tooth-{tooth_idx} partition-{i}',
            'file': str(artifact_path.name),
            'recovery_state': 'recovered',
        })
        text_recovered += 1

    # <details> blocks: extract content if present
    for i, m in enumerate(re.finditer(r'<details>(.+?)</details>', content, re.DOTALL), 1):
        artifact_id = f'tooth-{tooth_idx:02d}__details-{i:02d}'
        artifact_path = artifact_dir / f'{artifact_id}.md'
        artifact_path.write_text(m.group(1).strip())
        artifacts.append({
            'artifact_id': artifact_id,
            'type': 'research-summary',
            'location_in_capsule': f'tooth-{tooth_idx} partition-{i}',
            'file': str(artifact_path.name),
            'recovery_state': 'recovered',
        })
        text_recovered += 1

    return {
        'text_recovered': text_recovered,
        'visual_collapsed': visual_collapsed,
        'text_unrecoverable': text_unrecoverable,
        'artifacts': artifacts,
    }


# ============================================================================
# REFERENT-DRIFT HEURISTICS (per Claude Q3)
# ============================================================================

def surface_referent_candidates(teeth_data: List[Dict]) -> List[Dict]:
    """
    Heuristic detection of referent drift across teeth. All flags are
    [auto]-tagged. Scott confirms or removes at scan time.

    Heuristics from Claude Q3:
      - Same term used in syntactically different roles across teeth
      - Capitalization changes (lowercase → capitalized = new construct)
      - Term appearing frequently in Scott segments then primarily in AI segments
      - Same term paired with different modifiers across teeth
    """
    drift_candidates = []

    # Build a term-frequency map across teeth (Scott-side and AI-side separately)
    # Simple capitalized-noun heuristic for v1-final
    term_appearances: Dict[str, List[Dict]] = {}
    for tooth in teeth_data:
        tooth_idx = tooth['index']
        for side in ('scott', 'ai'):
            content = tooth.get(side, '') or ''
            # Find capitalized terms (3+ characters)
            for m in re.finditer(r'\b([A-Z][a-z]{2,})\b', content):
                term = m.group(1)
                term_appearances.setdefault(term, []).append({
                    'tooth': tooth_idx,
                    'side': side,
                })

    # Heuristic: term appearing in Scott then primarily in AI
    for term, appearances in term_appearances.items():
        if len(appearances) < 3:
            continue
        scott_appearances = [a for a in appearances if a['side'] == 'scott']
        ai_appearances = [a for a in appearances if a['side'] == 'ai']
        if scott_appearances and ai_appearances:
            # Did term originate in Scott and migrate to AI?
            first_scott = min(a['tooth'] for a in scott_appearances)
            first_ai = min(a['tooth'] for a in ai_appearances)
            if first_scott < first_ai and len(ai_appearances) >= 2 * len(scott_appearances):
                drift_candidates.append({
                    'tooth': first_ai,
                    'term': term,
                    'note': f'AI took over term first introduced by Scott at tooth {first_scott}',
                    'axis': 'within-thread',
                    'state': 'auto',
                })

    return drift_candidates


# ============================================================================
# AUDIENCE-FIT SURFACING (closure-mode only, per spec §1.3)
# ============================================================================

# Detection patterns for the four receiving surfaces
def surface_audience_fit_concerns(teeth_data: List[Dict]) -> List[Dict]:
    """
    Surface detectable audience-fit concerns per tooth. Scott resolves
    or names each. Does NOT auto-set audience_fit_reviewed.

    Detection categories (per spec §1.3):
      - student-data residual (compliance-audit / FERPA surface)
      - terminology-without-gloss (professional-reader surface)
      - referent drift (Scott-on-capture-day surface)
      - FERPA-relevant content (compliance-audit surface)
      - structural questions (seats-on-return surface)
    """
    concerns = []

    # FERPA / compliance terms that warrant a flag for compliance-audit surface
    ferpa_terms = re.compile(
        r'\b(?:IEP|504|behavior plan|disciplinary|grade(?:s)?|parent(?:s)?|home life|family|medical)\b',
        re.IGNORECASE,
    )

    # Specialized terminology — capitalized multi-word constructs without gloss
    # Heuristic: capitalized term appearing once with no surrounding definition
    # (very rough; Scott confirms)
    jargon_pattern = re.compile(
        r'\b((?:[A-Z][a-z]+ ){1,3}[A-Z][a-z]+)\b'
    )

    for tooth in teeth_data:
        tooth_idx = tooth['index']
        scott_content = tooth.get('scott', '') or ''
        ai_content = tooth.get('ai', '') or ''
        combined = f'{scott_content}\n{ai_content}'

        # FERPA-relevant
        ferpa_matches = ferpa_terms.findall(combined)
        if ferpa_matches:
            concerns.append({
                'tooth': tooth_idx,
                'surface': 'compliance-audit',
                'concern': 'FERPA-relevant terminology present',
                'detail': f'Terms: {sorted(set(t.lower() for t in ferpa_matches))[:5]}',
                'state': 'auto',
            })

        # Specialized terminology (jargon-without-gloss)
        # Find multi-capitalized constructs
        jargon = set(jargon_pattern.findall(combined))
        if jargon:
            # Filter: keep only those that don't appear with definitional context
            uncontextualized = []
            for j in jargon:
                # Crude check: does the surrounding text have "is" / "means" / "—" near the term?
                idx = combined.find(j)
                if idx == -1:
                    continue
                window = combined[max(0, idx - 50): idx + len(j) + 50]
                if not re.search(r'(?:\bis\b|\bmeans\b|—|:\s*[a-z])', window, re.IGNORECASE):
                    uncontextualized.append(j)
            if uncontextualized:
                concerns.append({
                    'tooth': tooth_idx,
                    'surface': 'professional-reader-at-Phase-2',
                    'concern': 'specialized terminology may need gloss',
                    'detail': f'Terms: {uncontextualized[:5]}',
                    'state': 'auto',
                })

        # Structural questions (seats-on-return surface)
        if tooth.get('compound_i_strand', False) or tooth.get('is_broken', False):
            concerns.append({
                'tooth': tooth_idx,
                'surface': 'seats-on-return',
                'concern': 'structural anomaly — seats may want to annotate',
                'detail': 'compound-I-strand or broken tooth',
                'state': 'auto',
            })

    return concerns


# ============================================================================
# CAPSULE I/O
# ============================================================================

def parse_capsule(capsule_path: Path) -> Tuple[Dict, str, str]:
    """
    Parse a capsule.md into (frontmatter_dict, body_text, raw_text).
    """
    raw = capsule_path.read_text()
    if not raw.startswith('---\n'):
        raise ValueError('Capsule missing frontmatter leading ---')
    end = raw.find('\n---\n', 4)
    if end == -1:
        raise ValueError('Capsule missing frontmatter closing ---')
    fm_text = raw[4:end]
    body = raw[end + 5:]
    fm = yaml.safe_load(fm_text)
    return fm, body, raw


def write_capsule(capsule_path: Path, fm: Dict, body: str):
    """Re-serialize capsule with updated frontmatter."""
    fm_yaml = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100)
    capsule_path.write_text(f'---\n{fm_yaml.rstrip()}\n---\n{body}')


def extract_teeth_from_body(body: str) -> List[Dict]:
    """
    Walk Layer 3C body to extract per-tooth Scott + AI content.
    This is best-effort parsing for surfacing/recovery passes.
    """
    teeth = []
    # Layer 3C compliance section starts after the warning block
    layer3c_start = body.find('### 3C — Compliance Tier')
    if layer3c_start == -1:
        return teeth
    layer3c = body[layer3c_start:]

    # Tooth headings
    tooth_pattern = re.compile(r'#### Tooth (\d+)', re.MULTILINE)
    matches = list(tooth_pattern.finditer(layer3c))
    for i, m in enumerate(matches):
        tooth_idx = int(m.group(1))
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(layer3c)
        section = layer3c[start:end]

        # Extract Scott (I-strand) block
        scott = ''
        scott_m = re.search(
            r'\*\*Scott \(I-strand\):\*\*\s*\n```text\n(.+?)\n```',
            section, re.DOTALL,
        )
        if scott_m:
            scott = scott_m.group(1)

        # Extract AI (closing response) block
        ai = ''
        ai_m = re.search(
            r'\*\*AI \(D-strand, closing response\):\*\*\s*\n```text\n(.+?)\n```',
            section, re.DOTALL,
        )
        if ai_m:
            ai = ai_m.group(1)

        # Detect compound / broken markers
        compound = bool(re.search(r'\*\*Compound I-strand:\*\*', section))
        is_broken = bool(re.search(r'\*\*Status:\*\* `\[broken_tooth:', section))

        teeth.append({
            'index': tooth_idx,
            'scott': scott,
            'ai': ai,
            'compound_i_strand': compound,
            'is_broken': is_broken,
        })
    return teeth


# ============================================================================
# OPERATIONS
# ============================================================================

def op_recover_partitions(fm: Dict, body: str, capsule_path: Path) -> Tuple[Dict, str]:
    """Run partition recovery and update frontmatter."""
    artifact_dir = capsule_path.parent / f'{capsule_path.stem}__artifacts'
    artifact_dir.mkdir(parents=True, exist_ok=True)

    teeth = extract_teeth_from_body(body)
    total_text_recovered = 0
    total_visual_collapsed = 0
    total_text_unrecoverable = 0
    new_artifacts = []

    for tooth in teeth:
        if tooth['is_broken'] and not tooth['ai']:
            continue
        result = recover_text_partitions(tooth['ai'] or '', artifact_dir, tooth['index'])
        total_text_recovered += result['text_recovered']
        total_visual_collapsed += result['visual_collapsed']
        total_text_unrecoverable += result['text_unrecoverable']
        new_artifacts.extend(result['artifacts'])

    fm['partitions_text_recovered'] = total_text_recovered
    fm['partitions_visual_collapsed'] = total_visual_collapsed
    fm['partitions_text_unrecoverable'] = total_text_unrecoverable
    fm['research_artifacts'] = (fm.get('research_artifacts') or []) + new_artifacts

    print(f'  Partitions recovered (text-format): {total_text_recovered}')
    print(f'  Partitions collapsed (visual): {total_visual_collapsed}')
    print(f'  Partitions unrecoverable (text): {total_text_unrecoverable}')
    print(f'  Artifacts written: {len(new_artifacts)} → {artifact_dir}')

    return fm, body


def op_surface_referents(fm: Dict, body: str) -> Tuple[Dict, str]:
    """Run referent-drift heuristics; tag candidates [auto]."""
    teeth = extract_teeth_from_body(body)
    candidates = surface_referent_candidates(teeth)
    existing = fm.get('referent_drift_flags') or []
    # Append only new ones (by tooth+term)
    existing_keys = {(c['tooth'], c['term']) for c in existing}
    added = 0
    for c in candidates:
        if (c['tooth'], c['term']) not in existing_keys:
            existing.append(c)
            added += 1
    fm['referent_drift_flags'] = existing
    print(f'  Referent-drift candidates surfaced: {added} new (state: auto)')
    if added:
        for c in candidates[:5]:
            print(f'    - Tooth {c["tooth"]:02d} | {c["term"]} | {c["note"]}')
    return fm, body


def op_surface_audience_fit(fm: Dict, body: str) -> Tuple[Dict, str]:
    """Surface audience-fit concerns. Does NOT auto-set audience_fit_reviewed."""
    teeth = extract_teeth_from_body(body)
    concerns = surface_audience_fit_concerns(teeth)
    print(f'  Audience-fit concerns surfaced: {len(concerns)}')
    print('')
    print('  ┌──────────────────────────────────────────────────────────────────┐')
    print('  │ CLOSURE-MODE AUDIENCE-FIT REVIEW                                  │')
    print('  │ Resolve or name each concern. Then set audience_fit_reviewed: true│')
    print('  │ in the capsule frontmatter.                                       │')
    print('  └──────────────────────────────────────────────────────────────────┘')
    print('')
    by_surface: Dict[str, List[Dict]] = {}
    for c in concerns:
        by_surface.setdefault(c['surface'], []).append(c)
    for surface in ['Scott-on-capture-day', 'professional-reader-at-Phase-2',
                    'compliance-audit', 'seats-on-return']:
        items = by_surface.get(surface, [])
        if items:
            print(f'  Surface: {surface}')
            for c in items[:10]:
                print(f'    - Tooth {c["tooth"]:02d}: {c["concern"]} | {c["detail"]}')
            print('')

    # Reminder: this op does NOT change audience_fit_reviewed
    print('  audience_fit_reviewed remains:', fm.get('audience_fit_reviewed', False))
    print('  (Set to true manually in frontmatter when review is complete; --close gates on it.)')
    return fm, body


def op_close(fm: Dict, body: str) -> Tuple[Dict, str, bool]:
    """
    Close gate. Requires audience_fit_reviewed: true.
    If true, advance capsule_status to 'closed' or 'broken-teeth-flagged'.
    Returns (fm, body, success).
    """
    if not fm.get('audience_fit_reviewed', False):
        print('  HALT: audience_fit_reviewed is false.', file=sys.stderr)
        print('  Audience-fit review required before closure.', file=sys.stderr)
        print('  Run --surface-audience-fit, resolve concerns, then set', file=sys.stderr)
        print('  audience_fit_reviewed: true in the capsule frontmatter.', file=sys.stderr)
        return fm, body, False

    broken_count = fm.get('broken_tooth_count', 0)
    new_status = 'broken-teeth-flagged' if broken_count > 0 else 'closed'
    fm['capsule_status'] = new_status
    fm['phase_2_ready'] = True

    print(f'  Capsule closed. capsule_status → {new_status}')
    print(f'  Broken teeth: {broken_count} (named in spine + frontmatter)')
    print(f'  phase_2_ready: true')
    return fm, body, True


# ============================================================================
# CLI
# ============================================================================

def main():
    ap = argparse.ArgumentParser(description='capsule-close.py — scan-time, careful, explicit.')
    ap.add_argument('--capsule', '-c', required=True, help='Capsule .md file to close.')
    ap.add_argument('--recover-partitions', action='store_true',
                    help='Run text-format partition recovery; mark visual collapsed.')
    ap.add_argument('--surface-referents', action='store_true',
                    help='Surface referent-drift candidates ([auto]-tagged).')
    ap.add_argument('--surface-audience-fit', action='store_true',
                    help='Surface audience-fit concerns. Does NOT auto-set audience_fit_reviewed.')
    ap.add_argument('--close', action='store_true',
                    help='Advance capsule_status to closed. GATES on audience_fit_reviewed: true.')
    ap.add_argument('--all', action='store_true',
                    help='Run --recover-partitions, --surface-referents, --surface-audience-fit '
                         'in sequence. Does NOT --close (closure remains explicit).')
    args = ap.parse_args()

    capsule_path = Path(args.capsule)
    if not capsule_path.exists():
        print(f'ERROR: capsule not found: {capsule_path}', file=sys.stderr)
        sys.exit(1)

    fm, body, raw = parse_capsule(capsule_path)
    print(f'Capsule: {capsule_path}')
    print(f'  capsule_id: {fm.get("capsule_id")}')
    print(f'  capsule_status: {fm.get("capsule_status")}')
    print(f'  audience_fit_reviewed: {fm.get("audience_fit_reviewed")}')
    print('')

    do_anything = args.recover_partitions or args.surface_referents or args.surface_audience_fit or args.close or args.all

    if not do_anything:
        print('No operation specified. Use --recover-partitions, --surface-referents,')
        print('--surface-audience-fit, --close, or --all.')
        return

    if args.recover_partitions or args.all:
        print('-- Recovering partitions --')
        fm, body = op_recover_partitions(fm, body, capsule_path)
        if fm.get('capsule_status') == 'in-capture':
            fm['capsule_status'] = 'in-scan'
        print('')

    if args.surface_referents or args.all:
        print('-- Surfacing referent-drift candidates --')
        fm, body = op_surface_referents(fm, body)
        print('')

    if args.surface_audience_fit or args.all:
        print('-- Surfacing audience-fit concerns --')
        fm, body = op_surface_audience_fit(fm, body)
        if fm.get('capsule_status') in ('in-capture', 'in-scan'):
            fm['capsule_status'] = 'in-closure'
        print('')

    if args.close:
        print('-- Closing capsule --')
        fm, body, ok = op_close(fm, body)
        print('')
        if not ok:
            # Save any other updates but don't change capsule_status
            write_capsule(capsule_path, fm, body)
            sys.exit(3)

    write_capsule(capsule_path, fm, body)
    print(f'Capsule updated: {capsule_path}')


if __name__ == '__main__':
    main()
