<!-- vault-loop: operational — leverage-repo execution owed; capture loop cannot run the experiment. -->
<!-- vault-prestaged: skipped — already covered by DQ-004 / [[2026-07-30-prestaged-portfolio-revival-still-worth-doing]], decision already closed 2026-08-01, this note only tracks owed unexecuted work -->

---
type: note
status: inbox
created: 2026-08-01
tags: [inbox, leverage-repo, deferred, approved-unexecuted]
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
