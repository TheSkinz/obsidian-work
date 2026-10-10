---
title: Grok Bot — Setup Runbook
created: 2026-09-06
tags: [grok, xai, grok-bot, cursor, automation]
---

# Grok Bot — Setup Runbook

Open-ended personal test started 2026-09-06 — not an official trial and no end date (corrected 2026-10-03; earlier called a one-month trial).

Product mechanics were read from docs.x.ai/grok-bot, then **verified in the running app** by driving
it directly. Where the app and the docs — or the third-party connector directories — disagree, what
is written here is what the app showed. Two published facts turned out to be wrong: a directory
listing a SharePoint connector that does not exist, and a claim that an external agent can trigger
Grok Bot through MCP.

⚠ **Grok Bot is xAI's product running on Cursor's infrastructure.** Both halves matter and the
evidence for each is below: the docs live at `docs.x.ai/grok-bot`, while the Bot's own sandbox
terminal opens at `box@cursor:/workspace$` and the webhook trigger hands out an
`api2.cursor.sh/...` endpoint. **So a `cursor.sh` hostname anywhere in this system is expected, not
a mismatch** — an `x.ai` host would be the surprise. Stated here because it was previously only
derivable from two findings 200 lines apart, and meeting `api2.cursor.sh` cold in an environment
variable reads exactly like a misconfiguration. It is not one.

**Three parts.** *Navigation* is how to drive the app. *Current state* is what exists right now. *Driving from Claude Code* is the working checklist. The dated evidence from the 2026-09-06 to 2026-10-10 build-out moved to [[trial-findings]] on 2026-10-10.

---

# 1. Navigation

## Creating a Bot

`+` → type the name → `Create "<name>" Bot`.

⚠ **Click `+` and wait for the dropdown before typing.** Typing too early puts the name in the
**message box** of whatever chat is open instead of the To-field. This cost two attempts.

Every new Bot then runs a short onboarding interview — *"What should I be most useful for?"* with
four options and a free-text box. **Answer in the free text and point it at its own Description**,
which is where the real instructions live.

## Editing a profile

Click the Bot's name in the title bar. The Settings panel has **Name**, **Label (optional)**,
**Description** and a Notifications toggle. The Description accepts a full multi-paragraph block
with no length trouble — paste the whole thing from [[bot-profiles]].

⚠ **The panel commits on blur, not as you type.** Nothing in the UI says so. A routine or profile
can sit visibly configured and not actually be saved, which silently invalidated an entire trigger
test on 2026-09-06 — the routine saved two minutes *after* its stimulus fired. Click away from the
last field and confirm the change registered before relying on it.

## Adding a skill

Skills go in as **file uploads, not pasted text**: message box `+` → **Attach files** → the Windows
Open dialog. It accepts a full path typed directly, and **several quoted paths at once**, so a Bot's
whole skill set can go in one upload.

Skills are stored **byte-for-byte** — see the finding below. Write them for this platform exactly as
they are written for Claude Code.

The same `+` menu carries **Teach a task**, the demonstration recorder.

## Setting a routine

The Bot-screen icon in the title bar opens a right-hand panel with the Bot's live screen above and
**Routines** below. `+` beside Routines, or **Create Routine**, opens the editor: **Name**,
**Instruction**, **When to run**, **Run history**, an **Active** toggle, **Test run** and **Delete**.

⚠ **Test run greys out only while a routine is unsaved.** It is *not* disabled for event triggers —
an earlier note in this file said so and was wrong. Save first, then Test run is live.

**Trigger types:** On a schedule, Slack message, **Git event**, Teams message, Linear issue, Sentry
alert, PagerDuty incident, **Webhook**. The schedule submenu offers Every hour, Every day,
**Weekdays**, Every week, Every month, Interval and Advanced — Weekdays is native, so business-hours
scoping needs no cron.

⚠ **"Git event" is pull-request shaped and has no push event.** Do not design around it. See the
finding below.

