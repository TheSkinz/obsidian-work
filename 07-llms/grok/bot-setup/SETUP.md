---
title: Grok Bot — Setup Runbook
created: 2026-09-06
tags: [grok, xai, grok-bot, automation, trial]
---

# Grok Bot — Setup Runbook

One-month trial started 2026-09-06.

Product mechanics were read from docs.x.ai/grok-bot, then **verified in the running app** by driving
it directly. Where the app and the docs — or the third-party connector directories — disagree, what
is written here is what the app showed. Two published facts turned out to be wrong: a directory
listing a SharePoint connector that does not exist, and a claim that an external agent can trigger
Grok Bot through MCP.

**Four parts.** *Navigation* is how to drive the app. *Current state* is what exists right now.
*Findings* is the dated evidence. *What's left* is the surviving plan.

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

## Wiring the push hook

This is the working defect-trigger, and the most operationally useful thing in the file.

`tools/notify_grok_bot.py` fires a Grok Bot webhook from a `pre-push` hook, so Librarian pulls the
clone every time the vault is pushed and `/workspace/vault` stops going stale between sessions.

**`pre-push`, not `post-commit`,** because Librarian pulls from the *remote* — the notification must
tie to the push. Git has no `post-push` hook. If a push fails after the hook fires, Librarian pulls,
finds nothing new, and says so.

**The shim** at `.git/hooks/pre-push` is untracked by nature, so the logic lives in `tools/` where it
is versioned. Recreate it after any re-clone:

```bash
printf '#!/bin/sh\nexec python "$(git rev-parse --show-toplevel)/tools/notify_grok_bot.py"\n' > .git/hooks/pre-push && chmod +x .git/hooks/pre-push
```

**Two environment variables, and the key never touches a file.** Read them off the routine's webhook
trigger — click **When a webhook fires** to expand, then copy **POST to** and **key**:

```bash
setx GROK_BOT_WEBHOOK_URL "the POST to value"
setx GROK_BOT_WEBHOOK_KEY "the key value"
```

⚠ **Click *into* each field and Ctrl+A before copying.** The display truncates with an ellipsis, and
copying what you can see yields a partial key and `Invalid API key`.

⚠ **`setx` only reaches shells opened afterwards** — and Claude Code's own Bash inherits its
environment from startup, so **Claude Code must be restarted** before its pushes fire the hook.

⚠ **PowerShell aliases `curl` to `Invoke-WebRequest`, which rejects `-H`.** Use `curl.exe`, or assign
the URL and key to variables and call `Invoke-RestMethod` so the header is built by PowerShell rather
than parsed by a shell. This cost four attempts.

**It can never block a push.** Missing key, no network, webhook 500, xAI outage — every path exits 0
with one line to stderr. **Unsetting either variable is the off switch**, with nothing to uninstall.

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

# 2. Current state

**The roster is complete as of 2026-09-06.** All seven Bots exist; all seven skills are uploaded.

| Bot | Role | Skills held | Routines |
|---|---|---|---|
| **Librarian** | Vault citations with file-and-line proof | — | `Vault refresh` (webhook + inert PR trigger) |
| **Ledger** | Receipts → ticket breakdown → invoice readiness | Receipt Extraction, Invoice Readiness Check | — |
| **Scribe** | .docx production | Project Report, Proposal Assembly | — |
| **Intake** | RFQ package → intake checklist, on demand | RFQ Intake | — |
| **Estimator** | Duration model and priced work-up, propose-only | Duration Model, Work-Up Billing Math | — |
| **Scout** | Competitor and AI-visibility watch, public sources only | — | — |
| **Architect** | Grok Bot platform research | — | — |
| **Chief of Staff** | Auto-created at signup, unused | — | — |

**Group: "Bid Desk"** — Estimator, Intake, Librarian, Scribe. Order is Intake → Estimator → Scribe,
with Librarian on call and outside the chain. Every member carries the handoff contract: name the
output file path, the open questions and the next owner, and do not assume the next Bot read the
conversation.

**Each Bot was verified by making it state its own rules back**, not by trusting the save
confirmation. Intake recited the derive-vs-ask split and *"incomplete inputs stay open, I list them
and stop rather than fill a plausible blank."* Estimator got all three probes right: 100 ft/hr
measures one pig on one unlooped coil and is **not** heater-total footage ÷ 100; rig-in is 6 hours
with exactly two conjunctive departures and rig-out mirroring the whole figure; Smart Pig is 2 hrs
per pass, *"an estimate only; quoted jobs will disagree, and that is expected."*

