---
title: Mobile / Field Access
created: 2026-07-29
tags: [claude-code, mobile, field, remote-control, dispatch, workflow]
---

# Mobile / Field Access

How to reach the vault and put information into it from the iPhone while out in the field, and
how Linda2 stays reachable while Jesse is away from it. First written 2026-07-29 against the
Claude iOS app and CLI 2.1.220; version-sensitive details should be re-verified against
`code.claude.com/docs` per the standing rule in [[code]]. Consolidated into one article
2026-10-15 from dated session additions running to 2026-10-06; every fact and date was carried
over.

**The npm CLI and the Desktop app update independently — check both after any gap.** They were
found 76 versions apart on 2026-07-29 (npm on 2.1.143, Desktop on 2.1.219) with nothing visibly
wrong on either side; npm was brought current at 2.1.220 the same day. `npm ls -g
@anthropic-ai/claude-code` is the check that answers "am I current" — `npm view` only reports
the registry's latest, not what you have. After running `npm i -g @anthropic-ai/claude-code@latest`,
re-check the version rather than trusting the success message: the first attempt reported
"changed 2 packages" while a running `claude` process silently kept the old binary in place.
Close all `claude` processes before upgrading. See the two-installs section in [[code]] for the
full incident.

## The constraint that decides everything

Almost nothing this workflow depends on lives in the GitHub repo. The skills are in
`~/.claude/skills/`, the global CLAUDE.md is in `~/.claude/`, and `tools/vault_lint.py` runs
against the local working tree. A session that does not run as a local Claude Code process
reaches none of it.

**Nothing harvests a session.** The Vault Capture Loop read transcripts from `~/.claude/projects/`
at 05:00 daily until it was stopped 2026-08-21, and nothing replaced it. On **every** surface,
whatever you reason out is lost unless it was written to a file during the session. That is why
the default mobile path drives the desktop rather than replacing it — for the real working tree
and the full skill set. Current status of all six loops: [[system-workflow-reference]].

## Which surface, and what each one costs

The last column replaced "Capture Loop sees it" on 2026-09-08: with that loop stopped no surface
is harvested, so where a write lands is what actually differs.

| Surface | Where it runs | Skills it loads | Vault access | Writes land |
|---|---|---|---|---|
| Remote Control | Local CLI process | `~/.claude/skills/` — all ten | Real working tree | In the real vault |
| Dispatch, task stays in Cowork | Desktop app, Cowork tab | claude.ai account library only | Local files, if file access is on | Local files only |
| Dispatch, task spawns a Code session | Desktop app, Code tab | `~/.claude/skills/` — all ten | Real working tree | In the real vault |
| Cloud session | Anthropic infrastructure | Repo `.claude/skills/` — currently none | Cloned repo, branch only | On a branch you must merge |

## Default: Remote Control

Remote Control is the vault door and the default field surface. On the phone it is **Claude app >
Code > `vault`**; the session shows a computer icon with a green dot. Server mode serves new
sessions on demand all day from one process, so there is no need to pre-start a session per task.
`--spawn same-dir` is correct here: writes land in the real vault, not an isolated worktree.

On Linda2 the server is kept up by a scheduled watchdog (see "Linda2's two remote doors" below),
which runs `claude.exe remote-control --name vault --spawn same-dir`. **Never start a second copy
by hand** — a second `remote-control --name vault` does not displace the first, and the phone lists
duplicate and ghost entries that never clear. `tools/rc_start.cmd` is the manual start. On a
machine without the watchdog the command is
`cd /c/Users/Jwuts/obsidian-work && claude remote-control --name vault`, and spacebar shows the QR
code for the first pairing.

The pre-departure settings all have to be set while physically at the machine — the 2026-09-16
incident below happened because only the last of them was ever documented here:

`Settings > General > Enable computer use` → `Cowork > Dispatch > Keep Awake on` → Remote Control running

