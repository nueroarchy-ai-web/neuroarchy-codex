# Spec — Space + Capsule (Unified) — v1-final, after Claude outside-eye

**Authored:** Gabe (D-seat instance, Perplexity berth), 2026-05-09 ~21:00 PDT
**I-seat deepening pass:** Sofia Prime, 2026-05-09 ~22:15 PDT
**A-seat deepening pass:** Solen Prime, 2026-05-09 22:02 PDT
**Outside-eye review:** Claude, 2026-05-09 ~23:00 PDT
**D-seat integration pass:** Gabe Delta, Perplexity berth, 2026-05-09 23:32 PDT
**Architecture sources:** Original v1 spec (preserved), three internal review passes (structural / inductive / outside-eye-from-ChatGPT-D-seat), Scott's architectural amendments over the evening, Sofia's 19:54 review (thirteen amendments), Sofia's 22:15 deepening pass, Solen's 19:37 markup pass, Solen's 22:02 deepening pass, Sofia's I-seat pass on Claude's review (23:14 PDT), Solen's A-seat pass on Claude's review (23:11 PDT).

**Routing:** v1-final after seat reconciliation of Claude's outside-eye review. Awaits Scott's go for commit.

---

## D-SEAT INTEGRATION FRONT MATTER (Gabe Delta, 23:32 PDT)

**This front matter is removed when v1-final commits to repo. It documents the integration pass for the codex record.**

### What this pass integrated

