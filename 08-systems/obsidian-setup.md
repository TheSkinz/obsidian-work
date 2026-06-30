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

**Obsidian Sync (Standard plan)** — syncs to Obsidian's servers, available on desktop and iPhone. This is the primary sync mechanism for the vault.

**Git backup** — vault is also git-tracked and pushed to `TheSkinz/obsidian-work` on GitHub. Git is the authoritative version history; Obsidian Sync is the live cross-device sync. The two are independent — Obsidian Sync does not go through git.

## Plugin ecosystem

The `claude-obsidian` plugin lives at `C:\Users\Jwuts\ClaudeWorkspace\claude-obsidian`. It's installed and functional but not actively used as a regular workflow step yet. It provides skills for wiki ingest, query, lint, save, and canvas operations that can be invoked from Claude Code sessions.

Standard community plugins (templater, dataview, etc.) — (Placeholder: document which are installed and active once audited.)

## Folder structure

See vault `CLAUDE.md` for the authoritative folder list. Short version: `01-context/` auto-loads, `02-facilities/` and `04-knowledge/` load on demand, `00-inbox/` is capture, `06-insights/` is session output, `07-llms/` / `08-systems/` / `09-interests/` are the new personal knowledge layers (added June 2026).

## Known issues

(Placeholder — document any sync conflicts, plugin conflicts, or startup issues as they occur.)
