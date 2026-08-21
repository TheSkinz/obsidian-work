<!-- vault-loop: operational — leverage-repo execution owed; capture loop cannot run the experiment. -->
<!-- vault-prestaged: skipped — already covered by DQ-004 / [[2026-07-30-prestaged-portfolio-revival-still-worth-doing]], decision already closed 2026-08-01, this note only tracks owed unexecuted work -->

---
type: note
status: closed-unactioned
created: 2026-08-01
closed: 2026-08-15
tags: [inbox, leverage-repo, deferred, retired]
---

# Owed — thesis experiment v2 re-run — RETIRED 2026-08-15

> **RETIRED, NOT RUN** (Jesse, 2026-08-15). The re-run cannot produce a discriminating result on this corpus, and that is provable from data already in hand rather than from anything the run would return. Reasoning below; everything under the rule is the original note, kept as written.
>
> **The pre-registered verdict is already determined.** `DESIGN.md` records v1 at A 0.795 / B 0.962 / C 0.962, and the audit found **100% of failures across all three conditions** were the unit artifact. v2 rescoring only converts failures to passes, so A rises toward ~1.0 and B rises from 0.962 or holds. The frozen thresholds call it **inconclusive** when B pass@1 is within 10pp of A — and B at 0.962 is within 10pp of *any* value A can take, since the ceiling is only 3.8pp above it. There is no arithmetic path to a validating or falsifying result. The run would spend ~450 calls to return "items too easy," which the design already prescribes the remedy for.
>
> **Secondary: the frontier arm tests a routing choice no longer made.** Condition A names `claude-fable-5`. Current routing is Opus 5 for nearly everything, with Fable reserved for maximal long-horizon runs — structured field extraction is the opposite shape. Swapping it is not a flag change: `DESIGN.md:3-4` freezes the thresholds and requires a new version of the file with a stated reason.
>
> **What this closes.** The thing that actually needed resolving was the non-citable v1 headline sitting on record. A ruling retires it as cleanly as a measurement would: *the v1 result was a scoring artifact, v2 rescoring cannot discriminate on this corpus, and the experiment is retired pending a harder item set.* The v1 numbers remain non-citable — that does not change.
>
> **If the thesis is ever wanted for real**, the work is not a re-run. It is building items hard enough that a cheap model does not already score 96% on them, which the pre-registration itself names as the remedy. That is a fresh build to be decided on its own merits, not a commitment inherited from July.

---

# Owed — thesis experiment v2 re-run

Approved by Jesse 2026-08-01 under DQ-004
([[2026-07-30-prestaged-portfolio-revival-still-worth-doing]], option B). Approved
as a decision, not yet executed — this note is the only thing carrying it.

**The work:** run `run.py` against the existing 30-item corpus in
`C:\Users\Jwuts\leverage\experiments\thesis` under the corrected v2 scoring rule
(numeric-core + hyphen/space equivalence), already committed at `6febf55`. Then
record what the result says about the infrastructure bet.

**Why it can't be skipped or judged from the existing data.** The first full run's
headline — frontier scores far below cheap models — was traced to a scoring
artifact, 100% of it: natural-language units on otherwise-correct values.
`DESIGN.md:112-132` states that result "should not be cited as a conclusion under
this design." So there is no v2 verdict to interpret; the owed work is the run
itself. The real answer may be that the frontier model does not trail at all.

**Explicitly dropped at the same ruling** (do not revive as part of this): the
Knowledge Loop OS C/D/F re-verification, and routing pass output as decision-queue
rows. Both were bookkeeping with no forcing function. This note owes one thing.

Supersedes [[2026-07-22-deferred-portfolio-revival-full-pass]], which is closed by
the same ruling.

Cost is non-trivial (frontier-model calls across 30 items), so this wants a
deliberate session, not a spare-moment run.

**Runbook: [[2026-08-15-thesis-v2-rerun-handover]]** — exact commands, the
dry-run/smoke/full sequence, conditions, call volume, the frozen pre-registered
thresholds to judge against, and what to record afterwards. Built 2026-08-15 by
reading the repo rather than from recall.
