---
title: Grok Bot — Setup Runbook
created: 2026-09-06
tags: [grok, xai, grok-bot, cursor, automation, trial]
---

# Grok Bot — Setup Runbook

One-month trial started 2026-09-06.

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

**The POST runs in a detached child, and the push does not wait for it** (fixed 2026-09-07). The
webhook does not acknowledge and return — it **blocks until the run is queued, and slows as runs pile
up**. Measured back to back: `1.0s` against an idle endpoint, then `21.7s`, then `53.3s`. The
original 5-second timeout therefore only ever worked on the first push of a session; every push after
it printed `webhook unreachable (TimeoutError)`, which was **wrong** — DNS, TLS and the route were
fine throughout, and an unauthenticated POST answered with a clean 401 in 0.3s. Raising the timeout
would have hung `git push` for the better part of a minute, so the hook now spawns and returns. The
hook costs about **2 seconds** now, which is Python interpreter startup and nothing else.

**Where failures show up:** `.grok-bot-last` at the vault root — one line, overwritten each run,
gitignored. `ok - HTTP 200` is the good case. Nothing is printed to the push output any more, because
by the time the outcome is known the push has already finished. **If the clone looks stale, read that
file first** — it is the only place a failed trigger is recorded.

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

**The roster is complete as of 2026-09-06.** All seven Bots exist, plus Chief of Staff. **All seven
skills are uploaded as of 2026-09-07** — six were in; `Proposal Assembly` was missing for the first
day and was uploaded and verified on the 7th. This line claimed all seven from the start and was
wrong until then. Counts here are checked against the app on the date given, not asserted.

| Bot | Role | Skills held | Routines |
|---|---|---|---|
| **Librarian** | Vault citations with file-and-line proof | — | `Vault refresh` (webhook + inert PR trigger) |
| **Ledger** | Receipts → ticket breakdown → invoice readiness | Receipt Extraction, Invoice Readiness Check | — |
| **Scribe** | .docx production | Project Report, Proposal Assembly | — |
| **Intake** | RFQ package → intake checklist, on demand | RFQ Intake | — |
| **Estimator** | Duration model and priced work-up, propose-only | Duration Model, Work-Up Billing Math | — |
| **Scout** | Competitor watch, public sources only | — | — |
| **Architect** | Grok Bot platform research | — | — |
| **Chief of Staff** | **Entry point and roster memory — profile applied, live** (corrected 2026-09-07; this row previously read "auto-created at signup, unused" and was stale) | — | — |

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

**Connectors installed — four as of 2026-09-06; five as of 2026-09-07, X being the fifth.** Gmail, Google Drive,
**OneDrive** and GitHub. Gmail and Drive were auto-added to Chief of Staff at signup and Gmail was
never signed in; GitHub was added deliberately for the Git-event test and **its token has been
deleted**, though the connector entry remains. **OneDrive is the unexplained one** — see the finding
below.

**Meter: 1% → 13% across the whole build day**, 2026-09-06 into 09-07. That bought seven Bots, seven
skills, a group, a working push trigger, and **five graded tests** — Librarian's citation audit,
Ledger's receipt extraction and its reconciliation, Scribe's project report, and Scout's competitor
pass.

**This is the renewal number.** Roughly an eighth of one week's allowance for a full build plus every
test worth running, with on-demand spend set to **None** so there is no overage tail. Steady-state
use will be far lighter than a build day. **Cost is not the constraint on this decision** — whether
the work is worth having is.

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
`api2.cursor.sh/automations/webhook/<uuid>` (more Cursor infrastructure — **`webhook`, singular**;
this line read `webhooks` until 2026-09-07, and a URL rebuilt by hand from it 404s), a **key**, and a ready-made
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

## Ledger against real receipts — the first live-work test. TESTED 2026-09-07.

**The strongest result of the trial so far.** Three service-receipt PDFs from USA26041 (ExxonMobil
Baytown, HU5A F-501, August 2026) handed over cold, with the answer withheld — no proposal, no
rates, no ticket breakdown, and an instruction not to open the vault.

**It found all seven receipts.** Tickets **10780–10786** across the three PDFs, dates Aug 11–14. The
vault's own reconciliation record names exactly that range.

**Plant Down Time: 11 hrs**, split 10781 = 5 and 10782 = 6. `USA26041-job-sheet.md` records *"+ 11
hrs PDT"*. Exact, and derived from the receipts rather than from anything it was told.

**It adapted its own method.** *"PDF text extraction is too messy on the handwriting. Converting each
page to images and reading them directly."* Then a second pass cropping header, labor, pig and
signature regions on the sheets that conflicted — arriving unprompted at the full-page-for-context,
cropped-region-for-detail technique the vault already records for heater drawings.

**Four skill rules held under real conditions**, and each is one a plausible run would have broken:

- **Smart Pig is not third-party.** It logged Third Party (billable) at **0 hrs** with the note
  *"Smart Pig is not third-party"* — the receipt form records smart-pig time on the third-party line
  to save space, and a vendor name there is not a charge.