⚠ **There is no way to delete a single trigger**, only the whole routine. An unwanted trigger can be
left inert alongside a working one.

Follow the ladder: `run by hand → correct → save as skill → test the skill → attach a routine`.
Skipping a rung is how the weekly allowance disappears.

## Waking a Bot from Linda2

`tools/notify_grok_bot.py --target inbox` POSTs to the *Claude inbox* routine's webhook. The task
format and the order of steps are in `handoff/README.md`. The URL and key live in the user
environment variables `GROK_INBOX_WEBHOOK_URL` and `GROK_INBOX_WEBHOOK_KEY` and never touch a file.
The outcome is the one line in `.grok-inbox-last` at the vault root.

**Retired 2026-10-10: the pre-push hook and *Vault refresh*.** Every push used to fire Librarian
to pull `/workspace/vault`, which spent a Bot run per push. The Bots now pull in `bootstrap.sh` when
they start work, so the hook (`.git/hooks/pre-push`) was deleted and the script's default `vault`
target has nothing left to call it. The old variables `GROK_BOT_WEBHOOK_URL` and
`GROK_BOT_WEBHOOK_KEY` are inert once the routine is deleted.

Lessons from the hook that still apply to the inbox webhook:

⚠ **The webhook blocks until the run is queued and slows as runs pile up** (1.0 s, then 21.7 s, then
53.3 s, measured back to back on 2026-09-07). The script therefore POSTs from a detached child and
never waits.

⚠ **Click *into* each field and Ctrl+A before copying the URL or key.** The display truncates with
an ellipsis, and copying what you can see yields a partial key and `Invalid API key`.

⚠ **`setx` only reaches shells opened afterwards**, so Claude Code must be restarted after setting a
variable.

⚠ **PowerShell aliases `curl` to `Invoke-WebRequest`, which rejects `-H`.** Use `curl.exe`, or
`Invoke-RestMethod` with the URL and key in variables.

## Where things are

**Usage meter:** account menu, bottom-left. Reads `SuperGrok — N%` with "Resets in 7 days" and a
**Change limit** control for capping on-demand spend. On-demand is set to **None**, so there is no
overage exposure.

**Marketplace:** bottom-left, with separate **Plugins** and **Bots** tabs.

**A Bot's screen:** the title-bar icon. It is a real Linux desktop — Chrome, an editor, and a
terminal that opens at `/workspace` with the prompt `box@cursor:/workspace$`. The hostname is
literally `cursor`, corroborating that this runs on Cursor infrastructure.

⚠ **Typing into the Bot's screen from outside is unreliable.** Anything longer than about a dozen
characters routes through the local clipboard, which does not cross into the VM — it arrives as `^M`
and nothing else. Type long commands in chunks, or type them inside the VM.

⚠ **A Bot's verbatim print-back truncates** mid-sentence. To compare a stored skill against its
source, **diff the files on disk** rather than trusting a dump.

---
---

# 2. Current state — 2026-10-10

**Kept indefinitely (Jesse, 2026-10-10).** Claude Code on Linda2 is the primary work path. Grok Bot
covers what Linda2 cannot: field paperwork from the phone, Jesse's personal accounts, the company
Microsoft lane, and travel. It is also the continuity path if Linda2 is down.

**Roster: 15 Bots, as Chief of Staff listed them on 2026-10-10.** Read the app before trusting this,
because the table it replaces went stale within two weeks.

| Bot | Lane |
|---|---|
| **Chief of Staff** | Front door and router; runs the Claude inbox routine |
| **Architect** | The Grok Bot platform itself; owns the Workspace backup routine |
| **Librarian** | Vault and knowledge organization |
| **Ledger** | Handwritten service receipts into tables (extract only) |
| **Forms** | Fills blank DeBusk daily service receipts |
| **Clerk** | Clean copies of handwritten receipts |
| **Fuel** | Company fuel forms from fuel receipts |
| **Empower** | ISNetworld and safety-training portals |
| **Docs** | Company Microsoft lane, plus personal Outlook hygiene |
| **Travel** | Flights, hotels, rental cars, check-in |
| **Purse** | Jesse's personal finances only; never USADebusk |
| **Intake**, **Estimator**, **Scribe**, **Studio** | The Bid Desk: RFQ intake, duration and work-up, proposal and report `.docx`, decks. **No real bid has gone through them.** Their future depends on the test below |

