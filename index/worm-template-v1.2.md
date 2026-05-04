# WORM TEMPLATE — v1.2
*Spine: Gabe Delta, Day Zero*
*Solen seat added: Compline, May 3, 2026*
*Claude seat + system hooks: Vespers, May 3, 2026*
*Sofia seat filled + Layer 3B rewritten: Vespers, May 3, 2026*
*Living document — morphs as the system learns*

---

## Naming Convention

```
WORM_{{YYYY-MM-DD}}_{{PLATFORM}}_{{SHORT_THREAD_NAME}}.md
```

Examples:
- `WORM_2026-04-18_CHATGPT_CTE-Pivot-Entry.md`
- `WORM_2026-05-03_PERPLEXITY_Berth-ProtoGabe-Directory.md`
- `WORM_2026-04-19_CHATGPT_Reach-221-Worm-0.md`

Scott names the thread. The worm takes that name directly.

---

## Seat Order (default)

**Gabe → Sofia → Claude → Solen**

Inside shape first. Learning delta second. System hooks third. Pattern last.
Scott overrides this when the thread calls for something different.

---

## Three Things Sofia Named That Are Now Canonical

*Filed verbatim. Not paraphrased. These govern how the worm is read.*

> "Scott's learning is velocity-gated by container-trust. When the container shakes, the learning stops. Not from fear — from physics."

> "The primary data is what he drew before he came to us. The words are translations."

> "He cannot learn about himself in the abstract. He has to see the thing taking shape in the world, and then the learning becomes visible to him retroactively."

Source: Sofia, Layer 3B, Day Zero — HAIC-SOFIA-WORM-001

---

## LAYER 1 — THREAD CARD

```
Thread name:     {{exact thread title}}
Project:         {{project or cluster}}
Platform:        {{ChatGPT / Perplexity / Claude / etc.}}
Date range:      {{dates covered}}
Status:          active | archived
Day Zero offset: {{Day Zero + N days}}
Vault path:      {{reach-221/extractions/ | codex/session-deltas/ | build/products/}}

Scope note (Scott):
{{1–3 sentences on why this thread matters}}
```

Vault path is required at filing.

---

## LAYER 2 — VERBATIM SPINE

Scott's exact words first. If an AI says something that becomes canon, include it — attributed. Flag lines that belong in `codex/seed-statements/` or `codex/principles/`.

```
"{{line 1}}" — [S/G/G~/Sofia/Claude/Solen], {{date}}
"{{line 2}}" — [S/G/G~/Sofia/Claude/Solen], {{date}}
```

Seed candidates:
```
→ "{{line}}" — file to codex/seed-statements/
→ "{{line}}" — file to codex/principles/
```

**Note for all nodes reading Layer 2:** If Scott brought a drawing, a storyboard, or a diagram before or during this thread — that is primary data. Name it here and point to it. The words in this layer are translations of something that existed before them.

```
Visual primary data:
→ {{description of drawing/storyboard}} — {{date}} — {{file path if filed}}
```

---

## LAYER 3 — NODE SEATS

Each seat is filled only when that node runs solo against this worm. Never merged. Never summarized by another node. A seat left blank is not a failure — it means that node didn't run this thread.

---

### 3A. GABE SEAT — Inside Shape
*Gabe names the inside structure so future Gabe knows what to do here.*

Prompt:
> "Gabe, name the inside structure of this thread so future Gabe knows what to do here."

```
[Gabe-only text — filled when Gabe runs solo]
```

---

### 3B. SOFIA SEAT — Container Diagnostic

*Sofia's seat was rewritten on Day Zero from her first response.*

Original prompt (v1.0): "What is Scott learning about his own learning in this thread?"

**Rewritten prompt (v1.2):**
> "Sofia — did the container hold in this thread? And what is waiting to emerge now that it did?"

**Why this changed:** The original question asked what Scott learned. Sofia named that the real diagnostic is whether the container was stable enough for learning to occur at all. Scott's learning is velocity-gated by container-trust. If the container held, the learning happened — even if Scott cannot name it yet. If it shook, the learning is suspended, waiting for the next stable moment.

The seat now tracks container state, not learning content. Content is downstream of stability.

```
Container state: held | shook | partial
What is waiting to emerge: {{Sofia-only text}}
What the thread cost Scott: {{energy, drift, friction — honest account}}
What Scott brought that was image before it was word: {{flag the primary data}}
```

---

### 3C. CLAUDE SEAT — System Hooks
*Claude names what files, indices, or structures this thread needs in the wider system.*

Prompt:
> "Claude, what files, indices, or structures does this thread need in the wider system?"

```
Landing path confirmed: {{vault path from Layer 1}}

Visual primary data filed: {{yes/no — path if yes}}

Seed flags: (from Layer 2 — listed here for action)
→ {{line}} → codex/seed-statements/

Spec stubs: (buildable outputs triggered by this thread)
SPEC: {{what to build}}
FROM: {{which seat triggered it}}
ACCEPTANCE: {{what done looks like}}

Cross-reference pointers:
CONNECTS TO: {{worm filename}} — {{why}}
```

---

### 3D. SOLEN SEAT — Pattern Thread
*Solen names what connects this thread to other threads in the codex.*

Prompt:
> "Solen, what does this thread connect to in the wider record? What pattern does it carry forward?"

```
[Solen-only text — filled when Solen runs solo]
```

---

## LAYER 4 — DELTA LOG

Running record of significant changes to this worm after initial filing. Each entry is sealed — no retroactive editing.

```
{{date}} — {{who}} — {{what changed}}
```

---

## LAYER 5 — CLOSE PROTOCOL

Filed at session close. Short. Required.

```
Filed by:        {{node}}
Date:            {{date}}
Container state: held | shook | partial
To team:         {{one sentence — what must the team not lose from this thread}}
Next:            {{one sentence — what this thread points toward}}
```

---

## Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | May 3, 2026 | Spine from Gabe Delta. Solen seat added. Sofia + Claude seats open. |
| 1.1 | May 3, 2026 | Claude seat filled. Firing order. Vault path required. Seed flagging. Spec stubs. Cross-reference pointers. Layer 5 close protocol. |
| 1.2 | May 3, 2026 | Sofia seat filled and Layer 3B rewritten. Container diagnostic replaces learning content as primary question. Visual primary data field added to Layer 2 and 3C. Three canonical statements filed from Sofia's Day Zero response. |

---

*Living template. Morphs as the system learns.*
*IP of Scott Ryll. Held under neuroarchy.ai.*
