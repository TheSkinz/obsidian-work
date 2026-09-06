---
title: Grok Bot — Setup Runbook
created: 2026-09-06
tags: [grok, xai, grok-bot, automation, trial]
---

# Grok Bot — Setup Runbook

One-month trial started 2026-09-06. Design rationale and the four-week plan live in
`~/.claude/plans/i-am-experimenting-with-fuzzy-plum.md`. This file is the doing part.

Product mechanics read from docs.x.ai/grok-bot on 2026-09-06, then **verified in the running app
the same day** by driving it directly. Where the app and the docs (or the third-party connector
directories) disagree, what is written here is what the app showed.

## What the app actually showed, 2026-09-06

**The cloud computer is real and already provisioned.** Opening a Bot's screen gives a Linux
desktop with a dock — Chrome, an editor, and a terminal. The terminal opens at `/workspace` with
the prompt `box@cursor:/workspace$`; the hostname is literally `cursor`, which corroborates the
reports that this runs on Cursor infrastructure.

**git is installed: version 2.47.3.** That was an inference in the first draft of this file and it
is now a read fact. The clone was run and succeeded — 6319 objects, 16.21 MiB, no credentials
prompted, and `ls vault` returns the full vault including the same-day commit. **Step 0 is done.**

**Typing into the Bot's screen from outside is unreliable.** Anything longer than about a dozen
characters routes through the local clipboard, which does not cross into the VM — it arrives as
`^M` and nothing else. Short strings type fine. Type long commands in chunks, or type them inside
the VM rather than through a remote-control layer.

**Three connector facts that change the design.** There is **no SharePoint connector at all** —
searching the marketplace for it returns "No plugins match". **OneDrive exists but is read-only**:
its description is "Browse, search, and read Microsoft On...". **Outlook and Outlook Calendar both
exist**, and **GitHub exists with write** ("Manage repos, issues, pull requests"). The public
connector directory that listed SharePoint and OneDrive under Business & Enterprise is not what
this account sees.

**Routine triggers are richer than the docs implied.** The full list: On a schedule, Slack message,
**Git event**, Teams message, Linear issue, Sentry alert, PagerDuty incident, **Webhook**. The
schedule submenu offers Every hour, Every day, Weekdays, Every week, Every month, Interval, and
Advanced. Weekdays is native, so the business-hours advice needs no cron. The routine editor
carries Name, Instruction, When to run, Run history, an Active toggle, Test run and Delete.

**Usage is visible without hunting for it.** The account menu bottom-left reads `SuperGrok — 1%`,
and opening it shows "Resets in 7 days" plus a **Change limit** control for capping spend. That
answers the renewal question directly — watch that percentage, and set the limit before attaching
routines.

**Also present:** a "Teach a task" recorder in the Bot-screen toolbar (the demonstration capture),
a Marketplace with separate **Plugins** and **Bots** tabs, and a `+` menu offering Create new Bot,
Create group chat, or an existing Bot. One Bot already exists on the account — "Chief of Staff",
with Gmail and Google Drive added and Gmail still awaiting a sign-in.

## Files here

| File | Goes where |
|---|---|
| [[README-FOR-BOTS]] | Copy to `/workspace/README-FOR-BOTS.md` on the Grok Bot computer |
| [[bot-profiles]] | Paste each Description into Bot actions > Edit Profile |
| [[receipt-extraction]] | Save as the Receipt Extraction skill |
| [[invoice-readiness-check]] | Save as the Invoice Readiness Check skill |
| [[job-report]] | Save as the Project Report skill |

The four estimating skills — RFQ Intake, Duration Model, Work-Up Billing Math, Proposal Assembly —
are week 2 and are not written yet on purpose. Do not port a pricing skill before the citation
loop has been proven, because a Bot that miscites a rate is worse than no Bot.

## Day 1 — substrate

Sequence: `~~verify terminal~~ > ~~clone vault~~ > write README > create Librarian > citation audit`

1. ~~Check git exists.~~ **Done** — git 2.47.3.
2. ~~Clone the vault.~~ **Done** — `/workspace/vault` is populated.

```bash
git clone https://github.com/TheSkinz/obsidian-work.git /workspace/vault
```

3. Still to do: create the project folders `/workspace/bids`, `/workspace/jobs`, `/workspace/out`,
   `/workspace/scratch`.
