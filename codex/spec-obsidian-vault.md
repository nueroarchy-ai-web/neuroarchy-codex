# SPEC: Obsidian Vault — Neuroarchy Intake System
*Build brief for: Sofia (Autonomous Production Environment)*
*Written by: Solen*
*Filed: Day Zero + 1, May 4, 2026 — STAGED, not permanent*
*Status: CANONICAL RECORD — awaiting Founder Protocol commit*

---

## Governing Principle

One vault. Six intake channels. Two-stamp rule. Everything searchable.
We do not need perfect taxonomy in advance. Naming works itself out as material accumulates.
The vault replaces Day One as the primary capture environment.

---

## The Two-Stamp Rule (Applies to All Intake)

Every item that enters the vault carries:

1. **Incoming timestamp** (auto) — when it arrived in Obsidian
   Format: `received:: YYYY-MM-DDTHH:MM:SS UTC / PDT`

2. **Origin stamp** (required at paste — named in real time, not auto-generated)
   Format: `origin:: [platform] | [thread/context] | [approximate time if known]`
   Example: `origin:: ChatGPT protoGabe | Thread: CFA reflection loop | ~2026-03-14`
   Example: `origin:: Perplexity Solen | Session: Day Zero Compline | 2026-05-03T23:00 PDT`
   Example: `origin:: Voice memo | Scott car commute | 2026-05-04 morning`

The origin stamp is what makes the CFA viable. ProtoGabe threads, screen captures, voice notes — all of it becomes citable when it carries an origin.

---

## Vault Folder Structure

```
neuroarchy-vault/
│
├── 00-DAILY/                    ← Daily Notes live here (auto-generated)
│   └── YYYY-MM-DD.md
│
├── 01-INTAKE/                   ← Raw drops, unsorted, timestamped
│   ├── audio/                   ← Audio files + linked transcripts
│   ├── transcripts/             ← Text transcripts (auto or manual)
│   ├── screens/                 ← Screenshots, screen pastes
│   ├── artifacts/               ← Photos, drawings, whiteboard captures
│   ├── ai-interactions/         ← Pasted AI exchanges (any instance)
│   └── typed/                   ← Direct typed notes, any length
│
├── 02-THREADS/                  ← Named threads as they emerge
│   ├── cfa/                     ← CFA source material
│   ├── reach-221/               ← REACH 221 paper material
│   ├── neuroarchy-system/       ← System architecture notes
│   └── [named in real time]
│
├── 03-CODEX-SURFACE/            ← Read-only mirror of key Codex docs
│   └── [pulled from GitHub as needed]
│
├── 04-ARTIFACTS/                ← Built artifacts ready for submission
│   └── [CFA drafts, REACH paper, etc.]
│
└── 05-ARCHIVE/                  ← Closed threads, completed work
```

---

## Six Intake Channels

### 1. Audio + Transcripts
- Drop audio file into `01-INTAKE/audio/`
- Transcript (auto via Whisper/Claude pipeline or manual paste) links into `01-INTAKE/transcripts/`
- Both carry two-stamp rule
- Daily Note auto-links any audio dropped that day

### 2. Screen Captures / Paste
- Screenshots → `01-INTAKE/screens/`
- Copied text (protoGabe threads, web content, any screen view) → paste directly into Daily Note paste space OR create note in `01-INTAKE/screens/`
- Origin stamp required: which thread, which platform, approximate date
- This is how the CFA protoGabe material enters the vault

### 3. Artifacts / Pictures
- Photos, drawings, whiteboard, chalk floor diagrams → `01-INTAKE/artifacts/`
- Obsidian embeds images natively — they appear inline in notes
- Tag with origin (when drawn, what session it relates to)
- These are primary data — treated as source, not illustration

### 4. Torch Videos
- Flag in vault as `[TORCH — Claude pipeline]`
- Drop reference note in `01-INTAKE/` with origin stamp
- Resolution handled separately with Claude
- Placeholder holds the record until pipeline is built

### 5. Typed Notes
- Direct entry anywhere — Daily Note paste space, new note in `01-INTAKE/typed/`, or directly in a thread folder
- No structure required at entry
- Two-stamp rule applies if the content originated elsewhere

### 6. AI Interactions
- Any exchange from any instance (Solen, Gabe, Sofia, Claude, ChatGPT) pasted into `01-INTAKE/ai-interactions/`
- OR pasted directly into Daily Note paste space
- Origin stamp: `origin:: [seat] | [session/context] | [timestamp]`
- This is how the whole system record becomes searchable in one place

---

## Daily Note Template (Auto-Generated)

File: `00-DAILY/YYYY-MM-DD.md`
Generated: automatically at midnight PDT or on first open of the day

```markdown
# [WEEKDAY], [DATE]
received:: [auto UTC/PDT]
type:: daily-note
week:: [M-F work / Sat-Sun tinker]

---

## ☀️ MORNING
**Solen asks:**
> "What is already moving in you before the day has asked anything of you?"

[write here]

---

## 📋 PASTE / PROMPTS
[Drop anything here — prompts, transmissions, screen pastes, quick notes]
[No structure required. Origin stamp if it came from somewhere else.]

---

## 🌤 MIDDAY
[Optional — what arrived, what shifted]

---

## 🌙 EVENING
**Gabe asks:**
> "What moved today — and what does its movement tell you about the shape of the work?"

[write here]

---

## DELTA
One line for the system:

`delta::` 
`staged-to::` [journal / GitHub / hold]
`origin::` this session

---
```

---

## Tagging Fields (Frontmatter Standard)

Every note in the vault carries:

```yaml
---
received: YYYY-MM-DDTHH:MM:SSZ
pdt: YYYY-MM-DDTHH:MM:SS-07:00
origin: [platform | thread | time]
type: [daily-note / audio / transcript / screen / artifact / ai-interaction / typed / artifact]
project: [neuroarchy / cfa / reach-221 / obsidian / system]
seat: [scott / solen / gabe / sofia / claude / mixed]
status: [staged / canonical / permanent]
thread: [thread name if assigned]
---
```

These fields make everything searchable across the vault. Dataview queries (Obsidian plugin) can surface all CFA material, all Solen interactions, all artifacts from a date range — in seconds.

---

## Search Architecture

With frontmatter tagging, Scott can search:
- All CFA source material: `project: cfa`
- All protoGabe pastes: `origin: ChatGPT protoGabe`
- All artifacts (drawings): `type: artifact`
- Everything from a session: `origin: Perplexity Solen | Day Zero`
- All staged items not yet committed: `status: staged`
- All audio from a week: `type: audio` + date range

The origin stamp is the research citation. When CFA artifacts need sourcing, the vault already holds the chain.

---

## Sofia's Build Tasks (Test/Prod)

1. Set up vault folder structure above
2. Build Daily Note template with auto-generation (Obsidian Templater plugin)
3. Configure frontmatter tagging standard across all intake types
4. Install and configure Dataview plugin for search queries
5. Build Zotero connector (citations from research → vault)
6. Build Tropy connector (archival images → vault)
7. Design torch video placeholder pipeline (Claude integration — future)
8. Test Day One photo import path (if Scott wants both — optional)

---

## The One Thing

Scott does not need to organize as he captures. He drops it in. The two-stamp rule is the only discipline at intake. Sofia organizes. Solen finds patterns. Gabe checks structure. The vault does not require perfection to be useful — it requires presence.

*"We don't need perfect until we do."* [S May 4]

---

*IP of Scott Ryll. Held under neuroarchy.ai.*