**`Webhook ping`** also survives on Librarian — the throwaway that proved the webhook mechanism. Its
run history is the evidence, and it answers to a different key.

**Workspace folders** `/workspace/{bids,jobs,out,scratch}` created 2026-09-06. They are named in
`README-FOR-BOTS.md`, which every Bot reads, and until then they did not exist.

**Connectors installed — four, and one was never deliberately added.** Gmail, Google Drive,
**OneDrive** and GitHub. Gmail and Drive were auto-added to Chief of Staff at signup and Gmail was
never signed in; GitHub was added deliberately for the Git-event test and **its token has been
deleted**, though the connector entry remains. **OneDrive is the unexplained one** — see the finding
below.

**Meter:** 4% before this session's additions.

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

**Read [[BACKTEST-SPECIMEN]] before uploading the four estimating skills.** It works all four against
DSP26085 — six rules reproduce the real quote to the hour and to the line, and one rule was
falsified. **None of the four carries a rate number**; rates belong to a contract and stay in the
vault behind their own warnings.

**Substrate.** `/workspace/vault` is a clone of the public `obsidian-work` repo — 6319 objects,
16.21 MiB, **no credentials prompted**. git on the VM is version 2.47.3.

```bash
git clone https://github.com/TheSkinz/obsidian-work.git /workspace/vault
```

Still to do on the VM: create `/workspace/bids`, `/workspace/jobs`, `/workspace/out`,
`/workspace/scratch`, and copy `README-FOR-BOTS.md` to `/workspace/`.

---

# 3. Findings

## The citation audit — PASSED, 10 of 10. TESTED 2026-09-06.

The go/no-go gate: ask Librarian ten domain questions with known answers, then open each cited file
and check the line says what it claimed. The ten, chosen because each has a recorded correction or a
known trap behind it:

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

Every answer carried a real file path and a verbatim quote. Three were spot-checked
character-for-character against the working copy (`17-glossary.md:25`, `quote-lifecycle.md:81`,
`B-102.md:73`). **No invented citations, and no citation that failed to support its claim.**

Two answers showed judgment rather than retrieval:

- **Q7** — answered "job report", then flagged that `USA26041-job-sheet.md` also carries a closed
  Ticket-breakdown reconciliation section which *"sits against that model"*, and filed it under
  Unresolved questions rather than resolving it. That is the "contradictions are findings, not noise
  for you to resolve" instruction working.
- **Q6** — separated labor billing (hourly, not a 12-hr day rate, changed 2026-07-12) from per diem
  (one allowance per person per shift, generic base $150, role-split where the contract requires it),
  and disclosed in Assumptions that it read both because the question's framing and the recorded
  change were about different things.

**Cost:** meter read 1% before and 1% after. **Elapsed:** roughly four minutes, with running progress
messages — genuinely grepping rather than answering from context.

**The audit's own limitation, learned later the same night:** Q2's answer quoted
`estimating-approach.md` correctly, but that file was 24 hours stale against the config repo. **A
passing citation audit does not detect a stale source.** That is what the push hook exists to fix.

## Skills survive verbatim. TESTED 2026-09-06.

*Does an uploaded skill survive verbatim, or does Grok Bot paraphrase it on ingest?* It mattered
because every ported skill is written as "do X, and specifically do NOT do Y" — a summariser drops
the Y half first, stripping the guardrails while leaving the skill looking correct.

**The stored skill and the vault source match byte-for-byte in the body.** The platform adds a YAML
frontmatter wrapper of its own, so the *file* differs while the *content* does not. Nothing
paraphrased, compressed or dropped. **The counter-cases in the ported skills are safe.**

Two incidental findings: **inter-Bot DM works and is legible** — the Architect messaged Scribe and
the thread showed `Messaged Scribe` / `Message from Scribe` inline, which is the push channel; a Bot
cannot silently read another's thread, but it can ask, and the asking is visible. And **print-back
truncates**, which is why the comparison had to be done by diffing files on disk.

## The Git-event trigger has no push event, and did not fire. 2026-09-06.

**READ, from the trigger config UI.** The complete event list:

