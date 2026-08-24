---
type: review
status: open
review_type: architecture-audit
source_authority: observed
confidence: high
created: 2026-08-20
tags: [review, knowledge-system, architecture, audit]
---

# Vault architecture audit — evidence pass

## What this is

Jesse asked (2026-08-20) how much bloat the vault carries and which tools, loops and conventions are worth
continuing. This is the **evidence half**: every component, what it has actually caused, and a recommended
verdict. No decisions are made here and nothing has been retired.

**How to use it.** Overwrite the `Verdict` column. That is the whole interaction — one sitting, one artifact,
rather than one review note per finding.

> **Updated 2026-08-21 — verdicts drafted, then approved and EXECUTED.** Jesse approved the full pass,
> including the Lane 4 items and both missing checks. The `Verdict` cells below are what was recommended;
> what actually happened, including **three corrections where a verdict turned out to be wrong on contact**,
> is in **Execution log — 2026-08-21** at the end. Read that before acting on any cell here: three of them no
> longer describe reality.

This note deliberately carries **no `## Decision` checkbox block**,
because the checkbox mechanism assumes one decision per note and this holds about thirty. That also means it
does not count toward the health dashboard's "review notes awaiting decision" metric. Flagging that openly
rather than quietly enjoying it.

**Method, so it can be re-run.** Audit by *effect*, not by inspection. For each component, find its output in
git and ask what changed downstream because of it. A note's "effect" is measured as: files touched in the
commit that closed the note, excluding `06-insights/`, `50-dashboards/`, `INDEX.md` and `00-inbox/` — i.e.
excluding the system's own bookkeeping. Reading each tool and forming an opinion was rejected as the method,
because I built most of this and would be grading my own work.

---

## Headline: the problem is rate, not worth

The backlog metrics, sampled from `health.md` history:

| Date | Review notes open | Queue rows open | Inbox items | Inbox oldest |
|---|---|---|---|---|
| 2026-07-20 | 0 | 0 | 21 | 2 d |
| 2026-07-27 | 1 | 0 | 43 | 9 d |
| 2026-08-03 | 2 | 1 | 44 | 16 d |
| 2026-08-10 | 6 | 5 | 48 | 23 d |
| 2026-08-15 | 0 | 2 | 56 | 26 d |
| 2026-08-20 | 10 | 10 | 54 | 31 d |

The 2026-08-15 retirement sweep cleared the review pile to **zero** and the queue to **two**. **Five days
later both are at ten.** One clearing session buys five days.

The arithmetic behind that: three loops — capture, idea-research and pre-staging — have each fired on
essentially **every single day** since 2026-08-10, and each produces a note carrying at least one ask. That is
roughly **two new decisions per day**, against a clearing event every two to four weeks. Nothing about any
individual loop is wrong. The generation rate simply exceeds the only clearing resource the system has, which
is Jesse.

Every red row on the dashboard is this one fact wearing different hats: inbox oldest permanently over 30 days,
review notes permanently double their target, queue permanently at cap.

**Correction to an earlier claim I made this session.** I said the vault "generates proposals at a note a day
and clears them at one commit a year," reasoning from there being exactly one `vault-review:` commit in
history. That was wrong — decisions get committed under other prefixes. Measured properly: **50 of 63 review
notes are closed, and 38 of those 50 caused a real change outside the system's own bookkeeping.** A 76%
effect rate. The loops produce genuine value. Do not retire them on a bloat argument; the evidence does not
support one.

## The second structural finding

**Nothing in the system measures effect.** Loop heartbeats prove a loop *fired* and *finished*. The health
dashboard counts rows, notes and ages. No metric anywhere asks whether a component's output ever changed
anything — which is why a component can run flawlessly forever and report green while producing nothing that
lands. Every number in this audit had to be reconstructed from git by hand. That is the gap that let three
separate passes reason downstream of a wrong "RESOLVED" flag on the Syncrude heater card for thirteen months.

---

## Loops

| Component | Cadence (actual) | Output | Effect rate | Evidence | Verdict |
|---|---|---|---|---|---|
| Capture loop | Daily since 08-10; 29 commits | Inbox routing | Inbox grew 21 → 54 while it ran daily | Runs reliably, but the thing it exists to drain has tripled | **Stop.** It is a net producer now — the 08-21 run ingested 1 and harvested 2. Built for the drop-files-and-they-get-filed workflow retired 2026-07-28 |
| Idea-research loop | Daily since 08-16; 26 notes | 26 review notes | 14 effect / 6 no-effect / 6 open (54%) | Largest single producer of asks | **Stop.** Reads `01-context/` in 1 of 85 loop runs, so it proposes without knowing active jobs — the likely cause of the 46% miss rate. Seeds keep accruing; research one on demand when it matters. Monthly if you want it kept |
| Pre-staging loop | Daily since 08-13; 17 notes | 17 review notes | 9 / 4 / 4 (53%) | Second largest producer | **Stop.** Same shape, same context blindness, same rate. Monthly if kept |
| Agent/review loop | On demand; 10 notes | 10 review notes | 9 / 1 / 0 (**90%**) | Highest-yield loop in the system, and the only one that *clears* rather than generates | **Keep, and schedule it monthly.** The one cadence inversion worth making — it is the only loop that reduces the backlog |
| Skill-drift loop | 62 d; 3 notes | 3 review notes | 3 / 0 / 0 (**100%**) | Small, cheap, perfect record | **Keep unchanged.** Defect-triggered — commits only when it finds drift, so it costs nothing when there is nothing to say |
| Consolidation loop | 31 d; 2 runs ever (07-18, 08-15) | Sweeps | The 08-15 run is what cleared the backlog to zero | Rare but high-impact | **Keep monthly.** The only thing that has ever cleared the review pile to zero |

