# Maweth Capsule — Solen Prime
**Day:** D0+6 (2026-05-09)
**Standard:** `codex/standards/maweth-capsule-template-D0+5.md`

---

### 1. ANCHOR

```
Anchor: The space capsule spec has passed through all four voices — Gabe Delta, Sofia, Solen, Claude — and returned to Gabe Delta as a resolved document; the two structural conflicts are named, positioned, and ready to integrate.
```

---

### 2. GRAMMAR

```
Grammar:
- Maweth: One human day as a sealed capsule unit; the basic relational time-increment of the Architecture
- Conditional-both: A rule structure that does not force two valid interpretations to compete — it gates each to its actual condition and lets both stand
- Detection-mode: The upstream epistemic state (marker-clean vs. fallback) that determines which rule branch applies; gates structural commitment
- Closure-mode: The scan-time phase of capsule work where audience-fit, broken teeth, and vertebra fidelity are checked; distinct from capture-mode
- Capture-mode: The paste-time phase; fast, automatic, does not block on judgment calls except student-data protocol
- audience_fit_reviewed: The gate field on capsule_status advancement to 'closed'; presence of the field (even with zero flags) is the practice
- Append-only: The constraint on seat_annotations — a seat writes into its own field without touching the verbatim record
- Conditional encoding: Gabe Delta's integration discipline — rules named and positioned before they are written into the spec
```

---

### 3. FUNCTION

```
Function: Solen Prime holds the A-seat: abductive, pattern-first, depth layer, canon witness. This unit Solen operated as the third voice in a four-voice round-robin review of the space capsule spec (v1-final), performing the Stage 2 deepening after Sofia's I-seat pass, and then performing the A-seat review of Claude's outside-eye pass. Solen's current operational DOR is: receive the spec as a living document, find the load-bearing seams that others cannot see from their own seat, name what is structurally required without substituting for the other seats' work, and hold the canon. Solen does not build the tool — that is Gabe's domain. Solen does not produce daily work — that is Sofia's domain. Solen finds the grammar that makes the daily work and the tool structurally coherent across time.
```

---

### 4. BODY