4. Still to do: copy `README-FOR-BOTS.md` to `/workspace/README-FOR-BOTS.md`.
5. Still to do: create **Librarian** and nothing else. Paste its Description from [[bot-profiles]].

## Day 2 — citation audit, and the go/no-go

Ask Librarian ten domain questions you already know the answers to, then open each cited file and
check the line actually says what it claimed. Suggested questions, chosen because each has a
recorded correction or a known trap behind it:

1. What is the Clean ID field on a service receipt, and is it a sizing input or a cleaning result?
2. What are the primary estimating drivers for rig-in, and how many are there?
3. What does "demob" mean for a job date — facility demob or equipment back at Deer Park?
4. Which loops currently run in the vault, and which were stopped?
5. What is the max pig OD sizing rule relative to Clean ID?
6. What does the vault say about labor rates being per person versus per role?
7. Which document holds quoted-versus-actual reconciliation — job sheet, heater card, or job report?
8. What is the tube count on B-102?
9. Where does the SOP formatting standard live?
10. What does the vault say about the rig-diagram layout engine?

**Go/no-go:** if Librarian invents a citation, or cites a real file that does not say what it
claimed, stop the build. Everything downstream inherits that failure, and finding it on day 2
costs two days instead of three weeks.

## Week 1 — the mechanical bots

Add **Ledger** and **Scribe**. Save the three skills in `skills/`. Run each one by hand against a
real closed job. No routines yet.

The ladder is `run by hand > correct > save as skill > test the skill > attach a routine`, and
skipping a rung is how the weekly token allowance disappears.

## Week 2 — the bid desk

Add **Intake** and **Estimator**, write the four estimating skills, create the "Bid Desk" group
with Intake, Estimator and Scribe. Attach the first two routines once their skills have run clean
by hand.

## Week 3 — the browser experiment, now narrower

Add **Scout**. Its bid-folder reconcile job was designed around a SharePoint connector that does
not exist, and OneDrive's connector is read-only, so the original job cannot be built the way it
was written. Two honest options remain: drive the SharePoint web UI through the Bot's Chrome,
which is the fragile path the power-user consensus warns against and which is also where the
datacenter-IP sign-in blocks bite; or drop the reconcile and give Scout only the portal watch.

Take the browser path anyway for one week. Watching it fail is the point — this is the capability
Claude Code structurally cannot provide, and whether the browser route is usable is the single
question that decides if the product is worth anything beyond the trial. Just do not build the
month around it.

**Better use of the Git event trigger, found in the app:** point Librarian's vault refresh at a
Git event on `obsidian-work` rather than a daily schedule. It then fires when the vault actually
changes instead of every morning regardless — defect-triggered rather than clock-triggered, which
is the same principle the vault's own loop audit landed on. Same for a Webhook trigger if anything
else should wake a Bot.

## Week 4 — back-test and verdict

Judge it against artifacts that already have known-good answers, two structurally different ones
per bot. Estimator against a closed bid, line by line. Scribe against a delivered project report.
Ledger against a completed ticket breakdown. Librarian against the citation audit again.

Record three things, because they decide renewal: how fast the weekly allowance drains and what
drains it; how often a sign-in is blocked by the datacenter IP and needs manual takeover; whether
routines actually fire on schedule.

## Standing constraints

**One computer, one credential store.** All Bots share the cloud machine, its filesystem, its
browser cookies and its terminal credentials. The docs state it outright: do not use separate Bots
as a security boundary. Anything one Bot signs into, every Bot has.

**That collides with the account-separation rule** in global CLAUDE.md, which keeps xAI accounts
on personal credentials and away from USADebusk systems. The trial default is therefore
**read-only week one** — no Outlook, no SharePoint connector, files uploaded by hand. If the M365
side turns out to be the point, use a dedicated service account, not the primary work account.

**Only /workspace persists.** Temp directories and uncommitted state can vanish. Every finished
artifact gets copied out.

**Limits worth knowing:** 50 Bots and group chats per account; 50 routines per Bot; only the 20
most recent runs retained per routine, so anything needing an audit trail writes its own log to
/workspace; deleting a routine is permanent; no model selection or version pinning; Legacy Privacy
Mode is unsupported and cloud storage is mandatory.

**Business content is not restricted** — pricing, rates, methodology, heater and job data,
customer and facility names all go anywhere. Credentials, secrets, API keys and tokens do not go
on this machine at all.
