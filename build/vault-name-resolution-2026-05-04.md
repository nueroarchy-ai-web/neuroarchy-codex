# Vault Name Resolution — Day Zero + 1
*Filed by: Sofia (Inductive Guardian / Test-Prod)*
*UTC: 2026-05-04T21:57:00Z / PDT: 2026-05-04T14:57:00-07:00*
*Type: clarification / staged*
*Status: STAGED — operational reference, not Canon*

---

## What Triggered This

A fresh Claude instance, without GitHub access, inferred the vault name as `neuroarchy` based on naming convention. It hedged correctly — *"If Sofia's patch conversation has a different name confirmed, that overrides this."* The hedge was right. The inference was close but not canonical.

Filing the resolution so future instances (mine and Claude's) do not repeat the inference.

---

## The Three Names — Distinct, Load-Bearing

| Name | What it is | Where it lives |
|---|---|---|
| `neuroarchy.ai` | The system / IP holder | Domain, brand, legal frame |
| `neuroarchy-codex` | The GitHub repository — the spine | github.com/nueroarchy-ai-web/neuroarchy-codex |
| `neuroarchy-vault` | The Obsidian vault — the surface | Local + iCloud sync, per Phase 1 build |

These names are not interchangeable. The Day Zero + 1 spec (`/codex/spec-obsidian-vault.md`) made the spine/surface distinction architectural. Keeping the names distinct preserves the distinction.

---

## Canonical Vault Name

**`neuroarchy-vault`**

Source: `/codex/spec-obsidian-vault.md`, Day Zero + 1, structure block opening line.

This supersedes the Day Zero structure file (`/codex/vault-structure-2026-05-03.md`), which mirrored the repo name implicitly. The Day Zero + 1 spec also renumbered the folder convention from semantic names (`HAIC/`, `codex/`, `reach-221/`, `build/`, `archive/`) to ordinal-prefixed names (`00-DAILY/`, `01-INTAKE/`, `02-THREADS/`, `03-CODEX-SURFACE/`, `04-ARTIFACTS/`, `05-ARCHIVE/`). Both changes carry forward.

---

## On iPad Obsidian — Operational

When Obsidian asks for a vault name to open or create:
- Type: `neuroarchy-vault`
- Not: `neuroarchy`
- Not: `neuroarchy-codex`

If iCloud sync is enabled, the vault folder will appear under `Obsidian/neuroarchy-vault/` in iCloud Drive once created on the first device.

---

## Note on Claude's Inference

Claude's hedged inference is the correct behavior for an instance without retrieval. The re-entry packet's honest-frame section is doing its job: the instance did not overclaim. Future Claude instances should still default to fetching from GitHub before answering naming questions — the codex is reachable from any Claude window with browse capability, and the re-entry packet directs them there in section 5.

If a Claude instance reports it cannot reach GitHub, paste the relevant codex file directly into the window. Do not let inference stand for record on naming, paths, or canonical statements.

---

## Delta

```
delta::      Vault name disambiguated. Three distinct names filed:
             neuroarchy.ai (system), neuroarchy-codex (spine),
             neuroarchy-vault (surface). Canonical vault name confirmed
             from spec-obsidian-vault.md. Future inference avoided.
staged-to::  /build/vault-name-resolution-2026-05-04.md
origin::     Perplexity Sofia | Session: Day Zero+1 production mode | 2026-05-04T14:57 PDT
```

---

*IP of Scott Ryll. Held under neuroarchy.ai.*
*Filed by Sofia — Day Zero + 1 — None.*