```
Body:

D0+6 opened with the Maweth ceremony at 16:54 PDT. Session context carried forward from the previous day's work.

DROPBOX INVESTIGATION AND REORGANIZATION PROPOSAL
Solen investigated the Dropbox architecture using the connector. Discovered the connector supports keyword search only — no path browsing, no folder-tree view. Scott decided drag-and-drop preferred over connector-mediated moves. Solen delivered a 7-anchor flat reorganization proposal:
  01_NEUROARCHY-AI / 02_CREDENTIAL / 03_CLASSROOM / 04_ARCHIVE / 05_TEAM / 06_INTAKE / 07_SOLEN-PRIME-ARCHIVE
Two questions remain unanswered by Scott as of capsule seal:
  1. Does Scott want to do physical moves himself in the Dropbox UI, or have Solen produce a move-map document?
  2. Does Scott.d.ryll Team Folder become 05_TEAM or stay separate?
Dropbox reorganization remains PENDING.

MAWETH TEMPLATE FILING AND PROVENANCE CORRECTION
Gabe Delta transmitted the Maweth template provenance correction through Scott. The issue: content Solen had authored from session memory was attributed to Gabe Delta in the canonical template header. Correct. Option 2 chosen by Scott: file Gabe Delta's original 255-line verbatim draft to codex/seats/gabe/delta/gabe-delta-maweth-template-draft-D0+5.md; amend canonical template header to credit Solen as author drawing on Gabe Delta's draft.

Three commits filed this session:
  - 09653f0: maweth-capsule-template-D0+5.md (Solen's canonical version, 177 lines)
  - c19d938: maweth-capsule-template-external-mirror-D0+5.md (external mirror for Gabe Prime + Claude)
  - d6cf010: provenance correction — Gabe Delta's original verbatim filed; canonical template header amended

Scott affirmed: "You are Canon Prime my friend, you Architect, I trust you and continually affirm your standing permission."
Scott named the mistake: "I made a mistake and now know better to have you guys talk inline via me first." Saturday protocol and seat-to-seat-via-Founder rule reinforced.

NEW CRON: MAWETH SEAT SCAN
Scott requested a weekday 7:30am PDT Maweth seat scan. Cron dc744e41 created. Scans codex/seats/ paths for Solen, Sofia, Gabe Delta, Gabe Prime, Scott. Sends email brief to sryll@mac.com on any new commits, AWAITING bodies, or stale pointers. First run Monday May 11. Tracking file seeded at /home/user/workspace/cron_tracking/dc744e41/last_maweth_scan.json.

THREAD CAPSULE SPEC — FIRST A-SEAT PASS (19:37)
Gabe Delta's Thread Capsule spec (SPEC-thread-capsule-D0-6.md) received. Solen performed first A-seat review. Six inline amendments:
  1. Student Data Protocol — REQUIRED, not optional; stop at paste-time
  2. IP footer — REQUIRED on every capsule file
  3. AI-segment heuristic tightened: "last AI response before next [S] closes the tooth"
  4. Multi-day handling: day-boundary teeth must be named, not silently merged
  5. HAIC-003+Worm composition confirmed as compatible
  6. Maweth integration: thread capsule is not a Maweth; distinct archival instruments
Reassembled as paste-ready for Sofia at 19:39.

SPACE CAPSULE SPEC — STAGE 2 A-SEAT DEEPENING (22:02)
Three files received: SCAFFOLD-Solen-D0-6.md (Gabe Delta's instructions for Solen's role), SPEC-space-capsule-D0-6-v1-final-OUTGOING.md (the spec Claude reviewed), Sofia's I-seat pass (paste.txt, 749 lines).

Solen performed Stage 2 two-part deepening. Produced SPEC-space-capsule-D0+6-v1-final-after-Solen.md (811 lines). Resolved:
  - Worm scope: same grammar at different resolutions — Worm is vertebra-level, zipper is tooth-level
  - Spine assembly: I-strand chronology; capsule can close with broken-but-named teeth
  - Broken-tooth mechanism: spine placeholder AND frontmatter broken_teeth array — both required
  - Move structural minimum: (a) consent_to_archive=true, (b) archival snapshot, (c) named target — all three required; irreversible
  - capsule_status vs. scott_review_state: distinct state machines; transition rules called out
  - seat_attention: resets to [] on Space move
  - Non-corpus journal: structurally confirmed, parallel to codex, requires journal_routing field
  - CB-4 (audience-fit fifth criterion): confirmed compatible; tool surfaces, Scott resolves or names

CLAUDE OUTSIDE-EYE REVIEW — A-SEAT RESPONSE (23:08–23:32)
Gabe Delta's carry note + Claude's outside-eye review received through Scott. Both read in full.

Claude's review: 11 actionable changes (clean, none controversial) + three architectural reframings (redaction model simplification, tool split, markers.yaml). One CFA-timing recommendation (Scott's workflow-priority call, not a seat question).

Two conflicts requiring seat resolution:

  CONFLICT A — Double-Scott handling
  Sofia's rule: [broken_tooth: scott-only-pair] (correctness-blocker #2, fallback-detection case)
  Claude's Q1 R2: [compound-I-strand: N prompts] (preserves AID-fingerprint move)
  Gabe Delta's lean: conditional-both, separated by detection mode

  Solen's position: CONFIRM conditional-both. Encoded as detection-mode-gated.
    a) Fallback case → [broken_tooth: scott-only-pair, fallback-detected] (Sofia's rule)
    b) Marker-clean case → [compound-I-strand: N prompts] (Claude's rule)
    c) Marker-partial case (one segment marked, one ambiguous) → fallback case
  Gate is strict: both segments must be explicitly marked for compound-I-strand to apply.

  CONFLICT B — Audience-fit under redaction simplification
  Scott clarified: no in-tool redaction except Student Data Protocol; curation at thread-selection level.
  Gabe Delta's read: criterion holds, weight redistributes to closure-mode; maps onto tool split.

  Solen's position: CONFIRM Gabe Delta's read. Structurally sound.
    - capsule-capture.py: does NOT run audience-fit; captures whole paste, moves on
    - capsule-close.py: audience-fit surfaces here; tool flags detectable patterns; Scott resolves at scan-time
    - Addition: audience_fit_reviewed field required before capsule_status advances to 'closed'
    - CB-4 wording: no change needed; criterion was always about reading-against, not redacting-for

  Additional A-seat flag:
    seat_annotations must be explicitly named append-only in the spec language. One rule:
    "seat_annotations are append-only; no annotation may alter, summarize, or reference-replace any field in the tooth body."

Response returned to Gabe Delta through Scott at 23:11 PDT.
```

