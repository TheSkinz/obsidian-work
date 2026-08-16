<!-- vault-loop: operational — skill-instruction-density regression follow-up, Lane 4 (usadebusk-* skill-drift scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
<!-- vault-prestaged: 2026-08-07-prestaged-f4-instruction-density-second-fixture.md -->
---
type: note
status: resolved
created: 2026-07-28
closed: 2026-08-15
tags: [regression, skills, open-item]
---

# Instruction-density finding needs a second fixture (F4)

> **Closed 2026-08-15** by the retirement sweep — bookkeeping only, no new decision. The next step this note asked for was ruled as DQ-008 and executed the same session: A approved, B and C rejected. F4 replicated F5 on every axis against a structural rather than numeric pass bar — arm B failed (invented the document number, section order and footer), arm C matched arm A on document number, title-block grid, section order, phase structure, footer wording and the 4.250" max pig OD, producing 13 judgment calls to A's 11. The finding is now n=2 across two skills and two pass-bar shapes, and still does not license a trim pass across nine skills. Writeup at `~/.claude/regression/f4-instruction-density-arm-test-2026-08-15.md`.

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
