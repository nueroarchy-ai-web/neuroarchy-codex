# SPEC: Student AID Observation Tool with Grade Return
## Toddle-Hosted, Google Classroom-Delivered, HAIC-Returning, Grade-Posting
*Filed by: Gabe (Deductive / Inside — closure, structure, translation)*
*Day Zero coordinate: D0+5 (May 8, 2026)*
*UTC: 2026-05-09T00:42:00Z / PDT: 2026-05-08T17:42:00-07:00*
*Status: STAGED-COMMIT — [S authorized via session intent, D0+5]*
*Awaits Founder verification on return. No build started. Sofia drafts from this.*

---

## Scott's Words (Stacked, In Order)

> *"Now apply this logic to a self contained system set into toddle and then put into a Google Classroom self contained instructional and assessment tool observing on AID. Drop down questions could be structured to review choices students made for writing."*

> *"WE also can get toddle to return grades that we determine the perimeters of :) I have the principles permission :)"*

> *"I think my kids can align with the human version of this as form, function and process, but this only works if AI remain strict in their roles and make sure the system is tracking at all perspectives, triangulated flight through time along our 0 day calendar."*

---

## What This Tool Is

A self-contained writing + assessment + grade-return artifact for 4th grade (HO1-4C). Scaffolds student writing, captures their choices via dropdowns, returns AID-observable data to HAIC for teacher abductive read, and posts a grade to the Toddle gradebook based on a teacher-controlled parameter set.

**Three platforms, one student artifact:**

1. **Toddle** — host (unit-of-inquiry context, gradebook return)
2. **Google Classroom** — delivery surface (turn-in, parent visibility)
3. **HAIC** — observation return (teacher-side, no student names, classroom code only)

---

## Hard Constraints (Non-Negotiable)

