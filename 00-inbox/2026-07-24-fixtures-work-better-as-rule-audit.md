---
type: note
status: inbox
created: 2026-07-24
tags: [inbox, regression, methodology, skills, insight]
---

# The regression fixtures work better as a rule audit than as a drift detector

The Opus 5 battery was built to answer "did the new model break anything." It answered no. The
more useful result was accidental: **four of the six fixtures exposed a defect in the thing they
were being measured against, not in the model.**

- **F4** — the dropped RFWN definition looked like a miss. It was a defect in the vault's SOP
  formatting standard, which listed a conditional flange-type term as always-included. Standard
  amended.
- **F3** — the *old baseline* carried "no overrun flag" on a ticket that booked 1.0 standby hour
  against 0 quoted. The skill already required flagging past 90% of quoted. The baseline had been
  frozen in violation of a live rule.
- **F1** — the whole suite had been reading the 100 ft/hr benchmark as heater-total when the
  skill's own build-up method said per-coil. On a 4-pass job that is a third of the pigging hours
  and ~20% of the quote.
- **F6** — caught a precedence defect in wording introduced *the same morning* by the F1 fixes:
  a job-stated travel rate was being overridden by the baseline table.

Why this happens: a fixture forces a rule to be *executed* rather than read. Rules that are
merely implicit, internally inconsistent, or contradicted by a real actual survive any number of
readings and fail the moment something has to produce a number from them.

**Worth considering.** The battery is currently framed and scheduled as a model-transition
artifact — it runs when a new model lands. That is the wrong trigger for its most valuable
output. A fixture replay is also the cheapest available audit of whether a *skill edit* actually
works, and this session proved it twice: F6 validated the F1 duration rewrite in one run, and
caught the one thing that rewrite got wrong. Candidate: replay the one or two fixtures that load
a skill after any substantive edit to it, not only on model change.

Not proposing a build — no new tooling is needed, the fixtures and the protocol already exist.
The change would be to the trigger, and it is Jesse's call whether that is worth the run cost.

Related: [[idea-fallback-regression-battery]]. Full record in `~/.claude/regression/runs/claude-opus-5/REPLAY-CHECKLIST.md`.