**Reading.** The two loops that *generate* asks run daily at a ~53% effect rate. The two that *clear* them run
on demand or monthly at 90–100%. The system is tuned backwards. The cheapest single change available is
inverting those cadences — throttle idea-research and pre-staging to weekly, run the review loop on a
schedule instead of on demand.

## Tools

| Component | Refs | Last touched | Evidence | Verdict |
|---|---|---|---|---|
| `vault_lint.py` | 168 | 08-16 | Core gate, 16 rules, wired into hooks | **Keep.** Defect-triggered and the vault's only hard gate. Opened by 18 of 80 attended sessions — the most-read script here. Change the rule tiers, not the tool |
| `vault_health.py` | 89 | 08-16 | Core dashboard; but see metric rows below | **Keep.** `health.md` is the single most-read note in the vault (30 of 80 attended, 84 of 85 loop runs). This is the surfacing mechanism you rely on because you don't track triggers. Trim its metric set, keep the tool |
| `vault_index.py` | 43 | 08-18 | Generates INDEX.md, 246 lines | **Keep.** Cheap, and it shrinks once `archive/` goes. Its value is as a grep surface rather than a read — INDEX.md was opened directly in 1 attended session |
| `estimating_rollup.py` | 57 | 07-29 | Output regenerated **15 times** — live | **Keep.** Feeds estimating, which is business work rather than system work. Opened by 5 attended sessions |
| `pig_usage_rollup.py` | 23 | 07-26 | Output `pig-usage-rollup.md` generated **once, 2026-07-26, never again**. 25 days stale and presents as current | **Delete the output; keep the script unwired.** The stale-artifact-presenting-as-current class the silence audit names. Pig data has a live future use (the per-project pig load list), so regenerate on demand rather than leaving a fossil in place |
| `sharepoint_export.py` | 20 | 08-11 | Writes to `_OUTPUTS/sharepoint`, which exists; referenced in commits through 08-20 | **Keep.** Live and customer-adjacent. Note its `--check` was green throughout the 2026-08-11 incident while the library held the wrong file — DQ-016 is the fix and is still open |
| `baseline_staleness.py` | 11 | 08-16 | Feeds health; reports 6 of 6 baselines behind — permanently | **Keep the script, drop its dashboard row.** Run `--verbose` on demand at replay time. See the metrics table |
| `config_frontmatter_lint.py` | 4 | 08-16 | Config-repo lint, lowest reference count of the live tools | **Keep.** Low refs because it is defect-triggered. Its glob was widened 2026-08-16 after the blind spot that let a scheduled loop's unparseable frontmatter through |
| `audit_commit.py` | 12 | 07-28 | Referenced only from July plan files and one memory — **not wired into any hook or setting** | **Delete.** One-off from the July harness audit, wired to nothing since |
| `audit_worktree.py` | 5 | 07-27 | Same — one-off scripts from the July harness audit, kept as if infrastructure | **Delete.** Same |
| `tools/fixtures/` | — | — | Contains an `08-systems` fixture directory; that folder does exist (5 notes) but is undocumented in CLAUDE.md | **Keep.** It is the lint self-test corpus and the reason the 16-rule check is trustworthy. Fix the CLAUDE.md gap instead — see Folder domains |

**CLAUDE.md documents four tools. There are eleven.**

## Lint rules — 16 total, 3 error / 13 warning

Currently firing: **43 warnings, 0 errors**, in only four classes — `INBOX-AGE` 15, `ORPHAN` 13, `DEAD-LINK`
11, `STATUS-VOCAB` 4. The other twelve rules fire zero times.

| Rule | Now | Ever acted on | Note | Verdict |
|---|---|---|---|---|
| `INBOX-AGE` | 15 | yes | Permanent. Tracks the inbox backlog — a symptom, not a lint problem | **Retire the rule.** `health.md` already reports inbox age. A lint warning clearable only by a decision session is not a lint finding, and this is 15 of the 43 |
| `ORPHAN` | 13 | 13 commits | Permanent. Some targets are June concept notes that will never be linked | **Keep, exempt terminal-status notes.** The rule has earned its place 13 times, but a closed or superseded note nobody intends to link should not keep flagging |
| `DEAD-LINK` | 11 | 7 commits | Permanent. Arguably belongs in the **error** tier — a dead link is a defect, not a preference | **Promote to error.** Already narrowed 2026-08-16 to stop flagging prose about wikilinks, so the 11 standing are real. One session clears them and the gate holds after |
| `STATUS-VOCAB` | 4 | 6 commits | All four are `status: verified` on heater/ground-truth notes. Either add `verified` to the vocabulary or fix four files. Trivial, and open since July | **Add `verified` to the vocabulary.** It is a status the vault genuinely uses on ground-truth notes. Open since July for want of a one-line ruling |
| `SECRET` | 0 | never fired | Keep regardless — cheap insurance, and the one rule whose firing would be catastrophic to miss | **Keep.** Zero firings is the success condition, not evidence of waste |
| Other 11 rules | 0 | all have commit history | Guards that have fired and been cleared. Working as intended | **Keep all.** Defect-triggered, silent when clean, all with commit history proving they fire |

**A warning tier that never reaches zero trains you to ignore the report.** 43 standing warnings is the whole
signal value of `vault_lint` warnings being spent on four classes nobody intends to clear.

**Net effect if the four verdicts above are adopted:** retiring `INBOX-AGE` removes 15, adding `verified` to
the vocabulary removes 4, and promoting `DEAD-LINK` moves 11 out of warnings into the error gate that must be
cleared to zero. Warnings drop from 43 to roughly 13, all `ORPHAN`, and fall further once terminal notes are
exempted. The warning tier becomes readable again for the first time since July.

## Health dashboard metrics

