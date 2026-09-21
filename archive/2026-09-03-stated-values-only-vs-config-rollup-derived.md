---
type: finding
status: resolved
created: 2026-09-03
tags: [inbox, heater-card, schema, vault-ingest, regression, resolved]
---

# Two schema texts contradict: "stated values only" vs Config Rollup "DERIVED FROM TUBE GEOMETRY"

Surfaced by the 2026-09-03 F2 regression replay, which flagged the tension itself, named the artifact that settles it, and marked its own answer as an interpretive call rather than a verified one. That was the right handling. **Nothing has been changed.**

## The contradiction, both sides read

`usadebusk-vault-ingest/SKILL.md:576`, Behavior Rules, no carve-out stated:

> **A heater card carries stated values only — never derived ones, marked or unmarked.** If the source document does not state a field, that field stays blank on the card. This holds even when the value is trivially computable from fields the source *does* state…

`04-knowledge/_canonical-heater-card.md`, the Config Rollup section header comment:

> DERIVED FROM TUBE GEOMETRY — hand-entered (no formula layer), so re-derive on any edit and never invent a value Tube Geometry can't back.

and, on the two mandatory rows:

> "Heater total" — the full installed total, accounting for the actual loop arrangement… Two rows, always both present, not alternatives.

## Why it bites

F2's source (a DSP quote) states per-circuit tube counts and lengths and states 6 circuits. It never states installed totals. Under the ingest behavior rule the two Heater total cells must stay blank; under the exemplar they are mandatory and are exactly the multiplication the section exists to carry.

The run populated them — 60 tubes / 2,280 ft convection, 72 / 2,736 ft radiant — which is what the exemplar requires and what the frozen baseline has always carried. **The exemplar settles it in practice; the ingest skill's wording does not reflect that.**

## Why the distinction is real and not pedantry

The behavior rule's worked case is **wall thickness**, and that case is genuinely different from this one. Wall is a claim about the customer's steel — computing `(OD − ID) ÷ 2` asserts a physical fact about metal nobody measured. A Config Rollup heater total is arithmetic on the card's own stated per-circuit figures and asserts nothing new about the world. The rule is right about wall and overreaches onto the rollup.

## Proposed fix — wording only, no schema change

Add a carve-out sentence to the behavior rule at `usadebusk-vault-ingest:576`, something like:

> The one exception is `## Config Rollup — Estimating Reference`, which the canonical card defines as derived from Tube Geometry and whose two SCALE rows are always both present. Multiplying stated per-circuit figures by a stated circuit count is arithmetic on the card's own data, not a claim about the customer's steel — which is what this rule exists to prevent.

## For Jesse

Confirm the exemplar governs and the ingest wording is what is wrong, rather than the reverse. If the ingest rule is actually right and Heater total should stay blank on a per-circuit-only source, that is a schema change affecting every card built from a quote and is much bigger than a wording fix.

Related: [[2026-09-03-regression-battery-findings]], [[2026-09-03-core-154-looped-max-od-pointer]]

---

## RULED and APPLIED 2026-09-17 (Jesse) — the exemplar governs, the ingest wording was wrong

Confirmed as the note framed it: `04-knowledge/_canonical-heater-card.md` governs, and
`usadebusk-vault-ingest`'s behavior rule was overreaching. The alternative — Heater total stays blank
on a per-circuit-only source — would have been a schema change affecting every card built from a
quote, and was declined.

**Applied** as a second carve-out beside `Max pig OD`, using this note's own reasoning: multiplying
stated per-circuit figures by a stated circuit count is arithmetic on the card's own data and asserts
nothing new about the world, whereas `(OD − ID) ÷ 2` asserts a physical fact about metal nobody
measured. The rule is right about wall and was wrong about the rollup. The skill now reads **"Two
carve-outs, and only two"** rather than "One carve-out, and only one."

**The line number in this note was stale.** It cites `usadebusk-vault-ingest:576`; the rule is at
`:595`. Its sibling note had the same drift (`core:154` against a real `:177`) and had already
recorded the lesson — grep for the rule text, never trust a line number carried in a note.
