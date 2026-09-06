---
title: Grok Bot — Setup Runbook
created: 2026-09-06
tags: [grok, xai, grok-bot, automation, trial]
---

# Grok Bot — Setup Runbook

One-month trial started 2026-09-06. Design rationale and the four-week plan live in
`~/.claude/plans/i-am-experimenting-with-fuzzy-plum.md`. This file is the doing part.

Product mechanics read from docs.x.ai/grok-bot on 2026-09-06. Anything marked *inference* was not
stated in the docs and needs checking on day 1.

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

Sequence: `verify terminal > clone vault > write README > create Librarian > citation audit`

1. In a Bot terminal, check git exists (*inference: the docs describe a terminal but do not say git
   is installed*). If it is missing, `apt-get install git`, or fall back to the GitHub connector.

```bash
git clone https://github.com/TheSkinz/obsidian-work.git /workspace/vault
```

2. Create the project folders: `/workspace/bids`, `/workspace/jobs`, `/workspace/out`,
   `/workspace/scratch`.
3. Copy `README-FOR-BOTS.md` to `/workspace/README-FOR-BOTS.md`.
4. Create **Librarian** and nothing else. Paste its Description from `bot-profiles.md`.

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

## Week 3 — the browser experiment

Add **Scout** and the reconcile routine. This is the only capability Claude Code structurally
cannot provide, so it decides whether the product is worth anything beyond the trial.

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