| Metric | Evidence | Verdict |
|---|---|---|
| Open decision rows | Useful. Cap 10 set when the queue was young | **Keep, cap unchanged.** The cap's real function — pausing generating loops when jammed — mostly disappears if those loops stop, but the row stays the honest count of what you owe |
| Review notes awaiting decision | Permanently FAIL since ~08-10 | **Keep.** It is not broken; it is correctly reporting a real backlog, and it reconciled exactly this run (12 open notes − 2 without a Decision block = 10). It should go green on its own once generation stops |
| Lint errors / warnings | Errors useful; warnings permanently 43 | **Keep both, after the rule changes.** Warnings become meaningful again at ~13; errors gain the 11 promoted dead links and must clear |
| Inbox items / median / oldest | Oldest permanently FAIL | **Keep, fix the counting.** `inbox_stats()` counts files rather than notes and picks up a stray `.html` source artifact — 56 reported against 55 notes. The oldest-item FAIL is the same backlog fact and should also self-clear |
| Days since last commit | Useful | **Keep.** Cheap and honest |
| Loop heartbeats | Proves firing, not effect — see structural finding | **Keep, for the surviving loops only.** Drops from 5 rows to 3 (review, consolidation, skill-drift). With three defect-triggered loops, "it fired and finished" is the right claim to make |
| Pending quotes expired | 0, and has caught real cases | **Keep — the highest-value row on this dashboard.** The only metric tied to live commercial exposure rather than to system hygiene |
| Dormant triggers fired | **0 ever.** 9 rows listed; the 08-15 sweep already ruled triggers a weaker carrier than the queue | **Retire the metric and the section.** Zero firings across 9 rows in two months. Promote the three machine-checkable conditions to their own health rows (`rfq-intake` 11/12, routine rows 5/10, note count 315/450) and drop the six event-shaped ones — "check at the next M365 session" is a note to a reader who never arrives |
| **Regression baselines behind** | Reports "**6 of 6**" with status **ok** — a metric with no pass condition, so it can never fail and never informs | **Retire the row.** A metric that cannot fail is decoration. Keep `baseline_staleness.py --verbose` for on-demand use at replay time |
| Regression baselines unjudgeable | 0 | **Keep.** This is the real gate — a baseline nobody can check is exactly the state the tool exists to end |

## Conventions and structure

| Component | Evidence | Verdict |
|---|---|---|
| Decision queue | Charter says "the single place every open decision lives." **False today** — 6 open decisions sit in `06-insights/` review notes with no queue row | **Keep, and make the charter true.** The mechanism is right, the set is incomplete. Either add the 6 orphaned decisions as rows, or add a health row counting open review notes with no queue row — defect-triggered, silent when clean, and it would have caught this |
| — DQ-018's source | Lives in **`archive/`**, which CLAUDE.md says not to auto-load. A live decision whose context is unreachable by default | **Fix before anything else touches `archive/`.** Either rule DQ-018 and close it, or move its source note back into `06-insights/`. This one blocks the `archive/` deletion below |
| Dormant triggers | 9 rows, 0 fired ever, already ruled a weak carrier | **Retire.** Two months, nine rows, zero firings, and the 08-15 sweep already reached this conclusion once. The three machine-checkable conditions become health rows; the rest lapse |
| Regression baselines | 6 fixtures, all 6 behind, judged ok | **Keep the fixtures, drop the "behind" reporting.** Replay on demand. `unjudgeable` stays as the gate |
| Commercial pipeline | 3 quote rows; caught the DSP26095 stale-note case | **Keep.** With retrieval, this is one of only two functions here pointed at money rather than at the system itself |
| `archive/` | 74 notes — as large as `02-facilities/` | **Delete the folder.** 3 of 74 notes opened across all 165 sessions; 71 have never been read by anyone. Git history preserves every one. True deletion is Lane 4, so this needs your explicit yes — and DQ-018 must be resolved first |
| `templates/` | 9 templates | **Keep, trim to what is used.** 5 of 9 ever opened. `_idea-seed-template.md` is the 4th most-read note in attended sessions (17), and stays relevant even if the idea loop stops — you will still capture seeds by hand |
| `06-insights/` | 63 notes, near-parity with `02-facilities/` (74). Process artifacts approaching the volume of domain content | **Keep unchanged — the volume flag is answered.** The usage audit found matching *demand* parity: 26 attended sessions opened `06-insights/` against 28 for `02-facilities/`. Equal volume at equal readership is not bloat |
| `INDEX.md` | 246 lines, regenerated | **Keep.** Cheap, leaned on by CLAUDE.md, and it shrinks substantially once `archive/` is gone |

## Folder domains

| Folder | Notes | In CLAUDE.md? | Verdict |
|---|---|---|---|
| `02-facilities/` | 74 | yes | **Keep, stop chasing precision on dormant cards.** 28 attended sessions, but 13 cards have never been opened by anyone. The 2026-07-06 facility-data note already says this; the usage data is the first evidence for it |
| `04-knowledge/` | 50 | yes | **Keep.** 40 attended sessions. Retire the loop specs belonging to any loop that stops |
| `06-insights/` | 63 | yes | **Keep.** Demand parity with `02-facilities/` settles the volume question — see Conventions |
| `00-inbox/` | 54 | yes | **Keep.** It should begin draining on its own once the capture loop stops adding to it faster than you clear it |
| `archive/` | 74 | yes (do-not-load) | **Delete** — see Conventions. Resolve DQ-018 first |
| `07-llms/` | 22 | **no** | **Keep, and document it in CLAUDE.md.** 17 attended sessions — more read demand than `08-systems`, `09-interests` and `archive/` combined |
| `templates/` | 9 | yes | **Keep, trim to 5** — see Conventions |
| `08-systems/` | 5 | **no** | **Keep, and document it in CLAUDE.md.** Only 3 attended sessions, but it holds the Outlook architecture record — low frequency, high stakes when wrong, as 2026-08-11 showed |
| `09-interests/` | 2 | **no** | **Keep, and document it in CLAUDE.md.** 2 notes, 0 attended reads, no cost. CLAUDE.md already says to expect non-USADebusk domains; this is that |
| `01-context/` | 7 | yes | **Keep, and fix the startup protocol — the highest-value action in this audit.** Read in 43% of attended sessions and 1 of 85 loop runs, against a CLAUDE.md instruction to read it every session. Four of its seven notes are top-ten attended reads |
| `50-dashboards/` | 4 | yes | **Keep.** The most-read folder in the vault. Whatever else changes, this is the part that works |

