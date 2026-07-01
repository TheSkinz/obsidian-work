---
type: note
status: complete
created: 2026-06-30
closed: 2026-07-01
tags: [skills, cleanup, claude-config]
---

# Skill naming/staleness cleanup — flagged 2026-06-30, resolved 2026-07-01

Two separate issues noticed while closing out the 2026-06-30 session. Both resolved.

**1. `usadebusk-vault-ingest` had stale references to the retired vault path.** Its SKILL.md description said "ingesting documents into the obsidian-usadebusk vault" — that's `C:\Users\Jwuts\OneDrive\obsidian-usadebusk`, retired 2026-06-27 per [[vault-source-of-truth]] in favor of the canonical `C:\Users\Jwuts\obsidian-work`. It also carried a `vault-onedrive-safety.md` reference file written against the dead path, and a vault schema diagram listing the retired `05-projects/` folder. **Fixed** in `claude-config` PR #1 (branch `claude/task-planning-99chnf`): description and schema updated to `obsidian-work`, `05-projects/` removed from the diagram, OneDrive safety reference de-hardcoded to a `[OneDrive vault root]` placeholder since no vault is currently OneDrive-backed. Confirmed via repo-wide grep: no other stale `obsidian-usadebusk`/OneDrive-vault references remain anywhere in `claude-config`.

**2. `claude-obsidian:*` (wiki, wiki-ingest, wiki-query, wiki-fold, wiki-lint, save, canvas, and others) is a whole unused plugin ecosystem.** It implements its own "wiki vault" pattern never adopted here — the vault uses the bespoke governance in `04-knowledge/` instead. Not stale, just idle, but its skill names are close enough to the real workflow that it nearly caused a mistake (`/wiki-ingest` almost got invoked instead of the vault's own ingestion workflow). **Decided (2026-07-01, Jesse):** keep as-is for now. Collision risk noted but accepted; revisit if it causes an actual mistake rather than a near-miss.