| Group | Events |
|---|---|
| Pull request | Opened · Updated · Merged |
| Review | Requested · Approved · Changes requested · Commented · Thread resolved · Thread reopened |
| Comment | PR comment · Inline review comment |
| Checks | CI passed · CI failed |
| Issue | Assigned |

**Nothing fires on a push.** The designed routine — Librarian pulls when `obsidian-work` changes —
**could not be built as specified**, because vault work commits straight to `main` and never opens a
PR. That was the most load-bearing assumption in the routine design.

**TESTED — the PR-opened salvage test also failed.** Routine armed and Active at 19:03, PR #5 opened
at 19:05:22, run history at 19:09 showed only a manual Test run. Nearly three hours later it still
showed one run. **The diagnosis is concrete:** `gh api repos/TheSkinz/obsidian-work/hooks` returned
**nothing — no webhook was ever registered on the repository**, so Grok Bot had no channel to learn
the PR existed. The trigger is not slow, it is not wired.

**Three candidate causes, undistinguished (INFERRED):** the fine-grained PAT may have lacked
**Webhooks: Read and write**, flagged as an inference when the token was minted; the connector may
register hooks lazily; or Grok Bot may poll on an interval longer than four minutes.

**What it cost to find out.** The trigger needs the **GitHub connector**, and the connector wants a
**personal access token, not OAuth** — *"Fine-grained or classic PAT from
https://github.com/settings/tokens with the repo scopes you want the agent to use."* That is better
than the account-wide grant the connector's description implies, because the **token** sets the real
ceiling: a fine-grained PAT scoped to one repository keeps everything else out of reach even on a
shared VM. **The PAT was deleted 2026-09-06** once the webhook path proved better — it existed only
to test a trigger that turned out to have no push event and never fired. The connector entry may
still show as installed; the token carried the access, and it is gone.

## The Webhook trigger fires. TESTED 2026-09-06.

A routine armed on the **Webhook** trigger and fired by an HTTPS POST returned **`WEBHOOK FIRED
2026-09-07 03:22:04 UTC`** — exactly the instructed output, nothing else, immediately.

**Event-triggered routines are real on this platform. They just do not work through GitHub.**

Selecting the trigger exposes three fields: a **POST to** endpoint on
`api2.cursor.sh/automations/webhooks/...` (more Cursor infrastructure), a **key**, and a ready-made
**header** line. Any process that can make an HTTPS POST can fire the routine — so **Claude Code can
trigger a Grok Bot routine programmatically.** That is the bridge a source video wrongly attributed
to an MCP server; it exists, just not where that claim put it.

**The webhook path is strictly better than the GitHub one.** It needs no connector and no token, so
it *removes* a third-party credential rather than adding one. It replaces the missing push event via
a local git hook, with the trigger owned locally. And it generalises — any defect the vault's own
tooling detects (a lint error, a failed rollup, a `RULE-FORK` fire) can fire a routine, which fits
this system far better than a clock.

**The key is a credential.** It authorises firing the routine, so it belongs in no repo, transcript
or shell history. Regenerate it if exposed, and read it from an environment variable rather than
writing it into a hook.

**Both hook paths verified 2026-09-06.** A push touching nothing under `01-context/` fired the
routine and produced no report — the correct quiet path. A push touching
`01-context/system-workflow-reference.md` fired it and it spoke: *"Vault pulled `d4c590b..03e6071`.
Standing context moved: `01-context/system-workflow-reference.md` — that file changes how every Bot
answers."* Two sentences, right file, correct commit range.

**The routine's instruction is deliberately quiet.** It fires on *every* push, so it pulls always but
speaks only when something under `01-context/` moved, replying `nothing new` otherwise even when many
other files changed. A routine reporting 24 files per push is the chatty failure the 2026-08-21 vault
audit retired; the clone refreshes either way, which is the part that matters.

## The account's four connectors, and why each is there. READ 2026-09-06.

**Gmail, Google Drive, OneDrive, GitHub.** Gmail and Drive were auto-added to Chief of Staff at
signup and Gmail was never signed in. **OneDrive was added by Jesse deliberately**, against possible
future use rather than for anything in the trial. GitHub was added for the Git-event test and **its
token was deleted the same evening**, though the connector entry remains.

A mid-session jump in the marketplace header from `2 installed` to `3 installed` was briefly flagged
as unexplained; it was OneDrive, and it was intentional. **Recorded because the count is worth
knowing, not because anything was wrong.**

