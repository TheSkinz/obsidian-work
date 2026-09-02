---
type: review
status: resolved
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-26
review_after: 2026-08-26
related:
  - "[[idea-pig-actuals-maturation]]"
  - "[[idea-pig-load-list-generator]]"
  - "[[2026-07-22-idea-research-pig-load-list-generator]]"
  - "[[idea-rollup-per-rig-coilset-grain]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, knowledge-system, idea-research, estimating, pigging]
---

# Idea Research — Maturing Pig Actuals (Condition Column + ft-per-Pig Rollup)

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Three idea-seeds were `unexplored`, all `created: 2026-07-25`: `idea-pig-actuals-maturation`, `idea-quotation-workup-reconciliation-check`, `idea-rollup-per-rig-coilset-grain`. Per the established tiebreak rule (first-commit timestamp when frontmatter dates tie), `git log --diff-filter=A` puts `idea-pig-actuals-maturation` first at 2026-07-25 12:44:58, ahead of the other two (18:16:38 and 22:34:36) — this seed was processed. No `**Gate:**` line, but the "To explore" prose states a data-volume trigger for the ft-per-pig rollup half of the idea ("three or four heaters carrying real counts") and a schema-timing trigger for the Condition-column half ("let it ride along the next time the card schema is opened for a reason carrying its own weight"). Both were checked before researching, per the loop's gate-check step.

## Evidence

