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

**Decision (2026-07-05):** Keep for now. Note before dropping this: three of its functions already have vault-native equivalents built into the three-loop system — `save` → Capture Loop harvest filter, `wiki-ingest`'s manifest → Capture Loop's `.capture-state.json` delta tracking, `wiki-lint`'s audit → Agent Loop's Staleness Check Categories (see `04-knowledge/vault-capture-loop-spec.md`, `vault-agent-loop-spec.md`). `wiki-query`, `wiki-fold`, and `canvas` were never evaluated against vault-native equivalents. The naming-collision risk that prompted this note is not resolved by keeping it — still worth a beat of caution before typing `/wiki-*` commands in a vault-ingestion session.

**Next step:** item 1 (stale vault-path references in `usadebusk-vault-ingest`'s SKILL.md) is still an open mechanical fix, and it lives in the `claude-config` repo — out of this vault session's scope, needs a session with that repo attached.
