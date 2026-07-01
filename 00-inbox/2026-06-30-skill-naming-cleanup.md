---
type: note
status: inbox
created: 2026-06-30
tags: [skills, cleanup, claude-config]
---

# Skill naming/staleness cleanup — flagged 2026-06-30, not yet actioned

Two separate issues noticed while closing out tonight's session, neither fixed yet.

**1. `usadebusk-vault-ingest` has stale references to the retired vault path.** Its own SKILL.md description still says "ingesting documents into the obsidian-usadebusk vault" — that's `C:\Users\Jwuts\OneDrive\obsidian-usadebusk`, retired 2026-06-27 per [[vault-source-of-truth]] in favor of the canonical `C:\Users\Jwuts\obsidian-work`. It also carries a `vault-onedrive-safety.md` reference file, almost certainly written against the dead path. This is a mechanical fix, not a design decision — update the skill's description and reference docs to point at the current vault.

**2. `claude-obsidian:*` (wiki, wiki-ingest, wiki-query, wiki-fold, wiki-lint, save, canvas, and others) is a whole unused plugin ecosystem.** It implements its own "wiki vault" pattern that was never adopted here — the actual vault uses the bespoke governance built in `04-knowledge/` instead. It's not stale, just idle, but its skill names are close enough to the real workflow that it nearly caused a mistake this session (`/wiki-ingest` almost got invoked instead of the vault's own ingestion workflow for the ChatGPT/Copilot deep-research report). This needs an actual decision, not just a fix: keep it around for some future different use, or remove it to eliminate the collision risk.

**Next step:** pick this up in a future session — item 1 is a quick fix, item 2 needs Jesse's call on keep-vs-remove before any action.