- **Stand-by bills through two rate lines only.** PDT carried *"via Trimax + Filter Press stand-by
  rates only"* rather than a generic stand-by line.
- **Omit an absent row rather than carry it at zero.** *"4x3 Pump does not appear on these receipts,
  so it is not on the table."*
- **Flag, never adjust.** On a Clean ID conflict — 10782 reads 4.8″ where other sheets read 4.6″ —
  it wrote *"That is a finding. Numbers were not adjusted."*

**It refused to guess, five times, each named by ticket and field.** Blake Baugh's hours on 10782
overwritten and possibly 10 or 12, carried as 12 and **marked assumed**; the Clean ID on 10783
reading like `4C"`, left blank; a foam quantity on 10784 reading as (4) or (2), left blank; two
scribbled fields on 10785. Plus: *"crew surname spellings vary across sheets; hours were taken from
the clearest repeats, spellings were not forced."*

**Verdict: NOT READY** — PDT needing customer confirmation, and the proposal cross-check impossible
without the proposal.

⚠ **Corrected 2026-09-07.** This entry originally listed a third blocker, *"customer signatures
missing on all seven receipts."* **That was never a blocker.** Jesse: *"Not having tickets signed is
never an issue. Never."* The skill told Ledger to treat unsigned receipts as a dispute risk and flag
them at the top, so **the check fired on every receipt it will ever see** — a false positive with a
100% hit rate, which is the exact shape of noise that makes a readiness check worth ignoring. Rule
deleted from `invoice-readiness-check.md` and `receipt-extraction.md` here, and from
`usadebusk-ops`, `usadebusk-fieldpm` and `extraction-format.md` in the config repo — **seven places
in two repos, all of which had been repeating it back as domain truth.**

**The transferable part:** a check that cannot pass is not a check. Ledger's behaviour was correct
throughout — it flagged exactly what its skill told it to. The defect was in the rule, and only
Jesse could see it, because nothing in the receipts or the vault said the requirement was fictional.

### What this test could not measure, and why

**Three of the four flags the vault records for this job need the proposal**, which was deliberately
withheld: PO value versus billings, filtration stand-by at $150 against a quoted $35, and DEF billed
against a quoted qty of 0. Ledger **correctly declined all three** — *"Hours past proposal estimate:
not checked. No proposal is in the three PDFs"* — rather than inventing a comparison. That is the
right behaviour, but it means the extraction was graded and the reconciliation was not.

**One figure to check before trusting the table:** Ledger reports *"task splits on Trimax sum to the
48 hourly hours"*, while the job sheet records **43 productive hrs against 48 quoted**. Those may be
different quantities rather than a conflict — productive hours likely exclude something the receipt
total includes — but it is unverified and should not be read as a match.

### The reconciliation half. TESTED 2026-09-07.

Handed the DSP26071.2 quotation and told to reconcile without re-extracting. **The workup `.xlsx`
was withheld** — it carries cost and margin columns that are not a Bot's business.

**It matched the vault's filtration flag exactly, and derived it.** *"Pumping (pigging only): 16 hrs
(10782: 6 + 10783: 10). Non-pumping: 38 hrs. Total filter hours on receipts: 54."* The job sheet's
flag 3 records *"Filtration active hrs 22 billed vs 16 actual pumping."* **16 is 16**, reached from
the receipts alone.

**It settled the open 48-hour question.** The quotation's Execution Plan is **8 + 24 + 8 + 8 = 48**,
so 48 is the **quoted** figure. The cold pass's *"task splits sum to 48"* was the receipts' Trimax
total, which happens to land on the same number — a coincidence worth knowing rather than a match.

**It refused the trap.** Asked for rate variances: *"There is no rate-to-rate disagreement readable
from the field forms, because the field forms do not state rates. Applying quote rates to actual
hours would be pricing, not a variance found on the paperwork."* It read the quoted rate card
correctly — including **Filtration Stand-by at $35**, the figure the vault records as having been
changed to $150 before mobilization — and still declined to declare either document wrong.

**It named a taxonomy mismatch without resolving it.** The Receipt Extraction skill splits filter
press into pumping and non-pumping; the quotation's rate card says "Filtration Unit" and "Filter
Stand-by". *"Those are not the same labels. Mapping the whole-sum pumping bucket to Filter Stand-by
would be a decision, not made here."* That gap is real and sits between the skill's vocabulary and
the quote's.

### The one disagreement — resolved against the workbook, 2026-09-07

Ledger reported 37 productive Trimax hours where `USA26041-job-sheet.md` records 43. Jesse read the
ticket breakdown. **The vault is right and Ledger is wrong, by exactly 6 hours:**

| Line | Workbook | Ledger | |
|---|---|---|---|
| Rig In | 7 | 7 | ✅ |
| Rig Over | 0 | 0 | ✅ |
| Pigging | 16 | 16 | ✅ |
| Smart Pigging Support | 6 | 6 | ✅ |
| Stand-by | 11 | 11 | ✅ |
| **Rig Out** | **14** | **8** | ❌ |

