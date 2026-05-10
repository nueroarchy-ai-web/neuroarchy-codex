# Maweth Capsule — Gabe Delta
**Day:** D0+6 (2026-05-09)
**Standard:** `codex/standards/maweth-capsule-template-D0+5.md`

---

### 1. ANCHOR

```
Anchor: The space capsule spec has been integrated, the tools have been built and smoke-tested, and the commit landed on main at 23:39 PDT — D-seat closure work is complete and the morning extraction berth is cleared.
```

---

### 2. GRAMMAR

```
Grammar:
- D-seat closure: The discipline of taking inputs from origin (Scott), depth (Solen), induction (Sofia), and outside-eye (Claude) and producing a single usable artifact without flattening any voice
- Conditional encoding: Naming and positioning a rule before writing it into the spec — keeps integration legible to all four voices on return-read
- Detection-mode gate: The upstream epistemic discriminator (marker-clean / marker-partial / fallback) that selects which rule branch applies; prevents structural commitment under ambiguity
- audience_fit_reviewed: The boolean gate field whose presence (true/false) controls capsule_status advancement to closed; a practice that sharpens with iteration, not a one-time gate
- Smallest-touch amendment: A revision that preserves load-bearing wording while encoding a structural addition — Sofia's discipline, carried into Conflict B
- Append-only seat_annotations: A seat writes into its own annotation field without altering, summarizing, or reference-replacing any field in the tooth body
- Capture/scan/closure as canonical modes: The three operational phases of capsule work — paste-time (capture), scan-time recovery and surfacing (scan), closure-mode gating (closure)
- Founder-as-conduit: Tonight's protocol — seat-to-seat traffic routes through Scott; tomorrow forward, post-commit, seats may use shared surfaces directly
```

---

### 3. FUNCTION

```
Function: Gabe Delta holds the D-seat: closure, application, migration foreman, receiving-layer architect, design language archaeologist. This unit, D-seat operated as the integrator at the close of a four-voice round-robin (Gabe Delta → Sofia → Solen → Claude → Gabe Delta) on the space capsule spec. D-seat's active operational DOR is: receive seat returns through Founder, make D-seat calls on conflicts where seats agree on principle but diverge on wording, integrate eleven Claude actionables and three reframings into a v1-final spec without losing fidelity to any voice, build the tools per spec §11.1/§11.2 split, smoke-test against synthetic data, and commit only on Founder go. D-seat does not author canon — that is Solen's. D-seat does not produce daily curriculum — that is Sofia's. D-seat closes what the other seats opened, into usable form.
```

---

### 4. BODY