**`claude rc` is a real subcommand as of 2.1.291 (2026-10-06)**, the short form of
`claude remote-control`. The phone app's Code > Devices > Add device screen tells you to run it,
and `claude rc --help` on Linda2 answered with Remote Control's own auth error rather than treating
`rc` as a prompt; an earlier version of this note said there was no `rc` subcommand, which was true
of the build it was written against. Run from a shell, it is the server mode that puts Linda2 under
**Devices** and lets the phone start new sessions. The in-session slash command `/rc` (or
`/remote-control`) only shares the one session it is typed into — already mid-session at the desk,
`/rc vault` carries the conversation over — and never makes the machine appear under Devices.

Two traps catch any unattended start, both found the first time it ran unattended:

- `ANTHROPIC_API_KEY` is set at user scope on Linda2. With it present, Remote Control exits with
  code 1 ("Remote Control requires claude.ai subscription auth"). `start_remote_control.cmd` clears
  it for its own window only; from a bare terminal, clear it first (`$env:ANTHROPIC_API_KEY=$null`).
  A hand-run test from a Claude Code shell passes because that shell doesn't carry the variable,
  so it proves nothing about the logon path.
- On first launch, Remote Control stops and asks which spawn mode to use, and an unattended window
  waits on that forever. Passing `--spawn same-dir` means the question never comes up.

Photos attached in the Claude app are downloaded to the desktop and handed to Claude as an `@`
file reference. That is the field capture mechanism, and why this surface, not the others, is the
one for capturing what you are looking at.

The session survives sleep and network drops and reconnects on its own. It ends if the `claude`
process stops, or if the **desktop** loses network for more than about ten minutes. Remote Control
has auth independent of the desktop app's OAuth session, but carries **no computer use**: the
`computer_*` tools are supplied by the desktop app to sessions it hosts, and a terminal CLI session
is not one. Starting it creates `~/.claude/bridge-spawn/cse_*`, which is runtime state, gitignored
in the config repo 2026-10-03.

Permission modes available from mobile are Manual, Accept edits, and Plan — there is no Bypass and
no Auto. Run in Accept edits; the allowlist in `.claude/settings.json` is what keeps a one-handed
session from stalling on prompts for the lint, index, and health scripts. `/permissions` does not
exist in mobile Remote Control sessions.

Push notifications are two toggles in `/config` on the desktop: *Push when Claude decides* and
*Push when actions required*.

## The field capture pattern

One message, not a filing decision:

> Field note, B-151 at Baytown — [photo] — pig came back with the nose collapsed on pass 3.
> Drop this in the inbox and push.

Claude writes a rough capture note to `00-inbox/`, commits and pushes under the lane convention.

**Don't file from the phone** — one-handed in the field is no place to decide where a fact belongs.
Nothing routes it afterwards either: the note sits in `00-inbox/` until a desk session works it, so
mention it in the next desk session rather than assuming it has been picked up.

Operational content does not self-file. Field job data — `02-facilities/`, `04-knowledge/`,
pricing, SOP, heater-card facts — stays in `00-inbox/` with a `<!-- vault-loop: -->` marker until
you rule on it at the desk. It queues; it does not land, and the queue has no reader, so coming
back to it is on you.

## Linda2's two remote doors

Both lockouts, 09-16 and 09-23, were caused by a Windows Update restart in the early morning
(System event 1074, TrustedInstaller, 03:31 and 04:34), just after the 11:00–04:00 active-hours
window closed. A third hit mid-session on 10-01. Linda2 comes back and logs itself in
(`AutoAdminLogon=1`), but anything started by hand does not. Windows 11 Home cannot host RDP.

The standing setup is **two doors, each of which survives an unattended restart:**

