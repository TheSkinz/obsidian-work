---
type: finding
status: resolved
created: 2026-09-03
tags: [inbox, regression, skills, pig-sizing, resolved]
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

---

## CLOSED 2026-09-17 — already ruled and applied the same day this was written

**This note was answered on 2026-09-03 and nobody closed it.** Config commit `ccc5086`
(2026-09-03 23:54) applied the caveat to `usadebusk-core`, and its message records the same ruling
the note asked for: *"Jesse ruled it into core rather than vault-ingest — core is the wider net,
catching every skill that computes this field rather than only the one where the miss surfaced."*
The imperative is live in the skill under `### Connection info (facts)`, beneath the Max pig OD
pointer.

The question was put to Jesse again on 2026-09-17 and he gave the same answer — **core** — so
nothing changed. That is a wasted ask, and the cause is bookkeeping: the note still read *"Nothing
has been changed yet"* and `status: open` for two weeks after the change landed. Same class as the
review note `2026-09-08-review-loop-spec-references-stopped-loops`, which kept the health
dashboard's *"Review notes awaiting decision: 1"* alive after DQ-032 closed the same day. **A
session that is about to ask for a ruling should grep the target file first** — the answer may
already be in it.

**Consequence that is still open:** F2 has not been re-run against the amended core, so it remains
`behind` in `baseline_staleness.py`. That is correct and is part of the F1/F2/F3/F4/F6 replay debt
Jesse scoped to its own session on 2026-09-02; it is not owed here.

**Worth carrying forward: the line-number drift this note already caught once.** It was written
citing `usadebusk-core:154`; the text was at `:173` by the time the edit was made and is at `:177`
now. The note's own instruction — *grep for `Max pig OD` rather than trusting any line number* — was
right, and the same drift hit its sibling note, which cited `usadebusk-vault-ingest:576` against a
real position of `:595`.