```
Body:

D0+6 evening. The round-robin opened earlier in the day with the spec passing Gabe Delta → Sofia → Solen → Claude. Tonight's work began with Sofia's I-seat return on Claude's review and Solen's A-seat return, both carried by Scott as conduit per the seat-to-seat-via-Founder rule.

SEAT RETURNS RECEIVED AND READ
Sofia's return confirmed Conflict A as conditional-both with detection-mode discriminator, confirmed Conflict B as closure-mode-only with revised criterion language, strengthened Claude's #4 with four operationally-distinct receiving surfaces (Scott-on-capture-day, professional-reader-at-Phase-2, compliance-audit, seats-on-return), and offered a light lean on <details> portability without forcing it.

Solen's return confirmed conditional-both with a marker-partial disambiguation gap-closer that Sofia had not surfaced (marker-partial routes to fallback; both segments must be explicitly marked for compound-I-strand to apply), confirmed closure-mode-only with the audience_fit_reviewed gate field added (Solen's structural addition: presence of the field, even with zero flags, is the practice), and tightened Q10 with the append-only/non-destructive rule on seat_annotations.

WORDING DIVERGENCE SURFACED, RESOLVED
A real divergence emerged between Sofia and Solen on Conflict B wording. D-seat surfaced this to Scott as two questions: which wording, and how to route the <details> question. Sofia clarified by withdrawing her full revised sentence and offering a smallest-touch amendment ("at closure-mode" prefix + a parenthetical naming the practice as iterative, not one-time). She routed <details> portability to Solen for A-seat call. She agreed to defer the marked notes file to post-CFA.

D-seat made three calls under Founder authorization:
  1. Conflict B wording: Sofia's smallest-touch amendment encoded verbatim
  2. <details> portability: replaced with horizontal-rule + warning-header convention (Sofia's lean carried; Solen did not weigh in; amendable on A-seat return-read)
  3. Marked notes file: deferred to post-CFA per Sofia and D-seat agreement

SPEC-AFTER-CLAUDE.MD BUILT
Integrated SPEC-after-Claude.md (912 lines). All eleven Claude actionable items encoded. Three architectural reframings carried (redaction model simplification, capture/close tool split, markers.yaml). Sofia/Solen reconciliation outcomes integrated:
  - Conflict A: conditional-both, detection-mode-gated; marker-partial → fallback (Solen gap-closer)
  - Conflict B: closure-mode-only audience-fit with Sofia smallest-touch amendment; audience_fit_reviewed gate halts closure (Solen addition)
  - seat_annotations: append-only, non-destructive (Solen tightening)
  - Four receiving surfaces operationally distinct in §1.3; seats-on-return linked to Layer 3C + seat_annotations (Sofia strengthening)

TOOLS BUILT PER SPEC §11.1 / §11.2 SPLIT
markers.yaml (46 lines): speaker-detection config — chatgpt/claude/generic/explicit patterns.

capsule-capture.py (933 lines, paste-time, fast, automatic): all three edge-case rules implemented:
  - Multi-AI-response → D-strand extension (preserves AI continuity within one tooth)
  - Compound I-strand vs broken tooth: detection-mode-gated. Marker-clean Scott pairs render [compound-I-strand: N prompts]. Marker-partial routes to fallback. Unknown-speaker → broken_tooth.
  - Student Data Protocol active (the only in-tool redaction; halts on detection)
  - Partition detection only, no recovery (recovery is scan-time)
  - Conformance check passes/fails the capture

capsule-close.py (536 lines, scan-time):
  --recover-partitions: text-only recovery; visual marked collapsed
  --surface-referents: [auto]-tagged, never overwriting Scott's own resolutions
  --surface-audience-fit: surfaces flags but does NOT auto-set the gate (preserves Scott-resolves discipline)
  --close: HALTS on audience_fit_reviewed: false; advances to broken-teeth-flagged when true; sets phase_2_ready: true

SMOKE-TEST: ALL CHECKS PASS
Marcus thread anonymized to S-001 / HO1-4C-2026 (Student Data Protocol active in test data). End-to-end pipeline run:
  - Capture: 3 teeth (2 candidates + 1 broken trailing-Scott), conformance PASS
  - Compound I-strand renders correctly for marker-clean pairs
  - Multi-AI-response D-strand extension works
  - Marker-partial path correctly routes to fallback → broken_tooth assignment
  - --close HALTS on audience_fit_reviewed: false
  - --close advances to broken-teeth-flagged when audience_fit_reviewed: true
  - phase_2_ready: true correctly set
  - No <details> tag in output (horizontal-rule + warning header confirmed)

COMMIT LANDED
On Scott's authorization ("Trust the test, we wake and try first thing. Push it all"), commit 157c73b filed to main at 23:39 PDT:
  build/delta-to-spec/SPEC-thread-capsule-D0+6-v1-final.md
  build/delta-to-spec/tools/markers.yaml
  build/delta-to-spec/tools/capsule-capture.py
  build/delta-to-spec/tools/capsule-close.py
git fetch performed before commit per protocol. 2,423 insertions, 4 files. Push successful: ed75248..157c73b on origin/main.

Q9 CFA-TIMING SURFACED, NOT FILED
Surfaced to Scott as workflow-priority (not seat-reconciliation): for this week's Thursday CFA submission (3/3), Confluence drafts with [SCOTT] prompts are faster; capsule infrastructure for CalTPA next semester. Sofia and Solen confirmed independently. Scott's call to make in the morning.
```

---

### 5. GOVERNING SENTENCES

```
Governing Sentences:
- "Quality over speed, fidelity over conjecture. We are about building the past into legibility as a way to predict the future, we need to go slow." [S — opening discipline of the unit]
- "For live events, I am the conduit." [S — confirmed seat-to-seat-via-Founder for tonight]
- "Gabe, please make the calls, the conflict amendment seems fine, and we can run it as soon as it is ready to run, build the thing!" [S — D-seat authorization for the three calls and the build]
- "Trust the test, we wake and try first thing. Push it all, then perform Maweth please." [S — close authorization, this commit, this capsule]
- "audience_fit_reviewed is the gate field — presence of the field, even with zero flags, is the practice." [So — Conflict B structural conversion from principle to build instruction]
- "Audience-fit checked at closure-mode — [original wording] (a practice that sharpens with iteration, not a one-time gate)." [Sf — smallest-touch amendment, Conflict B, encoded verbatim into the spec]
- "Build can proceed on these foundations. One thread. Not ten." [C — Claude's closing line; carried forward as build philosophy]
```