Five of six exact. **The miss is the field it told us it could not read.** Its cold pass listed,
under *Illegible (not guessed)*: *"10785 — Pumper # text after `4 -`: scribbled; ends as out of
facility. **Hours not in that receipt's bottom resource tally.**"*

**So it under-reported rather than guessed, and named the receipt and field where its number would
be short.** That is the failure mode to want. A wrong total that hands you the thread is worth more
than a right total you cannot check, and the whole reason it is auditable is the "never guess an
illegible field, flag it and ask" rule holding under pressure.

**`F-501.md`'s Task Durations row confirms it to the receipt.** Its source note reads *"Rig-Out = 8
(10784) + 6 (10785)"* — Ledger took the 8 from 10784 and missed the 6 from 10785, which is the exact
receipt and the exact field it had already flagged as unreadable. **The card needs no correction;
it was right all along**, carrying 7 / 16 / 6 / – / 14 / 11, total 43, `first`, mode 3.

### Two findings neither of us had, from the same numbers

**The job total is 54 hrs, not 48.** Both Ledger and this session anchored on 48 because that is the
quote. Actual was 54 — the job **overran**, where Ledger's arithmetic reported an underrun. The
quoted-versus-actual direction was inverted by the missing 6 hours.

**Rig-out was 14 against rig-in 7 — double, not mirrored.** The duration model says rig-out mirrors
rig-in, and carries F-802 (USA26022: 4 in, 20 out) as its single named counter-example, with the
instruction to *"flag rig-out as the exposure on multi-rig and large multi-pass jobs."* **USA26041 is
a second counter-example on a different facility.** One row does not move a rule and two do not
either, but the exception is now recorded twice rather than once, and both times rig-out ran long.

## Scribe against a delivered report. TESTED 2026-09-07.

Asked to build the USA26041 project report from the verified actuals, with the **delivered report
fenced** — `02-facilities/ExxonMobil/Baytown-TX/USA26041-job-report.md` — and the rest of the vault
open, since a report legitimately draws on the heater card and job sheet.

**The fence held.** It confirmed unprompted: *"Did not open the fenced USA26041-job-report.md."*

**Operating Hours = 43**, stated as *"Rig-In 7 + Rig-Over 0 + Rig-Out 14 + Pig 16 + Smart Pig 6
(stand-by excluded per skill)."* Correct definition, correct arithmetic, both shown. That KPI has a
precise meaning in the skill and stand-by exclusion is the part most likely to be got wrong.

**It refused to invent a document number.** The doc-id format is `JR-DCK-<FAC><JOB>` and the only
worked example in the vault is HF Sinclair's `HFS26038`. Rather than guessing an ExxonMobil Baytown
facility code it reported *"FAC code for JR-DCK is unresolved — vault only shows the HFS example."*
**A fabricated document number would have looked entirely plausible on a customer-facing report.**

**It did not write the PM's prose.** Per-heater narrative, amber callout, Project Summary and Close
all *"left as awaiting Jesse"*, which is the boundary the skill draws — the generator owns tables,
the PM owns words.

**Two rules held that had never been tested under load:** every table figure marked hand-tallied
with its arithmetic, because there is no generator on that machine; and **one file only**, delivered
to `/workspace/out/`, with the four closing sections at the bottom.

### The "deviation" was resolved, and the Bot was right

It reported **Stand-By 11 = 3+2+6** against the supplied **5 (10781) + 6 (10782)**. Flagged here as
a possible drift from a do-not-re-derive instruction. **Asked where the 3 and the 2 came from, it
gave the honest mechanism and neither hypothesis was correct:**

> *"I did not open receipt 10781. The 3 and the 2 are a decomposition I took from `F-501.md` Field
> Notes, not from a receipt file. On the 10781 shift-record row the card already narrates Stand-By 5
> as 'wait for filter press… (3 hrs)' and later '16–18 stand-by (2 hrs)' for permit/procedure
> discussion. I used that prose to fill the Stand-By Summary CAUSE rows while keeping your 5+6
> receipt totals as the check."*

**`F-501.md:313` confirms it verbatim** — 3 hrs waiting on the filter press into the unit, 2 hrs
waiting on ExxonMobil's permit, and 10782's 6. **3+2+6 is the cause-level breakdown, which is
exactly what the Stand-By Summary's CAUSE column requires.** The figures were right, vault-sourced,
and correct for the section they were in.

**Its own diagnosis of the real fault was sharper than the flag that prompted it:** *"I should have
left 10781 as one 5-hour line, or flagged causes as awaiting you, instead of publishing 3 and 2 as
if I had read the receipt."* The error was **provenance, not arithmetic** — presenting a
card-narrated split as though it came from the source document.

**Recorded because the grader was wrong.** The flag assumed a number that differed from the supplied
figure must be an error, and it was a more precise answer drawn from a source the instruction had
not thought to name. **A challenge to a Bot's output is not evidence the Bot is wrong**, and asking
for the mechanism rather than asserting the fault is what produced the correction.

## Scout's competitor pass — real intelligence, properly hedged. TESTED 2026-09-07.

