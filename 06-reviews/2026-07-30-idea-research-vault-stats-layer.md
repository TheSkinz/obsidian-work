---
type: review
status: resolved
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-30
review_after: 2026-08-30
superseded-by: "DQ-017 (2026-08-15) — Track 1 and Track 2 ride the scheduled bundle session rather than a schema open; `revisit-trigger:` retired"
related:
  - "[[idea-vault-stats-layer]]"
  - "[[idea-pig-actuals-maturation]]"
  - "[[idea-rollup-per-rig-coilset-grain]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, knowledge-system, idea-research, estimating, data-quality]
---

# Idea Research — Vault-Wide Stats Layer

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Five `unexplored` idea-seeds existed at
scan time; `idea-vault-stats-layer` (created 2026-07-26) is the oldest and was processed. The
seed carries no `**Gate:**` line, and its "To explore" section states no gating condition in any
of the usual phrasings ("not until," "the trigger is," "only once") — this is case (b), no gate
stated, proceed to research directly.

## Evidence

**1. The seed already reached its own conclusion, and it checks out against the linter's actual
code.** The seed's closing section ("Finding that arrived after this seed was first written")
argues the five defects it cites — pig OD vs. tube ID, footage arithmetic, a length in a diameter
column, two spellings of one alloy, a rate outlier — are lint-shape rule violations, not
statistics, and belong in `tools/vault_lint.py` rather than a new stats surface. Reading
`tools/vault_lint.py`'s current 17 check functions (`check_operational_frontmatter` through
`check_pointer_dead`) confirms none of them do cross-field numeric or business-rule validation
today — the closest, `check_durations_header`, validates table structure, not value relationships
between columns. The seed's self-correction is accurate: this gap is real and unfilled.

**2. External prior art confirms the fix has an established name and pattern, not just a plausible
guess.** Cross-column business-rule validation — "totals matching, date ordering, referential
integrity declaratively within the schema itself" — is Pandera's specific reason for existing
[Pandera vs. Great Expectations](https://endjin.com/blog/a-look-into-pandera-and-great-expectations-for-data-validation),
distinct from the DataFrame-level type checks simpler tools do. The five defects listed are all
this shape: a value checked against another field's value or a fixed rule, not against a fitted
distribution. This means the seed's proposed direction (rules in `vault_lint.py`) is not a novel
design — it is the standard shape of this class of tool, just implemented in Python functions
instead of a schema DSL, which is consistent with the vault's existing pattern of plain functions
per check.

**3. The "one distribution, one outlier" framing undersells how fragile that framing actually is —
reinforcing that the seed's shift away from statistics was the right call.** Literature on
small-sample outlier detection (Dixon's Q test for n ≤ 25, Chauvenet's criterion, z-score
thresholds that only apply reliably above n ≈ 80) is all built for *some* distribution to compare
against — a single new data point compared to zero prior points, which is what most of this
vault's dimensions have today (Task Durations: 22 rows across 17/32 cards; Pig Specifications:
78 rows across 23/32), has no such distribution to test against. None of the five defects the
seed cites were actually caught this way — all five are exact rule checks (an inequality, an
arithmetic identity, a type mismatch, a string-equality-after-normalization check, a hardcoded
reference rate) that need no distribution at all. This closes the door the seed's earlier framing
had left ajar: descriptive/validation stats here are correctly a synonym for lint rules, not a
separate statistical layer, at current data volume.

