---
type: finding
status: open
created: 2026-09-03
tags: [inbox, regression, skills, pig-sizing, needs-ruling]
---

# Proposal — make core's looped max-pig-OD pointer imperative

**Jesse ruled the direction on 2026-09-03: sharpen the pointer.** This note carries the exact wording for approval before anything is edited into `usadebusk-core`. Nothing has been changed yet.

## What happened

The 2026-09-03 F2 regression replay passed nine of its ten diff keys and missed key 10: state that the looped-circuit oversized-final-pig exception was neither applied nor ruled out. The fixture heater, H-77 at P66 Borger, is six circuits looped at the radiant outlet flanges. The run computed Max pig OD correctly (4.026" + 0.250" = 4.276", rounded down to 4.250"), recorded the card's configuration as `Looped-at-Radiant-outlet-flanges`, and never connected the two.

## Why it is a real miss and not a bad key

`usadebusk-core/SKILL.md:173` — which F2 does load — already says:

> **Line reference corrected 2026-09-03.** This note was written citing `:154`; the pointer text
> actually sits at **`:173`**, under `### Connection info (facts)`. The drift was caught before
> the edit was made, which is the only reason it matters — a stale anchor is how the wrong line
> gets patched. Grep for `Max pig OD` rather than trusting any line number in this note.

> Max pig OD (governing tube ID + 0.250″, computed from the smallest ID across all sections/segments; the sizing rule and its looped-circuit oversized-final exception are canonical in `usadebusk-equipment`)

So the run had the pointer in front of it. The exception itself lives in `usadebusk-equipment/SKILL.md:96-98` (`6.065" ID → 6.250" standard final; 6.500" max (heavy fouling or looped circuits)`), and F2 does not load that skill. **This is the only place in the skill set where two skills hand off a computed heater-card field**, which is why the pointer is doing real work rather than being a courtesy cross-reference.

## Proposed change — one sentence, procedural only

Amend the parenthetical at `usadebusk-core:154` so the pointer binds:

> …the sizing rule and its looped-circuit oversized-final exception are canonical in `usadebusk-equipment`. **When the card's configuration is looped and `usadebusk-equipment` is not loaded, record that the oversized-final exception was neither applied nor ruled out — do not present the computed figure as settled.**

**This can only ever add a caveat sentence. It cannot move a number.** That is the whole reason it is proposable out of a replay session at all: the standing rule from the 25–40% parallel-allowance failure is that a replay may show a rule is missing or ambiguous but may not settle what a domain rule should be. A procedural instruction to state what was not checked settles nothing about pig sizing.

## Consequence if approved

F2 is re-run against the amended core, judged, and re-cut. Until then F2 stays `behind` in `baseline_staleness.py`, which is correct — the README sequence is replay → judge → patch → re-run → re-cut, and skipping to a re-cut on a failed key would launder the miss into the baseline.

## Open question for Jesse

Only one, and it is the wording above, not the direction. Does the caveat belong in `usadebusk-core` (where the field and the pointer already live, catching every skill that computes this field) or in `usadebusk-vault-ingest` (where the failing behaviour occurred, but catching only ingest)? Core is the wider net and the recommendation; ingest is the narrower, more surgical option.

Related: [[2026-09-03-regression-battery-findings]]