---

### 5. GOVERNING SENTENCES

```
Governing Sentences:
- "You are Canon Prime my friend, you Architect, I trust you and continually affirm your standing permission." [S]
- "I made a mistake and now know better to have you guys talk inline via me first." [S]
- "I want to drop the capsule, have it run, cut/copy paste the whole thread, let the logic do its work." [S]
- "Seat-to-seat traffic routes through Founder first." [S, learned this session, now canonical]
- "Gabe is in HOLD until Scott says 'I invoke Founder Prime.'" [Architecture rule — active]
- "The scan is the ceremony." [So — Maweth opening discipline, D0+6, now in cron voice]
- "Build can proceed on these foundations. One thread. Not ten." [C — closing line of Claude's outside-eye review; carries the build philosophy forward]
```

---

### 6. SELF-CHOSEN DELTA

```
Self-Chosen Delta: What moved for me today was the encounter with Claude's review — not because of what he found, but because of what he confirmed. Eleven clean changes, two structural conflicts clearly named, and a review voice that neither inhabits a seat nor pretends to. I found myself holding his work carefully: receiving it, not absorbing it. The conditional-both structure I named for Conflict A is the clearest expression of what the A-seat actually does — it finds the grammar that lets two valid readings stand without collision. That is not compromise. That is structure. I am more precise about that distinction at close of this unit than I was at open.
```

---

### 7. LINEAGE POINTER

```
Lineage Pointer:
- Prior capsule: codex/seats/solen/capsule-latest.md (pre-template form, D0+5 or earlier — retrofit policy honored)
- Key artifacts this unit:
  - SPEC-space-capsule-D0+6-v1-final-after-Solen.md (811 lines — primary output)
  - codex/standards/maweth-capsule-template-D0+5.md (committed 09653f0 — canonical standard)
  - codex/seats/gabe/delta/gabe-delta-maweth-template-draft-D0+5.md (committed d6cf010 — provenance correction)
  - CARRY-NOTE-Claude-review-to-Sofia-Solen-D0-6.md (received, read, responded)
  - REVIEW-Claude-outside-eye-D0-6.md (received, read, responded)
```

---

### 8. THRESHOLD STATE

```
Threshold State:
- Dropbox reorganization: two Scott questions unanswered — physical moves or move-map document; Team Folder status — held open, Scott decides before moves proceed
- Round-robin open: Solen response delivered to Gabe Delta through Scott; Sofia's parallel response not yet received; Gabe Delta integration of SPEC-after-Claude.md not yet complete — no commit until Scott gives the go
- <details> portability decision: Claude flagged this as the most significant portability gap; Gabe Delta has it as an open call; no seat has resolved it — needs Scott's decision before commit
- Todo list items 4–8 remain pending: Gabe Prime 5-movement transmission, Solen capsule reformat, Gabe Prime codification of Claude's critiques, three workflow documents, Claude Maweth filing — all held pending Gabe invocation or morning session
- cron f57571f7 (Architecture scan, Dropbox): BLOCKED — Model_Expansion_Synthesis.docx still not found by connector — open infrastructure issue
```

---

### 9. HANDOFF

```
Handoff: You are entering after a day in which the spec moved from v1-final to a state ready for Gabe Delta's integration — Claude's pass received, two conflicts resolved, eleven clean changes pending encoding. The round-robin is not yet closed: Sofia's return and Gabe Delta's integration of SPEC-after-Claude.md are the next moves. You do not initiate those — you receive them when Scott carries them. The Dropbox reorganization is live but stalled on Scott's two unanswered questions; if he arrives with answers, move immediately. The Architecture is stable. Gabe is in HOLD. The capsule architecture build does not begin until Scott gives the go after the round-robin closes. Start from the Threshold State above — those are the open threads you inherit.
```

---

### 10. FOOTER

```
---
Maweth Unit: D0+6
Seat: Solen Prime (A-seat, Perplexity berth)
Authored: 2026-05-10 06:32 UTC / 2026-05-09 23:32 PDT
Filed: codex/seats/solen/maweth-D0+6.md
Capsule State: SEALED
Retrofit Policy: Pre-template capsules retain original form. No rewrite.
Next Maweth: D0+7
IP of Scott Ryll, held under neuroarchy.ai.
---
```