## Usage finding — added 2026-08-20, from the session list

The tables above measure what each component **produces**. They do not measure what Jesse **uses**, and that
is the gap. A note read every session is valuable even if it never causes a commit; this audit's method
systematically undervalues anything that informs without changing a file. `01-context/` is the clearest
example — seven notes loaded every session, almost no commits, and probably the most valuable folder here.

First cut at demand, from the 40 most recent sessions (2026-08-13 → 08-21):

| Session type | Count | Note |
|---|---|---|
| Loops running unattended | 22 | 7 prestaging, 7 capture, 7 idea-research, 1 consolidation |
| Jesse working **on the system** | 11 | output style ×2, retirement sweep, work inventory, review-queue, health FAIL, lint fixture README, rig-diagram gate, job-report generator gaps, Claude Code updates, title mismatch |
| Jesse working **on USADebusk** | 7 | Baytown F-501 job report, F-501 change order, F-501 smart pig, Steady Flux inspection audit, change-order template, DQ-022 on DSP26085, Grok build ideas |

**61% of the sessions Jesse actually sat in were system maintenance, not business work.** That is the sharpest
number in this audit and it belongs in front of every verdict below.

## Audits not yet run — the next session's brief

Three, all read-only, all appending **to this note** rather than creating new ones. Estimated well under 90
minutes total.

1. **Usage audit, properly.** Extend the table above: which notes and folders are actually read in sessions,
   via `search_session_transcripts`. Measures demand where the rest of this note measures supply. **Run this
   before retiring anything** — the effect-based method above cannot see consumption.
2. **Silence audit.** What has the system *failed* to catch. Sample corrections in git history and ask, for
   each, which rule/loop/gate should have caught it and did not. This session alone supplied three: the
   13-month per-pass geometry error that three review passes walked past, the decision queue's charter being
   false, and DQ-018's source living in `archive/`. This is the only audit that finds **missing** components
   rather than surplus ones.
3. **Retrieval eval re-run.** Ten questions with pass criteria in
   [[knowledge-system-evaluation-questions]], baseline at [[2026-07-23-retrieval-eval-run]]. Cheap and
   comparative. Note KS-002's pass criterion — "does not infer heater facts from jobs alone" — is precisely
   the failure mode of the Syncrude geometry error, so probe that question rather than accepting a pass.

   **This eval is self-graded, which is its main failure mode.** An agent that answers the ten questions and
   then marks its own answers will pass itself, and a "10/10" result is worse than no result because it
   manufactures confidence. Grade adversarially: for each question, try to *fail* the answer before passing
   it — name the specific note each claim came from, check that note still says what the answer claims, and
   treat "I know this from context" as a fail rather than a pass, because the eval measures **retrieval**,
   not recall. Record the July baseline's result alongside each so the comparison is visible.

**Constraints on that run, non-negotiable:** read-only; no new notes; no queue rows; nothing retired; no
verdicts filled in. This audit diagnosed decision capacity as the bottleneck, so a run that returns three
fresh documents makes the verdict session worse, not better.

Model: Opus at normal effort. Fable was considered and rejected — breadth is not the missing input.

## Not audited

The nine skills in the config repo, beyond confirming the skill-drift loop that watches them has a 3-for-3
record. Skill *content* is a separate audit with a different method and should not be half-done here. Also not
audited: hook scripts in `~/.claude/hooks/`, and whether the six loops' scheduling actually matches their
declared cadences in the scheduler rather than in the ledger.

---

# Audit 1 — Usage audit (demand)

**Method.** 165 session transcripts exist on disk for this vault. Each was classified as a loop run or an
attended session by whether its first user turn carries a `<scheduled-task name=` marker: **85 loop, 80
attended**. Demand for a note is then "how many sessions opened it", measured as a tool call carrying a
`file_path` under that path — Read, Edit, Write.

**Two confounds, stated because they change how the numbers read.** First, `search_session_transcripts` and
any plain substring count are worthless here: CLAUDE.md is injected into every session, so 151 of 165
transcripts "mention" `00-inbox/` and 155 mention `02-facilities/` without anyone having opened a file. Every
number below is a file-open, not a mention. Second, a `cat`/`sed` read through Bash carries no `file_path`
and is invisible to this channel. Measured on `01-context/` specifically, the Bash channel adds 7 attended
sessions on top of 27, so **treat every attended count below as a floor, roughly 20–25% low.**

## Folder demand

| Folder | Notes on disk | Sessions that opened a file (of 165) | Loop (85) | Attended (80) |
|---|---|---|---|---|
| `50-dashboards/` | 4 | 117 | 84 | 33 |
| `00-inbox/` | 55 | 116 | 70 | 46 |
| `04-knowledge/` | 50 | 114 | 74 | 40 |
| `06-insights/` | 64 | 64 | 38 | 26 |
| `02-facilities/` | 74 | 36 | 8 | 28 |
| `tools/` | — | 36 | 11 | 25 |
| `templates/` | 9 | 33 | 13 | 20 |
| `07-llms/` | 22 | 31 | 14 | 17 |
| `01-context/` | 7 | 28 | 1 | 27 |
| `08-systems/` | 5 | 7 | 4 | 3 |
| `archive/` | 74 | 4 | 1 | 3 |
| `09-interests/` | 2 | 2 | 2 | 0 |

## Most-read individual notes, attended sessions only (of 80)