**4. Previously uncited, directly relevant prior art: Obsidian's own native Bases plugin is already
enabled in this vault and answers half the seed's "To explore" question at zero build cost.**
`.obsidian/core-plugins.json` shows `"bases": true` — Bases ships as a core Obsidian feature since
v1.9 (mid-2025), needs no install, and provides exactly the "queried on demand rather than
materialized" option the seed's "To explore" section asks about: it turns frontmatter properties
into live, filterable, groupable tables with built-in summary functions (Sum, Average, Min, Max,
Median, Stddev, Count) and a formula layer
([Obsidian Bases formulas](https://obsidian.md/help/formulas),
[Bases roadmap — grouping and summaries](https://forum.obsidian.md/t/bases-roadmap-grouping-group-results-in-bases-and-show-summaries-e-g-sum-average-etc/104339)).
No `.base` file exists anywhere in this vault yet (`find . -iname "*.base"` returns nothing) — the
capability is on and unused.

**5. Bases' one hard limitation lands directly on the seed's own coverage table, and answers its
"which dimensions need new capture" question concretely for at least three rows.** Bases only
reads frontmatter *properties*, not markdown tables or freeform sections inside a note's body.
`_canonical-heater-card.md`'s frontmatter (lines 1–13) exposes `heater-id`, `heater-tag`, `unit`,
`facility`, `client`, `heater-type`, `service`, `configuration` — nothing for multi-ID/single-ID,
smart-pig election, or filtration election, all of which the seed's own coverage baseline places
inside body sections (Job Options, Config Rollup), not frontmatter. Bases could query and
aggregate by facility, client, or heater-type today with zero new work; it could not reproduce the
seed's own "13 multi-ID vs 19 single-ID · smart pigging 14/7/11 · filtration 13/7/11/1" figures
until those flags are promoted to frontmatter — which is itself a Lane 4 schema decision, the same
family as the Pig Specifications `Condition` column parked in
[[idea-pig-actuals-maturation]] and the per-rig-coilset table parked in
[[idea-rollup-per-rig-coilset-grain]].

**6. Row-level table stats (tube geometry per section, pig usage per job) are out of reach for
Bases regardless of frontmatter promotion, and the vault already has the proven answer for that
half.** Tube Geometry and Pig Specifications are row-per-record markdown tables inside note
bodies — the kind of data Dataview's `dataviewjs` escape hatch can parse but native Bases cannot
([Dataview vs. Bases comparison](https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases/)).
The vault does not need Dataview for this, though: `estimating_rollup.py` and
`pig_usage_rollup.py` already are exactly this pattern — a generated rollup script reading table
rows across all cards — proven twice, not hypothetical.

## Interpretation

**Two ideas bundled in one seed, at two different maturities — not one decision.** (a) Validation
rules for the five-defects class: sound, matches an established pattern (point 2), buildable now
with no new architecture decision beyond which specific checks to add, and the seed already
scoped this correctly onto `vault_lint.py` itself. (b) A descriptive/aggregate stats surface:
premature to build as custom tooling, not because the data is too sparse (point 3 shows sparse
data is fine for rule checks) but because the tooling question the seed asks — "spreadsheet,
dashboard, or on-demand query" — already has a zero-cost answer sitting enabled and unused in this
vault's own Obsidian install (point 4), and the real open question underneath it is a frontmatter
promotion / schema decision (point 5), the same shape of decision already parked twice elsewhere
in this vault. This mirrors the 2026-07-28 rollup-per-rig-coilset-grain finding almost exactly:
premature because a Lane 4 capture decision hasn't been made, not because of thin data or unclear
tooling.

## Recommended Action

Split into two independent tracks so one doesn't block the other. **Track 1 (validation rules,
low risk, buildable soon):** fold the five-defects class into `vault_lint.py` as new rule-check
functions (pig OD vs. governing tube ID + tolerance, footage arithmetic, column-type / unit
mismatch, alloy-name normalization, rate-magnitude sanity against sibling rates) — a bounded
addition using an established pattern, best scheduled the next time `vault_lint.py` is opened for
a reason carrying its own weight, per the same convention already used for the two parked schema
items above. **Track 2 (descriptive/aggregate stats surface, hold):** before building anything,
have Jesse try Obsidian's native Bases (already on, zero setup) against the frontmatter fields
already exposed today (facility, client, heater-type) to see whether it satisfies the itch at zero
build cost; separately and only if that's not enough, decide whether to promote multi-ID/
single-ID, smart-pig election, and filtration election to frontmatter properties — bundle that
decision with the other two parked schema changes since all three ride the same "next time the
canonical schema is opened for a reason that earns it" trigger. Row-level stats (tube geometry,
pig usage) need no new tooling decision at all — `estimating_rollup.py` / `pig_usage_rollup.py`
already are the proven pattern for that half, and Bases cannot reach into note-body tables
regardless (point 6).

## Decision

- [ ] ~~Approved — start Track 1 (validation rules into `vault_lint.py`) now~~
- [ ] ~~Approved with edits~~
- [x] **Park both tracks — revisit next time the canonical schema is opened for another reason** (Jesse, 2026-08-01)
- [ ] ~~Drop~~

Neither track is dropped; both wait on the same trigger. That trigger now carries three items —
this note's Track 1 and Track 2, the per-rig-coilset actuals sub-table from
[[2026-07-28-idea-research-rollup-per-rig-coilset-grain]], and the Pig Specifications `Condition`
column from [[2026-07-26-idea-research-pig-actuals-maturation]] — so one schema-open pass clears
all of them rather than three separate reopenings of the same file.

**On whether the trigger already fired:** `tools/vault_lint.py` *was* opened on 2026-08-01, for the
`WIKILINK_RE` escaped-pipe fix. That was a one-line regex correction, which does not meet the
"opened for a reason carrying its own weight" bar the convention names — and it touched the linter,
not the canonical heater-card schema, which is what the other two parked items actually ride.
Recorded here so a future session does not read the lint commit as having fired this trigger.

Track 2 has a zero-cost step available to Jesse independently of the trigger: try Obsidian's native
Bases (already enabled, unused) against the frontmatter fields exposed today — facility, client,
heater-type. If that satisfies the itch, Track 2 collapses to nothing and only the frontmatter-
promotion question remains.

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-01 | **Both tracks parked; `status` → `resolved`, `revisit-trigger:` added** | Claude | No code written. Trigger is event-shaped (a schema open), not machine-checkable — no row count decides it. Bundled with the two schema items already riding the same condition. Source seed `00-inbox/idea-vault-stats-layer.md` closed. |
| 2026-08-21 | **Track 2 unparked and largely answered; Track 1 split out of the bundle** | Jesse (ruling) / Claude (Opus 5) | **Point 4 was right and cheaper than it knew.** Bases was tried against the frontmatter exposed today, exactly as this note recommended, and it satisfies — `50-dashboards/heater-fleet.base` now carries four views (By client · By type · Never verified · Verification log) at zero build cost, no Dataview, no new tooling. **But the try surfaced something this note did not predict: the frontmatter it would query was not clean.** `heater-type` held 11 values across 41 cards where the schema specified 4 (and the schema was itself missing `coker`), and `verified` — a field absent from the exemplar entirely while lint checked its presence — held prose on ten cards. Both migrated and lint-locked the same day (vault `9718b8f`). **The order turned out to be the whole lesson:** built before the migration, the base would have needed nested `if()` chains to collapse `vacuum heater` into `vacuum` and parse a date out of a forty-word sentence, every one to be deleted after. Fix the data, and the view needs no formulas. **Still genuinely open from Track 2:** the frontmatter-promotion half — multi-ID/single-ID, smart-pig election, filtration election — which this note correctly gated behind "only if Bases is not enough." It has not been reached, because Bases *was* enough for the card-level questions. Not closed, just not needed yet. **Track 1 left the bundle entirely** (2026-08-21): five cross-field lint rules with no dependency on the durations schema, now `00-inbox/idea-cross-field-lint-rules.md`, riding `vault_lint.py`'s own trigger. Point 6 stands unchanged and was re-confirmed by building the base — Bases cannot reach note-body tables, so the two rollup scripts remain the answer for row-level data. |