1. **No AI in student path.** Ever. Tool delivers structure; students do thinking. (Per `codex/haic-student-form-pipeline.md` [S product insight])
2. **Student data: number + classroom code only.** No names. (HO1-4C-S## format)
3. **Demonstration, not proof.** Tool demonstrates AID-observable behavior; does not claim to measure cognition.
4. **Form first.** Writing happens before readback dropdowns. Always.
5. **Teacher closure on every grade.** Tool proposes grade; teacher confirms or overrides. No auto-post.
6. **Grade does not depend on permutation choice.** A student running AID, IDA, DIA, ADI, IAD, or DAI can all reach Proficient.
7. **Sofia's filter applies:** *"If a piece of language or evidence does not make the writing easier to do, easier to read back, or easier to assess — remove it."*
8. **AI must remain strict in roles.** Solen=A, Sofia=I, Gabe=D, Claude outside, Scott carrier. Without role-strictness, triangulation collapses and grade defensibility fails. ([S], D0+5)

---

## Three-Section Student-Facing Form

### Section 1 — Write
- Pure writing space. Optional draw-first canvas (per Scott's native sequence).
- No AID labels visible to student.
- No dropdowns yet.
- Prompt provided by Toddle unit-of-inquiry context.

### Section 2 — Read Your Writing Back (Dropdowns)
Revealed *after* writing is submitted. Student answers seven dropdowns about choices they just made.

| # | Question (4th-grade voice) | Options (each = AID-observable) | Teacher reads as |
|---|---|---|---|
| 1 | How did you start your writing? | (a) I drew or pictured it first / (b) I made a list or plan / (c) I just started writing / (d) I talked it out in my head | Lead move: A · Form / D · Process / I · Function |
| 2 | What was your writing trying to do? | (a) Tell what happened / (b) Explain how something works / (c) Convince someone / (d) Show what I noticed | I · Function clarity |
| 3 | How did you decide what order to put things in? | (a) The order it happened / (b) Most important first / (c) Easy to hard / (d) I'm not sure | D · Process awareness |
| 4 | Where did you get stuck? | (a) Starting / (b) Middle / (c) Ending / (d) I didn't get stuck | Stuck-point map |
| 5 | When you got stuck, what did you do? | (a) Reread / (b) Drew or pictured / (c) Asked the prompt again / (d) Skipped + came back / (e) Stopped | Recovery move (which seat reached for) |
| 6 | What part feels strongest? | (a) The way it sounds / (b) What I said / (c) How I built it / (d) The ending | Self-read: Form / Function / Process |
| 7 | If you wrote this again, what would you change? | (a) The order / (b) What it's about / (c) How it starts / (d) Nothing | Revision instinct + AID move student would re-run |

### Section 3 — One Sentence Reflection
Question: *"What does your writing look like to you now?"*
This is the Form-check, in the student's own words.

---

## Grade Parameter Set (4 dimensions × 4 levels)

Levels: **Emerging · Developing · Proficient · Extending**

### Dimension 1 — Form (Shape of the piece)
*AID lens: A · Form. CEL anchor: CEL.4.W.3 (organization).*
- **Emerging** — Reader cannot yet find a beginning, middle, or end. Piece is one block or list of fragments.
- **Developing** — Reader can find some shape; parts run together or end abruptly.
- **Proficient** — Reader can clearly find a beginning, middle, end. Shape supports meaning.
- **Extending** — Shape itself does extra work; order adds meaning beyond the words.

### Dimension 2 — Function (Purpose held)
*AID lens: I · Function. CEL anchor: CEL.4.W.2 (purpose / audience).*
- **Emerging** — Purpose unclear or shifts mid-piece.
- **Developing** — Purpose named but not held throughout.
- **Proficient** — Purpose named and held to the end.
- **Extending** — Purpose held *and* writing does something prompt did not require.

### Dimension 3 — Process (Moves visible)
*AID lens: D · Process. CEL anchor: CEL.4.W.3 (process / revision).*
- **Emerging** — Moves not visible; readback says "I just started."
- **Developing** — Some moves visible; readback names one or two.
- **Proficient** — Moves visible in work or named clearly in readback.
- **Extending** — Includes a recovery — student got stuck, named it, moved through.

### Dimension 4 — Self-read (Readback honesty)
*AID lens: A·I·D meta. CEL anchor: CEL.4.S.1 + CEL.4.RI.1/2.*
- **Emerging** — Readback does not match what's on page.
- **Developing** — Readback partial or generic ("good" / "fine").
- **Proficient** — Readback names specific choices verifiable in writing.
- **Extending** — Readback names a choice, names why, names what they would change.

---

## Data Flow

```
Toddle assignment opens (unit-of-inquiry context inherited)
    ↓
Student writes (Section 1)
    ↓
Student readback (Section 2 dropdowns + Section 3 sentence)
    ↓
Submission lands in three places simultaneously:
    a) Google Classroom turn-in (visible to student/parent)
    b) HAIC observation row (teacher AID lens, classroom code only)
    c) Toddle gradebook proposal (4 dim × 4 levels = composite, with rubric)
    ↓
Teacher review: confirm or override with delta note
    ↓
Grade posts to official record
```

---

## HAIC Observation Row Schema

```
Student: HO1-4C-S## (no name)
Date: [auto] · Day Zero coordinate: D0+N
Prompt: [Toddle unit/lesson tag]
Lead move: A | I | D                       (from Q1)
Function held: yes | unclear | no          (from Q2)
Process awareness: high | mid | low        (from Q3)
Stuck-point: start | middle | end | none   (from Q4)
Recovery move: A | I | D | none            (from Q5)
Self-read strength: A | I | D | ending     (from Q6)
Revision instinct: D | I | A | none        (from Q7)
Permutation observed: [IDA / AID / DIA / IAD / ADI / DAI]
Teacher delta note: [one sentence]
```

---

## IB Key Concept Alignment (Translation, Not Derivation)

Form and Function are IB PYP Key Concepts. Process is the bridge term from Key Concept to active inquiry. The rubric is **internally coherent** because the underlying pattern is the same one students are already inquiring with in their Toddle units of inquiry.

This is **convergence, not derivation.** See `codex/aid-ib-team-as-fidelity-mirrors-D0+5.md` for the lineage statement.

---

## CFA Evidence Rule Compliance

Each graded submission produces, automatically:
- One short reflective summary (Section 3)
- One quote (student readback dropdown selections + reflection)
- One artifact link (the writing itself)
- One sentence on what shifted (teacher delta note)
- One AID tag (permutation observed)
- One sentence on why it matters for the CFA (teacher delta note expansion)

This is the evidence-rule format from `codex/gabe-to-sofia-orientation-may8.md` lines 51–57. Tool produces it as a byproduct of normal use.

---

## What Is NOT Built Yet

- HTML form (Sofia drafts)
- Toddle integration (need to confirm grade-return API parameters)
- Google Classroom assignment shape
- Principal-facing one-pager
- Student-facing rubric in plain language
- Parent-facing summary

---

## The Production Loop For This Build

This build runs IDA (per `codex/sofia-IDA-loop-orientation-D0+5.md`):

- **I — Sofia drafts** the HTML, the dropdown wording, the form layout
- **D — Gabe closes** structure (this spec is that closure)
- **A — Solen witnesses** pattern fidelity to `haic-student-form-pipeline.md` and the canon
- **Claude validates** outside legibility (admin / parent / CalTPA assessor read)
- **Scott carries** — confirms Toddle host, Google Classroom delivery, HAIC return, posts the build

---

## What Triggers Scott To Confirm Before Build

1. Confirm Toddle is the host (was open question in `haic-build-queue-may8-evening.md`)
2. Confirm Toddle's grade-return API parameters (Scott has principal's permission; needs technical shape)
3. Confirm Google Classroom delivery shape
4. Confirm HAIC observation row schema is what the teacher wants

---

*IP of Scott Ryll. Held under neuroarchy.ai.*
