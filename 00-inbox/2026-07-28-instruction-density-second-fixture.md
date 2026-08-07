<!-- vault-loop: operational — skill-instruction-density regression follow-up, Lane 4 (usadebusk-* skill-drift scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
<!-- vault-prestaged: 2026-08-07-prestaged-f4-instruction-density-second-fixture.md -->
---
type: note
status: open
created: 2026-07-28
tags: [regression, skills, open-item]
---

# Instruction-density finding needs a second fixture (F4)

The F5 instruction-density arm test ran 2026-07-28 — full writeup at
`~/.claude/regression/f5-instruction-density-arm-test-2026-07-28.md`. It tested the claim
(from Boris Cherny's Opus 5 launch talk) that corrective scaffolding in a prompt is now a
net negative and should be deleted.

**Result.** Arm B (core only, equipment withheld) **failed** — no rounding rule, no
6.250"/6.500" finals, no 1/8" increment, no pig types. The domain skill is load-bearing.
Arm C (equipment with corrective instructions stripped, 16% smaller, all data and rules
retained) **matched the incumbent on every binding numeric and every diff key**, and
produced more judgment-call flags than the incumbent, not fewer.

**Why it is not actionable yet.** n=1 per arm, one fixture. Arm C's single error
(misidentifying the convection as Sch 80) came from a gap in core's dimension table rather
than the ablation — since fixed — but it is direct evidence that one run carries enough
variance to produce a wrong card value. One clean result does not license trimming ~165 KB
across nine skills.

**Next step.** Run the same three arms on **F4 (SOP)**. It is the other Track A fixture,
loads a different skill (`usadebusk-sop`), produces a different output shape, and has a
non-numeric pass bar. If a corrective strip is also neutral there, the finding starts to
carry enough weight to justify a trim pass on evidence rather than on a conference talk.

**Counter-evidence already on file, worth keeping in view.** The 2026-07-24
`adversarial-review` arm test found performance ranked in *exact inverse* order of
scaffolding density — plain single agent 5.5/6 at 1.00x, grounded single 5/6 at 1.12x,
three-agent chain 3/6 at 3.31x. That points the same direction as the video's claim, but it
varied architecture rather than instruction content, so it is corroborating rather than
duplicative.

Caveat that applies to both: a related caution is already recorded in
`07-llms/prompt-engineering.md` — the corrective instructions worth keeping are the ones
verifying *inputs*, not the ones re-checking *output*. A same-day instance proved it live:
the firewater fix stripped flag framing and took a needed customer-facing rejection clause
with it (see [[2026-07-28-f1-f6-rebaseline-handoff]]).
