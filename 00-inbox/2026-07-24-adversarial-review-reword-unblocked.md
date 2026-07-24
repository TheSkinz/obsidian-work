---
type: note
status: inbox
created: 2026-07-24
tags: [inbox, skills, config-repo, loose-end]
---

# adversarial-review + idea-triage reword — hold released, not yet done

Both skills carry self-verification scaffolding ("double-check", re-verify passes) written for a
model that needed prompting to check its own work. The reword was drafted 2026-07-24 and then
**deliberately held** until the Opus 5 regression replays showed concretely how the behaviour
manifests. The battery is now complete, so the hold is released. The edit itself has not been made.

**What the six replays actually showed, which should shape the reword:**

The self-verification is real and unprompted — F1 reconciled its project total two independent
ways, F6 cross-checked its effective ft/hr against a named job, neither was asked to. So
instructions to *re-check finished work* are genuinely redundant and cost extra passes.

But the valuable half is not that. Every run also verified its **premises** — reading the actuals
rollup and the F-802 heater card unprompted, and flagging contradicting actuals rather than
silently overriding them. That behaviour is what caught four defective baselines in this battery.
An instruction to check a claim against its authoritative source before acting on it should be
*kept*, not stripped as redundant scaffolding.

The distinction to encode: drop "verify your output," keep "verify your inputs."

Neither skill is exercised by any fixture, so the edit is safe to make without a replay.