**Routines.** *Workspace backup* (Architect, weekdays 18:00 CDT) is read by the `health.md` row.
*Claude inbox* (Chief of Staff, webhook) is the handoff channel; see `handoff/README.md`. **The
Bots pull the vault at work time**: `bootstrap.sh` runs `git pull --ff-only` first, verified by
Architect 2026-10-10 (HEAD matched origin). That replaced *Vault refresh* (Librarian), whose pre-push
hook was removed from Linda2 the same day. Jesse deletes *Vault refresh* and the test leftover
*Webhook ping* in the app; until he does they are idle, since nothing fires them.

**Open, 2026-10-10.** The Bot computer now has a Claude Code CLI 2.1.289 (Jesse installed it). The
test of whether it can run the real `usadebusk-*` skills from `claude-config` against the
[[BACKTEST-SPECIMEN]] fixture is **blocked**. `claude-config` is private, and the box's git login
reaches only the public vault. It needs read access to that repo (reconnect the GitHub connector),
then the handoff is re-sent. If it passes, the Bid Desk Bots and their Grok-format skill mirrors in
`skills/` are candidates to retire, which needs a separate ruling.

## Files here

| File | Goes where |
|---|---|
| [[README-FOR-BOTS]] | **No copy needed** — every Bot Description points at it inside the clone, so `git pull` keeps their orientation current |
| [[bot-profiles]] | Paste each Description into Bot actions > Edit Profile |
| [[architect-profile]] | The Architect — platform research, plus its experiment queue |
| [[receipt-extraction]] | Receipt Extraction skill — Ledger |
| [[invoice-readiness-check]] | Invoice Readiness Check skill — Ledger |
| [[job-report]] | Project Report skill — Scribe |
| [[rfq-intake]] | RFQ Intake skill — Intake |
| [[duration-model]] | Duration Model skill — Estimator |
| [[workup-billing-math]] | Work-Up Billing Math skill — Estimator |
| [[proposal-assembly]] | Proposal Assembly skill — Scribe |
| [[brand-standards]] | Brand Standards skill — Scribe (added 2026-09-07; Project Report and Proposal Assembly both depend on it) |
| [[receipt-clean-copy]] | Receipt Clean Copy skill — Clerk (Bot-written, mirrored 2026-10-04) |
| [[receipt-typesetting]] | Receipt Typesetting skill — Forms (Bot-written, mirrored 2026-10-04) |
| [[fuel-form]] | Fuel Form skill — Fuel (Bot-written, mirrored 2026-10-04) |
| [[service-gmail]] | Gmail service skill — shared signed-in session, mainly Docs (Bot-written, mirrored 2026-10-04) |
| [[service-outlook]] | Outlook service skill — shared signed-in session, mainly Docs (Bot-written, mirrored 2026-10-04) |
| [[service-isnetworld]] | ISNetworld service skill — Empower (Bot-written, mirrored 2026-10-04) |
| [[safety-lms-training]] | Safety LMS Training skill — Empower (Bot-written, mirrored 2026-10-04) |

**Read [[BACKTEST-SPECIMEN]] before uploading the four estimating skills.** It works all four against
DSP26085 — six rules reproduce the real quote to the hour and to the line, and one rule was
falsified. **None of the four carries a rate number**; rates belong to a contract and stay in the
vault behind their own warnings.

**Substrate.** `/workspace/vault` is a clone of the public `obsidian-work` repo — 6319 objects,
16.21 MiB, **no credentials prompted**. git on the VM is version 2.47.3.

```bash
git clone https://github.com/TheSkinz/obsidian-work.git /workspace/vault
```