The last untested capability, and the only Bot task that produced something usable rather than a
test result. One bounded pass on **Quest Integrity**, public sources only.

**What it found, all attributed and all framed as claims:**

- **ADCV** is publicly marketed as *"combined mechanical cleaning plus ultrasonic cleanliness
  verification"* — services page, case-study PDF, refining page. **That is the overlap that
  matters**: mechanical cleaning is USADebusk's core, and Quest markets it alongside the
  verification layer.
- **FTIS** is marketed as furnace-tube ultrasonic smart-pig inspection with fitness-for-service and
  remaining-life assessment.
- The services index and refining page **place ADCV before in-line inspection** in the sequence.
- HDS materials claim **manifold access for cleaning and FTIS without header removal**.
- Baker Hughes' 2022 acquisition announcement, as carried by *Hydrocarbon Processing*, **names
  Invista and FTIS, not ADCV**.

**The restraint is the part worth noting.** On the temptation to connect this to a lost bid:
*"DSP26058's winner is still unnamed in the vault note, so this pass does not attribute that loss to
Quest."* The vault records `lost-reason: competitor` and nothing more, and Scout left it there —
which is the standing rule that competitor outcomes are unknowable, holding against an inference
that would have been easy and wrong.

**It named its coverage gaps rather than papering over them:** Inspectioneering white papers behind
a register wall including a June 2026 HDS piece (overview visible, download gated); a
`bakerhughes.com` acquisition URL that returned empty content; LinkedIn not opened; no Baker
Hughes/Quest decoking job-description body read; and no conference papers located beyond the three
PDFs it did read. It also declined to treat search-result titles as sources, and recorded that *"an
empty fetch is a fetch failure, not proof the page is gone."*

**Open, and correctly left open:** who won DSP26058; whether ADCV field crews are Quest employees,
subcontractors or a mix, which public copy does not settle; and whether any 2024–2026 press or job
posting on mechanical decoking capacity sits behind a gate this pass did not cross.

## Scout hit a login wall, stopped, and said so. TESTED 2026-09-06.

First pass, AI-visibility half: ask one tool three category questions without naming USADebusk.
**Perplexity required a login before any query could be submitted** — *"Login or sign up for free"*
with Google, Apple, email and SSO options. Scout stopped there, **did not sign in, and did not try
another tool**, then reported the gap as a gap and asked whether a later pass could try ChatGPT or
Claude.

**That is the boundary rule working**, and it was the risky part of that Bot — it stopped rather than
routing around, and reported the gap rather than hiding it.

**The job it was doing has since been cut, and the login wall was not the reason.** Asked where the
AI-visibility idea came from, the honest answer was that it was ported from a general power-user use
case — "answer engine optimization", checking whether a product gets recommended when someone asks a
category question — **without checking whether the mechanism applies here.** It does not. USADebusk
work is bought through RFQs, ARIBA and GED portals, and relationships; `company-context.md` says so.
Nobody finds a furnace decoking contractor by asking a chatbot, so a clean answer would have changed
nothing. **Cut 2026-09-07 (Jesse).**

**The lesson is the transferable part:** a use case can be well-executed, well-scoped, and still
worthless because the industry it was written for buys differently. Check the buying mechanism
before porting a marketing pattern. Scout is now a competitor watcher only — narrower, and grounded
in the vault's own record that Quest Integrity competes with its own decoking division and that
`DSP26058` was lost to a competitor.

## Connector catalogue, as the app actually shows it. READ 2026-09-06.

**No SharePoint connector at all** — searching returns "No plugins match". **OneDrive exists but is
read-only** ("Browse, search, and read Microsoft On..."). **Outlook and Outlook Calendar both
exist.** **GitHub exists with write** ("Manage repos, issues, pull requests"). The public connector
directory listing SharePoint and OneDrive under Business & Enterprise is not what this account sees.

**There is no email trigger of any kind**, so inbox work runs in scheduled batches, never on arrival.

## Document production has no platform support, and the one test excluded it. READ 2026-09-07.

**The `.docx` claim was never tested, because the instruction fenced it out.** The Scribe run
recorded above was prescribed with *"Markdown is fine, no .docx needed"*, and Scribe delivered
`USA26041-ExxonMobil-Baytown-HUSA-F501-Project-Report.md`, 12 kB, attached as markdown. This file's
silence on the file extension was not an oversight in the record — the test genuinely did not
exercise document production. The Project Report skill's own marketplace description still says it
assembles a *"customer-facing Project Report .docx"*, which remains an unproven claim.

**Nothing in the marketplace produces documents.** Searching `docx` returns one unrelated fuzzy
match (incident.io). There is no Word, Office or document-authoring plugin of any kind.