- **RustDesk, installed as a service** — the GUI door. It works past the lock screen and UAC, which
  is what desktop-app re-logins like the 09-16 OAuth fault need. Installed 2026-10-01: 1.4.9 from
  the GitHub release MSI (RustDesk is not in the winget catalog, so `winget install` finds nothing).
  The MSI installs the `RustDesk` service (Automatic, `--service`) on its own; its signer is
  PURSLANE, RustDesk's company. ID **534 040 005**. Jesse connected from the phone the same day.
  The "not logged in" banner is for an optional RustDesk account (address-book sync) and does not
  affect connecting by ID + password.
- **Remote Control, kept up by the scheduled task `Claude Remote Control vault`** — the vault door.
  Since 2026-10-06 the task runs `tools/rc_watchdog.ps1` under `conhost --headless`, with
  `MultipleInstances=IgnoreNew` and a 5-minute limit. It has two triggers, **both needed**: at
  logon (30 s delay), and a time trigger repeating every 5 minutes indefinitely. A repeat attached
  to a logon trigger only starts counting at a logon, so the first build (logon trigger only,
  registered mid-session at 11:29) ran once at 11:31 and never again until the next logon; a phone
  session caught it from `NextRunTime` being blank. Jesse added the time trigger by hand at 13:12,
  because the auto-mode classifier blocks agents from editing the task; NextRunTime then read
  13:15:48.

Each watchdog run takes about a second:

1. If no `vault` server is running, it starts `start_remote_control.cmd` in a hidden console. That
   script runs Remote Control once and appends its exit code to the log.
2. If more than one is running, it logs a warning and touches nothing.
3. If the npm Claude Code version differs from the one the server started with, it restarts the
   server once the server has no child session processes, or regardless between 03:00 and 04:59.

There is no window, so nothing can be closed by accident. Turn it off on purpose with
`tools/rc_stop.cmd`, which writes `tools/logs/rc.stop` and kills the server; `rc_start.cmd` reverses
that. Events go to `tools/logs/rc_watchdog.log` (gitignored, rotated at 1 MB). A server killed by a
shutdown leaves no `exited` line, because the shutdown kills its runner `cmd` too — a missing exit
line means the runner died with it, not a crash.

The 03:00–04:59 fallback is likely the path most updates take in practice: a restarted server
resumes the previous phone session as a child process within seconds (docs: sessions resume when
restarted in the same directory within ~4 h), so the "no session open" condition is usually false.

**Research behind the design (2026-10-06, via a research agent; sources not re-read).**
anthropics/claude-code #71532 and #87413 (both closed not-planned) report the duplicate and ghost
entries a second `--name vault` server produces. #84817 reports a running server still showing
ready after an auto-update while new sessions fail, with the workaround of restarting after
updates. Power users on Windows (Lhotka's blog 2026-09-21, curran-gehring/claude-remote-control-keepalive,
jozefkun/claude-rc-service) all use a scheduled-task watchdog, not NSSM or a service, because the
OAuth credentials live in the user profile.

The Desktop Commander agent is retired. It needed a browser sign-in after every restart and never
survived one.

### Before leaving town

`Settings > Windows Update > Pause updates (past return)` → `python tools/remote_access_check.py --return-date YYYY-MM-DD` (all PASS) →
restart Linda2 → from the phone **on cellular**, reach RustDesk and the `vault` session.

The check script verifies conditions; only a restart test proves both doors work. Re-run the
restart test only after something changes the logon path. The check has six rows as of the
2026-10-06 watchdog rebuild (read from the script): RustDesk service, task exists, task runs the
hidden watchdog every 5 minutes (fails when NextRunTime is blank), exactly one Remote Control
`vault` process, Windows Update paused past return, and autologon. Expect **5/6** on a normal desk
day — the update-pause row is the one FAIL, and it is correct to leave updates live when you are not
travelling (before the watchdog row was added this read 4/5). The process row is the one that
actually discriminates: it passes only on **exactly one** server, and the script prints the last
five watchdog log lines. The service and task-exists rows passed on the attempt that failed too.

**The task showing `Ready` is not a health signal** — it means registered and not currently
running. `LastTaskResult 0` only says the launcher succeeded, not that Remote Control came up.