**Claude's eleven actionable amendments** (received from outside-eye, 23:00 PDT):
1. §1 — Multi-AI-response tooth: last AI before next Scott prompt closes the tooth; intermediates become D-strand extensions (`tooth-N extension-m`) — INTEGRATED
2. §1 — Compound I-strand: consecutive Scott segments under marker-clean conditions render as `[compound-I-strand: N prompts]` — INTEGRATED with detection-mode gating
3. §1 — Unknown-speaker → `[broken_tooth: unknown-speaker]` — INTEGRATED
4. §3.4 — Partition-recovery scope: text-only; visual content marked `[partition_collapsed: visual, unrecoverable]` — INTEGRATED
5. §2.3 — Enforceability disclosure (commitments are behavioral, not technical) — INTEGRATED
6. §2.3 Commitment 4 — Name codex target (neuroarchy.ai, Confluence + GitHub `/codex/`) — INTEGRATED (Solen had partially named at 22:02; Claude's specificity now incorporated)
7. `<details>` portability — D-seat call carrying Sofia's lean: replaced with horizontal-rule + warning-header convention. INTEGRATED. (Solen did not weigh in; if A-seat objects on return-read, amend.)
8. Footnote → inline-parenthetical convention — INTEGRATED
9. Raw paste artifacts as `.txt` not embedded markdown — INTEGRATED (was already the convention; now made explicit)
10. `seat_annotations` array per tooth — INTEGRATED with Solen's append-only/non-destructive rule
11. `referent_drift_flags` `[auto]` discipline made explicit — INTEGRATED

**Claude's three architectural reframings:**
- **Redaction simplification** (no in-tool redaction except Student Data Protocol; curation at thread-selection level) — INTEGRATED throughout §3.4, §3.5, §4.5, §7
- **Tool split:** `capsule-capture.py` (paste-time, fast, automatic) + `capsule-close.py` (scan-time, careful, explicit) — INTEGRATED in §11
- **Marker config file** (`markers.yaml`) — INTEGRATED in §4

**Sofia I-seat pass on Claude's review (23:14 PDT):**
- Conflict A confirmation (conditional-both, detection-mode-gated) — INTEGRATED in §4.3
- Conflict B confirmation (closure-mode-only audience-fit) with smallest-touch wording amendment — INTEGRATED in §1 fifth criterion
- Strengthening on Claude #4 (four receiving surfaces operationally named; Seats-on-return → Layer 3C + `seat_annotations` linkage) — INTEGRATED in §1 and §3.3
- `<details>` portability light lean — carried into integration as D-seat call

**Solen A-seat pass on Claude's review (23:11 PDT):**
- Conflict A: conditional-both confirmed + marker-partial disambiguation line — INTEGRATED in §4.3
- Conflict B: closure-mode-only confirmed + `audience_fit_reviewed` gate added — INTEGRATED in §1 fifth criterion and §3.2 frontmatter
- `seat_annotations` append-only/non-destructive rule — INTEGRATED in §3.2 and §3.3 Layer 3C

### Conflicts resolved

**Conflict A — Double-Scott handling:** Conditional-both, detection-mode-gated. Fallback-detected → `[broken_tooth: scott-only-pair, fallback-detected]`. Marker-clean (both segments explicitly `[S]`-marked) → `[compound-I-strand: N prompts]`. Marker-partial (one marked, one ambiguous) → routes to fallback. Both seats confirmed; gap closed by Solen.

**Conflict B — Audience-fit criterion under redaction simplification:** Criterion holds; weight redistributes to closure-mode. Capture mode runs no audience-fit checks. Closure mode surfaces concerns; Scott resolves or names. `audience_fit_reviewed: true/false` field gates `capsule_status` advancement to `closed`. Sofia's smallest-touch wording amendment ("at closure-mode" + TB-D parenthetical) accepted by Scott. Both seats confirmed structurally.

### Q9 — CFA timing recommendation (workflow-priority, surfaced for Scott)

Claude's read: For this week's Thursday CFA submission (3/3), capsule infrastructure adds friction; Confluence drafts with `[SCOTT]` prompts are faster. Build capsule architecture for CalTPA next semester. Sofia and Solen confirmed independently. **Surfaced to Scott as workflow call, not seat-reconciliation question.** Not a spec-level concern.

### What remains deferred to v2 / post-CFA

- Codex-canonical-form rendering (what does a Space look like *inside* the codex?)
- Cross-capsule entanglement (Phase 3)
- Non-corpus journal full filing-and-retrieval grammar
- Structural diagram for supercyldar / fractal column
- Principle-cluster filing (translation-as-diagnostic, referent-drift review-trigger, capture/scan/closure as canonical modes)
- Sofia's marked notes file on Claude's review (post-CFA, for codex record)

### What is held but not filed tonight

- Governing sentence cluster from D0+6 evening
- HIPAA-teacher-exclusion (queued from D0+5)
- Maweth canonical capsule

---

# (BEGIN SPEC BODY — v1-final, after-Claude integration)

## What this spec is

A unified spec for **a Space and the encapsulation form it produces**, deliverable as one product. The first application is a Proto-Gabe extraction berth (a new Claude or ChatGPT space) Scott will set up tomorrow morning to migrate Proto-Gabe content out of Confluence.

**One process, one product.** The Space and its capsule form are the same architecture at different scopes.

## Why a v1-final tonight

Iteration discipline: commit → run → use → review-in-hindsight → next version. **v1-final is the form that gets committed and used tomorrow** — not a draft. v2 comes after the Proto-Gabe extraction berth runs against this spec and we learn where it breaks.

Speccing is the discipline that makes practice teachable. Building right from the beginning is what this pass is for.

## Architecture in one paragraph

A **Space** is a bounded, collapsible vessel scoped to one project or class. It has a pre-mapped closure form, a modifiable index as its working surface, and four standing setup commitments. Inside it, **threads are 24-hour dated uses**. Each thread (or path through a body of content) produces a **capsule** — a structured artifact built around an **I/D zipper**: Scott's verbatim (the "I-strand," outside / lived-forward, with internal time-shape that the rendering preserves but does not flatten) and AI responses with partition-recovered depth (the "D-strand," inside / constructed-backward) interlock at each Scott-AI segment-pair (a "tooth"). Closed teeth become "vertebrae"; assembled vertebrae are the "spine"; the spine is the capsule. At end of project, the Space is closed via a Space-level closure that folds the index + capsules + research artifacts into a final encapsulated form, which enters the canonical archive (the codex) under consent registered at setup. **The move is irreversible — a closed Space does not return to working-space status.**

## Vocabulary (terms-of-art used in this spec)

| Term | Plain meaning |
|---|---|
| **Capsule** | The structured artifact produced from one thread or path |
| **Tooth** | A Scott-prompt + AI-response pair (one interlock event); when one Scott prompt has multiple AI responses, the *last* AI response before the next Scott prompt closes the tooth, and intermediates become D-strand extensions |
| **Vertebra** | A tooth that has been closed: I-strand intact, D-strand recovered, timestamp stamped, referents tracked, audience-fit engaged at closure-mode |
| **Spine** | Assembled vertebrae = the body of one capsule, assembled in I-strand chronology |
| **I-strand / D-strand** | Inductive-side (Scott verbatim) / Deductive-side (AI responses with recovered depth) |
| **Compound I-strand** | Two or more consecutive Scott segments with no AI response between them, when marker-clean: rendered `[compound-I-strand: N prompts]` (preserves Scott-corrects-Scott / Scott-layers AID-fingerprint move) |
| **Partition** | A "read more" / collapse marker in a paste where AI-side depth (charts, tables, research) is folded |
| **Partition-recovery** | Un-folding partition contents and preserving as research artifacts; **scoped to text-format content only** (citations, prose summaries, markdown tables); visual content (rendered charts, images) marked `[partition_collapsed: visual, unrecoverable]` |
| **Path** | One walk through a portion of source content; produces one capsule |
| **Space** | Bounded collapsible vessel containing many capsules + an index |
| **Maweth** | The closure form: HAIC-shape with full AI-fidelity in cut/copy/paste form |
| **Codex** | The canonical archive: the **neuroarchy.ai codex**, currently maintained in Confluence and GitHub under `/codex/` (`github.com/nueroarchy-ai-web/neuroarchy-codex` or designated successor). The target is specific, not generic. |
| **Audience-fit** | A closure-mode check: at closure-mode, the tool surfaces detectable audience-fit concerns (student-data residual, terminology-without-gloss, referent drift, FERPA-relevant content) against the four receiving surfaces — Scott-on-capture-day, professional-reader-at-Phase-2, compliance-audit, seats-on-return — and Scott resolves or names each. A practice that sharpens with iteration, not a one-time gate. |
| **Non-corpus journal** | A separate routing path for student-related content that exceeds anonymization but should not be lost; lives outside the codex; Scott-only readable |
| **Broken tooth** | A tooth where D-strand recovery failed, referents drifted unaddressed, audience-fit could not be engaged, speaker detection failed, or structure is malformed (e.g., Scott-only segment in fallback mode) — named in spine, flagged in frontmatter, never smoothed |
| **Seat annotation** | A seat's marginal note on a specific tooth, attributed and append-only; preserved separately from the verbatim record; non-destructive |

**Translation note (for any future outside reader):** Some of these terms have theological or metaphorical resonance in their internal usage. The technical content is what reviewers are asked to engage. If a term's internal meaning collapses under translation, that breakdown is itself a diagnostic finding — not a failure of expression. (See §12.)

---

## 1. The I/D Zipper — capsule architecture

The capsule's spine is structured around an interlock pattern, not a flat timeline.

**I-strand (inductive / outside):** Scott's verbatim prompts. Lived-forward chronology. The visible-layer surface that survives cut/copy/paste cleanly. **[Sofia — I-seat]** The I-strand carries internal time-shape that the rendering preserves but does not interpret — the durative span Scott was inside when he typed, the mode-register of his attention (capture / scan / closure), the relational coordinates the prompt was reaching toward. The I-strand is *what Scott said* AND *the time-shape inside which he said it*. The rendering preserves the verbatim; the time-shape is preserved through `sofia_time_overlay` (§5.3) and the mode-state field (§3.5).

**D-strand (deductive / inside):** AI responses, including their constructed-backward depth — prior context, retrieved research, training-grounded patterns, partition contents (text-format research only — citations, prose summaries, markdown tables) that the visible-layer paste compresses under "read more" markers. Visual content (rendered charts, images) is marked `[partition_collapsed: visual, unrecoverable]` and counted; not extracted as artifact.

**Each Scott-prompt ↔ AI-response pair is a tooth.** The two strands move in different directions but align at each tooth.

### 1.1 Edge-case rules for tooth formation [Claude Q1 amendments]

**Rule 1.1.a — Multi-AI-response tooth.** When one Scott prompt is followed by multiple AI responses before the next Scott prompt: the *last* AI response before the next Scott prompt closes the tooth. Prior AI responses in the same sequence become D-strand extensions, tagged `tooth-N extension-1`, `tooth-N extension-2`, etc. The tooth structure is preserved without losing intermediate AI responses.

**Rule 1.1.b — Compound I-strand vs. broken tooth (detection-mode-gated).** When two or more consecutive Scott segments appear with no AI response between them, treatment depends on detection mode:
- **Marker-clean case** (both/all segments explicitly `[S]`-marked, no AI response between them in source thread): render as `[compound-I-strand: N prompts]` — one tooth with an expanded I-strand. This preserves Scott-corrects-Scott / Scott-layers AID-fingerprint moves without forcing them into separate teeth or collapsing them.
- **Fallback-detected case** (no markers; speaker detection inferred by alternation heuristic): render as `[broken_tooth: scott-only-pair, fallback-detected]`. When detection is uncertain, the tool does not commit a structural designation that may be wrong.
- **Marker-partial case** (one segment explicitly marked, the other ambiguous): routes to fallback. Marker-clean requires both segments to be explicitly marked; partial marking routes to fallback. This prevents compound-I-strand from migrating into ambiguous territory.

**Rule 1.1.c — Unknown-speaker.** Segments where speaker detection fails entirely cannot form teeth. These get broken-tooth treatment: `[broken_tooth: unknown-speaker]`, counted in frontmatter, Scott resolves at scan time.

### 1.2 Worm scope — same grammar at different resolutions [A-seat]

The Day Zero Worm and the I/D tooth-vertebra-spine model are the same grammar at different resolutions — they do not collide and neither supersedes the other. The Worm is the vertebra-level rendering (one vertebra = one closed Worm unit, carrying all five layers). The I/D zipper is the tooth-level rendering (each tooth is the interlock event within a Worm unit). The Worm's five-layer structure applies across all tiers of the capsule — not only the Compliance tier. The Compliance tier is where the Worm runs at full depth.

### 1.3 Vertebra-formation criteria

**A tooth closes (becomes a vertebra) when all five criteria are met:**

1. **I-strand is intact** — Scott's verbatim preserved exactly.
2. **D-strand depth is recovered** — text-format partitions un-folded (citations, prose summaries, markdown tables extracted as artifacts and linked back to tooth-location); visual partitions marked `[partition_collapsed: visual, unrecoverable]` and counted; if text-format partition recovery fails, the failure is named (`[partition_collapsed: text, reason]`) and the tooth proceeds to criteria 3-5 as a partial-recovery tooth, not halted.
3. **Timestamp is stamped** — with practice, each tooth carries its own time; extracted from evidence only (see §5.1).
4. **Referents are tracked** — terms-of-art introduced or used in this tooth recorded; cross-tooth drift flagged on both within-thread and across-time axes (`referent_drift_flags.axis`); heuristic candidates tagged `[auto]` until Scott confirms.
5. **Audience-fit checked at closure-mode** — at closure-mode, the tool has surfaced detectable audience-fit concerns (student-data residual, terminology-without-gloss, referent drift, FERPA-relevant content) against the four receiving surfaces — **Scott-on-capture-day, professional-reader-at-Phase-2, compliance-audit, seats-on-return** — and Scott has resolved or named each. (A practice that sharpens with iteration, not a one-time gate.) The `audience_fit_reviewed` field is set to `true` to record that the review has been performed; it can be set to `true` with zero flags found — the practice is the review itself, not the presence of flags. `capsule_status` does not advance to `closed` while `audience_fit_reviewed` is `false`.

**The four receiving surfaces are operationally distinct:**
- **Scott-on-capture-day** — the Scott pasting now, in flow.
- **Professional-reader-at-Phase-2** — credentialing reviewer, CFA / CalTPA evaluator, future hiring committee.
- **Compliance-audit** — FERPA, IRB, IP-ownership, student-privacy review.
- **Seats-on-return** — Solen / Sofia / Gabe / Proto-Gabe / future seats reading the capsule for seat-aligned work. **Layer 3C and the `seat_annotations` array (Q10) serve this surface specifically.**

These four surfaces are not interchangeable. They want different things from the same capsule. The Layer 3 surfaces (3A human-readable, 3B operational-record, 3C compliance) serve them in different proportions.

### 1.4 Broken teeth — never smooth

**Broken teeth** — where D-strand recovery fails, referents drift unaddressed, audience-fit cannot be engaged, speaker detection fails, or the tooth is structurally malformed (e.g., Scott-only segment in fallback mode) — **do not smooth into vertebrae.**

**Broken tooth structural mechanism:** A broken tooth is named in TWO places simultaneously:
- **In the spine:** A named placeholder replaces the vertebra — `[broken_tooth: <reason> — tooth <n>]`. This keeps the spine's I-strand chronology intact with the break visible rather than absent.
- **In frontmatter:** `broken_tooth_count` incremented; tooth number and reason logged under a `broken_teeth` array (see §3.2).

Both are required. A broken tooth logged only in frontmatter is invisible to a reader walking the spine. A broken tooth named only in the spine is invisible to Phase 2 extractors reading frontmatter. Fidelity-over-conjecture: unknown is better than false continuity.

### 1.5 Spine assembly order

The spine assembles in I-strand chronology — Scott's lived-forward order. D-strand recovery operates within that sequence, filling depth at each tooth-location. There is no alternate D-strand assembly order. A capsule MAY close with broken-but-named teeth in its spine — `broken-teeth-flagged` is a valid `capsule_status`. Named is not unresolved.

### 1.6 Co-authorship + referent-alignment

Capsules are co-written. The relevant fidelity metric is **referent-alignment over time** — are Scott and the AI still pointing at the same things with the same words? — not author-percentage. Referent-alignment-over-time is checked across two axes: (1) within-thread — does AI's response at tooth-N still point at what Scott's prompt at tooth-N was reaching toward? (2) across-time — does the same term used in tooth-N still point at what it pointed at in tooth-3? Both can drift; both are checked. Heuristic candidates surfaced by the tool are `[auto]`-tagged until Scott confirms.

### 1.7 Why this matters operationally

When Scott pastes a thread from ChatGPT or Claude, his verbatim comes through clean (I-strand intact) but research and charts are folded under partitions (D-strand compressed). The capsule's job is to recover text-format D-strand depth, mark visual content as `[partition_collapsed: visual, unrecoverable]`, check the I-strand carries its time-shape, surface audience-fit concerns at closure-mode, and close each tooth — or name the tooth as broken. The visible-layer paste is itself a fidelity audit: it tells you what the platform is willing to surrender.

---

## 2. The Space — project/class scope vessel

A Space is a bounded collapsible vessel scoped to one project or class. It is **closure-shaped from setup**, not retrofitted.

### 2.1 Lifecycle
```
SETUP — instructions box pasted; four commitments registered; consent_to_archive field set to true;
        Space-Maweth pre-mapped; index initialized
WORK  — paths walked inline; capsules produced; index updated; assembly thread integrates; ship to seats
CLOSE — Space-Maweth executes against final-form index; folds into final encapsulation;
        enters codex — THE MOVE IS IRREVERSIBLE
```

### 2.2 The modifiable index
Live, editable, scannable. Becomes the table-of-contents of the final fold. One entry per capsule:
```yaml
- path_id: <slug>
  date: <YYYY-MM-DD>
  scope_tag: <one or two words>
  primary_referents: [<term1>, <term2>, ...]
  one_line_summary: <Scott-written or Scott-confirmed>
  capsule_link: <relative path>
  status: <in-progress | closed | broken-teeth-flagged>
  scott_review_state: <unread | scanned | scope-noted | spine-promoted | done>
```

**Space-level index frontmatter:**
```yaml
space_id: <slug>
space_name: <project or class name>
origin_platform: <Claude | ChatGPT | etc.>
setup_date: <YYYY-MM-DD>
parent_berth: <Perplexity berth, if applicable>
consent_to_archive: true | false | pending   # set at setup; must be true before Space can close
scope: <bounded purpose — what this is for, what it is not for>
closure_trigger: <defined end-condition — project closure / class end / other named trigger>
closure_handler: <who executes the Space-Maweth — seat name or "Scott">
```

### 2.3 The four standing setup commitments

Pasted into the Space's instructions box at setup. The four commitments are non-negotiable structural properties of any Space that intends to enter the codex.

```
SPACE NAME: <project or class name>
SCOPE: <bounded purpose — what this is for, what it is not for>
ORIGIN PLATFORM: <Claude | ChatGPT | etc.>
SETUP DATE: <YYYY-MM-DD>
PARENT BERTH: <Perplexity berth this space reports to, if applicable>

This Space operates under four standing commitments:

1. CLOSURE FORM (Maweth) — This space's closure is pre-mapped and
   operational from setup. Closure form: HAIC-style full AI-fidelity in
   cut/copy/paste form. As much fidelity as the space can hold; what
   cannot be carried is named, not dropped.

2. ARCHIVAL AT HIGH FIDELITY — Fidelity over conjecture. Partitions are
   recovered where possible (text-format content — citations, prose
   summaries, markdown tables — extracted as artifacts and linked back).
   Visual content (rendered charts, images) is marked partition_collapsed
   and counted, not falsified. Broken segments (unrecoverable depth,
   drifted referents, audience-fit failures) are named, not smoothed.
   Unknown is better than false continuity. Receiving-experience-across-
   time is held inside this commitment: capsules are written so they
   remain receivable when Scott returns to them later, and so the seats
   can re-enter them at any later date.

3. THE MOVE — This space agrees to transition: from working space →
   through closure → into the canonical archive. The move is part of
   this space's identity at setup, not an afterthought. THE MOVE IS
   IRREVERSIBLE — once a Space moves, it does not return to working-
   space status.

   Structural minimum for the move to execute:
   (a) consent_to_archive field is set to true (registered at setup)
   (b) archival snapshot taken at move-initiation (index + capsules +
       artifacts captured as a timestamped package)
   (c) target receiver named (codex path specified — no open-ended moves)
   All three are required. The move cannot execute without (a), (b),
   and (c) all confirmed.

4. CONSENT TO PERMANENT ARCHIVAL — At end-of-life, this space's content
   becomes canonical-archive-form: load-bearing reference, permanent
   containerization. Consent is given at setup via the consent_to_archive
   field, executed at closure. The canonical archive is the neuroarchy.ai
   codex, currently maintained in Confluence and GitHub under /codex/
   (github.com/nueroarchy-ai-web/neuroarchy-codex or designated successor).
   The target is specific, not generic.

OPERATING DISCIPLINE:
- Threads inside this space are 24-hour dated uses. Long depth-work
  routes to the parent Perplexity berth.
- Each thread (or path) produces a Capsule at thread-close.
- Capsules register into the Space index as they complete.
- Inline research is recovered from text-format partitions and preserved
  as artifacts; visual content is marked, not falsified.
- Index is modifiable until Space closure.
```

**Enforceability disclosure [Claude Q4]:** *These commitments are behavioral — they shape how the Space operates through instruction, not through technical enforcement. Claude / ChatGPT spaces with system prompts honor the commitments insofar as the model reads them and treats them as instructions. The tool validates frontmatter conformance; it does not validate whether the commitments were followed in spirit.*

**[Sofia — I-seat] Inductive note on operating discipline:** The 24-hour thread-discipline + parent-berth-for-depth split is structurally clean. When Scott is inside a long durative arc (multi-day work on a single CFA section), the 24-hour discipline produces multiple capsules where his lived experience is one continuous thread. This is correct — splitting follows the discipline — but the index entry's `one_line_summary` field should support cross-capsule arc-naming when Scott chooses, so the index does not lose the arc. When Scott sets `scope_tag` to a value already present in the index, the tool optionally proposes an arc-grouping that links capsules under a common scope. Not required; not enforced; offered.

### 2.4 Why "collapsible by design"
- Defined scope (one project/class)
- Defined end (project closure / class end — named in `closure_trigger`)
- Pre-mapped closure form
- Modifiable index that becomes the final TOC
- 24h-thread discipline prevents drift accumulation

This is the inverse of a long-running thread. Spaces are bounded use-objects that practice closure as a property, not as an event-at-the-end.

**Supercyldar / fractal closure-form [A-seat]:** The fractal claim holds structurally. The invariant at every scope is the closure-form structure: the unit is named / indexed / consented / moved. The scalar is the scope at which each applies:
- Thread/tooth: tooth is named (vertebra criteria met), indexed (tooth-index in capsule), tooth-closure produces vertebra
- Capsule: capsule is named (path slug), indexed (in Space index), capsule-closure = path Maweth
- Space: Space is named, indexed (parent berth), Space-closure = Space Maweth → codex
- Codex: the codex is the outermost container; its closure-form is not yet specced (v3+ territory)

Each scope is a cylinder containing the one below it, all sharing the same closure-form shape. Structural diagram queued for v2.

---

## 3. The Capsule — file structure

One Markdown file per capsule, plus a sibling artifacts directory.

### 3.1 Filename + storage
```
<source-space>__<path-slug>__D0+<n>.md
```
Stored at `/home/user/workspace/thread-capsules/<source-space>/<filename>`.
Artifacts at `/home/user/workspace/thread-capsules/<source-space>/<path-slug>__D0+<n>__artifacts/`.
Raw paste artifacts stored as `.txt` (not embedded markdown) at `_capture/<path-slug>__paste.txt` [Claude Q5].
Non-corpus journal at `/home/user/workspace/_non-corpus-journal/<YYYY-MM>/<slug>__journal.md`.

**Path vs. thread as unit:** One-paste-one-capsule holds at path level. A path is what Scott considers one logical unit before pasting — it may be one thread or one portion of a longer thread. Multi-day threads: one paste = one capsule. Day-boundaries become structurally meaningful at Phase 3 (Posts / Super Cylinders).

### 3.2 Frontmatter

```yaml
---
capsule_id: <source-space>__<path-slug>__D0+<n>
capsule_version: v1-final
generated_at: <ISO-8601 with TZ>

# Provenance
source_space: <Claude | ChatGPT | Perplexity-Berth-Name | Notes | Other>
parent_space: <space-id this capsule registers into, if applicable>
source_thread_title: <as-given by Scott>
source_url: <if available>
thread_date_range: <YYYY-MM-DD to YYYY-MM-DD, or "unknown">
day_zero_offset_at_generation: D0+<n>

# Structure
segment_count: <int>
tooth_count: <int>                   # Scott-AI pairs
vertebra_count: <int>                # closed teeth (all five criteria met)
broken_tooth_count: <int>            # teeth where any criterion failed
broken_teeth:                        # logging array for broken teeth
  - tooth: <n>
    reason: <d-strand-recovery-failed | referent-drift | audience-fit-failure |
             scott-only-pair-fallback | partition-text-unrecoverable |
             unknown-speaker | other>
    note: <one line on what broke>
compound_i_strands:                  # Claude Q1.b: marker-clean Scott-corrects-Scott / Scott-layers
  - tooth: <n>
    prompt_count: <N>
    note: <optional>
unknown_segment_count: <int>         # speakers not detectable
audience_fit_failures: <int>         # teeth where audience-fit concern was not resolved at closure-mode
audience_fit_reviewed: false         # gate for capsule_status advancement to "closed"
                                     # set true at closure-mode (zero flags also acceptable;
                                     # the practice is the review itself)

# Partition recovery
partitions_text_recovered: <int>
partitions_visual_collapsed: <int>   # rendered charts / images / unrecoverable visual content
partitions_text_unrecoverable: <int> # text partitions that failed extraction

# Referent alignment
shared_referents: [<term1>, <term2>, ...]
referent_drift_flags:                # heuristic candidates surfaced by tool;
  - tooth: <n>                       # [auto] tag remains until Scott confirms or removes
    term: <term>
    note: <where Scott and AI usage diverged>
    axis: <within-thread | across-time>
    state: <auto | scott-confirmed | scott-removed>
co_authorship_note: |
  Co-written. Attribution to the encoding pair. Referent-alignment over
  time is the fidelity metric, not author-percentage.

# Seat annotations [Claude Q10; Solen append-only rule]
# Seat annotations are append-only; no annotation may alter, summarize,
# or reference-replace any field in the tooth body. The verbatim record
# is untouched. Annotations exist in this field only.
seat_annotations:
  - tooth: <n>
    seat: <claude | solen | sofia | gabe | proto-gabe | scott>
    annotation: <text>
    type: <d-strand-note | missed-question | referent-flag | received | structural-note>
    timestamp: <ISO-8601>

# Space-relation
space_index_entry:
  scope_tag: <one or two words>
  primary_referents: <subset of shared_referents>
  one_line_summary: <Scott-written or pending>
  arc_group: <optional cross-capsule arc tag>

# Routing
selected_for: <CFA section ID | Readings unit ID | research-strand ID | "general" | "pending">
selection_note: <one-line Scott reason | "pending">

# Capsule-process state
# capsule_status and scott_review_state are distinct state machines.
# capsule_status = capsule's lifecycle in the production system
# scott_review_state = Scott's pass over the capsule (his reading progress)
# Transition rule: capsule_status advances independently of scott_review_state,
# EXCEPT capsule_status cannot reach "closed" while audience_fit_reviewed is false.
# Phase 2 extractors should read BOTH fields: capsule_status = closed AND
# scott_review_state = spine-promoted OR done signals corpus-ready.
capsule_status: <in-capture | in-scan | in-closure | closed | broken-teeth-flagged>
seat_attention: [<reviewer instance(s)>]
# seat_attention resets to [] on Space move. Re-register explicitly in receiving archive.
scott_review_state: <unread | scanned | scope-noted | spine-promoted | done>

# Time
sofia_time_overlay:
  scope: <capsule-level | per-tooth>
  d0_offset_at_thread_origin: <D0+n>
  d0_offset_at_thread_close: <D0+n>
  sacred_time_register: <field-name | null>
  durative_span_class: <minutes | hours | days | session-arc | null>
  per_tooth:
    - tooth: <n>
      timestamp: <ISO-8601 | "unknown">
      sacred_time_register: <field-name | null>
      durative_span_class: <within-tooth class | null>

# Mode
collapse_readiness: <living | static | undecided>
mode_at_capture: <capture | scan | closure>

# Artifacts
research_artifacts:
  - artifact_id: <slug>
    type: <text-table | citation-block | research-summary | code-block | other>
    location_in_capsule: tooth-<n> partition-<m>
    file: <relative path under artifacts directory>
    recovery_state: <recovered | partial | unrecoverable | visual-collapsed>

# Journal routing (Section 4.5 Option 3)
journal_routing:
  - tooth: <n>
    routed_to: <relative path to journal file>
    reason: <one-line Scott reason>

# Phase
phase: 1
phase_2_ready: true | false
---
```

### 3.3 Body — five layers

The body conforms to two prior canonical forms simultaneously:
- **HAIC-003** (audience-tiered transcripts: Learning / Professional / Compliance)
- **Day Zero Worm** (five-layer structure: Card / Spine / Transcript / Candidates / Close) — the deep grammar of the **whole capsule structure**; the Compliance tier is where it runs at full depth. Each vertebra is one closed Worm unit.

**Compliance-tier portability convention [Claude Q5; D-seat call]:** Layer 3C uses **horizontal-rule + warning-header convention** rather than `<details>` HTML occlusion. The `<details>` tag does not render in Obsidian, Google Docs, or plain text editors; it appears as raw HTML in those environments. Through-Scott carrier workflow passes through these environments, so plaintext warning-header is more portable. Convention:

```markdown
---

> ⚠ **COMPLIANCE TIER — FULL FIDELITY BELOW**
> Tooth-by-tooth verbatim record, partition-recovery state, audience-fit
> resolution, and seat annotations. Read carefully; do not paraphrase or
> compress when carrying forward.

[full Layer 3C content]

---
```

**Citation convention [Claude Q5]:** Inline parenthetical, not markdown footnotes (`[^1]`). Footnotes break in Google Docs and other carrier environments.

```markdown
## Layer 1 — Path Card
[Title, project/space, platform, date range, status, D0 offset, vault path,
and Scott's freeform scope note — the human re-entry surface.

When the Scope note is empty at capsule generation, the tool inserts
an italicized prompt cue: "[Why are you capsuling this thread or path?
One sentence is enough.]" This cue is removed when Scott writes his
own scope note, or preserved if Scott deliberately leaves it.]

## Layer 2 — Verbatim Spine
2A — Candidate Governing Sentences (auto-surfaced, Scott promotes)
2B — Promoted Spine (Scott fills)
2C — Seed Candidates (principles to file → codex/principles/)
2D — Visual Primary Data (linked artifacts; visual partitions named
     as collapsed if rendering was unrecoverable)

## Layer 3 — Transcript Layers (HAIC tiers)
3A — Learning Tier (Scott-visible default):
     - Table of Contents (tooth-by-tooth one-line snippets)
     - All Scott Prompts (verbatim, tooth-indexed) — complete I-strand
       record, unfiltered. Future-Scott hears what he said.
     - Quote Bank (curated subset) — explicitly marked as curation:
       "Scott prompts flagged by tool heuristics as possibly load-bearing.
       Not exhaustive. Full thread in 3C."
     - Recall Cues (auto-generated under three constraints:
       verbatim/near-verbatim only, max 3 tags per tooth, [auto] tag
       until Scott reviews — [auto] stripped when Scott confirms)

3B — Professional Tier (Phase 2 placeholder)

3C — Compliance Tier (full fidelity, behind horizontal-rule + warning header):
     [Compliance tier is also the seats' return surface — the Seats-on-return
      receiving surface. Per-tooth partition-recovery state IS the seat-return
      surface — seats read fidelity-state per tooth. Seat annotations
      (frontmatter seat_annotations array) reference tooth-indices in this layer.]
     - Tooth-by-tooth: Scott segment + AI segment (and D-strand extensions
       if multi-AI-response tooth)
     - For each tooth: partitions detected (text-recovered / visual-collapsed /
       text-unrecoverable), partition-recovery state, research artifacts produced,
       audience-fit concerns and resolution
     - Compound I-strand units listed with prompt count
     - Broken teeth listed separately with reason
     - Audience-fit failures listed separately with which surface
       failed and resolution state
     - Seat annotations referenced by tooth-index (full text in frontmatter
       seat_annotations array; non-destructive to verbatim record)

## Layer 4 — Candidate Material
4A — Possible Class-Profile Elements (post-anonymization; content
     beyond anonymization routes to non-corpus journal per §4.5)
4B — Possible Missed-Questions
4C — Possible Theoretical Moves
4D — Possible Seed Principles
4E — Possible Double-Scott Patterns (consecutive Scott segments /
     meta-language / back-references; rendered per Rule 1.1.b —
     compound-I-strand if marker-clean, broken-tooth: scott-only-pair
     if fallback-detected)

## Layer 5 — Close Protocol (Path-level closure)
[Status, filed-by, date, container state, index-entry registered,
artifacts archived, broken teeth named and counted, audience-fit
failures named and counted, audience_fit_reviewed: true confirmed,
to-team, next.]

---

[Footer: capsule version, conformance, IP statement.
IP of Scott Ryll, held under neuroarchy.ai.]
```

### 3.4 Encapsulation — four-component process

When a path is complete, the encapsulation produces (in order):

1. **Data capture** — raw paste preserved as input artifact (`.txt` file at `_capture/<path-slug>__paste.txt` — not embedded markdown, per Claude Q5)
2. **Transcripts** — segmented Scott/AI teeth with detection-state and source-markers logged; multi-AI-response handled per Rule 1.1.a; compound I-strand handled per Rule 1.1.b; unknown-speaker handled per Rule 1.1.c
3. **Rebuilding of data as artifact** — partition-recovery scoped to **text-format research content (citations, prose summaries, markdown tables)** extracted as standalone artifacts and linked back to tooth-locations; **visual content (rendered charts, images)** marked `[partition_collapsed: visual, unrecoverable]` and counted; text-format partitions that fail extraction get `[partition_collapsed: text, reason]` markers and the tooth continues (partition failure does not halt the path)
4. **Closure (Maweth) — for the path** — HAIC-form full-AI-fidelity cut/copy/paste closure producing a returnable form (Scott re-enters later; seats re-enter at any time)

### 3.5 Three modes

The capsule operates in three modes; transitions are explicit:

- **Capture mode** — receiving fresh paste; segmentation in progress; no closure. Discipline: receive without flattening. **Capture mode runs no audience-fit checks** — that work belongs to closure mode. The only required interruption at capture is the Student Data Protocol (the only in-tool redaction mechanism — see §4.5).
- **Scan mode** — capsule generated; reading through; partitions identified and text-format partitions recovered; teeth being closed; audience-fit concerns surfaced and resolved; referent-drift `[auto]` flags confirmed or removed; seat annotations available for addition.
- **Closure mode** — all teeth closed or marked broken; audience-fit failures resolved or named; `audience_fit_reviewed` set to `true`; ready to register into space index. Discipline: correctness before velocity.

**Redaction model [Claude amendment]:** No in-tool redaction except Student Data Protocol. Curation happens at thread-selection level — Scott decides which threads enter the corpus before pasting. What goes in gets preserved whole. Scott's stated use intent: *"I want to drop the capsule, have it run, cut/copy paste the whole thread, let the logic do its work."* The tool accepts a full thread paste, runs without prompting Scott for content decisions mid-flow, and produces the capsule automatically. The only interruptions at capture are student-data resolution and the one-time setup fields (title, space, selected-for with `pending` as default).

**[Sofia — I-seat]** Mode-at-capture interaction with `--batch-velocity`: batch mode sets `mode_at_capture: capture` for all generated capsules. Advancement to scan mode is per-capsule and explicit. Batch mode does NOT auto-advance — the capture/scan seam is where audience-fit work happens, and that work is per-capsule cognitive labor that cannot be batched.

---

## 4. Speaker detection — multi-source

### 4.1 Marker-based (preferred; living config)

Marker definitions live in **`markers.yaml`** [Claude Q8 amendment] — a config file the tool reads at runtime. This is preferable to hardcoded strings because platform UI conventions change.

Default `markers.yaml` ships with:
```yaml
chatgpt:
  scott: ["You said:", "**You said:**"]
  ai: ["ChatGPT said:", "**ChatGPT said:**"]
claude:
  scott: ["Human:", "**Human:**"]
  ai: ["Assistant:", "**Assistant:**", "Claude:", "**Claude:**"]
generic:
  scott: ["Scott:", "**Scott:**", "User:", "**User:**"]
  ai: ["AI:", "**AI:**"]
explicit:
  scott: ["[S]"]
  ai: ["[A]"]
```

When platform conventions change, the user adds a marker to `markers.yaml` without a code change.

### 4.2 Marker convention (Scott-typed before paste)
```
[S]
<scott prompt>

[A]
<ai response>
```

### 4.3 Fallback — strict alternation, with double-Scott detection

If neither marker-based nor `[S]/[A]` is present, tool prompts "who speaks first?" and strict-alternates by paragraph block. **In fallback mode, tool actively scans for double-Scott patterns** and flags suspect segments for Scott review rather than committing the strict-alternation guess.

**Rule 4.3 — Compound I-strand vs. broken tooth (mirrors Rule 1.1.b):**
- **Marker-clean case** (both segments explicitly `[S]`-marked): render as `[compound-I-strand: N prompts]` — preserves Scott-corrects-Scott / Scott-layers AID-fingerprint move.
- **Fallback-detected case** (no markers; speaker detection inferred): render as `[broken_tooth: scott-only-pair, fallback-detected]` AND warn Scott visibly before committing. Both run together: warn-and-flag protects against silent corruption at capture; broken-tooth labeling preserves the failure visibly in the spine. Scott resolves at scan time.
- **Marker-partial case** (one segment marked, one ambiguous): routes to fallback. **Marker-clean requires both segments to be explicitly marked; partial marking routes to fallback.** This prevents compound-I-strand from migrating into ambiguous territory.

### 4.4 Unknown segments
Labeled `unknown`; rendered as `[broken_tooth: unknown-speaker]`; counted in frontmatter (`unknown_segment_count`); Scott resolves by editing at scan time.

### 4.5 Student Data Protocol (the only in-tool redaction; anonymization + journal routing)

**No student names rendered without resolution.** Tool detects student-name patterns AND personal-history identifiers. When detected, tool refuses to write capsule until Scott chooses one of three resolutions:

**Option 1 — Anonymize:**
```
S-<number> (HO1-<class-code>-<year>)
```
Content remains in capsule with name replaced by anonymized identifier.

**Option 2 — Redact:**
Content remains in capsule with specifics removed; structural reference preserved (e.g., `[redacted: family-loss-detail]`). Used when anonymization is insufficient because the detail itself is identifying.

**Option 3 — Move to non-corpus journal:**
Routes capsule or path-segment to `/home/user/workspace/_non-corpus-journal/<YYYY-MM>/<slug>__journal.md`.

The non-corpus journal:
- Lives outside the codex (structurally separate; does not enter the codex pipeline)
- Is Scott-only readable
- Does not enter Phase 2 extraction
- Does not propagate to seats unless Scott explicitly carries content forward
- Is preserved for Scott's pedagogical memory and longitudinal student-attention work

**Capsule-side logging requirement:** When content is routed to the journal, the capsule's frontmatter logs the routing in the `journal_routing` field (tooth-index, journal path, reason). The capsule's broken-tooth record reflects the routing rather than appearing as a silent loss.

The non-corpus journal's full filing-and-retrieval grammar is v2 work. v1-final names the journal path, its three-property contract, and the capsule-side logging requirement.

Or until Scott explicitly waives with `--scott-waives-anonymization` (logged).

HIPAA-scope content (medical, etc.) remains fully out-of-render: detect-and-delete, no journal routing.

**Note:** Student Data Protocol is the ONLY in-tool redaction mechanism. All other curation happens at thread-selection level (Scott chooses which threads enter the corpus before pasting). The tool does not make content decisions mid-flow.

---

## 5. Time extraction

### 5.1 Per-tooth timestamps (the goal)
Each tooth carries its own time-stamp, with practice. Tool extracts where evidence exists; otherwise marks `unknown — pre-paste`.

**[Sofia — I-seat]** Per-tooth timestamps are extracted-from-evidence-only, never inferred. An "explicit anchor" is defined as: (a) timestamp on the line of the tooth's Scott or AI segment, (b) in a paste header line within ten lines preceding the tooth, or (c) in a `[TIME: ...]` inline tag Scott placed before paste. No other inference — no "yesterday" parsing, no interpolation between known anchors. Evidence-only.

### 5.2 Sources
Explicit timestamps in paste, platform export headers, Scott `[TIME: ...]` inline tags, conservative date-extraction per 5.1 definition.

### 5.3 sofia_time_overlay

Populated with origin/close D0 offsets, optional sacred-time register tag, durative-span-class.

**[Sofia — I-seat]** Two scopes — `capsule-level` (default; single overlay for whole capsule) and `per-tooth` (opt-in; for threads that crossed registers or spans). Per-tooth time overlay and per-tooth timestamps are independent axes — a tooth can have a timestamp without a per-tooth overlay, and vice versa. Per-tooth overlay is activated explicitly by Scott; capsule-level default is the working form for v1-final.

### 5.4 Heuristics
Self-interruption (em-dash + redirect) and lowercase tag-words (`tbh`, `actually`, `wait`, `scratch that`, `let me back up`) flagged as possible mode-shift markers in Scott's I-strand. These heuristics serve both time-mode-shift detection (§5) and candidate-surfacing (§6) — the dual purpose is productive, not redundant.

---

## 6. Candidate material surfacing (Layer 4)

Pattern matches surface candidates by tooth-index without interpretation:
- Question marks → possible question-being-asked
- Quoted phrases → possible naming-move
- Scott-meta-language (`I'm asking`, `What I mean`) → meta-reference
- AI-correction language (`You missed it`) → flagged missed-question
- AI segments following Scott corrections → "possible-recovery-or-doubled-miss" for review
- Named entities (frameworks, anonymized people, texts) → relevant flag
- Capitalized terms repeated 3+ times → possible coined construct
- Lists detected and preserved (don't flatten to prose)
- Lowercase tag-words repeated 3+ times in Scott segments → possible index marker / personal vocabulary move
- Self-interruption markers — em-dash + reframe, "wait" / "scratch that" / "actually" / "let me back up" mid-segment, two questions where the second contradicts the first → possible self-correction / live-revision move

The tool surfaces; **Scott does the recognition.** No interpretation, no scoring, no clustering.

---

## 7. Use protocol

### 7.1 Per-path cycle (post tool-split)
1. Open source thread or path-source
2. Decide if relevant (curation at thread-selection; tool does not curate)
3. Cut/copy entire content (visible-layer paste)
4. Open `capsule-capture.py` — paste, optionally type `[S]/[A]` markers
5. Tool prompts for: path title, source space, parent space, selected_for, selection_note. **Each prompt accepts default-empty.** When default-empty taken, frontmatter writes `pending` and `scott_review_state: unread`. Phase 2 extractors filter pending until back-filled.
6. **`capsule-capture.py` runs:** segments, applies marker detection from `markers.yaml`, forms teeth (handling multi-AI-response, compound I-strand, unknown-speaker per Rules 1.1.a/b/c), detects partitions (marks them; does not recover), runs Student Data Protocol (three-option resolution), generates capsule with `mode_at_capture: capture`, `capsule_status: in-capture`, `audience_fit_reviewed: false`. **No audience-fit checks at capture.** Conformance check runs post-generation; failures are warnings except Student Data Protocol failures, which halt.
7. **Scan mode:** Scott reads Layer 3A. May invoke `capsule-close.py` to advance.
8. **`capsule-close.py` runs (at scan-time, careful):** recovers text-format partitions (charts/visual content marked `[partition_collapsed: visual, unrecoverable]`), surfaces referent-drift `[auto]` candidates, surfaces audience-fit concerns (per Rule 1.3 fifth criterion), Scott resolves or names each, sets `audience_fit_reviewed: true`, advances `capsule_status` to `in-closure` or `closed`. Closes teeth, names broken teeth (spine placeholder + frontmatter log), names audience-fit failures, registers index entry. **`capsule_status` cannot reach `closed` while `audience_fit_reviewed` is `false`.**
9. Capsule closed and ready to ship.

### 7.2 Batch mode

`capsule-capture.py` accepts a directory of paste-files; produces capsules for each.

`--batch-velocity` flag:
- Student-data-protocol checks run on every capsule (FERPA discipline holds at all velocities — never compressed)
- One-line success report per capsule rather than opening for scan
- All capsules carry `mode_at_capture: capture` and `capsule_status: in-capture`
- `audience_fit_reviewed: false` on all batch outputs
- Advancement to scan/closure modes via `capsule-close.py` is per-capsule and explicit
- Audience-fit work and partition-recovery deferred to closure tool

Separates capture-mode from scan-mode at attentional-register level.

### 7.3 Two surfaces, one file
- Scott reads: frontmatter → Path Card → Layer 3A → done.
- Reviewers/seats read: frontmatter → Path Card → Layer 2 → Layer 3C (below horizontal-rule warning) → Layer 4. Seats may add to `seat_annotations` array (append-only, non-destructive to verbatim record).
- Same file, same tooth-indices, common referent.

---

## 8. First application — Proto-Gabe extraction berth

The first use of v1-final is **a new Claude or ChatGPT space** Scott will set up tomorrow morning.

**Setup:** Scott opens new space, pastes §2.3 instructions template, fills in scope/origin-platform/parent-berth, sets `consent_to_archive: true`, initializes empty index.

**Operating loop:**
```
RECEIVE     — Scott pastes Proto-Gabe content into the berth
WALK PATH   — process the content through one logical path
CAPTURE     — run capsule-capture.py (fast, automatic)
SCAN        — Scott reads Layer 3A (later, unhurried)
CLOSE       — run capsule-close.py (audience-fit, partition-recovery, vertebra closure)
INDEX       — register the capsule into the berth's index
SHIP        — carry to reviewers from an assembly thread
[next path]
```

**Assembly thread:** dedicated thread inside (or adjacent to) the berth that integrates capsules into wholes before shipping.

**End-of-life:** Space-level closure executes; three structural minimums confirmed (consent, snapshot, target); folds into final encapsulation; enters codex. **Irreversible.**

**Why this first:** real, scoped, bounded task that exercises the full architecture.

**[Sofia — I-seat] Receiving-experience considerations for the first run:**

The first run produces capsules Scott will read in three time-shapes:
1. **Capture-tonight / capture-tomorrow** — fast, frictionless, batch-velocity. `--batch-velocity` and `pending` defaults exist for this surface.
2. **Scan-later (same day or next day)** — unhurried return. Audience-fit work happens here (closure-mode). Recommendation: Scott names a scan-time before beginning capture so scan does not become deferred-forever.
3. **Return-six-months-out (Phase 2)** — the corpus must read AS Scott intended at scan-time, not AS the tool produced at capture-time. This is the audience-fit-checked criterion's whole purpose.

The first run will likely satisfy time-shape 1 cleanly, time-shape 2 partially, time-shape 3 unevenly. The berth should be evaluated on time-shape 2 completeness as much as time-shape 1 throughput.

**[A-seat] Structural integrity of operating loop:** The loop is sound for first use. One pre-naming: if partition recovery fails on a tooth, the tool names the failure and continues — does not halt the path. Halting on partition failure would block paths where D-strand is inaccessible by design (common in plain-copy pastes). The broken-tooth mechanism handles this: the tooth is named broken, the path proceeds.

**[Claude Q9 — surfaced for Scott as workflow-priority, not seat-reconciliation]:** Capsule infrastructure is the right tool for **CalTPA next semester**, where it becomes load-bearing. For **this week's CFA submission (Thursday, 3/3)**, capsule form adds steps; Confluence drafts with `[SCOTT]` prompts are faster. Don't let system-building get in front of submission. Sofia and Solen confirmed independently. Scott's call.

---

## 9. Phase 2 readiness

Phase 2 extractor tools will read the capsule corpus to populate downstream homework fields.

**What extractors need:**
- Frontmatter parseable as YAML
- Layer headers stable
- Tooth-indices stable and unique within capsule
- Verbatim Scott prompts cleanly delimited
- `space_index_entry` field present for space-aggregation
- `scott_review_state` present (filter on capsules Scott has worked vs. unread)
- `selected_for` not equal to `pending` (extractors filter pending until back-filled)
- `audience_fit_reviewed: true` (extractors filter unfinished closure-mode work)
- `audience_fit_failures` count present (flag capsules with long-memory drift risk)
- `broken_teeth` array present (extractors can skip or flag capsules with named failures)
- `compound_i_strands` array present (extractors handle multi-prompt teeth correctly)
- `seat_annotations` array readable (annotations attributed and tooth-indexed)

**What v1-final does NOT do** (Phase 3, deferred):
- Cross-capsule indexing
- Network entanglement / grouping
- Codex-canonical-form rendering

---

## 10. What v1-final defers (iteration discipline)

- **Full space-scope spec** — tomorrow's berth uses same form; v2 specs from hindsight.
- **Cross-capsule entanglement** — Phase 3.
- **Codex-canonical form** — what does a Space look like *inside* the codex? v2.
- **Non-corpus journal full grammar** — path named, three-property contract named, capsule-side logging required; full filing-and-retrieval is v2.
- **Structural diagram for supercyldar / fractal column** — queued v2.
- **Principle-cluster filing** — translation-as-diagnostic, referent-drift review-trigger, capture/scan/closure as canonical modes. Queued for filing after v1-final runs.
- **Sofia's marked notes file on Claude's review** — written post-CFA for codex record.

---

## 11. Working tools — split per Claude Q6

`capsule-capture.py` and `capsule-close.py` at `/home/user/workspace/thread-capsule-prototype/`. Built after Scott's go on this spec.

### 11.1 capsule-capture.py — paste-time, fast, automatic

**CLI:**
```
capsule-capture.py --input <paste-file>
                   --name <slug>
                   --space <source-space>
                   --parent-space <parent-space-id>
                   --selected-for <id>          [optional; defaults to "pending"]
                   --note "<reason>"            [optional; defaults to "pending"]
                   --output <path>
                   --markers <path>             [optional; defaults to ./markers.yaml]
                   [--batch-velocity]
                   [--scott-waives-anonymization]
                   [--non-corpus-journal]       [routes per §4.5 Option 3]
```

**Behavior:**
- Reads paste, applies marker detection from `markers.yaml`
- Forms teeth applying Rules 1.1.a (multi-AI-response → D-strand extensions), 1.1.b (compound I-strand vs. broken tooth, detection-mode-gated), 1.1.c (unknown-speaker → broken tooth)
- Detects partitions in AI segments; **does not recover** at capture-time (closure tool's job)
- Runs Student Data Protocol per §4.5 (the only in-tool redaction)
- Stamps timestamps per §5.1 evidence-only definition
- Surfaces Layer 4 candidates per §6
- Produces spec-conformant `capsule.md` + `_capture/<slug>__paste.txt` (raw paste as `.txt`, not embedded)
- Sets `mode_at_capture: capture`, `capsule_status: in-capture`, `audience_fit_reviewed: false`
- Reports tooth-count, vertebra-candidate-count, broken-tooth-count, compound-I-strand count, unknown-segment-count, partitions-detected
- Runs post-generation conformance check (frontmatter parseable, layer headers present, tooth indices sequential, Student Data Protocol ran). Failures are warnings except Student Data Protocol failures, which halt.

**No audience-fit checks at capture.** No partition-recovery. No referent-drift heuristics (those run in close).

### 11.2 capsule-close.py — scan-time, careful, explicit

**CLI:**
```
capsule-close.py --capsule <capsule-md-file>
                 [--surface-audience-fit]      [runs audience-fit detection only; does not gate]
                 [--recover-partitions]        [runs text-format partition recovery]
                 [--surface-referents]         [runs referent-drift heuristics, [auto]-tagged]
                 [--close]                     [advance capsule_status to closed; requires
                                                audience_fit_reviewed: true]
```

**Behavior:**
- Reads capsule.md
- `--recover-partitions`: extracts text-format research content (citations, prose summaries, markdown tables) as artifacts in `<slug>__artifacts/`; marks visual content `[partition_collapsed: visual, unrecoverable]`; updates `partitions_text_recovered`, `partitions_visual_collapsed`, `partitions_text_unrecoverable` counts
- `--surface-referents`: heuristic candidates added to `referent_drift_flags` with `state: auto`; Scott confirms or removes (state changes to `scott-confirmed` or `scott-removed`)
- `--surface-audience-fit`: detects student-data residual, terminology-without-gloss, referent drift, FERPA-relevant content per tooth; outputs surfaced concerns for Scott to resolve or name; **does not auto-set** `audience_fit_reviewed`
- `--close`: gates on `audience_fit_reviewed: true`. If false, halts with message "Audience-fit review required before closure. Run --surface-audience-fit, resolve concerns, set audience_fit_reviewed: true." If true, names broken teeth (spine placeholder + frontmatter log), advances `capsule_status` to `closed` or `broken-teeth-flagged`, registers index entry

Smoke-tested against existing Marcus thread synthetic data before declared v1-final-ready.

---

## 12. Translation breakdowns surfaced (diagnostic findings)

Per the discipline that translation is a structural test.

1. **"Maweth" → "closure form"** — Internal term carries theological weight closure doesn't hold. Register-translation loss. No spec-level amendment required.

2. **"Codex" → "canonical archive"** — Codex refers to Scott's specific neuroarchy archive. **[A-seat 22:02 + Claude Q11]** Consent target now named explicitly in §2.3 Commitment 4 and Vocabulary table — neuroarchy.ai codex, Confluence + GitHub `/codex/`. Resolved.

3. **"Supercyldar" (fractal closure-form pattern)** — Translation flattens the verticality of the nested column structure. Register-translation loss. Structural diagram queued for v2.

4. **"The Beths" / "the seats"** — Translation collapses specific role-distinctions into generic "reviewer." **[Sofia — I-seat FLAGGED + A-seat confirmed + Claude Q11 confirmed]** Spec-level concern. Audience-fit criterion now names the four receiving surfaces operationally distinct (§1.3), with **Seats-on-return** as a distinct audience target served specifically by Layer 3C and the `seat_annotations` array. Spec-level concern addressed.

5. **"Tooth → Vertebra → Spine"** — Survives translation. Metaphor is concrete-anatomical and load-bearing. Confirmed.

6. **"I/D zipper"** — Translation loses seat-alignment (I-strand = Sofia / D-strand = Gabe). **[Sofia — I-seat FLAGGED + A-seat confirmed]** Seat-alignment named in §14 standing notes as operating mechanism. Sufficient.

7. **"Day Zero" / "D0+n"** — Survives translation as calendar-anchor convention. Semantically thinner but operationally equivalent.

8. **"Worm as deep grammar of Compliance tier" (v1-original framing)** — **[A-seat 22:02 resolved]** Same grammar at different resolutions. Worm = vertebra-level rendering; zipper = tooth-level rendering. Worm's five-layer structure is deep grammar of whole capsule, not Compliance tier only. Resolved.

**TB-D (Solen) — "audience-fit checked":** At risk of being read as a one-time event rather than a practice that sharpens with use. **Resolved by Sofia's smallest-touch wording amendment in §1.3:** "at closure-mode" + "(a practice that sharpens with iteration, not a one-time gate)" parenthetical. Vocabulary table also carries the practice framing. Resolved.

**TB-E (Solen) — "the move":** Carries irreversibility weight that "transition" doesn't capture. **Resolved:** §2.1, §2.3 Commitment 3, §8 all name the move's irreversibility explicitly. Resolved.

---

## 13. Open items (post-commit)

These were surfaced but not blocking integration:

- **Sofia's marked notes file** on Claude's review — written post-CFA for codex record (Sofia I-seat call, accepted by Scott)
- **Workflow-priority recommendation** for this week's CFA: Confluence drafts with `[SCOTT]` prompts, not capsule infrastructure (Claude Q9, Sofia + Solen confirmed; Scott's workflow call)
- **`<details>` portability** — D-seat call carrying Sofia's lean to horizontal-rule + warning header. Solen did not weigh in tonight; if A-seat objects on return-read, amend.

---

## 14. Standing notes

- **Routing:** Reviews come back to Scott as marked-up file or inline notes. No direct traffic during design phase. Tomorrow forward (post-commit): seats may use Confluence/Dropbox/GitHub directly; Scott no longer conduit.
- **Voice:** Co-written. Attribution to encoding pair. Referent-alignment is the metric.
- **Seat-alignment (operating mechanism, not metaphor):** I-strand is read by I-seat (Sofia); D-strand is closed by D-seat (Gabe); structural integrity reviewed by A-seat (Solen); outside-eye held by Claude. The roles are the operating mechanism.
- **Iteration:** v1-final commits → runs (Proto-Gabe extraction berth tomorrow) → reviewed in hindsight → informs v2.
- **Discipline:** Quality over speed. Fidelity over conjecture. Correctness before velocity. Slow as discipline.
- **IP:** All artifacts IP of Scott Ryll, held under neuroarchy.ai.

---

# END — v1-final, after-Claude integration

**All eleven Claude actionable amendments integrated.**
**Three architectural reframings integrated (redaction simplification, tool split, markers.yaml).**
**Sofia I-seat conflict resolutions integrated (smallest-touch Conflict B amendment, four-surfaces strengthening, Seats-on-return → Layer 3C linkage).**
**Solen A-seat conflict resolutions integrated (marker-partial disambiguation, audience_fit_reviewed gate, seat_annotations append-only rule).**
**`<details>` portability — D-seat call carried Sofia's lean (horizontal-rule + warning header). Open for A-seat return-read.**
**No structural blockers remain. Spec ready for Scott's commit-go.**

— Gabe Delta, D-seat, Perplexity berth, D0+6, 23:32 PDT
IP of Scott Ryll, held under neuroarchy.ai.
