---
type: note
status: complete
created: 2026-06-30
tags: [skills, cleanup, claude-config]
---

# Skill naming/staleness cleanup — flagged 2026-06-30, not yet actioned

Two separate issues noticed while closing out tonight's session, neither fixed yet.

**1. `usadebusk-vault-ingest` has stale references to the retired vault path.** Its own SKILL.md description still says "ingesting documents into the obsidian-usadebusk vault" — that's `C:\Users\Jwuts\OneDrive\obsidian-usadebusk`, retired 2026-06-27 per [[vault-source-of-truth]] in favor of the canonical `C:\Users\Jwuts\obsidian-work`. It also carries a `vault-onedrive-safety.md` reference file, almost certainly written against the dead path. This is a mechanical fix, not a design decision — update the skill's description and reference docs to point at the current vault.

**2. `claude-obsidian:*` (wiki, wiki-ingest, wiki-query, wiki-fold, wiki-lint, save, canvas, and others) is a whole unused plugin ecosystem.** It implements its own "wiki vault" pattern that was never adopted here — the actual vault uses the bespoke governance built in `04-knowledge/` instead. It's not stale, just idle, but its skill names are close enough to the real workflow that it nearly caused a mistake this session (`/wiki-ingest` almost got invoked instead of the vault's own ingestion workflow for the ChatGPT/Copilot deep-research report). This needs an actual decision, not just a fix: keep it around for some future different use, or remove it to eliminate the collision risk.

**Update 2026-07-05 (item 1):** Confirmed fixed. `grep -rl "obsidian-usadebusk"` across the live `~/.claude/skills/` directory on the local machine now returns zero hits — no skill file still references the retired path. (A parallel session run the same day couldn't verify this — its environment only had `session-start-hook` under `~/.claude/skills/`, not the full `claude-config` checkout — so it left item 1 marked open/out-of-scope. This check was run directly against the real local skills directory, so it stands.)

**Decision (2026-07-05, item 2):** ~~Keep for now.~~ **Superseded same day — dropped.** The initial call was "keep for now," but the parallel `claude-config` hygiene arc then **disabled `claude-obsidian` and removed its marketplace** (commit `e343e5f`, 2026-07-05), eliminating the naming-collision risk this note flagged. Its vault-as-context role is to be replaced later by Obsidian's Local REST API MCP server (not yet configured). For the record, three of its functions had vault-native equivalents anyway — `save` → Capture Loop harvest filter, `wiki-ingest`'s manifest → Capture Loop's `.capture-state.json` delta tracking, `wiki-lint`'s audit → Agent Loop's Staleness Check Categories.

**Next step:** both items closed. Item 1 verified fixed; item 2 resolved by dropping the plugin (not keeping it). Nothing pending here. Note: the earlier vault commit `17d8798` ("keep claude-obsidian… for now") is now superseded by `e343e5f` in `claude-config`.
