---
title: Mobile / Field Access
created: 2026-07-29
tags: [claude-code, mobile, field, remote-control, dispatch, workflow]
---

# Mobile / Field Access

How to reach the vault and put information into it from the iPhone while out in the field.
Written 2026-07-29 against the Claude iOS app and CLI 2.1.220; version-sensitive details should
be re-verified against `code.claude.com/docs` per the standing rule in [[code]].

**The npm CLI and the Desktop app update independently — check both after any gap.** They were
found 76 versions apart on 2026-07-29 (npm on 2.1.143, Desktop on 2.1.219) with nothing visibly
wrong on either side; npm is now current at 2.1.220. `npm ls -g @anthropic-ai/claude-code` is
the check that answers "am I current" — `npm view` only reports the registry's latest, not what
you have. After running `npm i -g @anthropic-ai/claude-code@latest`, re-check the version rather
than trusting the success message: the first attempt here reported "changed 2 packages" while a
running `claude` process silently kept the old binary in place. Close all `claude` processes
before upgrading. See the two-installs section in [[code]] for the full incident.

## The constraint that decides everything

Almost nothing this workflow depends on lives in the GitHub repo. The skills are in
`~/.claude/skills/`, the global CLAUDE.md is in `~/.claude/`, and `tools/vault_lint.py` runs
against the local working tree. A session that does not run as a local Claude Code process
reaches none of it.

**Nothing harvests a session any more.** The Vault Capture Loop read transcripts from
`~/.claude/projects/` at 05:00 daily until it was stopped 2026-08-21, and nothing replaced it.
The rule that used to apply only to cloud sessions now applies to **every** surface, this one
included: whatever you reason out is lost unless it was written to a file during the session.
That is why the default mobile path drives the desktop rather than replacing it — for the real
working tree and the full skill set, not for a harvest that no longer runs. Current status of
all six loops: [[system-workflow-reference]].

## Which surface, and what each one costs

The last column replaced "Capture Loop sees it" on 2026-09-08. That loop is stopped, so no
surface is harvested and the question stopped discriminating between them; where a write lands
is what actually differs now.

| Surface | Where it runs | Skills it loads | Vault access | Writes land |
|---|---|---|---|---|
| Remote Control | Local CLI process | `~/.claude/skills/` — all ten | Real working tree | In the real vault |
| Dispatch, task stays in Cowork | Desktop app, Cowork tab | claude.ai account library only | Local files, if file access is on | Local files only |
| Dispatch, task spawns a Code session | Desktop app, Code tab | `~/.claude/skills/` — all ten | Real working tree | In the real vault |
| Cloud session | Anthropic infrastructure | Repo `.claude/skills/` — currently none | Cloned repo, branch only | On a branch you must merge |

## Default: Remote Control

Start it at the desk before leaving. The full pre-departure sequence is three settings, all of
which have to be set while you are physically at the machine — the 2026-09-16 incident below
happened because only the third was ever documented here:

`Settings > General > Enable computer use` → `Cowork > Dispatch > Keep Awake on` →
`claude remote-control --name vault`

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

Claude writes a rough capture note to `00-inbox/`, commits and pushes under the lane convention.

**Still don't file from the phone** — one-handed in the field is no place to decide where a fact
belongs. But nothing routes it for you afterwards either, which is the part that changed. The
note sits in `00-inbox/` until a desk session works it, so mention it in the next desk session
rather than assuming it has been picked up.

One expectation to hold: operational content does not self-file, and now nothing else files it
either. Field job data — `02-facilities/`, `04-knowledge/`, pricing, SOP, heater-card facts —
stays in `00-inbox/` with a `<!-- vault-loop: -->` marker until you rule on it at the desk. It
queues; it does not land. That is still correct behaviour, but the queue no longer has a reader,
so coming back to it is on you.

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
the machine asleep is deferred to next launch. That matters less than it did — the three daily
loops stopped 2026-08-21 and the three that survive run monthly — but a monthly task that keeps
slipping to next launch still drifts off its cadence.

