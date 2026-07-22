---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-22
review_after: 2026-08-22
related:
  - [[idea-pig-load-list-generator]]
  - [[vault-idea-loop-spec]]
tags: [review, knowledge-system, idea-research, estimating, equipment]
---

# Idea Research — Pig Load List Generator from Heater Cards

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Three idea-seeds were still `unexplored`: this one and `idea-workup-to-proposal-generator` (both `created: 2026-07-19`), plus `idea-lint-lock-heater-schema` (`created: 2026-07-20`, not close to the tie). Following the tiebreak rule the prior two nights' runs established (first-commit timestamp when frontmatter dates tie), `git log --diff-filter=A` shows this seed's first commit at 2026-07-19 21:22:20 vs. the workup-to-proposal seed at 22:29:56 — this seed is older and was processed.

## Evidence

**Internal — the "input side" of this idea is already partially built, just unevenly populated.** Grepped all `02-facilities/` heater cards for the `## Pig Specifications` table the schema already defines: 23 cards carry the section. Of those, 9 have real populated rows sourced from actual job reports (`H19`, `H20`, `210-1401A/1402B/1403A/1404B`, `DSP26058`, `7-1-F-1`, `H-102A/H-102B`); the remaining 14 — including `H-28` and `H-29`, the very cards that motivated this idea's "Max Pig OD" language — have the table present but every row blank. So the scaffolding for a generator's data source already exists vault-wide; the gap is data capture, not schema design.

**Internal — the H-28/H-29 case shows exactly the "scattered and inconsistently useful" pattern the seed describes.** `H-28.md`'s `Pig Specifications` table is empty, but its `Field Notes` section has the real data as unstructured prose: "Pigs Ran (combined H-28/H-29 job totals): 2\" TC ×2, 2.25\" TC ×7, 2.5\" TC ×6, 2.625\" TC ×12, 2.75\" ×42 (40 TC + 2 foam)…" down to 16 distinct sizes. The data the seed wants a generator to consume already exists — it just hasn't been transcribed from prose into the structured table it belongs in.

**Internal prior art — the vault already has a working generator for exactly this shape of problem.** `tools/estimating_rollup.py` walks every `02-facilities/` card, parses frontmatter and a named `##` section (`Task Durations`), and aggregates it into a single reference file (`04-knowledge/estimating-actuals-rollup.md`), explicitly marked reference-only — it "never changes a rate or a skill value." The same parser pattern (`parse_frontmatter` + section-by-heading extraction) applied to `Pig Specifications` tables instead of `Task Durations` would produce a pig-usage-by-size rollup with almost no new engineering — this is a fork of an existing script, not a new build.

**External — no off-the-shelf tool fits this niche.** Searched pipeline-pigging equipment vendors (Enduro, PigTek, Atlas Copco) and general BOM/material-takeoff software (Vertex, BOM Tabulator, Matrix, various Excel BOM templates). Pigging vendors sell hardware, not load-planning software. BOM/MTO tools all assume a stable engineering bill of materials to explode into a pick list — that assumption doesn't hold here, because (per the seed's own "To explore" question) pig quantity per job is experience-driven, not spec-derived: the 24012 usage distribution is heavily skewed to 2.75"/2.875" sizes rather than spread evenly across the sizing ladder. This is a genuinely bespoke problem; there is no power-user solution to import.

## Interpretation

**Sound, but scoped one level too ambitious.** The seed correctly identifies the real fork — quantity is not cleanly rule-derivable, so any generator that tries to *recommend* sizes/counts from geometry alone would be guessing on a 9-card dataset. But the seed frames the whole thing as "not yet built," when the structured field already exists on all 23 cards and is already populated on 9 of them. The actual blocker is a data-entry backfill (moving prose out of Field Notes into the table on the 14 empty cards, starting with H-28/H-29) plus a small rollup script — not a sizing engine. That smaller version delivers precisely the behavior the seed's own "To explore" section names as correct for bend-limited coils: "refuse to guess and surface the restriction plus prior actuals for a human call."

## Recommended Action

**Bounded one-shot investigation/build, scoped smaller than the seed originally framed** — not the full sizing-inference generator, which should stay parked until the actuals dataset is much larger than 9 cards. Two-step version: (1) backfill `Pig Specifications` rows on cards where the data already sits in Field Notes prose (H-28/H-29 first, since they're already flagged); (2) fork `tools/estimating_rollup.py` into a `pig_usage_rollup.py` that aggregates all `Pig Specifications` tables into one `04-knowledge/` reference file, same reference-only framing. This is a data-hygiene + small-script pass, not a new sizing tool — it directly answers the seed's "does quantity exist at all" question by making the existing actuals queryable, without attempting to solve the harder (and currently underdetermined) sizing-rule problem.

## Decision

- [ ] Build now — backfill + rollup script as scoped above
- [ ] Approved with edits
- [ ] Park — revisit once more cards have populated Pig Specifications data
- [ ] Drop

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
|  |  |  |  |
