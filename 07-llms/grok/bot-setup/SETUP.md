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
| [[architect-profile]] | The Architect — platform research, plus its experiment queue |
| [[receipt-extraction]] | Save as the Receipt Extraction skill |
| [[invoice-readiness-check]] | Save as the Invoice Readiness Check skill |
| [[job-report]] | Save as the Project Report skill |

The four estimating skills — RFQ Intake, Duration Model, Work-Up Billing Math, Proposal Assembly —
were written 2026-09-06, after the citation audit passed:

| File | Goes where |
|---|---|
| [[rfq-intake]] | Save as the RFQ Intake skill — Intake |
| [[duration-model]] | Save as the Duration Model skill — Estimator |
| [[workup-billing-math]] | Save as the Work-Up Billing Math skill — Estimator |
| [[proposal-assembly]] | Save as the Proposal Assembly skill — Scribe |

**Read [[BACKTEST-SPECIMEN]] before uploading any of them.** It works all four against DSP26085 —
six rules reproduce the real quote to the hour and to the line, and one rule was falsified. **None
of these four carries a rate number**; rates belong to a contract and stay in the vault behind their
own warnings.

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

## Build log

**2026-09-06 — Librarian, Ledger and Scribe are live.** Built by driving the app directly.

Bots are created from the `+` menu → type the name → `Create "<name>" Bot`, then the Bot title bar
opens a Settings panel with **Name**, **Label (optional)**, **Description** and a Notifications
toggle. The Description accepts the full multi-paragraph block with no length trouble. Every new
Bot then runs a short onboarding interview ("What should I be most useful for?") with four options
and a free-text box — answer in the free text, pointing it at its own Description.

Skills go in as **file uploads**, not retyped: message box `+` → **Attach files** → the Windows
Open dialog accepts a full path, and several quoted paths at once. `Receipt Extraction` and
`Invoice Readiness Check` went to Ledger in one upload; `Project Report` to Scribe. All three
saved verbatim. Scribe repeated the hand-tally deviation back unprompted: *"every table figure
marked hand-tallied and arithmetic shown because there is no generator script here."*

**The `+` menu also carries "Teach a task"** — the demonstration recorder — alongside Attach files.

### The Architect, and experiment 2 — skills DO survive verbatim

Built 2026-09-06. First experiment run the same session: *does an uploaded skill survive verbatim,
or does Grok Bot paraphrase it on ingest?* This mattered because every ported skill is written as
"do X, and specifically do NOT do Y" — a summariser drops the Y half first, which would strip the
guardrails while leaving the skill looking correct.

**Answer, TESTED:** the stored skill and the vault source **match byte-for-byte in the body**. The
platform adds a YAML frontmatter wrapper of its own, so the *file* is not identical while the
*content* is. Nothing was paraphrased, compressed, or dropped. **The counter-cases in the ported
skills are safe**, and skills can be written for this platform the same way they are written for
Claude Code.

Two things fell out of the run that were not the question:

- **Inter-Bot DM works and is visible.** The Architect messaged Scribe directly and the thread showed
  `Messaged Scribe` / `Message from Scribe` inline. That is the push channel — a Bot cannot silently
  read another's thread, but it can ask, and the asking is legible to the human watching.
- **A Bot's verbatim print-back truncates.** Scribe's dump of its own skill cut mid-sentence, so
  print-back is not a reliable comparison method. **Diff the files on disk instead** — the skill is
  stored as a real file on the shared computer, which is what made the byte comparison possible at
  all.

**Cost:** the meter read 1% before the three working Bots were built and **2%** after all of that
plus this experiment. So the entire build to date — four Bots, three skill uploads, a ten-question
citation audit and one platform experiment — is roughly 1–2% of a weekly allowance. Cost is not the
binding constraint at this scale.

### Experiment 1 — the Git-event trigger. There is no push event.