**Gate check — data-volume trigger is met, and has been for a while.** The seed states the vault held "exactly one usable data point" (HF-0012, ~180 pigs / 12,036 ft) as of 2026-07-25. A full re-scan of every `## Pig Specifications` table across `02-facilities/` today finds real per-size actual counts (sourced from executed job reports, not quotes) on at least 11 cards: `HF-0012`, `HP-0002`, `HP-0003`, `HP-0006`, `HP-0007`, `HP-0025` (all McPherson-KS, USA25025, 2025 plant-wide TA), `H19`, `H20` (HF-Sinclair, USA25051), `7-1-F-1` (Syncrude, CAD25004), and `H-102A`/`H-102B` (Valero, USA26025, combined total). That comfortably clears the "three or four" threshold the seed named. (The Marathon Garyville cards — `210-1401A/1402B/1403A/1404B` — also carry populated Qty rows, but their `Job History` says "Lost to competitor — quote-only scope; no job executed," so those are quoted, not actual, quantities and don't count toward the actuals trigger.)

**Gate check — schema-timing trigger for the Condition column is not yet met.** `git log --since=2026-07-25` on `04-knowledge/_canonical-heater-card.md` and `templates/_heater-template.md` shows no commits — the schema hasn't been opened for any reason since this seed was written, so the seed's own stated ride-along condition still holds. This half of the idea stays correctly parked on its own terms; nothing to do here yet.

**Already covered — this seed is a direct continuation of a related idea Jesse already reviewed and parked.** `06-insights/2026-07-22-idea-research-pig-load-list-generator.md` researched a closely related idea (`idea-pig-load-list-generator`) three days earlier, found 9 cards with populated `Pig Specifications` data at the time, and Jesse's recorded decision was **Park — revisit once more cards have populated Pig Specifications data** (2026-07-22). That review's own recommended next step was smaller than a sizing engine: backfill blank cards from Field Notes prose, then fork `tools/estimating_rollup.py` into a `pig_usage_rollup.py` that aggregates raw `Pig Specifications` rows — explicitly *not* the harder rate-by-bore-and-condition problem this new seed is now asking for. The population count has grown since then (11+ actuals cards today vs. 9 on 2026-07-22, and the 9-card count on 2026-07-22 was looser — it included the Marathon quote-only rows this scan excludes). The revisit trigger on the parked idea looks met; Jesse should treat these as one decision, not two.

**Internal prior art confirms the rollup is a straightforward fork, not a new build.** `tools/estimating_rollup.py` already parses frontmatter plus a single named `##` section across every card (`Task Durations` today) into `04-knowledge/estimating-actuals-rollup.md`, explicitly reference-only. The same `parse_frontmatter` + `section_lines` + `table_rows` pattern applied to `## Pig Specifications` would produce a usage rollup with minimal new code — same conclusion the 2026-07-22 review reached.

**Internal — the current estimating method is confirmed still footage-scaling, no formula in place.** `usadebusk-estimating` SKILL.md's "Pig Quantity Estimating" section resolves quantity in priority order (1) heater history, (2) coil footage scaling, (3) fouling-by-unit-type — deliberately rough, explicitly warns against "per-pass derivation." No ft-per-pig formula or rollup exists there today; the seed's proposal would be new, not a duplicate of skill content.

**External — no off-the-shelf tool exists for this specific metric.** Searched for furnace-decoke pig consumption rate/pigs-per-foot estimating tools. Results returned only decoking method literature and equipment patents (Union Carbide, delayed-coker decoking patents), pipeline-pigging vendor sites, and general BOM/MTO software — none address rate-per-length estimation for tube-cleaning pigs in fired heaters. This matches the 2026-07-22 review's finding on the sibling idea: genuinely bespoke, nothing to import.

**External — the actual statistical shape of this problem has well-established prior art, and it directly answers the seed's own open question.** The seed worries that "a formula off one point is a formula pretending to be evidence," and asks whether the ft-per-pig ratio holds across bore sizes given how few points populate any one bore×condition cell. This is precisely the shape empirical Bayes / partial-pooling shrinkage estimation is built for: pooling sparse, uneven-n categorical groups toward a data-driven overall rate, shrinking small-n cells (1–3 points, which is what most bore×condition cells will have here) harder than well-populated ones, rather than either trusting a raw per-cell mean or refusing to compute anything until an arbitrary count is reached. It is a standard, well-documented technique (see sources) — not something to build from scratch, and it sidesteps the "one point pretending to be evidence" trap the seed correctly flags for the naive approach.

## Interpretation

**Sound, and partly already covered — but it should be merged with the already-parked sibling idea rather than treated as new.** The data-volume trigger for the ft-per-pig rollup is met; the schema-timing trigger for the Condition column is correctly still unmet and needs no action. The bigger finding is that this seed overlaps substantially with `idea-pig-load-list-generator` (parked 2026-07-22 on the same revisit condition, now also arguably met) — Jesse deciding on one without the other risks building the rollup script twice under two different names. The seed's harder question — whether a sparse, unevenly-populated ft-per-pig rate is trustworthy enough to use — has a real answer: not as a raw per-cell mean, but a shrinkage/partial-pooling estimate is the right tool for exactly this data shape and is a known, off-the-shelf statistical method (not a research problem). The seed's own Syncrude-outlier caution (item raised in the sibling `idea-rollup-per-rig-coilset-grain` seed, not this one, but structurally the same concern) reinforces that a raw mean would be dangerous here — shrinkage handles that gracefully rather than needing a manual "service class" carve-out for every outlier.

## Recommended Action

**Bounded one-shot investigation/build, combining both parked/gated related ideas into one pass** — not a standing rollup service yet. Suggested shape if Jesse takes this on: (1) revisit the 2026-07-22 park decision on `idea-pig-load-list-generator` alongside this one, since both are now sitting on a met trigger; (2) fork `tools/estimating_rollup.py` into a pig-usage rollup reading `## Pig Specifications` (reference-only, same framing as the existing script); (3) when computing any per-bore or per-condition rate from it, use empirical-Bayes/partial-pooling shrinkage rather than a raw per-cell mean, given most cells will have 1–3 points; (4) leave the Condition column exactly where the seed put it — parked until the card schema is next opened for an unrelated reason. Do not build the sizing-inference engine the 2026-07-22 review already ruled out (dataset still too thin for that).

## Decision

- [x] **Approved with edits — raw rollup only, built 2026-07-26** — Jesse
- [ ] ~~Approved — build the combined rollup now~~
- [ ] ~~Park — revisit later (state new trigger)~~
- [ ] ~~Drop~~

**Edit to the recommendation:** step (3), the empirical-Bayes/shrinkage rate by bore and
condition, was **not** built. Jesse's call was the raw aggregation only — show the data,
fit nothing — so `tools/pig_usage_rollup.py` computes per-job `ft / pig` as visible
division and reports counts and ranges by bore and by condition, with no mean and no
pooled estimate anywhere. Whether shrinkage is worth it is now a better-informed separate
decision, because the shape of the data is finally visible.

**What the first run shows** (78 actual rows, 14 cards, 4 jobs): condition separates
cleanly — crash 15–43 ft/pig against routine 41–212 — while bore does not order at all,
with 6.065" alone spanning 43–212. But the two are **confounded**: the only crash points
are H-19 and H-20 and both sit at 3.068" bore, so the apparent small-bore effect and the
crash effect are the same two rows counted twice. Separating them needs a crash job at a
large bore or a routine job at a small one. That is the real gate on any rate model, and
it is a data gate, not a method gate.

Steps (1), (2) and (4) went as recommended: the sibling park decision is closed below,
the script is a fork of `estimating_rollup.py` reusing its parsers, and the Condition
column stays parked on its own schema-timing trigger.

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| | | | |
