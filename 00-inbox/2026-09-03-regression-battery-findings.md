---
type: note
status: complete
created: 2026-09-03
tags: [inbox, regression, skills, session-record]
---

# Regression battery, 2026-09-03 — what ran and what it found

Index note for the session that cleared the replay debt owed since 2026-09-02. Full plan and judging record at `~/.claude/plans/plan-mode-plan-the-flickering-lightning.md`; runs at `~/.claude/regression/runs/claude-opus-5/f{1,2,4,6}-replay-2026-09-03.md`.

## Result

Four fixtures replayed blind, all four passing their surviving diff keys. Three re-cut.

| Fixture | Keys | Verdict | Effect |
|---|---|---|---|
| F6 | 11 of 11 surviving | pass | duration 48 → 40 hrs; **re-cut** |
| F1 | 9 of 9 surviving | pass | duration 48 → 37 hrs, total $61,595.60 → $50,492.60; **re-cut** |
| F4 | 7 of 7 + new key 8 | pass | struck port-naming and role-boundary content corrected; **re-cut** |
| F2 | 9 of 10 | **missed key 10** | not re-cut — awaiting a core patch, then a re-run |

F3 and F5 were **judged not to need a replay**, with evidence: `references/extraction-format.md` (what F3 executes) is untouched since its baseline and 21 of its 25 `behind` commits are the job-report generator it never invokes; F5's only equipment commit is the port-naming and looped-end correction, and F5's frozen output already stated the corrected position independently.

## Why three baselines were wrong

Two rules struck on 2026-08-23 — the 25–40% parallel-friction allowance and the whole-shift landing rule — were still encoded as *requirements* in F1's and F6's frozen outputs, so a run following the current skill correctly would have failed. **F4 turned out to be a third and nobody had flagged it**: it carried `Trimax rear CONV port` / `RAD port` in four places against `fc7f8f6`, and wrote the launcher install as USADebusk's own work against `9cddfaf`. It went unseen because all seven of F4's diff keys were structural — none looked at content — which is why a new content key 8 was added at re-cut.

**Standing lesson: when a rule is struck, grep `frozen/` for it the same day.** A frozen output encoding a retired rule does not fail loudly; it silently redefines a regression as the standard.

## Confidence in the re-cuts

The lines that should not have moved did not move, to the cent. F1 reproduced mob $3,648.00 / demob $3,648.00, per diem $1,800.00, crew truck Qty 1, max pig OD 4.250", and the four-term piece-count swing at **$552.00**. F6 reproduced its whole mob/demob build-up line for line. Only rate-driven lines moved, which is what distinguishes a rule change from model drift.

## Rulings made this session

- **Derate gate: only records open it** (Jesse, 2026-09-03). A customer's stated expected condition — *"cleaned 3 years ago, nominal buildup expected"* — is a claim, not a known fouling history. The gate needs prior actuals on that heater, a recorded fouling history, or hard service Jesse has personally seen. This is what puts F1 on the round 100 ft/hr. Recorded in `change-log.md` and in F1's frontmatter as `derate_gate_RULING`, deliberately: the allowance this battery once manufactured carried Jesse's name with no ruling behind it, and this figure does not.
- **F2 key 10: sharpen core's pointer** rather than demote the key — see the linked note for the proposed wording, which is awaiting approval before any edit.

## Open, one note each

- [[2026-09-03-core-154-looped-max-od-pointer]] — the F2 patch, blocking F2's re-run
- [[2026-09-03-fitter-adder-absorbed-at-rig-in-cap]] — ~4 hrs of stated exposure vanishing at the 12-hr cap
- [[2026-09-03-stated-values-only-vs-config-rollup-derived]] — two schema texts contradicting
- [[2026-09-03-nearest-even-rounding-gaps]] — undefined ties, and an unbounded discretionary hatch
- [[2026-09-03-regression-coverage-gaps]] — F2's uncompelled schema fields, no `/report` fixture, and the tool's inability to say "judged, not owed"
- [[2026-09-03-sop-voice-pipefitter-role]] — whether an SOP body is customer-facing, and `9cddfaf` disagreeing with its own worked example

## Protocol change

Blinding now fences the vault's `06-reviews/` as well as `~/.claude/regression/`. The F6 run found `06-reviews/2026-08-08-prestaged-f6-rig-tier-decision.md` — a note naming that fixture and carrying its expected figures — outside the fence as it stood. It handled the contamination correctly and the leak is disclosed in F6's frontmatter rather than hidden, but fixture answers live in the vault and the protocol had not accounted for that.