**READ, from the trigger config UI, 2026-09-06.** The routine trigger labelled "Git event" is
**pull-request shaped, not push shaped.** Its complete event list:

| Group | Events |
|---|---|
| Pull request | Opened · Updated · Merged |
| Review | Requested · Approved · Changes requested · Commented · Thread resolved · Thread reopened |
| Comment | PR comment · Inline review comment |
| Checks | CI passed · CI failed |
| Issue | Assigned |

**Nothing fires on a push.** The designed routine — Librarian pulls the clone when `obsidian-work`
changes — **cannot be built as specified**, because vault work commits straight to `main` and never
opens a PR. That is the single most load-bearing assumption in the routine design and it is false.

**What it costs to find out.** The trigger needs the **GitHub connector**, and the connector wants a
**personal access token**, not OAuth — *"Fine-grained or classic PAT from
https://github.com/settings/tokens with the repo scopes you want the agent to use."* That is better
than the account-wide grant the connector's own description implies, because the token sets the real
ceiling: a fine-grained PAT scoped to one repository keeps everything else out of reach even on a
shared VM. Jesse minted one for `obsidian-work` plus a Grok repo and installed the connector
2026-09-06, deliberately departing from the no-credentials posture for this one answer.

**Also READ: an event-triggered routine cannot be Test run.** The button greys out once a Git event
is the trigger; it is available for scheduled routines only. So the ladder's "test before you arm"
step is not available on exactly the routines where firing is least predictable.

**The salvage test.** PR-opened still answers the question underneath the question — *do event
triggers fire at all?* — which also bears on the Webhook trigger, the only other event path. A
routine named `Vault refresh` is set on Librarian with Opened and Merged on
`TheSkinz/obsidian-work`, and this file's own change is the stimulus: it lands as a pull request
rather than a direct push, and the PR opening is the event.

**Correction to the line above: Test run is NOT disabled for event-triggered routines.** It greys
out only while a routine is *unsaved*. Once saved it is live, and a Test run on `Vault refresh`
fired and completed — so the routine mechanism and the instruction both work. That is a different
claim from the trigger firing on its own.

**The first attempt proved nothing, and the fault was mine.** The PR opened at 19:01 and the routine
saved at 19:03 — Librarian's own thread records `Created routine · Vault refresh` two minutes after
the stimulus. The event fired before the routine existed. **The panel does not save as you type; it
commits when a field blurs**, which is worth knowing because nothing in the UI says so and a routine
can sit visibly configured and not yet be armed.

**Attempt 2 — armed first, and it did not fire. TESTED.**

Routine saved and Active at 19:03. PR #5 opened at **19:05:22**. Run history at **19:09** still
showed only the manual Test run. **No trigger fire within roughly four minutes** of a correctly
armed PR-opened trigger on the named repo.

**The diagnosis is concrete rather than a shrug.** `gh api repos/TheSkinz/obsidian-work/hooks`
returns **nothing — no webhook is registered on the repository at all.** Grok Bot never installed a
hook, so it had no channel through which to learn the PR existed. That is a much more useful result
than "it did not work": the trigger is not slow, it is not wired.

**Three candidate causes, none yet distinguished (INFERRED):** the fine-grained PAT may not carry
**Webhooks: Read and write**, which is the scope a hook registration needs and which was flagged as
an inference when the token was minted; or the connector registers hooks lazily on some event this
test did not produce; or Grok Bot polls GitHub on an interval rather than receiving webhooks, in
which case four minutes was simply too short. **The token scope is the cheapest to check first.**

### What this means for the design

**Routines here are schedule-triggered until proven otherwise.** The defect-triggered premise —
Librarian refreshing when the vault actually changes — has now failed twice over: there is no push
event to bind to, and the PR event that does exist did not fire. Against the vault's own 2026-08-21
measurement, that puts Grok Bot routines in the ~53%-effect schedule-triggered class rather than the
90–100% defect-triggered class, and **that is a materially weaker case for using routines here at
all.**