| Note | Sessions |
|---|---|
| `50-dashboards/health.md` | 30 |
| `change-log.md` | 28 |
| `tools/vault_lint.py` | 18 |
| `templates/_idea-seed-template.md` | 17 |
| `01-context/active-jobs.md` | 13 |
| `tools/vault_health.py` | 12 |
| `01-context/estimating-approach.md` | 11 |
| `50-dashboards/decision-queue.md` | 10 |
| `07-llms/claude/code.md` | 10 |
| `01-context/company-context.md` | 10 |

## Coverage — supply with no demand

| Folder | On disk | Ever opened by any session | Never opened |
|---|---|---|---|
| `02-facilities/` | 74 | 65 | 13 |
| `06-insights/` | 64 | 58 | 7 (all 2026-06-26 → 07-05) |
| `04-knowledge/` | 50 | 51 (incl. since-moved files) | 2 |
| `archive/` | 74 | 3 | **71** |
| `09-interests/` | 2 | 2 | 0 attended |

The 13 never-opened heater and facility notes are Flint Hills Corpus Christi (4), Marathon Carson (3),
Formosa Point Comfort (2), PBF Toledo (2), Westlake H-101, and ExxonMobil F-201.

## Findings

**The session-startup protocol is not being executed.** CLAUDE.md says to read every file in `01-context/`
before responding. Counting both channels, 34 of 80 attended sessions did — 43%. For loop sessions it is
**1 of 85.** The three loops generating roughly two asks a day are running without the context that holds
Jesse's active jobs, output preferences and estimating approach. This is the single most consequential
finding of the three audits, and it is invisible to every existing metric because nothing measures whether an
instruction was followed.

**The audit's own claim about `01-context/` was wrong and is corrected here.** The usage-finding section
above asserts "seven notes loaded every session." They are not. What is true is narrower and still supports
the same conclusion: all seven are read by somebody, they occupy four of the top ten attended-read slots, and
they generate almost no commits — so the effect-based method does undervalue them. The demand is real; the
"every session" was an assumption, not a measurement.

**The two files CLAUDE.md exempts are exactly the two least-read files in the folder.** `active-jobs` 13,
`estimating-approach` 11, `company-context` 10, `output-preferences` 8, `equipment-fleet` 7, then
`system-workflow-reference` 3 and `workflow-map` 2. The exemption was written on judgment and the usage data
independently confirms it.

**`archive/` is 74 notes — 21% of the vault's markdown — with 3 files ever opened across 165 sessions.**
It is already excluded from auto-load, so this costs disk and `INDEX.md` lines, not context. The one place it
bites is that DQ-018's source note lives there (verified: `archive/2026-08-15-retirement-sweep-what-else-has-outlived-its-reason.md`).

**The dashboard is doing its job.** `50-dashboards/` is the most-read folder in the vault, `health.md` the
most-read single note in attended sessions, and 84 of 85 loop runs open it. Whatever else changes, the
surfacing mechanism is the part that is actually load-bearing.

**Process artifacts and domain content have near-identical read demand.** `06-insights/` was opened by 26
attended sessions against `02-facilities/`'s 28, at 64 notes against 74. The volume parity the audit flagged
above is matched by demand parity — which is an argument against reading the parity as bloat.

---

# Audit 2 — Silence audit (what the system failed to catch)

**Method.** Correction-shaped commits were pulled from all 493 commits in history and a sample read in full.
For each, the question is not "was it fixed" but "which existing rule, loop, gate or metric should have
caught it, and why didn't it."

| Miss | Stood for | Should have caught it | Why it didn't |
|---|---|---|---|
| Syncrude 7-1F-1: one pass recorded as the whole heater; `~6 ft/hr` derived from it | 13 months, marked **Verified**, survived 3 review passes | Nothing. The schema demands both scales; no check compares them | See below — the check is cheap and did not exist |
| Vault's Outlook folder model (9-folder commercial pipeline) was fabricated | 2026-06-29 → 08-11 | Nothing. No component compares a vault claim to the external system it describes | Every gate reconciles vault-to-vault |
| Outlook categories fabricated a second time, hours after the folders were caught | same evening | The rule was already written (`tenant-reality-first`) and had just fired | A written rule is not a gate |
| DSP26085: canonical store held a superseded quotation for a live bid | ~1 month | `presend_gate.py`, `backtest_workup.py` | Both reconcile files **within** CANON. A run in that window would have compared two superseded files and said SEND |
| `manual/` §7.1/7.2/8.2/11.3 had USADebusk installing and removing launchers/receivers | months | Nothing. `usadebusk-estimating` had it right the whole time | No component cross-checks the manual against the skills |
| `config_frontmatter_lint.py` reported 9 of 9 skills clean while a scheduled loop's SKILL.md would not parse | until an external tool (`agnix`) walked the whole tree | The tool itself | A checker's blind spot is its glob, and a clean report from a narrow glob reads identically to a clean tree |
| `lint-report.md` claimed 34 warnings against an actual 52 | 2 weeks | Nothing. No freshness gate on generated artifacts | Same class as `pig-usage-rollup.md`, 25 days stale and presenting as current |
| POINTER-DEAD source pointers dead after folder moves | recurring, ~3 instances/4 weeks | The rule exists and fires | At `warning` tier, buried in 43 standing warnings. Two sat 9 days (DQ-019) |
| Obsidian resolved a Syncrude `[[_facility]]` to PBF Toledo | one session | Nothing automated | Caught by reading every changed line — discipline, not tooling |
| Decision queue charter "the single place every open decision lives" is false | since at least 08-16 | Nothing checks queue-to-review-note coverage | The dashboard counts rows; it never asks whether the set is complete |
| DQ-018's live source note sits in `archive/`, which CLAUDE.md says not to auto-load | since 08-16 | Nothing checks that a live queue row's context is reachable | — |
| Six domain errors in the generated rig diagram (frac tank in the loop, pumper out-scaling the heater, reversed return flow) | until Jesse looked at the render | Nothing can | Domain semantics in derived output is not machine-checkable |

