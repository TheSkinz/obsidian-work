---
type: note
status: resolved
created: 2026-08-24
tags: [inbox, vault-system, housekeeping]
---

# Cosmetic drift found 2026-08-24, deliberately left

> **CLOSED 2026-09-08.** Every item below is now dispositioned, and the state of each was re-checked rather than assumed — two had already resolved themselves.
>
> - **`Untitled/`** — already gone. No action.
> - **`07-llms/local-models/`** — not empty; it holds `overview.md`. The "may be intentional scaffolding" guess was right. No action.
> - **`00-inbox/raw-docs/`** — **deleted.** Jesse confirmed the drop-zone concept is dead: he originally wanted to dump documents there for analysis and filing, and stopped doing it. `usadebusk-vault-ingest` still named it in three places, so a session reading that skill would have been told to use a path he abandoned.
> - **`07-llms/diagram-creation.md:28`** — placeholder **struck**. Gemini retired 2026-07-07, so it was queued work for a tool that had not existed for two months.
> - **`.obsidian/graph.json`'s 6 dead colour groups** — **won't-fix, deliberately.** The file is gitignored (`.gitignore:22`), so it is local Obsidian state and not vault content, and Jesse confirmed 2026-09-08 that he barely opens Obsidian. Fixing it is work on a surface with no viewer. If his Obsidian use ever changes, the six groups are a five-minute delete.

Found during the retired-claims audit and scoped out at the time — none of it states anything false, which is why it was not fixed alongside the claims that did. Recorded so it is not re-discovered from scratch.

**`.obsidian/graph.json` — 6 of 14 graph colour groups query folders that no longer exist:** one `path:03-jobs` and five under `path:05-projects` (plus `/sales-proposals`, `/operations-admin`, `/field-execution`, `/technical-docs`). Both folders were decommissioned. The groups fail silently — they simply colour nothing. Note this file is **gitignored and app-owned**: Obsidian rewrites it on close, so edit it with the app shut, or fix the colour groups in the app UI. (I re-pathed the `06-insights` group during the rename without checking its neighbours — that was the miss that left these.)

**Three empty folders:** `Untitled/` at the vault root (created 2026-08-22, almost certainly an Obsidian slip), `00-inbox/raw-docs/`, and `07-llms/local-models/`. The last may be intentional scaffolding — there is a `project-local-model-backend` thread about Vulkan on RDNA 4 — so confirm before removing that one.

**`07-llms/diagram-creation.md:28`** carries a placeholder to-do: "evaluate Gemini's diagram generation in a dedicated session". Gemini retired 2026-07-07, so this is queued work for a tool that no longer exists. Either delete the placeholder or re-point it at a tool that does.

**`06-reviews/2026-08-03-idea-research-rig-layout-diagram.md:28`** describes `tools/` as containing `audit_commit.py` and `audit_worktree.py`, neither of which exists. It is a dated review note, so this is historical rather than wrong — listed only so it is not mistaken for a live inventory.
