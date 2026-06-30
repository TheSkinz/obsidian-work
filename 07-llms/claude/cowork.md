---
title: Cowork (Claude Code Scheduled / Auto-Context)
created: 2026-06-29
tags: [claude, cowork, automation, scheduled-tasks]
---

# Cowork

Cowork is the Claude Code harness feature that runs scheduled agents and auto-loads session context. It is not a separate product — it's the scheduled-task and hook layer built into the Claude Code desktop app.

## Scheduled tasks (deployed)

**1pm CT Work Brief** — runs daily on a cron schedule. Reads `01-context/` (active-jobs, company-context, equipment-fleet, estimating-approach, output-preferences, workflow-map) and generates a brief summary of active state. This is what auto-loads vault context each afternoon.

Other scheduled tasks: none currently deployed beyond the work brief.

## Auto-load mechanism

When Cowork triggers a session, it reads every file in `01-context/` before responding. This is why the folder exists as a distinct layer — it's the guaranteed-loaded context, not just documentation. Files there are kept short and current precisely because they load every session.

## Planned: capture loop

A capture loop has been prototyped in concept but not built. The idea: an automated agent that polls `00-inbox/`, proposes how to file or process each item (propose-don't-commit model), and waits for confirmation before writing to the vault. Directly related to [[self-improving-systems]].

Design constraint: the loop should propose, not commit, to prevent automated writes from corrupting vault state.

## Hook layer

Beyond scheduled tasks, Cowork's hook system runs shell commands in response to tool-call events. The active hook is the git guard at `~/.claude/hooks/usadebusk-git-guard.mjs`. More hooks can be added via `/update-config` or by editing `settings.json` directly.