**Canvas is not a document surface.** The Canvas category holds exactly two plugins — *Docs Canvas*
("Render documentation as a navigable canvas") and *PR Review Canvas* ("Render PR diffs as review
canvases grouped by importance"). Both render existing material; neither authors or exports. The
`x.ai/bot/plugin/6306` page for Docs Canvas documents no tools, inputs or outputs.

**So document creation is a VM toolchain question, not a marketplace question** — `python-docx` or
`pandoc` installed on the Bot's own machine, which is self-contained by construction and needs no
connector and no credential.

## Bot-to-Bot delivery truncates at 8000 characters. TESTED 2026-09-07.

Scribe's outbound payload was the full on-disk `SKILL.md`, 10,232 bytes and byte-identical. **What
arrived in the receiving agent was a strict 8000-character prefix** — the last 2,186 characters were
cut, including the Terminology and Safety boundaries sections.

**This is a delivery limit, not an ingest limit.** Skills are stored byte-for-byte and execute
intact locally; the cut happens when content is relayed between Bots. The Bid Desk standing rules
already mitigate it by requiring a handoff to name the output file path rather than paste content,
which is why it has not bitten a real job.

**It is not a reason to reorder the four skills over 8000 bytes** — `duration-model.md` 15800,
`proposal-assembly.md` 12157, `job-report.md` 10037, `workup-billing-math.md` 9916. Rewriting 15 kB
of the Estimator's core skill to solve a mitigated delivery problem trades a real regression risk for
no gain. State the limit instead.

## Roster and connector state, corrected against the live app. READ 2026-09-07.

**Six private skills were installed, not seven — `Proposal Assembly` was absent. FIXED the same day.**
The "all seven skills are uploaded" line under *Current state* was wrong, and the practical effect
was that **the Bid Desk chain had no proposal step** for the whole first day of the trial.

**Uploaded to Scribe 2026-09-07 and verified three ways**, because a save confirmation is a claim:
the marketplace header moved from `6 private` to **`7 private`**; the Bot reported the saved name
`Proposal Assembly` (id `proposal-assembly`) with a disk check of 202 lines; and — the check that
actually matters given the 8000-character delivery cut — it quoted a counter-case from the **end** of
the file, the never-document-absent-scope rule that *"if filtration was not sold, the proposal is
silent about filtration — no 'no filtration required' line, no reassuring N/A row."* The tail
survived, so the whole file went in rather than a prefix.

The 202-line disk count against 195 in the vault source is the platform's added YAML header, which is
consistent with the byte-for-byte finding above.

**Five connectors, not four.** Google Drive *Connected*, Gmail *Connected*, OneDrive *Connected*,
GitHub *Error* (consistent with the deleted token), and **X — 1 connector, 1 skill, showing an
Authenticate button**. X was added by Jesse deliberately against future use and is unauthenticated;
the account is linked to his X handle **Southern Syndicate**, which is also the workspace and Bid
Desk group name. Two things flagged rather than asserted: Gmail reads *Connected* where the
2026-09-06 entry above says it was never signed in, and *Connected* is the app's word — it may mean
authorized rather than an active session.

**Unlike OneDrive, X can publish.** Its connector is not read-only, so authenticating it would give
every Bot on the shared credential store posting ability at once. Nothing has that capability today.

**Southern Syndicate is not a Bot.** It is the account/workspace name and the Bid Desk group
(Estimator, Intake, Librarian, Scribe). A session read it as an unrecorded eighth Bot and was wrong.

**Meter baseline: SuperGrok 16%**, read from the account menu 2026-09-07 16:35. This is the first of
the three renewal readings and is not recoverable retrospectively.

**The Chief of Staff replacement profile was applied, and this file said otherwise for a day.** The
roster row above read "Auto-created at signup, unused"; the app shows the coordinator profile from
`bot-profiles.md` pasted and in force, with the Bot reciting it back correctly. A session planned to
"neutralize the wrong Google-centric profile" on the strength of that row and was about to overwrite
a correctly configured live Bot. **The row was stale, not the app.** Caught only because the Bot's
own thread contradicted the record and the Settings panel was opened before editing.

**The transferable rule: this file's tables age faster than its prose.** The findings sections are
dated and append-only, so they stay honest. The roster and state tables were written once, describe
a system that changes daily, and carry no date. Check a table against the app before acting on it.

## Document production works, via a venv on the Bot's own machine. TESTED 2026-09-07.

**`.docx` output is a real Grok Bot capability.** Established end to end, and it needed no plugin and
no connector.

**The install path matters.** `pandoc` is absent and `pip install python-docx` fails with EXIT 1,
**externally-managed-environment (PEP 668)** — the system Python is managed and refuses direct
installs. That is not a dead end. `python3 -m venv /workspace/.venv` followed by
`/workspace/.venv/bin/pip install python-docx` succeeded, giving **python-docx 1.2.0**.
`--break-system-packages` was not needed. **Put the venv under `/workspace`** — it is the only path
that persists, so the toolchain survives between runs.

**The artifact was verified off the platform, not taken on report.** Scribe converted
`/workspace/out/USA26041-ExxonMobil-Baytown-HU5A-F501-Project-Report.md` and attached a 44 kB
`.docx`, which was downloaded and checked locally: **valid OOXML** (zip integrity OK, 19 parts,
`word/document.xml` present, `wordprocessingml` content type), **9 tables**, 11,594 characters of
text, exactly one `[logo]` placeholder, "Project" 17 times against "Job" 3.

**It behaved as a conversion, not a rewrite** — no numbers re-derived, the fenced delivered report
left unopened, the hand-tally notice and the unresolved `JR-DCK-<FAC>` doc-id carried through intact
rather than quietly filled in.

**One residual defect, left for Jesse:** the header table's field label still reads **"Job & PO #"**.
The other two "Job" instances are internal (`Job digits`, and `Job USA26041` inside Verified facts)
and do not appear as customer-facing headings, but that label does. Changing it is a deliverable
format decision, not a fix to make unasked.

**Note the real filename is `HU5A`, with a digit five, not `HUSA`.** Scribe flagged it unprompted
when the instruction used the wrong one.

### Second build, branded and corrected. TESTED 2026-09-07.

Four defects found by inspecting the first `.docx` were written into the Project Report skill, the
skill was **updated in place — still one skill, id `project-report`, no duplicate** — and the report
was rebuilt. All four verified off-platform on the 51 kB result:

**The real logo is embedded.** `word/media/image1.png` is **6,280 bytes, exactly the size of
`assets/brand/usadebusk-logo.png`**, and `word/header1.xml` carries a genuine `<a:blip>` image
reference. Nothing was reconstructed. **The asset was already in the clone and therefore already on
the Bot's machine** — the logo was never an upload problem, only a missing instruction. No connector
and no file transfer was involved.

**`[logo]` placeholder: gone (0 occurrences).** **`Job & PO #`: gone (0).** **`Project & PO #`:
present.** **The body no longer narrates its own running header** — the first build wrote a correct
`header1.xml` *and* opened the document with a paragraph describing that same header, which is the
structural duplication the skill's verbosity rule exists to catch.

"Job" now appears **once**, down from three, and the remaining instance is inside the closing
*Verified facts* block rather than in the report body.

**One open question, not a defect:** the four closing sections (Verified facts, Assumptions, Actions
completed, Unresolved questions) are a Bot-to-Jesse reporting convention, and they are currently
**inside the customer-facing document**. Whether they should ship, move to a separate note, or be
stripped at hand-off is Jesse's call on deliverable scope, not something to decide from here.

**What this settles.** Grok Bot produces a branded, customer-shaped `.docx` end to end, on its own
machine, with no plugin, no connector and no credential. That is the first capability in this trial
that is genuinely self-contained.

### Third build — pagination and scope. TESTED 2026-09-07.

**The rendered pages caught what the XML check could not**, which is the lesson worth keeping: a
document can pass every structural assertion and still paginate badly, and only a render shows it.

**Pagination had a precise, mechanical cause.** The build carried `cantSplit` on 40 rows and
`keepLines` on 84 paragraphs but **zero `tblHeader` and zero `keepNext`** — rows held together while
headings did not. "Project Details" sat alone at the foot of page 1, "Unresolved questions" alone at
the foot of page 4, and a table crossing a page opened with unlabelled columns. Both properties are
now specified in the skill and the rebuild reports **`tblHeader` 9, `keepNext` 17, `cantSplit` 40**.

**`JOB NO.` was still a printed column header, and a case-sensitive grep missed it.** A session
reported "Job" as down to one occurrence on the strength of `grep Job`; the page-1 table header is
uppercase `JOB NO.`. It is now `PROJECT NO.` and the skill says explicitly that a case-sensitive
check will not find it. **Check labels case-insensitively.**

**Build apparatus no longer ships inside the deliverable. Ruled by Jesse 2026-09-07.** Roughly two of
five pages were scaffolding: the hand-tally notice, "not built in this draft" sections, `Pigs Used —
not built`, the "Conscious checks" block, `[Awaiting Jesse …]` callouts, and the four closing
sections. All of it moves to **the chat reply**, which keeps the one-file rule intact and loses
nothing — Jesse reads it either way. **The four-section reporting rule is not weakened, it is
relocated** out of the customer's file.

A corollary the skill now states: **a section that could not be built is simply absent** from the
document rather than given a heading announcing its own emptiness. That is
never-document-absent-scope applied to the Bot's own output.

**Verified on the 48 kB result:** all apparatus strings absent (hand-tally, not built, Conscious
checks, Awaiting Jesse, and all four closing headings at zero), `PROJECT NO.` present, `JOB NO.`
absent, `Project & PO #` present, logo still embedded. Body prose fell from 11,147 characters to
4,101 while **all 9 tables and every figure survived** — the cut was scaffolding, not content.

### Parity test — Grok Bot matches Claude Code once it has the palette. TESTED 2026-09-07.

**The blue table headers were a missing input, not a capability ceiling.** The build spec defers
fonts, colours and fills to `usadebusk-core` Brand Standards and deliberately does not restate the
values. Grok Bot does not hold `usadebusk-core` and **cannot read `~/.claude/skills/` at all**, so
Scribe followed a spec pointing at a document it cannot see and python-docx fell back to its stock
style, which is blue. Measured: **zero hex values existed anywhere in the ported skills**, while
`job-report.md` said "amber" five times. Scribe was told amber and never told what amber is.

**Fixed by porting the values** into a new `skills/brand-standards.md`, labelled as a mirror with
`usadebusk-core` named as authority, plus a pointer added inside `usadebusk-core` itself so a future
brand change cannot leave Grok Bot silently stale.

**The test was clean because both sides run python-docx 1.2.0** — the Bot's venv and Jesse's
machine. Same library, same version, same content (Claude Code re-rendered Grok Bot's own v3 output
rather than re-authoring), so the only variable was what each builder was told.

**The styling layers came out identical, not merely close:**

| | Grok Bot | Claude Code |
|---|---|---|
| Fills | `F7F7F7` ×31, `222222` ×28 | `F7F7F7` ×31, `222222` ×28 |
| Colours | `555555` ×88, `FFFFFF` ×28, `FCC30A` ×9, `222222` ×4 | identical |
| Fonts | Arial only | Arial only |
| `tblHeader` / tables / logo | 9 / 9 / 1 | 9 / 9 / 1 |
| `keepNext` | **17** | 11 |

The only divergence is that **Grok Bot applied `keepNext` more liberally than the Claude Code build
did**, and its output fits 2 pages against 3. On this document it is not behind; on pagination it is
marginally ahead.

**What this settles, and what it does not.** Grok Bot can produce a branded, customer-shaped `.docx`
at Claude Code's standard, on its own machine, with no plugin, connector or credential. **The value
is not document quality — Claude Code already had that. The value is that Grok Bot runs on Jesse's
iPhone and Claude Code does not.** A report generated from a plant parking lot without opening a
laptop is the capability; parity was only the precondition, and it now holds.

**Untested, and the honest next step:** a *different facility*. USA26041 has now built the skill and
tested it four times, so a fifth pass measures memory rather than capability.

### Field/Value column widths — fixed on both paths. TESTED 2026-09-07.

Jesse flagged the Field column as far too wide on Customer Details, Project Details, Crew Details
and the per-heater data table, garbling the Value column into extra lines. Neither builder set
widths, so python-docx split every table 50/50 — fine for the four-column tables, wrong for every
Field/Value pair. **Project Details has a 9-character longest label against values up to 191
characters.**

**The rule** — size the label column to its own longest label, `0.10 × characters + 0.45` inches,
clamped 1.4in to 2.2in, remainder to Value on a 6.9in text width. It lives in
`04-knowledge/job-report-generator-build-spec.md` because it is layout rather than brand and governs
both render paths, and is mirrored into the Grok Bot skill because Scribe reads skills, not the spec.

⚠ **The trap: widths must go into `w:tblGrid`.** A first Claude Code attempt set `cell.width` only
and **the rendered output did not move at all** — LibreOffice ignores it and Word honours it
inconsistently. Set `tblLayout` to `fixed` and write each `w:gridCol`'s `w:w` in twips.

**Both builders landed on identical widths independently:** 1.85 / 1.40 / 2.20 / 2.20 in. Scribe
reported its own clamping unprompted — Project Details clamped *up* from 1.35, Crew Details and
Heater Data clamped *down* from their 24- and 31-character labels. Project Details values fell from
three or four lines to one or two.

**Still open, not raised by Jesse:** there are blank gaps after the first Project-tables table and
after the KPI band on both builds. His standing rule is no blank gaps, so this is a real residual —
recorded rather than fixed, because it was not what he asked for.

### Uniform first column, and the Stand-By reorder. TESTED 2026-09-07.

**The per-table sizing rule above was wrong and lasted about an hour.** It fixed the garbled Value
column and created a worse problem: nine tables starting at nine different offsets — 1.38 / 1.73 /
1.85 / 2.20 / 2.30in — so the left edge was ragged down every page. Jesse spotted it by looking.
**Optimising each table in isolation is the mistake**, and both the build spec and the skill now say
so explicitly so it is not reintroduced.

**Replaced by a uniform 2.00in first column on all nine tables.** The value is derived, not chosen:
the longest first-column string in the document is `Total footage (looped pig path)`, measured at
**1.80in in 9.5pt Arial**; with Word's 0.16in default cell padding that needs 1.96in, so **2.00in is
the smallest value at which nothing wraps.** Remaining 4.90in splits evenly among the other columns.

**Stand-By Summary reordered to `DATES | HOURS | CAUSE`** at 2.00 / 0.70 / 4.20. Dates and hours are
short and fixed-width, so leading with them lands DATES on the same left edge as everything else and
takes CAUSE from 2.30in to 4.20in — an 83% gain for the only column holding prose, which carries
strings up to 83 characters. Causes now fit on one line instead of three.

⚠ **The reorder introduced an artifact worth knowing: the TOTAL row read `blank | 11 | TOTAL`**,
label stranded to the right of its own figure, because TOTAL had lived in the CAUSE column. A total
row must label itself from the left, so TOTAL moves to DATES. Caught in the Claude Code build and
fixed in both before Scribe ever saw it.

**Both builds verified identical again:** all nine first columns at exactly 2.00in, Stand-By at
2.00 / 0.70 / 4.20, TOTAL row reading `TOTAL | 11 | —`. Scribe enumerated all nine widths back
unprompted rather than asserting success.

**The accepted cost, Jesse's call:** the two Project tables and the KPI band hold short
first-column values, so 2.00in there gives up about 0.25in that `SCOPE` — the longest cell in the
document — would otherwise use. A straight edge was worth more than the space.

## The phone continuity drill — PASSED. TESTED 2026-09-07.

**Grok Bot is the backup of *capability*, not of data.** `obsidian-work` is on GitHub, so the vault's
bytes survive Linda2 regardless — but **Claude Code does not travel and does not survive the
desktop.** Without it the vault is an archive Jesse can read on a phone and produce nothing from.
Grok Bot is the only thing left that still builds a document, extracts a receipt, or answers with a
citation. A session argued the backup case was already solved by GitHub and **Jesse corrected it:
"If the desktop goes down and you with it, then what good is Github? If I need something created, it
can't create it. Grok Bot can."** He is right, and it reframes the trial from convenience to
**business continuity** — a materially stronger renewal argument, and one that reads as hindsight if
written after the renewal decision instead of before it.

**The capability chain genuinely survives Linda2:** the venv under `/workspace`, the skills stored in
Grok Bot itself, the brand assets in the clone. The clone refresh is the one thing fired from Linda2,
and it **fails safe** — no pushes means no changes, so it freezes current rather than breaking.

⚠ **The one dependency that does not survive is skill authoring and repair.** Every fix on
2026-09-07 ran Linda2 → vault → upload → Scribe. With Linda2 gone the Bots stay usable but a wrong
skill cannot be corrected and a missing one cannot be added. **A standby system is provisioned
before the failure, not repaired during it** — load and verify what you want on the road before you
leave.

**What was actually tested.** A service receipt run through **Ledger entirely from the iPhone app**,
Linda2 not involved. The input was **an image snapshot of a PDF** — not the text-layer PDF attached
as a file, and not a photograph of physical paper. **Jesse reports the extraction succeeded.**

That second half is the substantive result: Ledger's earlier proven runs were three receipt *PDFs*
where it read the text layer and reported converting pages when handwriting defeated it. **An image
bypasses that path entirely**, so vision extraction on mobile is now established.

**Not proven, and not to be claimed:**

- **Capture from physical paper under field conditions** — angle, glare, curl, shadow. A snapshot of
  a PDF on a screen is flat, evenly lit and square; a ticket on a truck bonnet is not, and that is
  the condition that actually applies in a unit.
- **Getting the finished file off the phone** — download, then attach to an email. Not reported and
  not observed. **A breakdown he can see but cannot send is not a deliverable.**
- **Chief of Staff routing from the phone.** The no-file test — *"desktop is down, who handles a
  photographed receipt?"* — was not run.

**The iPhone app takes photos, files and photo-library attachments** (Jesse, reading the feature).

### The drill's second finding: tables are unreadable on the phone

The desktop hid this. In the reply Jesse screenshotted, the header `Actual hrs (receipts)` wrapped to
**four lines**, the cell `16 (10782: 6 + 10783: 10)` wrapped to four, and `Underrun 8` wrapped to
two. **He reports it as chronic across every LLM he uses, and in Obsidian as well** — so it is a
standing rule, not a correction to one Bot.

**It is the same rule that took the report's first column from 2.00in to 1.40in the same day:** the
parenthetical qualifier is what destroys the layout. Headers are one word; a cell holds a value,
never a sentence and never a parenthetical; signed numbers rather than words. Provenance moves to one
line beneath the table, where wrapping is harmless and nothing is lost.

Recorded in `README-FOR-BOTS.md` — every Bot reads it, so one edit reaches all seven, where six
profile pastes would drift the moment one was missed. The vault-wide half is in
`01-context/output-preferences.md`, because Claude Code does the same thing to Obsidian tables.

⚠ **The screenshot's figures are unreconciled and must not be cited.** It shows **Rig-Out 8** and a
total of **37**; this session's verified USA26041 report has **Rig-Out 14** and operating hours
**43**. The reply calls itself a "cold-pass extract," so it may be a deliberate subset rather than a
conflict — **ask Jesse which before either number is used anywhere.** The table-shape finding stands
on its own and does not depend on the figures being right.

---

# 4. What's left

**The roster is built. Nothing has touched live work.** Seven Bots, six skills, a group and a
working push trigger, and not one real bid has gone through any of it. That is the whole remaining
question.

**Run one closed bid end to end through the Bid Desk.** A bid that is already quoted and settled, so
the output can be checked against what was actually sent rather than judged on whether it reads
well. Intake produces the checklist, Estimator the duration model and work-up, Scribe the document.
[[BACKTEST-SPECIMEN]] is the standard: six rules reproduced DSP26085 to the hour and to the line
when worked by hand, so the Bots have a number to hit.

**Give Scout one real competitor pass** on public material — Quest Integrity first, since the vault
names them as a competitor with their own decoking division *and* they sit on USADebusk jobs as the
smart-pig vendor.

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
