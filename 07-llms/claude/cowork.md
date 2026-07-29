---
title: Cowork
created: 2026-06-29
tags: [claude, cowork, dispatch, automation, scheduled-tasks]
---

# Cowork

Rewritten 2026-07-29. The prior version of this note said Cowork "is not a separate product —
it's the scheduled-task and hook layer built into the Claude Code desktop app," listed a "1pm CT
Work Brief" scheduled task, and described the capture loop as prototyped but unbuilt. All three
are now wrong: Cowork is a distinct surface, that task no longer exists, and the capture loop has
been live since June and daily since 2026-07-28. Version-sensitive details below should be
re-verified against `code.claude.com/docs` per the standing rule in [[code]].

## What it is

Cowork is one of the three tabs in the Claude Desktop app — **Chat**, **Cowork**, **Code**. It
hosts [Dispatch](#dispatch) and longer agentic knowledge work: research, documents, spreadsheets.
The Code tab is Claude Code proper. They are different execution contexts, and the difference
that matters is where they get their skills.

**Cowork sources its skills, plugins, and connectors from the claude.ai account configuration**
(Customize in the Desktop sidebar, or skills settings on claude.ai) — **not** from
`~/.claude/skills/`. That library is a separate upload with no sync in either direction, which is
the drift exposure recorded in `00-inbox/2026-07-20-claudeai-skill-library-is-a-second-copy.md`:
the Skill-Drift Loop maintains the config-repo copies, and nothing updates the uploaded ones.

A Claude Code session, including one Dispatch spawns into the Code tab, is a local session and
reads `~/.claude/skills/` normally. So the same question can get a maintained answer or a frozen
one depending only on which surface handled it.

## Dispatch

One continuous conversation messaged from the Claude mobile app, executing on the desktop with
local files, connectors, plugins, and apps. Requires Pro or Max; not available on Team or
Enterprise. Setup is **Cowork tab > Dispatch (left panel)**, with toggles for file access and
Keep Awake.

Dispatch routes each task: development-shaped work spawns a Claude Code session that appears in
the Code tab with a **Dispatch** badge, while research, document, and spreadsheet work stays in
Cowork. You can force the routing by asking for it — *"open a Claude Code session and …"* — and
for vault or USADebusk work you should, for the skill-sourcing reason above.

What is controllable: file access, Keep Awake, memory (viewable and manageable), scheduled tasks,
and computer use (off by default, research preview, Pro/Max, available on Windows). What is not:
there is one thread, with no way to start or manage a second. That rules Dispatch out as the home
for a per-job field thread, which `usadebusk-fieldpm` builds around one dedicated session per job.

See [[mobile-field-access]] for how Dispatch fits against Remote Control and cloud sessions.

## Desktop scheduled tasks

The five vault loops run as **desktop scheduled tasks** — local cron-like runs defined under
`~/.claude/scheduled-tasks/`, executing on this machine and loading skills from the same places
any local session does. This is the mechanism, not Cowork cloud:

| Task | Schedule |
|---|---|
| `vault-idea-research-loop` | 02:00 daily |
| `vault-skill-drift-loop` | 03:00 on the 1st |
| `vault-consolidation-loop` | 03:00 on the 15th |
| `vault-capture-loop` | 05:00 daily |
| `vault-prestaging-loop` | 06:00 daily |

Each carries a jitter offset, so the listed fire times are approximate by a few minutes.

**A sleeping or closed machine defers them to next launch, and it is visible.** On 2026-07-29 the
idea-research, capture, and pre-staging loops all recorded `lastRunAt` of 14:41 — a catch-up batch
firing together at app launch instead of at 02:00, 05:00, and 06:00. That collapses the deliberate
one-hour gap between capture (05:00) and pre-staging (06:00), which exists so pre-staging reads the
current day's deferrals. Dispatch's **Keep Awake** toggle is the direct fix and is worth enabling
independent of any mobile use.

## Hook layer

Hooks run shell commands on tool-call events, configured in `settings.json`. The active one is the
git guard at `~/.claude/hooks/usadebusk-git-guard.mjs`, which blocks git mutation verbs on paths
containing a `USADEBUSK\` directory. A block there is expected behaviour, not an error.

## Links

- [[code]] — Claude Code surfaces and the post-cutoff capture rule
- [[mobile-field-access]] — which surface to use from the phone, and what each one costs
- [[vault-capture-loop-spec]] — the 05:00 loop
- [[chat]] — the claude.ai chat surface and its own skill-library exposure