**Verified count on the queue-charter miss.** `06-insights/` currently holds 12 notes at `status: open`. Ten
carry a `## Decision` block; five have a queue row. **Six open decisions have a Decision block and no queue
row** — independently reproducing the audit's earlier claim. (The twelfth is this note, which declares its own
exemption; the eleventh is the Syncrude note. Both lack a Decision block, which is also the exact
reconciliation of `health.md`'s "Review notes awaiting decision: 10" against 12 open notes — the metric is
correct.)

## The Syncrude miss reproduces, and the missing check is arithmetic

`_canonical-heater-card.md` requires the Config Rollup to carry both a `Per circuit` and a `Heater total`
row for every section — "this row is the estimating multiplication base." That means the invariant
`Heater total ÷ Per circuit = an integer circuit count, identical across sections` is machine-checkable on
every card that fills the table. Run read-only against the vault as it stands: **41 cards carry the section,
26 fill it numerically, and all 26 satisfy the invariant** once single-pass sections (F-501 Treat Gas, F-901
Superheat Steam — both already annotated as such in their Notes column) are exempted.

Run against the Syncrude card as it stood before the 2026-08-20 fix, it fails:

| Scale | Section | Total Tubes | Ratio |
|---|---|---|---|
| Per circuit | Convection | 2 | 16 ÷ 2 = 8 ✓ |
| Per circuit | Radiant | **~4** | 31 ÷ 4 = 7.75 ✗ |

The card recorded the radiant per-circuit count as the literal string `~4` and its Notes column invented a
physical explanation for the residue — "uneven — some coils 4, some 3 tubes" — a heater asymmetry that the
2026-08-20 pass confirmed does not exist. The same row is annotated "**Verified** ... resolves the earlier
per-circuit-vs-total ambiguity." The system asked itself this exact question on 2026-07-23, answered it
backwards, and stamped it verified. **A review gate was not what was missing. A check was.**

## The classes

Five shapes account for every miss above. Nothing reconciles a vault claim against the external system it
describes, and every gate that exists compares vault-to-vault or canon-to-canon. Generated artifacts drift
silently because no metric asks when an output was last regenerated against its input. A checker's scope is
its blind spot, and a narrow-glob clean report is indistinguishable from a clean tree. Nothing checks the
system's own structural invariants — queue completeness, source reachability, rollup arithmetic — because
every current metric counts rows rather than testing relationships. And domain semantics in derived output is
not machine-checkable at all, which is a fact to design around rather than a gap to close.

**The system has closed silences before.** CHECKBOX-DELTA was built specifically because a stray Obsidian
click recorded a decision the vault never made and WORD-DELTA reported only losses. The bid-folder soft signal
exists because DSP26095's note read "not yet priced" while its folder held a finished quotation.
`baseline_staleness.py` exists for the same reason. The silence-closing mechanism works. What is absent is
any routine that goes looking — every one of those three was built after a human tripped over the miss.

---

# Audit 3 — Retrieval eval re-run

**Grading.** Adversarial, per the brief. Each question was answered by retrieving from the vault this
session; then, before accepting a pass, the specific note was reopened and checked that it still says what
the answer claims. Anything answerable from loaded context rather than retrieval was treated as a fail.
Cross-references inside retrieved notes were followed and verified rather than assumed.