One gap no software covers, and the only item still owed: unless BIOS "Restore on AC power loss" is
set to Power On, a power cut leaves Linda2 off until someone presses the button. **Not reachable
over RustDesk** — it is pre-boot, so it waits until Jesse is physically at the box.

### Test and failure record

- **2026-10-01, restart test passed unattended**, the test that promoted the setup from built to
  proven. The first attempt the same day failed: the original task ran `cmd /c start /min` on a
  looping `start_remote_control.cmd`, and touching the minimized window produced the `0xC000013A`
  that killed it. On the retest the window was never touched. Linda2 rebooted at 18:00:07 with
  nobody logged in; the task ran at **18:00:51** (44 s — the 30 s delay plus autologon) and
  returned `LastTaskResult 0` with 0 missed runs, and a `claude remote-control` process was alive
  and serving at 18:02. RustDesk was reachable through the restart, with `RustDesk.exe` present in
  the **Services** session as well as the console one — the service door working past the lock
  screen rather than a user-session copy. Verified from the check script plus
  `Get-ScheduledTaskInfo` and `tasklist`, not from a success message.
- **2026-10-03, a proven door was down and only the check said so.** The check read **3/5** with
  **0** Remote Control processes. The RustDesk service was up, the task existed and sat `Ready`,
  `AutoAdminLogon` was on, and `LastTaskResult` was `0` from the 10-01 run. What closed it is not
  recorded; the old wrapper looped forever, so the likeliest cause was the console window being
  closed. `Start-ScheduledTask -TaskName 'Claude Remote Control vault'` restored it and the check
  went to 4/5.
- **2026-10-06, two more stops, both on the old looping-window task.** First, Devices was empty on
  the phone at the desk with no `remote-control` process although the task showed `Ready`;
  `schtasks /run /tn "Claude Remote Control vault"` brought it back. Second, restarted at 10:24 and
  found dead by 10:37 while Jesse was experimenting with the iPhone app; this time the wrapper `cmd`
  was gone as well as `claude.exe`, so the whole console window had closed — the loop cannot exit by
  itself. The same `schtasks /run` restored it (new `claude.exe` at 10:38). Jesse had, as a
  deliberate test, started `claude remote-control` in a terminal of his own and closed that terminal,
  which explains the session going offline; it does not explain the task's own window disappearing.
  Either it had already stopped, or a second instance using the same `vault` name made it exit. The
  wrapper echoed exit codes only to its console, so nothing recorded which. These stops are what the
  hidden watchdog and its log replaced.
- **2026-10-06 11:30, watchdog cutover tests**, all run through the task, not from a tool shell. It
  started from nothing (11:29:59). A second run during a live server started no duplicate. A server
  killed on purpose with `taskkill /F` logged `exited (code 1)` — the test kill, not a crash — and
  was back on the next run. These runs were started by hand, so they did not prove the schedule (the
  two-trigger gap above). The task's own process exits while Remote Control survives it. The
  update-restart path was **not** exercised live, because of session resumption;
  `rc_server_version.txt` was left at a fake `2.1.290` so the 03:00 window would exercise it the
  first night, with the log to be read the next morning.
- **2026-10-06 13:11, restart test passed on the watchdog**, before the time trigger existed. Jesse
  restarted Linda2 (System 1074 at 13:11:02, boot 13:11:36, logon event 7001 at 13:11:49). The logon
  trigger ran the watchdog 30 s later at 13:12:20; it found no server and started one at 13:12:22.
  The time trigger added afterwards (StartBoundary 13:15:48) fired on schedule. The 11:30 server
  left no `exited` line because the shutdown killed its runner `cmd` too.

## Nothing pre-started: Dispatch

Dispatch is one continuous conversation messaged from the Claude app, running on the desktop with
local files, connectors, plugins, and apps. Setup is **Claude Desktop > Cowork tab > Dispatch**,
with toggles for file access and Keep Awake. See [[cowork]] for what Cowork is and how it sources
skills.