Dispatch has one thread and no way to start a second. That rules it out as the home for a
per-job field thread — [[system-workflow-reference]] and the `usadebusk-fieldpm` skill are
built around one dedicated session per job, and Dispatch would interleave that with everything
else asked of it that week.

## When Dispatch says "Looking for your desktop" (2026-09-16)

Diagnosed and fixed from Montreal, with nobody able to reach Linda2. The phone showed
"Looking for your desktop… Make sure you have the Claude Desktop app installed, open, and
signed in" while the desktop app was in fact running, computer use was enabled, and the device
bridge was authenticated. **The message is misleading: the app being open is not the thing it
is actually checking.**

The real fault was an expired OAuth scope, visible only in `AppData\Local\Claude\Logs\main.log`:

```
[sessions-bridge] Cowork OAuth stale-session (session_stale_relogin); parking bridge until re-login
oauth authorize rejected with session_stale_relogin; sessionKey is valid but too old for the requested scope expansion
[DispatchTools] start_code_task failed for C:\Users\Jwuts\obsidian-work: Sign in again to continue
```

The session key was still valid — which is why Claude Code, the `remote-tools-device` bridge and
computer use all kept working — but too old to grant the scope expansion Dispatch needs, so the
sessions-bridge parked itself. It retries hourly (`[oauth] clearing latched session_stale_relogin
failures`) and fails every time. **It does not self-heal.** Grep `main.log` for
`session_stale_relogin` before assuming anything else; every other symptom was a red herring.

The fix is an interactive re-login in the desktop app, which needs the GUI. Three things made
that reachable and are worth keeping true:

**Remote Control has independent auth and survives this.** `claude remote-control` is an npm CLI
process; its credentials are not the desktop app's OAuth session. When Dispatch was dead the
`vault` session worked from Montreal all evening. That makes it the correct standing fallback,
not just a convenience — but note it carries **no computer use**, because the `computer_*` tools
are supplied by the desktop app to sessions it hosts, and a terminal CLI session is not one.

**Screen capture from a Claude Code session on the machine is only half a channel.** GDI
`CopyFromScreen` returns black for GPU-composited windows, and `PrintWindow` with
`PW_RENDERFULLCONTENT` gets Chromium's browser frame — enough to read the URL bar — but not the
rendered page, and nothing at all from Flutter apps. Synthetic keyboard input into a browser
sign-in flow is refused by the permission classifier, correctly. So a session on the box can
diagnose and can read a URL, but cannot complete a login.

**Linda2 had no remote-access software, and that is what turned a sixty-second fix into an
evening.** RustDesk was installed remotely as the way out, non-elevated — which means it runs
only while its process lives, does not survive a reboot, and cannot interact with UAC prompts.
Decide deliberately whether to install it properly as a service or remove it; a half-configured
remote door is the worst of both.

One durable trap: the permission grant needed to do any of this cannot be written by the agent
that needs it — the harness blocks an agent editing its own `permissions.allow`, and that guard
is correct. `/permissions` does not exist in mobile Remote Control sessions either. The route
that worked was editing `settings.json` in the `TheSkinz/claude-config` repo from the phone's
browser and pulling it on Linda2, since `~/.claude` is the live clone.

## Desktop down: cloud session

Claude app > Code tab > new session against `TheSkinz/obsidian-work`. Runs on Anthropic
infrastructure, so it works with the machine off. Two limits:

The vault `CLAUDE.md` and `.claude/settings.json` are committed, so vault structure and
conventions load — but `~/.claude/skills/` and the global CLAUDE.md do not exist there. Vault
navigation is reliable; USADebusk domain answers are not. Treat every number as unverified
until checked at the desk.

The transcript lives on Anthropic infrastructure. Anything worth keeping has to be written into
a file during the session, not just discussed — which, since the harvest stopped, is now true of
every surface rather than a limitation peculiar to this one.

On return: merge the branch it pushed, then `git pull` on the desktop before the next session
touches the vault.

## Links

- [[code]] — Claude Code surface reference and the post-cutoff capture rule
- [[cowork]] — what Cowork is, and how Dispatch sources skills
- [[obsidian-setup]] — vault path, git-as-sync
- [[system-workflow-reference]] — current status of all six loops, and the on-demand ingest flow
