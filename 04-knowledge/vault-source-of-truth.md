---
type: governance
status: active
source_authority: primary
confidence: high
created: 2026-06-26
last_reviewed: 2026-06-27
review_after: 2026-09-26
tags: [knowledge-system, vault, source-of-truth, guardrail]
---

# Vault Source Of Truth

The canonical USADeBusk Obsidian vault is:

```text
C:\Users\Jwuts\obsidian-work
```

Any Codex, Claude, plugin, script, or automation workflow that edits the USADeBusk vault must verify the target path starts with that exact path before writing.

## Edit Guardrail

Before writing vault files, confirm:

| Check | Required Result |
|---|---|
| Target path starts with canonical vault path | Yes |
| File is inside the active vault, not a cache/project metadata folder | Yes |
| Change is small and reviewable | Yes |
| Source notes are preserved unless explicitly approved | Yes |
| Canonical notes are changed only after approval when safety, pricing, SOP, field execution, customer-facing content, or heater-card facts are affected | Yes |

## Known Non-Canonical Paths

These paths are not the canonical vault for editing:

| Path | Current Status | Notes |
|---|---|---|
| `C:\Users\Jwuts\OneDrive\obsidian-usadebusk` | Retired on 2026-06-27 | Former OneDrive vault path. Do not edit as vault source. |
| `C:\Users\Jwuts\.claude\projects\C--Users-Jwuts-OneDrive-obsidian-usadebusk` | Exists | Claude project metadata/cache path, not an Obsidian vault. Do not edit as vault source. |
| `C:\Users\Jwuts\claudeworkspace\obsidian-usadebusk` | Not found on 2026-06-26 | Previously reported duplicate. Treat as stale evidence unless found again. |
| `C:\Users\Jwuts\obsidian-usadebusk` | Not found on 2026-06-26 | Previously reported duplicate. Treat as stale evidence unless found again. |
| `C:\Users\Jwuts\OneDrive\Documents\obsidian-usadebusk` | Not found on 2026-06-26 | Previously reported duplicate. Treat as stale evidence unless found again. |
| `C:\Users\Jwuts\OneDrive\Documents\obsidian-usadebusk1` | Not found on 2026-06-26 | Previously reported duplicate. Treat as stale evidence unless found again. |

## Relationship To Other Governance

This note supports `knowledge-system-governance.md`. If a future workflow finds another vault copy, create a review note before moving, deleting, merging, or editing anything.