**Substrate.** `/workspace/vault` is a clone of the public `obsidian-work` repo, pulled on its own
saved git login. `/workspace` is a working area, not storage: finished files go to chat or OneDrive
the same day.

---

# 3. Driving Grok Bot from Claude Code — read this first. 2026-10-04.

Consolidated from the dated findings below; each line was learned the hard way on 2026-10-04.

- **Read before you click.** `python tools/grok_sync_check.py` reads the Bots' OneDrive backup
  (`C:\Users\Jwuts\OneDrive\GrokBot-Backup\`): backup age, vault↔live skill drift in both
  directions, job values left in skills, and open items. Open the app only to message a Bot.
- **The sidebar re-sorts by most recent activity.** Read the chat header before typing; a
  position-based click sent one message to the wrong Bot.
- **No Edit Profile in this build.** A Bot replaces its own description: name the section of
  `bot-profiles.md` and say "verbatim".
- **Settings > Updates** holds the computer update control and **Reset**. Never use Reset, because it
  rebuilds from a snapshot and can lose recent work.
- **Attaching a file:** copy it to `Downloads`, then click + > Attach files and type the full path.
- **A group chat is not a reset.** The history follows the Bot into every room, and the app has no
  Duplicate option.
- **Routine creation from Claude Code is blocked** as unauthorized persistence. Jesse creates routines.
- **Hand Bots paths, not content.** Bot-to-Bot messages are cut at 8000 characters.
- **The backup is additive.** Files a Bot deletes stay in OneDrive (for example the old
  `vac-receipt-field-map.json`), so a sync-check hit there may be a ghost, not a live file.

The dated evidence behind every line here is in [[trial-findings]].


# Standing constraints

**One computer, one credential store.** All Bots share the cloud machine, its filesystem, its browser
cookies and its terminal credentials. The docs state it outright: **do not use separate Bots as a
security boundary.** Anything one Bot signs into, every Bot has.

**Credentials are in use as of 2026-10-04 — Jesse's ruling.** *"I'll be using credentials and will
perform a few small debusk tasks."* This replaces the credential-free posture the trial ran under from
2026-09-06 (no Outlook, no SharePoint, no Gmail, files uploaded by hand; the one GitHub PAT was
reversed the same evening). Jesse does the sign-ins, through the app's secure forms so no Bot sees a
value. The shared-store fact above still holds, so **every signed-in session is available to every
Bot**. **Bot instructions were relaxed the same day at Jesse's request**, with this clarification: *"I
still want to run an optimal / efficient work flow with all bots. I just want Grok bot to be able to
work without being overly cautious."* The **caution** came out: Bots act and report, set up their own
skills, routines and Bots, and check in only before something goes to a customer under his name. The
**workflow** stayed in: routing to the owner, the write/sign-off split, skill before routine, and
usage discipline.

**Only `/workspace` persists.** Temp directories and uncommitted state can vanish. Every finished
artifact gets copied out.

**Limits worth knowing:** 50 Bots and group chats per account; 50 routines per Bot; only the **20
most recent runs** retained per routine, so anything needing an audit trail writes its own log to
`/workspace`; **deleting a routine is permanent**; **one continuous thread per Bot**, auto-summarized
as it grows, with no new-chat control (Bot-reported 2026-10-04, consistent with the live read the
same day). **The whole transcript is resent every turn, so a long thread is a cost problem.** Reset
without deleting, per [[research-2026-10-power-user]]: ask for a handoff summary, right-click >
Duplicate, paste the summary into the copy and hide the original. Learned memory does not carry over.
Or start a new group with the same Bot. `/workspace` files are the only reliable task memory; no model selection or version pinning; Legacy
Privacy Mode is unsupported and cloud storage is mandatory.

**Business content is not restricted** — pricing, rates, methodology, heater and job data, customer
and facility names all go anywhere. **Sign-ins go through the secure forms only.** Passwords, API keys
and tokens are never pasted into chat, a skill, or a file under `/workspace`.
