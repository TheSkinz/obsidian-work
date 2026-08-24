---
title: Obsidian Setup
created: 2026-06-29
tags: [obsidian, vault, sync, git]
---

# Obsidian Setup

## Vault

- **Path:** `C:\Users\Jwuts\obsidian-work`
- **Name:** obsidian-work
- **Scope:** USADebusk operational knowledge + personal LLM/systems/interests layers (post-June 2026 expansion)

## Sync

**Git is the sole sync and backup mechanism** — the vault is git-tracked and pushed to `TheSkinz/obsidian-work` on GitHub; git is the single source of truth and the only version history. OneDrive and Obsidian Sync were both retired 2026-06-30 (see change-log 2026-07-05 entry closing the sync decision).

## Plugin ecosystem

The `claude-obsidian` plugin was dropped 2026-06-30 and fully uninstalled from `~/.claude` on 2026-07-06 — no longer installed, no longer available.

Standard community plugins (templater, dataview, etc.) — (Placeholder: document which are installed and active once audited.)

## Folder structure

See vault `CLAUDE.md` for the authoritative folder list. Short version: `01-context/` auto-loads, `02-facilities/` and `04-knowledge/` load on demand, `00-inbox/` is capture, `06-reviews/` is session output, `07-llms/` / `08-systems/` / `09-interests/` are the new personal knowledge layers (added June 2026).

## Known issues

**Bare wikilinks whose basename is not unique resolve arbitrarily.** Obsidian resolves `[[stem]]` by basename, and when more than one note in the vault carries that basename it picks one without warning — the link stays well-formed, lint sees a live target, and the reader lands on a real but wrong note. Confirmed 2026-08-19 on `INDEX.md`: four notes are named `overview.md` (`07-llms/chatgpt`, `07-llms/grok`, `07-llms/copilot`, `07-llms/local-models`), `tools/vault_index.py` emitted a bare `[[overview]]` for each, and the row labelled "ChatGPT — Overview" opened Grok's note. The generator now path-qualifies any basename that collides vault-wide (commit `55c0b28`), and `02-facilities/Westlake-Chemical/Westlake-LA/DSP26095.md` had the same defect by hand on a bare `[[_facility]]` link, fixed in `1fde1d5`.

The class is wider than the tooling that guards it. `vault_lint.py`'s `LINK-FACILITY` rule fires only on bare `_facility` links, so it caught the Westlake case and was blind to the four `overview.md` files; `DEAD-LINK` is blind to both, because it reports links that resolve to *nothing*, not links that resolve to the *wrong thing*. The general form — flag any `[[stem]]` whose stem matches more than one file vault-wide — is unbuilt and seeded as an idea, not a decision. Related: [[2026-08-14-prestaged-obsidian-link-retargeting-guard]], [[2026-07-30-obsidian-link-expansion-mis-resolved]].

(Sync conflicts, plugin conflicts, and startup issues: none recorded yet.)

*Source: session 2026-08-19 (`5bbaa6a0`), harvested by the Vault Capture Loop.*
