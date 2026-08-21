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
rather than one review note per finding. This note deliberately carries **no `## Decision` checkbox block**,
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
| Capture loop | Daily since 08-10; 29 commits | Inbox routing | Inbox grew 21 → 54 while it ran daily | Runs reliably, but the thing it exists to drain has tripled | |
| Idea-research loop | Daily since 08-16; 26 notes | 26 review notes | 14 effect / 6 no-effect / 6 open (54%) | Largest single producer of asks | |
| Pre-staging loop | Daily since 08-13; 17 notes | 17 review notes | 9 / 4 / 4 (53%) | Second largest producer | |
| Agent/review loop | On demand; 10 notes | 10 review notes | 9 / 1 / 0 (**90%**) | Highest-yield loop in the system, and the only one that *clears* rather than generates | |
| Skill-drift loop | 62 d; 3 notes | 3 review notes | 3 / 0 / 0 (**100%**) | Small, cheap, perfect record | |
| Consolidation loop | 31 d; 2 runs ever (07-18, 08-15) | Sweeps | The 08-15 run is what cleared the backlog to zero | Rare but high-impact | |

**Reading.** The two loops that *generate* asks run daily at a ~53% effect rate. The two that *clear* them run
on demand or monthly at 90–100%. The system is tuned backwards. The cheapest single change available is
inverting those cadences — throttle idea-research and pre-staging to weekly, run the review loop on a
schedule instead of on demand.

## Tools

| Component | Refs | Last touched | Evidence | Verdict |
|---|---|---|---|---|
| `vault_lint.py` | 168 | 08-16 | Core gate, 16 rules, wired into hooks | |
| `vault_health.py` | 89 | 08-16 | Core dashboard; but see metric rows below | |
| `vault_index.py` | 43 | 08-18 | Generates INDEX.md, 246 lines | |
| `estimating_rollup.py` | 57 | 07-29 | Output regenerated **15 times** — live | |
| `pig_usage_rollup.py` | 23 | 07-26 | Output `pig-usage-rollup.md` generated **once, 2026-07-26, never again**. 25 days stale and presents as current | |
| `sharepoint_export.py` | 20 | 08-11 | Writes to `_OUTPUTS/sharepoint`, which exists; referenced in commits through 08-20 | |
| `baseline_staleness.py` | 11 | 08-16 | Feeds health; reports 6 of 6 baselines behind — permanently | |
| `config_frontmatter_lint.py` | 4 | 08-16 | Config-repo lint, lowest reference count of the live tools | |
| `audit_commit.py` | 12 | 07-28 | Referenced only from July plan files and one memory — **not wired into any hook or setting** | |
| `audit_worktree.py` | 5 | 07-27 | Same — one-off scripts from the July harness audit, kept as if infrastructure | |
| `tools/fixtures/` | — | — | Contains an `08-systems` fixture directory; that folder does exist (5 notes) but is undocumented in CLAUDE.md | |

**CLAUDE.md documents four tools. There are eleven.**

## Lint rules — 16 total, 3 error / 13 warning

Currently firing: **43 warnings, 0 errors**, in only four classes — `INBOX-AGE` 15, `ORPHAN` 13, `DEAD-LINK`
11, `STATUS-VOCAB` 4. The other twelve rules fire zero times.

| Rule | Now | Ever acted on | Note | Verdict |
|---|---|---|---|---|
| `INBOX-AGE` | 15 | yes | Permanent. Tracks the inbox backlog — a symptom, not a lint problem | |
| `ORPHAN` | 13 | 13 commits | Permanent. Some targets are June concept notes that will never be linked | |
| `DEAD-LINK` | 11 | 7 commits | Permanent. Arguably belongs in the **error** tier — a dead link is a defect, not a preference | |
| `STATUS-VOCAB` | 4 | 6 commits | All four are `status: verified` on heater/ground-truth notes. Either add `verified` to the vocabulary or fix four files. Trivial, and open since July | |
| `SECRET` | 0 | never fired | Keep regardless — cheap insurance, and the one rule whose firing would be catastrophic to miss | |
| Other 11 rules | 0 | all have commit history | Guards that have fired and been cleared. Working as intended | |

**A warning tier that never reaches zero trains you to ignore the report.** 43 standing warnings is the whole
signal value of `vault_lint` warnings being spent on four classes nobody intends to clear.

## Health dashboard metrics

| Metric | Evidence | Verdict |
|---|---|---|
| Open decision rows | Useful. Cap 10 set when the queue was young | |
| Review notes awaiting decision | Permanently FAIL since ~08-10 | |
| Lint errors / warnings | Errors useful; warnings permanently 43 | |
| Inbox items / median / oldest | Oldest permanently FAIL | |
| Days since last commit | Useful | |
| Loop heartbeats | Proves firing, not effect — see structural finding | |
| Pending quotes expired | 0, and has caught real cases | |
| Dormant triggers fired | **0 ever.** 9 rows listed; the 08-15 sweep already ruled triggers a weaker carrier than the queue | |
| **Regression baselines behind** | Reports "**6 of 6**" with status **ok** — a metric with no pass condition, so it can never fail and never informs | |
| Regression baselines unjudgeable | 0 | |

## Conventions and structure

| Component | Evidence | Verdict |
|---|---|---|
| Decision queue | Charter says "the single place every open decision lives." **False today** — 6 open decisions sit in `06-insights/` review notes with no queue row | |
| — DQ-018's source | Lives in **`archive/`**, which CLAUDE.md says not to auto-load. A live decision whose context is unreachable by default | |
| Dormant triggers | 9 rows, 0 fired ever, already ruled a weak carrier | |
| Regression baselines | 6 fixtures, all 6 behind, judged ok | |
| Commercial pipeline | 3 quote rows; caught the DSP26095 stale-note case | |
| `archive/` | 74 notes — as large as `02-facilities/` | |
| `templates/` | 9 templates | |
| `06-insights/` | 63 notes, near-parity with `02-facilities/` (74). Process artifacts approaching the volume of domain content | |
| `INDEX.md` | 246 lines, regenerated | |

## Folder domains

| Folder | Notes | In CLAUDE.md? | Verdict |
|---|---|---|---|
| `02-facilities/` | 74 | yes | |
| `04-knowledge/` | 50 | yes | |
| `06-insights/` | 63 | yes | |
| `00-inbox/` | 54 | yes | |
| `archive/` | 74 | yes (do-not-load) | |
| `07-llms/` | 22 | **no** | |
| `templates/` | 9 | yes | |
| `08-systems/` | 5 | **no** | |
| `09-interests/` | 2 | **no** | |
| `01-context/` | 7 | yes | |
| `50-dashboards/` | 4 | yes | |

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

**Constraints on that run, non-negotiable:** read-only; no new notes; no queue rows; nothing retired; no
verdicts filled in. This audit diagnosed decision capacity as the bottleneck, so a run that returns three
fresh documents makes the verdict session worse, not better.

Model: Opus at normal effort. Fable was considered and rejected — breadth is not the missing input.

## Not audited

The nine skills in the config repo, beyond confirming the skill-drift loop that watches them has a 3-for-3
record. Skill *content* is a separate audit with a different method and should not be half-done here. Also not
audited: hook scripts in `~/.claude/hooks/`, and whether the six loops' scheduling actually matches their
declared cadences in the scheduler rather than in the ledger.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-20 | Evidence pass run at Jesse's request. Read-only against git and the vault; nothing retired, no rulings made, no queue rows added. Corrected my own earlier overstatement that the system rarely clears its output — measured effect rate is 76% of closed notes. | Claude |
