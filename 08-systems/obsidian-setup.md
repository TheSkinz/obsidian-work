---
title: Obsidian Setup
created: 2026-06-29
tags: [obsidian, vault, sync, git]
---

# Obsidian Setup

## Vault

- **Path:** `C:\Users\Jwuts\obsidian-work`
- **Name:** obsidian-work
- **Scope:** USADeBusk operational knowledge + personal LLM/systems/interests layers (post-June 2026 expansion)

## Sync

**Git is the sole sync and backup mechanism** — the vault is git-tracked and pushed to `TheSkinz/obsidian-work` on GitHub; git is the single source of truth and the only version history. OneDrive and Obsidian Sync were both retired 2026-06-30 (see change-log 2026-07-05 entry closing the sync decision).

## Plugin ecosystem

The `claude-obsidian` plugin was dropped 2026-06-30 and fully uninstalled from `~/.claude` on 2026-07-06 — no longer installed, no longer available.

Standard community plugins (templater, dataview, etc.) — (Placeholder: document which are installed and active once audited.)

## Folder structure

See vault `CLAUDE.md` for the authoritative folder list. Short version: `01-context/` auto-loads, `02-facilities/` and `04-knowledge/` load on demand, `00-inbox/` is capture, `06-insights/` is session output, `07-llms/` / `08-systems/` / `09-interests/` are the new personal knowledge layers (added June 2026).

## Known issues

(Placeholder — document any sync conflicts, plugin conflicts, or startup issues as they occur.)