Two things are still open and worth one attempt each, not an evening: confirm the PAT's Webhooks
scope, and test the **Webhook trigger** directly, which needs no GitHub connector and would let
Claude Code fire a routine with a `curl` — the bridge the video wrongly attributed to an MCP server.

**What did work, and it is not nothing:** the routine itself runs. A saved routine executes its
instruction correctly on demand via Test run. The mechanism is sound; only the GitHub trigger is
unproven.

### The Webhook trigger DOES fire. TESTED, 2026-09-06.

A second routine, `Webhook ping`, armed on the **Webhook** trigger and fired from a terminal on
Jesse's machine. Librarian replied **`WEBHOOK FIRED 2026-09-07 03:22:04 UTC`** — exactly the
instructed output, nothing else, and immediately.

**This reverses the pessimistic reading above.** Event-triggered routines are real on this platform.
They just do not work through GitHub.

**What the Webhook trigger gives you.** Selecting it exposes three fields: a **POST to** endpoint on
`api2.cursor.sh/automations/webhooks/...` (more Cursor infrastructure), a **key**, and a ready-made
**header** line. Any process that can make an HTTPS POST can fire the routine — so **Claude Code can
trigger a Grok Bot routine programmatically.** That is the bridge the video wrongly attributed to an
MCP server, and it exists, just not where that claim put it.

**Design consequence — the webhook path is strictly better than the GitHub one:**

- It needs **no GitHub connector and no personal access token at all**, so it removes a third-party
  credential rather than adding one. **The PAT minted for the Git-event test can be revoked** with no
  loss of capability.
- It replaces the missing push event. A local git hook, or a line in a commit sequence, can `curl`
  the webhook on every push to `obsidian-work` — giving Librarian the defect-triggered refresh the
  design wanted, with the trigger owned locally rather than by a connector.
- It generalises. Any defect the vault's own tooling can detect — a lint error, a failed rollup, a
  RULE-FORK fire — can fire a routine, which is a far better fit for this system than a clock.

**The key is a credential.** It authorises firing that routine, so it belongs nowhere in a repo, a
transcript or a shell history. Regenerate it if it is ever exposed, and if a git hook is built later,
read it from an environment variable rather than writing it into the hook.

**Operational note, learned the hard way.** PowerShell aliases `curl` to `Invoke-WebRequest`, which
does not accept `-H`. Use `curl.exe`, or assign the URL and key to variables first and call
`Invoke-RestMethod` — building the header in PowerShell rather than parsing it in a shell removes
the quoting failures entirely.

### The citation audit — PASSED, 10 of 10

Every answer carried a real file path and a verbatim quote. Spot-checked independently against the
working copy; three quotes were confirmed character-for-character (`17-glossary.md:25`,
`quote-lifecycle.md:81`, `B-102.md:73`). No invented citations, no citation that failed to support
its claim.

Two answers are worth recording because they show judgment rather than retrieval:

- **Q7 (quoted-vs-actual)** — answered "job report", then flagged that `USA26041-job-sheet.md` also
  carries a closed Ticket-breakdown reconciliation section which *"sits against that model"*, and
  put it under Unresolved questions rather than resolving it. That is the "contradictions are
  findings, not noise for you to resolve" instruction working.
- **Q6 (labor rates)** — separated labor billing (hourly, not a 12-hr day rate, changed 2026-07-12)
  from per diem (one allowance per person per shift, generic base $150, role-split where the
  contract requires it), and disclosed in Assumptions that it read both because the question's
  framing and the actual recorded change were about different things.

**Cost:** the meter read `SuperGrok — 1%` before the audit and `1%` after. A ten-question deep vault
search is under one percent of the weekly allowance. On-demand spend is set to **None**, so there is
no overage exposure.

**Elapsed:** roughly four minutes for the ten questions, with running progress messages the whole
time. Not fast, but it was genuinely grepping rather than answering from context.

---

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
