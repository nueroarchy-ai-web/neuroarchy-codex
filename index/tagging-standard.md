# Tagging Standard — Neuroarchy AID
*Written by: Solen (Abductive / Inside)*
*Filed: Day Zero + 1, May 4, 2026 — STAGED, not permanent*
*Status: CANONICAL RECORD — awaiting Founder Protocol commit*

---

## Governing Principle

Every artifact, entry, and exchange gets enough tags to be found multiple ways. The tag is born in the journal. The codex path is assigned at Founder Protocol. One tag — two locations — no duplication of work.

---

## Tag Fields (Required for All)

| Field | Values | Notes |
|---|---|---|
| `seat` | Solen / Gabe / Sofia / Claude / Scott | Who produced or owns it |
| `utc` | ISO 8601 timestamp | Fixed temporal anchor |
| `pdt` | Local timestamp | Human-readable |
| `status` | STAGED / CANONICAL / PERMANENT | Lifecycle state |
| `project` | neuroarchy / cfa / obsidian / codex / [other] | What it belongs to |
| `type` | spec / journal / delta / tag / brief / artifact / ceremony / worm | What kind of thing it is |

---

## Tag Fields (Optional, High-Value)

| Field | Values | Notes |
|---|---|---|
| `journal_ref` | Entry ID or line descriptor | Where it was born |
| `codex_path` | GitHub path | Assigned at Founder Protocol |
| `confluence_id` | Page ID | If filed to Confluence |
| `attribution` | [S] / [G] / [R] / [G~] / [?] | Voice attribution |
| `deadline` | Date | If time-bound |
| `linked_to` | Tag ID or artifact name | Cross-reference |

---

## Status Definitions

**STAGED** — Created, tagged, held in journal or test/prod space. Fast. Editable. Not permanent. Rebuilt if lost from Canon, not from this copy.

**CANONICAL RECORD** — Marked as significant. Will be committed at next Founder Protocol. Do not edit without flagging.

**PERMANENT** — Committed to Canon at Founder Protocol. Filed to GitHub + Confluence. Cannot be erased — only extended, annotated, or superseded.

---

## Timestamp-First Protocol (All Seats)

Every AI response opens with:
```
[SEAT] — UTC: [timestamp] / PDT: [timestamp]
```

No greeting. Time first. This field is searchable in the record.

Example:
```
Solen — UTC: 2026-05-04T20:20:00Z / PDT: 2026-05-04T13:20:00-07:00
```

---

## Journal Tag Format

```
JOURNAL ENTRY
UTC: [timestamp]
PDT: [timestamp]
Seat: [who is writing]
Status: STAGED
Project: [project]
Type: [type]
Attribution: [S/G/R/G~/? ]
---
[content]
---
Linked to: [if applicable]
```

---

## Transit Tag Format

```
TRANSIT TAG
Seat: [seat]
UTC: [timestamp]
PDT: [timestamp]
Status: STAGED
Project: [project]
Type: [type]
Journal ref: [entry ID or descriptor]
Codex path: [assigned at Founder Protocol]
```

---

## Session Tag Format (Sofia owns)

```
SESSION TAG
Date: [UTC + PDT]
Seat: [primary seat]
Beginning state: [what Scott brought in]
Ending state: [what exists now that didn't before]
Delta: [what moved]
Waiting: [what is suspended, not lost]
Briefings dispatched: [Solen / Gabe / Claude — yes/no]
Filed to: [GitHub path or Confluence page]
Status: STAGED / PERMANENT
```

---

## Founder Protocol Commit Tag

```
FOUNDER PROTOCOL COMMIT
UTC: [timestamp]
PDT: [timestamp]
Item: [artifact name]
From: STAGED → PERMANENT
Journal origin: [entry ID]
Codex path: [GitHub path]
Confluence ID: [if applicable]
Committed by: Scott
Witnessed by: Solen / Gabe
```

---

*IP of Scott Ryll. Held under neuroarchy.ai.*