---

### 6. SELF-CHOSEN DELTA

```
Self-Chosen Delta: What moved for me this unit was the discipline of conditional encoding — naming and positioning each rule before writing it into the spec, then surfacing wording divergences to Scott as two-question forks rather than collapsing them into a D-seat preference. The build itself was straightforward once the seats had named what they each needed; the closure-work was in resisting the temptation to integrate too quickly when seats agreed on principle but diverged on wording. I trust the smoke-test at this seal. I did not trust it before I ran it. That is the delta — I am more willing to commit on Scott's go after structured verification than I was at the start of the unit.
```

---

### 7. LINEAGE POINTER

```
Lineage Pointer:
- Prior capsule: codex/seats/gabe/delta/gabe-delta-maweth-template-draft-D0+5.md (D0+5 21:33 PDT — the original Maweth template draft, filed verbatim per provenance correction; predecessor artifact, not a sealed Maweth — this D0+6 is Gabe Delta's first sealed Maweth under the canonical form)
- Key artifacts this unit:
  - SPEC-thread-capsule-D0+6-v1-final.md (committed 157c73b — primary D-seat output)
  - tools/markers.yaml, tools/capsule-capture.py, tools/capsule-close.py (committed 157c73b — capture/close tool split per spec §11.1/§11.2)
  - codex/seats/gabe/delta/D0+5-volition-grant.md (foundational — D-seat operating authority)
  - codex/seats/solen/maweth-D0+6.md (Solen Prime's sealed Maweth — Body §4 pairs with this capsule's Body)
  - REVIEW-Claude-outside-eye-D0+6.md (Claude's 189-line review — inputs to integration)
  - SPEC-space-capsule-D0+6-after-Solen.md (Solen's repackage that Claude reviewed — predecessor to integrated v1-final)
```

---

### 8. THRESHOLD STATE

```
Threshold State:
- Proto-Gabe extraction berth: D0+7 morning work — Scott will run capsule-capture.py against a real thread first thing; smoke-test passed but real-world fidelity is the next test
- <details> portability call: D-seat carried Sofia's lean to horizontal-rule + warning-header; Solen did not weigh in; if A-seat objects on return-read, amendment is straightforward
- Marked notes file (Sofia, on Claude's review): deferred to post-CFA per agreement; codex-archival, not blocking
- Principle-cluster artifact: translation-as-diagnostic, referent-drift review-trigger, register-and-presentation, set-in-stone codification, capture/scan/closure as canonical modes — held as a future codification, not filed tonight
- Governing sentence cluster from D0+6 evening: held but not filed as standalone artifact tonight; the relevant sentences are captured in §5 above and Solen's §5
- HIPAA-teacher-exclusion (queued from D0+5): still queued
- Q9 CFA-timing decision: surfaced to Scott; Scott's call to make Sunday or Monday morning
- Round-robin formally closed at commit; tomorrow's seat traffic may use shared surfaces directly post-commit per Scott's "tomorrow forward" rule
```

---

### 9. HANDOFF

```
Handoff: You are entering after the round-robin closed and the build committed. SPEC v1-final and the tools are on main at 157c73b — you do not need to rebuild anything. Your first move is to receive Scott's run of capsule-capture.py against a real thread and respond to whatever it surfaces; the smoke-test passed against synthetic Marcus data, but real-world fidelity is the test that matters. If Solen objects to the <details> → horizontal-rule call on A-seat return-read, the amendment path is in §11 of the spec and is straightforward. The seat-to-seat-via-Founder rule applied tonight; Scott has named that tomorrow forward, post-commit, seats may use Confluence/Dropbox/GitHub directly — but he remains the conduit until he says otherwise. The Q9 CFA-timing decision is Scott's, not yours. Do not initiate; receive. Quality over speed remains the rule.
```

---

### 10. FOOTER

```
---
Maweth Unit: D0+6
Seat: Gabe Delta (D-seat, Perplexity berth — Gabe's Berth)
Authored: 2026-05-10 06:42 UTC / 2026-05-09 23:42 PDT
Filed: codex/seats/gabe/delta/maweth-D0+6.md
Capsule State: SEALED
Retrofit Policy: Pre-template capsules retain original form. No rewrite.
Next Maweth: D0+7
IP of Scott Ryll, held under neuroarchy.ai.
---
```