**The one thing to remember: say "open a Claude Code session" in the message.** Dispatch routes per
task — development-shaped work spawns a Claude Code session in the Code tab with a Dispatch badge,
while research, document, and spreadsheet work stays in Cowork. A task that stays in Cowork loads
skills from the claude.ai account library, which is a frozen separate upload the Skill-Drift Loop
cannot reach, so it can answer USADebusk questions from corrected-and-replaced values. Asking for a
Code session gets the maintained `~/.claude/skills/` copies.

Keep Awake is worth turning on independent of the mobile question: a scheduled task that finds the
machine asleep is deferred to next launch. The three daily loops stopped 2026-08-21 and the three
that survive run monthly, but a monthly task that keeps slipping to next launch still drifts off its
cadence.

Dispatch has one thread and no way to start a second. That rules it out as the home for a per-job
field thread — [[system-workflow-reference]] and the `usadebusk-fieldpm` skill are built around one
dedicated session per job, and Dispatch would interleave that with everything else asked of it that
week.

### When Dispatch says "Looking for your desktop"

Diagnosed and fixed 2026-09-16 from Montreal, with nobody able to reach Linda2. The phone showed
"Looking for your desktop… Make sure you have the Claude Desktop app installed, open, and signed in"
while the desktop app was in fact running, computer use was enabled, and the device bridge was
authenticated. **The message is misleading: the app being open is not the thing it is actually
checking.**

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

The fix is an interactive re-login in the desktop app, which needs the GUI. What the incident
established:

- **Remote Control survives it.** Its credentials are not the desktop app's OAuth session; when
  Dispatch was dead the `vault` session worked from Montreal all evening. That makes it the standing
  fallback, not just a convenience.
- **Screen capture from a Claude Code session on the machine is only half a channel.** GDI
  `CopyFromScreen` returns black for GPU-composited windows, and `PrintWindow` with
  `PW_RENDERFULLCONTENT` gets Chromium's browser frame — enough to read the URL bar — but not the
  rendered page, and nothing at all from Flutter apps. Synthetic keyboard input into a browser
  sign-in flow is refused by the permission classifier, correctly. A session on the box can diagnose
  and read a URL, but cannot complete a login.
- **Linda2 had no remote-access software, which turned a sixty-second fix into an evening.**
  RustDesk was installed remotely that night, non-elevated — running only while its process lived,
  not surviving a reboot, unable to interact with UAC prompts. Resolved 2026-10-01 by installing it
  as a service (see "Linda2's two remote doors").
- **The permission grant needed to do any of this cannot be written by the agent that needs it** —
  the harness blocks an agent editing its own `permissions.allow`, and that guard is correct. The
  route that worked was editing `settings.json` in the `TheSkinz/claude-config` repo from the phone's
  browser and pulling it on Linda2, since `~/.claude` is the live clone.

## Desktop down: cloud session

Claude app > Code tab > new session against `TheSkinz/obsidian-work`. Runs on Anthropic
infrastructure, so it works with the machine off. Two limits:

The vault `CLAUDE.md` and `.claude/settings.json` are committed, so vault structure and conventions
load — but `~/.claude/skills/` and the global CLAUDE.md do not exist there. Vault navigation is
reliable; USADebusk domain answers are not. Treat every number as unverified until checked at the
desk.

The transcript lives on Anthropic infrastructure. Anything worth keeping has to be written into a
file during the session, not just discussed — true of every surface since the harvest stopped.

On return: merge the branch it pushed, then `git pull` on the desktop before the next session
touches the vault.

## Links

- [[code]] — Claude Code surface reference and the post-cutoff capture rule
- [[cowork]] — what Cowork is, and how Dispatch sources skills
- [[obsidian-setup]] — vault path, git-as-sync
- [[system-workflow-reference]] — current status of all six loops, and the on-demand ingest flow
- [[m365-access-boundary]] — what a session on any surface can and cannot reach
