---
title: Mobile / Field Access
created: 2026-07-29
tags: [claude-code, mobile, field, remote-control, dispatch, workflow]
---

# Mobile / Field Access

How to reach the vault and put information into it from the iPhone while out in the field.
Written 2026-07-29 against Claude Code CLI 2.1.143 and the Claude iOS app; version-sensitive
details should be re-verified against `code.claude.com/docs` per the standing rule in
[[code]].

## The constraint that decides everything

Almost nothing this workflow depends on lives in the GitHub repo. The skills are in
`~/.claude/skills/`, the global CLAUDE.md is in `~/.claude/`, `tools/vault_lint.py` runs
against the local working tree, and the Vault Capture Loop harvests session transcripts from
`~/.claude/projects/` at 05:00 daily. A session that does not run as a local Claude Code
process is invisible to that harvest — whatever you reason out in it is lost unless it was
written to a file during the session. That is why the default mobile path drives the desktop
rather than replacing it. See [[vault-capture-loop-spec]].

## Which surface, and what each one costs

| Surface | Where it runs | Skills it loads | Vault access | Capture Loop sees it |
|---|---|---|---|---|
| Remote Control | Local CLI process | `~/.claude/skills/` — all nine | Real working tree | Yes |
| Dispatch, task stays in Cowork | Desktop app, Cowork tab | claude.ai account library only | Local files, if file access is on | No |
| Dispatch, task spawns a Code session | Desktop app, Code tab | `~/.claude/skills/` — all nine | Real working tree | Yes |
| Cloud session | Anthropic infrastructure | Repo `.claude/skills/` — currently none | Cloned repo, branch only | No |

## Default: Remote Control

Start it at the desk before leaving:

```
cd /c/Users/Jwuts/obsidian-work && claude remote-control --name vault
```

Spacebar shows a QR code. After the first scan it is just **Claude app > Code > `vault`** —
the session shows a computer icon with a green dot. Server mode serves new sessions on demand
all day from that one process, so there is no need to pre-start a session per task. The
default `--spawn same-dir` is correct here: writes land in the real vault, not an isolated
worktree. Already mid-session at the desk? `/rc vault` carries the conversation over.

Photos attached in the Claude app are downloaded to the desktop and handed to Claude as an `@`
file reference. That is the field capture mechanism — it is why this surface, not the others,
is the one for capturing what you are looking at.

The session survives sleep and network drops and reconnects on its own. It ends if the
`claude` process stops, or if the **desktop** loses network for more than about ten minutes.

Permission modes available from mobile are Manual, Accept edits, and Plan — there is no Bypass
and no Auto. Run in Accept edits; the allowlist in `.claude/settings.json` is what keeps a
one-handed session from stalling on prompts for the lint, index, and health scripts.

Push notifications are two toggles in `/config` on the desktop: *Push when Claude decides* and
*Push when actions required*.

## The field capture pattern

One message, not a filing decision:

> Field note, B-151 at Baytown — [photo] — pig came back with the nose collapsed on pass 3.
> Drop this in the inbox and push.

Claude writes a rough capture note to `00-inbox/`, commits and pushes under the lane
convention, and the 05:00 loop routes it the next morning. Do not file from the phone.

One expectation to hold: operational content does not self-file. The Capture Loop never writes
`02-facilities/`, `04-knowledge/`, pricing, SOP, or heater-card facts — it leaves them in
`00-inbox/` with a `<!-- vault-loop: -->` marker for the 06:00 pre-staging loop to analyse
for a desk decision. Field job data queues; it does not land. That is correct behaviour, not a
gap.

## Nothing pre-started: Dispatch

Dispatch is one continuous conversation messaged from the Claude app, running on the desktop
with local files, connectors, plugins, and apps. Setup is **Claude Desktop > Cowork tab >
Dispatch**, with toggles for file access and Keep Awake. See [[cowork]] for what Cowork is and
how it sources skills.

**The one thing to remember: say "open a Claude Code session" in the message.** Dispatch routes
per task — development-shaped work spawns a Claude Code session in the Code tab with a Dispatch
badge, while research, document, and spreadsheet work stays in Cowork. A task that stays in
Cowork loads skills from the claude.ai account library, which is a frozen separate upload the
Skill-Drift Loop cannot reach, so it can answer USADebusk questions from corrected-and-replaced
values. Asking for a Code session gets the maintained `~/.claude/skills/` copies.

Keep Awake is worth turning on independent of the mobile question: a scheduled task that finds
the machine asleep is deferred to next launch, and the 06:00 pre-staging loop reads the 05:00
run's output, so a sleeping machine desynchronises both.

Dispatch has one thread and no way to start a second. That rules it out as the home for a
per-job field thread — [[system-workflow-reference]] and the `usadebusk-fieldpm` skill are
built around one dedicated session per job, and Dispatch would interleave that with everything
else asked of it that week.

## Desktop down: cloud session

Claude app > Code tab > new session against `TheSkinz/obsidian-work`. Runs on Anthropic
infrastructure, so it works with the machine off. Two limits:

The vault `CLAUDE.md` and `.claude/settings.json` are committed, so vault structure and
conventions load — but `~/.claude/skills/` and the global CLAUDE.md do not exist there. Vault
navigation is reliable; USADebusk domain answers are not. Treat every number as unverified
until checked at the desk.

The transcript lives on Anthropic infrastructure, where the 05:00 harvest will never see it.
Anything worth keeping has to be written into a file during the session, not just discussed.

On return: merge the branch it pushed, then `git pull` on the desktop before the next 05:00 run
so the loop actually sees the new inbox file.

## Links

- [[code]] — Claude Code surface reference and the post-cutoff capture rule
- [[cowork]] — what Cowork is, and how Dispatch sources skills
- [[obsidian-setup]] — vault path, git-as-sync
- [[vault-capture-loop-spec]] — the 05:00 loop this workflow feeds
