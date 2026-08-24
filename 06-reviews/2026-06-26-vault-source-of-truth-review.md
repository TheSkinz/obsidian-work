---
type: review
status: complete
review_type: source-of-truth
source_authority: primary
confidence: high
created: 2026-06-26
review_after: 2026-09-26
related:
  - [[vault-source-of-truth]]
  - [[knowledge-system-governance]]
  - [[2026-06-26-knowledge-system-pilot-review]]
tags: [review, knowledge-system, vault, source-of-truth]
---

# Vault Source Of Truth Review

## Trigger

The first knowledge-system pilot review flagged a duplicate-vault/source-of-truth hazard from `00-inbox/read-only-inventory-task-do-elegant-summit.md`. Before deeper automation, the canonical edit target needed to be documented.

## Current Finding

The canonical USADeBusk Obsidian vault is:

```text
C:\Users\Jwuts\OneDrive\obsidian-usadebusk
```

This path exists, contains `.obsidian`, contains `CLAUDE.md`, and is the vault currently being edited for the knowledge-system pilot.

## Path Check Results

| Path | Exists 2026-06-26 | Vault Markers | Classification |
|---|---:|---|---|
| `C:\Users\Jwuts\OneDrive\obsidian-usadebusk` | Yes | `.obsidian`, `CLAUDE.md` | Canonical active vault. |
| `C:\Users\Jwuts\.claude\projects\C--Users-Jwuts-OneDrive-obsidian-usadebusk` | Yes | No `.obsidian`, no `CLAUDE.md` | Claude project metadata/cache, not a vault. |
| `C:\Users\Jwuts\claudeworkspace\obsidian-usadebusk` | No | None | Previously reported duplicate, currently not found. |
| `C:\Users\Jwuts\obsidian-usadebusk` | No | None | Previously reported duplicate, currently not found. |
| `C:\Users\Jwuts\OneDrive\Documents\obsidian-usadebusk` | No | None | Previously reported duplicate, currently not found. |
| `C:\Users\Jwuts\OneDrive\Documents\obsidian-usadebusk1` | No | None | Previously reported duplicate, currently not found. |

## Decision

Created `04-knowledge/vault-source-of-truth.md` as the active guardrail. Future agent or automation edits should verify the canonical path before writing.

## Remaining Risk

The earlier inventory may have observed transient or since-deleted duplicate folders. If another USADeBusk vault copy appears later, do not merge or delete it automatically. Create a review note first and compare source markers, modification times, and unique files.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-06-26 | Verified current paths and created canonical vault guardrail. No files moved or deleted. | Codex |