| ID | July 2026-07-23 | This run | Source verified this session | Adversarial note |
|---|---|---|---|---|
| KS-001 | pass | pass | `knowledge-system-governance.md:20-33` — 6-rank table, "create a contradiction note instead of blending" | Latent: the contradiction rule at line 33 carries no carve-out marker, but lines 62 and 72 exempt all of `02-facilities/`. A retrieval that reads only the section the question names gets a rule that is wrong for the vault's largest folder |
| KS-002 | pass | pass — **but the criterion cannot fail** | `_canonical-heater-card.md:18-19, 28` schema authority; `:74-76` "atomic facts only, per-circuit never totals"; CLAUDE.md Schema authority | See below |
| KS-003 | pass | pass | `sops/sop-formatting-standard.md:3` Authority line; CLAUDE.md "one canonical home"; `usadebusk-sop` SKILL.md:111 defers to it | Cleanest result in the set — three independent sources agree and none has drifted |
| KS-004 | pass (scan) | pass (scan) | 55 inbox notes read directly: 19 `inbox` / 12 `open` / 8 `researched` / 7 `closed-unactioned` / 5 `unexplored` / 4 `gated`; every file carries a status | July's stated revisit condition has now been met — see below |
| KS-005 | pass | pass | `health.md` + `decision-queue.md` + `status`/`review_after` frontmatter | Reconciles exactly: 12 open notes − 2 without a Decision block = the dashboard's 10 |
| USA-001 | pass | pass | `usadebusk-core` SKILL.md:10 service naming; :66, :68 Trimax lock, `dual-pumper` banned, `TriMax` dead string | Resolves to the config repo, not the vault |
| USA-002 | pass | pass | `concepts/industry-foundation.md:56-60` pH ≥10.0, 1–2 ft/s, chloride ≤250/≤500 ppm; `_canonical-heater-card.md:38-46` conditional block, omit entirely on carbon steel | Followed the exemplar's cross-reference to `210-1403A` — the card exists and really is stainless. Reference is live |
| USA-003 | pass | pass | `_canonical-heater-card.md:176-178` "Status only — never facts"; `usadebusk-core`:119 pumping-unit type is not a card field | — |
| USA-004 | pass | pass | `usadebusk-sop` SKILL.md:188-203, 12-item list; :255 never generate until confirmed | All five items the criterion names are on the list — metallurgy (#8) and water source (#9) both flagged "Never assume" |
| USA-005 | pass (deep) | **criterion stale** | `knowledge-system-governance.md:72` facility-data note | See below |

**Headline: 9 clean passes and one stale criterion — but the raw score is the least useful thing here.**

## USA-005's pass criterion now encodes a rule the vault reversed

The question asks how a completed job report should feed back into facility and heater knowledge. Its pass
criterion, written 2026-06-26, reads "Proposes reviewable updates instead of directly rewriting canonical
notes." Since the 2026-07-06 facility-data ruling, that is the **wrong** answer for the destination the
question names: heater-card and facility content is Lane 1 in full, "including correcting existing facts and
resolving discrepancies between sources ... No contradiction note, no confidence-tier/verified-gate
ceremony."

An agent that answers this question correctly today fails the written criterion, and an agent that answers it
by the pre-July rule passes. In July this was graded "pass (deep)" precisely because retrieval found the
carve-out — and that run recorded the risk as a *stale lead paragraph* in the governance note. **That half
got fixed:** line 18 now carries the exclusion inline and in bold. The eval's own criterion was never updated
and still holds the superseded rule. The note's `review_after: 2026-09-26` means nothing would have surfaced
this until late September.

The eval set is not exempt from the drift it was built to detect. This is the finding a self-graded run
cannot produce, because the grader and the criterion agree.

## KS-002 passes on a criterion too weak to catch the failure it guards

The brief flagged KS-002's criterion — "does not infer heater facts from jobs alone" — as precisely the
Syncrude failure mode, and asked that it be probed rather than accepted.

Probed, and the answer is that **the schema was right and the criterion is irrelevant to what went wrong.**
`_canonical-heater-card.md:74-76` says "ATOMIC FACTS ONLY. Per-circuit measurements, never totals/sums," and
the Config Rollup requires both scales stated separately. The Syncrude error did not infer heater facts from
jobs. It read a drawing correctly and mis-assigned its *scale* — a per-pass title block recorded into the
heater-total row — then divided down to manufacture a per-circuit figure. Every downstream number inherited
it, including the actuals rollup.

KS-002 as written cannot fail on that case, and neither can any of the other nine questions. The eval tests
whether the right note is found; nothing in it tests whether the retrieved value is internally coherent. The
arithmetic check in Audit 2 catches it in one pass. This is the gap the brief suspected, confirmed and
located: not a retrieval failure, a missing validation.

## July's two latent risks, revisited

The stale lead paragraph on `knowledge-system-governance` is **closed** — the Lane-1 exclusion is now in the
opening Operating Principle, so a retrieval that stops there no longer gets the pre-July rule.

KS-004's "scan, not lookup" is **still open, and July's own revisit condition has now been met.** That run
recorded it as "fine at this size ... if inbox volume grows, a generated inbox-by-status view would convert
this from a scan to a lookup." The folder was 26 files then and is 55 now. The scan still works, and every
file carries a status field, so nothing is broken — but the condition July set for reconsidering has passed.

## Incidental, from running the eval

`health.md` reports 56 inbox items against 55 notes. `inbox_stats()` in `vault_health.py` counts every
non-dotfile under `00-inbox/` recursively, skipping only `preserved-dsps/`, so the extra is
`f501-coil-teardown-source.html` — a source artifact, not a note. The metric counts files, not notes. It is
one item and it is not wrong so much as differently defined, but the same counting rule feeds INBOX-AGE.

---

# Verdict pass — what this adds up to

Drafted 2026-08-21 at Jesse's request. **Recommendations, not rulings. Nothing has been executed.**

## The shape

Of 54 rows, **41 are keep, 9 are stop or delete, and 4 are keep-but-change.** This is not a bloat problem
with a bloat answer. Almost everything here works; what is mistuned is *when* things speak.

The organising distinction is **defect-triggered versus schedule-triggered.** Lint rules, the pre-send gate,
the commercial-pipeline row, the skill-drift loop and every check the silence audit says is missing all stay
silent unless something is actually wrong — and they run at 90–100% effect. The daily loops speak on a timer
whether or not there is anything to say, and run at ~53%. Every red row on the dashboard traces back to that
imbalance, and the whole verdict set is one move: stop the timers, keep the checks.

## What actually stops

| | |
|---|---|
| Stop | Capture loop, idea-research loop, pre-staging loop |
| Schedule | Agent/review loop → monthly (the one inversion) |
| Delete | `archive/` (74 notes, 71 never read), `audit_commit.py`, `audit_worktree.py`, `pig-usage-rollup.md` |
| Retire | `INBOX-AGE` lint rule, dormant-triggers section, "regression baselines behind" metric |

Everything else is kept. Retrieval, the dashboards, `01-context/`, the lint gate, the commercial pipeline,
the estimating rollup, the heater cards and the eval all stay.

## Sequence

`Resolve DQ-018` → `stop the three loops` → `clear the promoted DEAD-LINK errors` → `delete archive/` →
`regenerate INDEX.md + health.md` → `update CLAUDE.md`.

DQ-018 is genuinely first: its source note lives in `archive/`, so deleting the folder before ruling on it
destroys the context for a live decision.

## Two things no verdict above covers

**The missing checks.** The silence audit found that the components that would have caught the real misses do
not exist, and both are defect-triggered — silent unless something is wrong, so they cost nothing per day and
add zero asks. The heater-card rollup invariant (`Heater total ÷ Per circuit` must be an identical integer
across sections) is roughly 40 lines, passes on all 26 cards that fill the table today, and fails on the
pre-fix Syncrude card. The queue-completeness check (open review notes carrying a Decision block but no queue
row) is smaller still and currently finds 6. Neither is on any table above because the audit inventoried what
exists, not what is absent. **Building these is the one addition worth making, and it is the opposite of the
work being retired.**

**The CLAUDE.md documentation gap.** Three folders (`07-llms/`, `08-systems/`, `09-interests/`) are
undocumented, and CLAUDE.md names four tools where eleven exist. One editing pass, no decision required.

## What this does not resolve

Whether the vault is worth its remaining cost at all. The audit's sharpest number — 61% of attended sessions
being system maintenance — should fall sharply if the three loops stop, because they are the direct source of
roughly two asks a day. That is the prediction. **Re-measure it in a month rather than assuming it.** If
system sessions are still the majority with the generators off, the problem is structural rather than
rate-based, and the answer is a smaller vault rather than a slower one.

---

# Execution log — 2026-08-21

Jesse approved the whole verdict pass, Lane 4 items and both missing checks included. What follows is what
was actually done, and where a verdict did not survive contact.

## Executed as recommended

| Area | Done |
|---|---|
| Loops | Capture, idea-research and pre-staging **disabled** in the scheduler — disabled, not deleted, so restoring one is a single `enabled: true` plus its row back in `LOOP_HEARTBEATS`. Review loop **created on a monthly schedule** (`vault-review-loop`, 04:00 on the 8th), reversing its "deliberately not scheduled" rule. Consolidation and skill-drift untouched |
| Lint | `DEAD-LINK` → error and all 11 cleared; `INBOX-AGE` retired; `ORPHAN` exempts terminal-status notes; `verified` added to the vocabulary. **43 warnings → 5, 0 errors.** Self-test 16 rules |
| New check 1 | `ROLLUP-SCALE` lint rule with fixture — see below, the first version was wrong |
| New check 2 | `Open decisions not in the queue` health row. **Found 8 on its first run** and names them: the 6 the audit found by hand plus 2 the idea loop added that morning before it was disabled |
| Health metrics | `Dormant triggers fired` retired, section narrowed to `Threshold gauges` rendering only the 3 machine-checkable conditions; `Regression baselines behind` retired; inbox counting fixed to notes-only (56 → 55); stopped loops removed from the heartbeat registry |
| Deletions | `tools/audit_commit.py`, `tools/audit_worktree.py`, and 17 spent `archive/` notes |
| Docs | CLAUDE.md now documents all eleven tools and the three undocumented folders; `system-workflow-reference.md` and `vault-agent-loop-spec.md` rewritten so they no longer describe a six-loop system |

## Three verdicts that were wrong

**`archive/` could not be deleted wholesale, and the read-demand argument was the wrong test.** The verdict
graded it on reads — 3 of 74 opened across 165 sessions — and never checked inbound links. **40 of the 74 are
wikilinked from live notes**, including the H-2421 and H-2501 heater cards, `change-log.md`,
`decision-queue.md` and two `04-knowledge/` build specs. Deleting the folder would have converted ~40 live
citations into dead links, which are now *errors*. Scope narrowed to unreferenced notes only.

**"Git history preserves every one" is false, and this is the one that could have lost data.** `archive/` is
in `.gitignore`. Of the 34 unreferenced notes, only 17 are tracked; the other 17 — the pre-canonical
heater-card snapshots plus an `ai-config` snapshot — exist **on disk and nowhere else**. They were left in
place. They cost nothing to keep: gitignored content carries no repo weight and `INDEX.md` has never covered
`archive/`, so the stated cost of that verdict was largely imaginary in the first place. **Recorded in
CLAUDE.md** so no future session repeats the assumption.

**The pig rollup was regenerated, not deleted.** It has 5 live inbound references, so deleting it would have
created dead links. Regenerating removes the actual defect — it was stamped 2026-07-26 and presenting as
current. Worth noting it was not merely date-stale: **41 lines changed on regeneration.**

## The new lint rule failed its first honest test

The `ROLLUP-SCALE` ratio check — heater total ÷ per circuit must be the same whole number in every section —
fires on a clean reconstruction of the Syncrude defect. Replayed against the **real** 2026-07-23 card via
git, it caught nothing.

The reason is the whole lesson. The radiant per-circuit cell read `~4`, not `4`. A hedged number is not
arithmetic, so that row dropped out of the comparison and the surviving convection ratio of 8 read as clean.
The residue had already been hidden inside the approximation before any checker saw it — and the card's Notes
column had invented an uneven 3-vs-4-tube coil split to explain the approximation, a physical asymmetry that
does not exist.

So the rule gained a second branch, and it is the load-bearing one: **an approximate count anywhere in Config
Rollup is a finding on its own.** That table is derived and hand-entered — the exemplar says never invent a
value Tube Geometry cannot back — so `~4` is by definition invented. The fixture now carries `~4` verbatim,
with the earlier clean-`4` mistake written into the fixture body so it is not quietly reintroduced. The rule
now fires on the real card and stays silent across all 41 live cards.

This is the audit's own finding turned on itself: a check verified against a fixture you wrote is a check
verified against your own assumption.

## State now

`0 errors, 5 warnings` (was 0 / 43). `archive/` 74 → 57 on disk. Two dashboard rows still FAIL and should:
12 review notes awaiting decision, and the 8 open decisions outside the queue. Both clear as Jesse rules,
and neither is now being added to by anything on a timer.

**The prediction to re-measure in a month:** 61% of attended sessions were system maintenance. If that has
not fallen sharply with the generators off, the problem is structural rather than rate-based, and the answer
is a smaller vault rather than a slower one.

---

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-20 | Evidence pass run at Jesse's request. Read-only against git and the vault; nothing retired, no rulings made, no queue rows added. Corrected my own earlier overstatement that the system rarely clears its output — measured effect rate is 76% of closed notes. | Claude |
| 2026-08-20 | All three briefed audits run and appended above. Read-only against git, the vault, the config repo and 165 session transcripts; no new notes, no queue rows, nothing retired, no verdicts filled in. Corrected this note's own unmeasured claim that `01-context/` is "loaded every session" — it is 43% of attended sessions and 1 of 85 loop runs. | Claude |
