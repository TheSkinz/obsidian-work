---
title: Claude Code
created: 2026-06-29
tags: [claude, claude-code, tooling]
---

# Claude Code

Claude Code is Anthropic's official CLI for Claude — an interactive agent that runs in the terminal and operates directly on the local filesystem and git repo. It is distinct from claude.ai chat; it has tool access (read, write, bash, grep, etc.) and executes tasks rather than discussing them.

## How I use it

Primary interface for all implementation work: writing vault notes, building and updating skills, running git operations, generating documents, and anything that touches files. The split is: **chat = decisions, Code = execution**.

The vault at `C:\Users\Jwuts\obsidian-work` is the working directory. Claude Code reads `CLAUDE.md` and `01-context/` on startup to load session context automatically.

Skills drive specialized behavior. When a task touches USADeBusk work, the relevant skill(s) are loaded (via `/skill` or Cowork's auto-load). Skills live at `~/.claude/skills/`. The active set:

- `usadebusk-core` — always loaded for USADeBusk tasks
- `usadebusk-equipment`, `usadebusk-estimating`, `usadebusk-fieldpm`, `usadebusk-ops`, `usadebusk-sop` — domain-specific
- `usadebusk-vault-ingest` — converts raw docs to vault notes
- `claude-obsidian` plugin skills — wiki query, ingest, lint, save, etc.

## Config repo

`~/.claude` IS the live runtime directory — no deploy step. Config repo: https://github.com/TheSkinz/claude-config. Fetch before working on it to avoid clobbering upstream changes.

## Key workflow patterns

**Recon before drafting.** Read the actual files first; never infer or assert unverified specifics as certain. This is the rule that prevents hallucinated content in documents that look authoritative.

**Staged-count guard.** Before every commit, verify staged file count matches what was intended. One extra file staged is an easy way to commit vault noise or credentials.

**Fetch before work.** For config repo edits, pull first.

**Two-failure stop.** After two consecutive failures from the same root cause, stop and diagnose before a third attempt. Prevents spinning on a wrong assumption.

**Git guard hook.** `~/.claude/hooks/usadebusk-git-guard.mjs` blocks git mutation verbs on any command containing a `USADEBUSK\` directory path. A block there is expected — get explicit confirmation before proceeding.

## Known limitations / gotchas

- Claude Code is session-scoped; context is rebuilt each session from `01-context/` and memory. Long context is summarized automatically, but deep state from early in a session can drift.
- File write on Windows uses PowerShell-style paths. Bash tool uses POSIX syntax inside Git Bash — path mismatches can cause silent failures if mixing shells.
- Large vault glob operations can be slow; prefer targeted reads over broad auto-scans.
- Vision / image reading works but hasn't been benchmarked against Gemini for engineering drawings. See [[gem-drawing-extraction]] for current production standard.

## Links

- Config repo: https://github.com/TheSkinz/claude-config
- Vault CLAUDE.md: `C:\Users\Jwuts\obsidian-work\CLAUDE.md`