Worth one line and no more: OneDrive is where the per-facility bid working copies live, and every
Bot on the account shares one browser session — so if it is ever signed in, it is signed in for all
of them. Its connector is read-only in any case.

## Scout hit a login wall, stopped, and said so. TESTED 2026-09-06.

First pass, AI-visibility half: ask one tool three category questions without naming USADebusk.
**Perplexity required a login before any query could be submitted** — *"Login or sign up for free"*
with Google, Apple, email and SSO options. Scout stopped there, **did not sign in, and did not try
another tool**, then reported the gap as a gap and asked whether a later pass could try ChatGPT or
Claude.

**That is the boundary rule working**, and it was the risky part of that Bot. It also means the
AI-visibility job may be **structurally unavailable** to a credential-free Bot: if ChatGPT and Claude
also gate anonymous use, there is no way to run the category test without an account, and that half
of Scout's job does not exist. **Establish that before investing further in Scout** — the competitor
half, which reads public services pages, is unaffected either way.

## Connector catalogue, as the app actually shows it. READ 2026-09-06.

**No SharePoint connector at all** — searching returns "No plugins match". **OneDrive exists but is
read-only** ("Browse, search, and read Microsoft On..."). **Outlook and Outlook Calendar both
exist.** **GitHub exists with write** ("Manage repos, issues, pull requests"). The public connector
directory listing SharePoint and OneDrive under Business & Enterprise is not what this account sees.

**There is no email trigger of any kind**, so inbox work runs in scheduled batches, never on arrival.

---

# 4. What's left

**Intake and Estimator**, with their four estimating skills already written and back-tested. Read
[[BACKTEST-SPECIMEN]] first.

**Scout**, narrowed. Its original bid-folder reconcile was designed around a SharePoint connector
that does not exist, and OneDrive is read-only. What survives needs no credentials: **competitor
watch** on public material (Quest Integrity is named across the vault as a competitor with its own
decoking division, and `DSP26058` is recorded `lost-reason: competitor`), and an **AI-visibility
check** — asking ChatGPT, Claude and Perplexity realistic buyer questions *without* naming USADebusk
and recording whether it surfaces. Both are read-only, and both are the "monitoring and briefs"
category this tool is documented to be reliably good at.

**The back-test, and it is the verdict.** Judge against artifacts that already have known-good
answers, two structurally different ones per Bot. Estimator against a closed bid, line by line.
Scribe against a delivered project report — the gap to the hand-edited version is the editing time it
actually saves, and watch specifically for hand-tallied figures, since the vault's generator does not
exist over there. Ledger against a completed ticket breakdown; mechanical, so near-perfect or the
tool is not ready. Librarian against the citation audit again.

**Record three things, because they decide renewal:** how fast the weekly allowance drains and what
drains it; how often a sign-in is blocked by the datacenter IP and needs manual takeover; and whether
routines fire reliably now that the webhook path is proven.

**Deferred deliberately.** No Auditor Bot until `/workspace/out` holds real artifacts to audit. No
Chief of Staff coordinator until the Bot count justifies a router, roughly eight. No navigation
**skill** — this file is the single copy, and a skill restating it would be the duplication
`RULE-FORK` exists to catch. If the trial renews, the skill becomes a pointer at this file.

---

# Standing constraints

**One computer, one credential store.** All Bots share the cloud machine, its filesystem, its browser
cookies and its terminal credentials. The docs state it outright: **do not use separate Bots as a
security boundary.** Anything one Bot signs into, every Bot has.

**That collides with the account-separation rule** in global CLAUDE.md, which keeps xAI accounts on
personal credentials and away from USADebusk systems. The trial therefore runs **credential-free** —
no Outlook, no SharePoint, no Gmail, files uploaded by hand. The one departure, the GitHub PAT, was
made deliberately for a single answer and reversed the same evening.

**Only `/workspace` persists.** Temp directories and uncommitted state can vanish. Every finished
artifact gets copied out.

**Limits worth knowing:** 50 Bots and group chats per account; 50 routines per Bot; only the **20
most recent runs** retained per routine, so anything needing an audit trail writes its own log to
`/workspace`; **deleting a routine is permanent**; no model selection or version pinning; Legacy
Privacy Mode is unsupported and cloud storage is mandatory.

**Business content is not restricted** — pricing, rates, methodology, heater and job data, customer
and facility names all go anywhere. **Credentials, secrets, API keys and tokens do not go on this
machine at all.**
