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
**Resolved 2026-10-01: install it as a service.** See "Before leaving town" below.

One durable trap: the permission grant needed to do any of this cannot be written by the agent
that needs it — the harness blocks an agent editing its own `permissions.allow`, and that guard
is correct. `/permissions` does not exist in mobile Remote Control sessions either. The route
that worked was editing `settings.json` in the `TheSkinz/claude-config` repo from the phone's
browser and pulling it on Linda2, since `~/.claude` is the live clone.

## A proven door can still be down, and only the check says so (2026-10-03)

Two days after the restart test proved both doors, `remote_access_check.py` read **3/5** and the
only discriminating row, `claude remote-control process running`, read **0 processes**. The
RustDesk service was up, the scheduled task existed and sat `Ready`, `AutoAdminLogon` was on, and
`LastTaskResult` was `0` from the 10-01 run. Everything that was easy to look at looked fine.

**The task being `Ready` means registered and not currently running — it is not a health signal.**
The vault door was simply shut, with nothing anywhere announcing it. What closed it between 10-01
and 10-03 is not recorded; the wrapper loops forever, so the likeliest cause is the console window
being closed rather than the process dying.

`Start-ScheduledTask -TaskName 'Claude Remote Control vault'` restored it and the check went to
4/5. **Two verification notes worth keeping.** `LastTaskResult 0` only says the launcher
succeeded, not that Remote Control came up: confirm the `cmd` window titled
`Claude Remote Control - vault` plus its `claude` children, or just re-run the check. And starting
Remote Control creates `~/.claude/bridge-spawn/cse_*` — runtime state, gitignored 2026-10-03 so it
stops showing as untracked in the config repo.

**`claude rc` is a real subcommand as of 2.1.291 (2026-10-06).** It is the short form of
`claude remote-control`; the phone app's Code > Devices > Add device screen now tells you to run
it, and `claude rc --help` on Linda2 answered with Remote Control's own auth error rather than
treating `rc` as a prompt. An earlier version of this note said there was no `rc` subcommand,
which was true of the build it was written against and is stale now. Two things still distinguish
it. Run from a shell it is the server mode that puts Linda2 under **Devices** and lets the phone
start new sessions; the in-session slash command `/rc` (or `/remote-control`) only shares the one
session it is typed into and never makes the machine appear under Devices. And from a bare
terminal it fails with "Remote Control requires claude.ai subscription auth" because
`ANTHROPIC_API_KEY` is set at user scope — clear it for that window first
(`$env:ANTHROPIC_API_KEY=$null`), which is what `start_remote_control.cmd` does.

**Recurrence 2026-10-06.** Devices was empty on the phone at the desk; no `remote-control` process
was running although the logon task showed `Ready`. `schtasks /run /tn "Claude Remote Control vault"`
brought it back (`claude.exe remote-control --name vault --spawn same-dir` confirmed in the process
list). Second time the task has been found stopped; cause again not recorded.

---

## Before leaving town (2026-10-01)

Both lockouts, 09-16 and 09-23, were caused by a Windows Update restart in the early morning
(System event 1074, TrustedInstaller, 03:31 and 04:34), just after the 11:00–04:00 active-hours
window closed. A third one hit mid-session on 10-01. Linda2 comes back and logs itself in
(`AutoAdminLogon=1`), but anything that was started by hand does not. Windows 11 Home cannot
host RDP, so that is not an option.

The standing setup is **two doors, each of which survives an unattended restart:**

- **RustDesk, installed as a service.** This is the GUI door. It works past the lock screen and
  UAC, which is what you need for desktop-app re-logins like the 09-16 OAuth fault.
  **Done 2026-10-01:** 1.4.9 installed from the GitHub release MSI. RustDesk is not in the
  winget catalog, so `winget install` finds nothing. The MSI installs the `RustDesk` service
  (Automatic, `--service`) on its own. Its signer is PURSLANE, RustDesk's company. ID
  **534 040 005**. Jesse connected from the phone the same day. The "not logged in" banner is
  for an optional RustDesk account (address-book sync) and does not affect connecting by
  ID + password.
- **Remote Control, started at logon by the scheduled task `Claude Remote Control vault`.**
  This is the vault door, and its auth is independent of the desktop app's. **Done
  2026-10-01.** The task runs `tools/start_remote_control.cmd` at logon (30 s delay, no time
  limit). The script loops, so a crash or a long network drop restarts it 30 s later. The
  task opens it in a **minimized** console window titled "Claude Remote Control - vault", via
  `cmd /c start /min`. Closing that window stops Remote Control. The exit code is then
  `0xC000013A`, which Windows doesn't count as a failure, so nothing restarts it. That happened
  in the first restart test on 2026-10-01, when the window was opened on screen. Two traps it handles, both
  found the first time it ran unattended:
  - `ANTHROPIC_API_KEY` is set at user scope on Linda2. With it present, Remote Control exits
    with code 1 ("requires claude.ai subscription auth"). The script clears it for its own
    window only. A hand-run test from a Claude Code shell passes because that shell doesn't
    carry the variable, so it proves nothing about the logon path.
  - On first launch, Remote Control stops and asks which spawn mode to use, and an unattended
    window waits on that forever. The script passes `--spawn same-dir` so the question never
    comes up.

**Restart test passed 2026-10-01 18:00, unattended.** This is the test the first attempt the
same day failed, and it is what promotes the setup from built to proven. Linda2 rebooted at
18:00:07 with nobody logged in; the `Claude Remote Control vault` task ran at **18:00:51**
(44 s — the 30 s delay plus autologon) and returned `LastTaskResult 0` with 0 missed runs, and
a `claude remote-control` process was alive and serving at 18:02. RustDesk was reachable
through the restart, with `RustDesk.exe` present in the **Services** session as well as the
console one — which is the service door working past the lock screen rather than a user-session
copy. Verified from the check script plus `Get-ScheduledTaskInfo` and `tasklist`, not from a
success message. Evidence of what makes the difference: the minimized window
(`cmd /c start /min`) was never touched this time, so nothing produced the `0xC000013A` that
killed the first attempt.

The Desktop Commander agent is retired. It needed a browser sign-in after every restart and
never survived one.

Before each trip:

`Settings > Windows Update > Pause updates (past return)` → `python tools/remote_access_check.py --return-date YYYY-MM-DD` (all PASS) →
restart Linda2 → from the phone **on cellular**, reach RustDesk and the `vault` session.

The check script verifies the conditions, but only the restart test proves both doors work —
done once unattended on 2026-10-01, so re-run it only after something changes the logon path.
Expect **4/5** on a normal desk day: the update-pause row is the one FAIL, and it is correct to
leave updates live when you are not travelling. The row that is actually the test is
`claude remote-control process running`; the service and task-exists rows passed on the attempt
that failed too, so they discriminate nothing on their own.

One gap no software covers, and the only item still owed: unless BIOS "Restore on AC power loss"
is set to Power On, a power cut leaves Linda2 off until someone presses the button. **Not
reachable over RustDesk** — it is pre-boot, so it waits until Jesse is physically at the box.

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
