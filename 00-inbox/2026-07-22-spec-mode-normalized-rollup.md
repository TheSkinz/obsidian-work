---
type: spec
status: resolved
created: 2026-07-22
related:
  - "[[2026-07-22-duration-model-capture]]"
  - "[[estimating-actuals-rollup]]"
  - "[[_canonical-heater-card]]"
tags: [spec, estimating, tooling, schema, duration-model]
---

# Spec — mode-normalized ft/hr in the actuals rollup

> **Built 2026-07-22.** Implemented as specced: `Mode` appended (optional, backward-compatible) to
> the Task Durations schema in the exemplar, template, and `usadebusk-vault-ingest`; `Mode` +
> `ft/hr per pig (norm)` columns added to `tools/estimating_rollup.py`; `tools/vault_lint.py`
> updated to accept the optional column; four cards backfilled (Valero H-102A/B = 3, HF Sinclair
> H-19/H-20 = 1). Rollup now shows the Valero triple-mode jobs at ~13 ft/hr per pig vs ~40 elapsed.

## Why

`04-knowledge/estimating-actuals-rollup.md` reports **ft / elapsed pig-hr** = heater footage ÷
elapsed Pig hours. Under the duration model captured in [[2026-07-22-duration-model-capture]], that
figure blends the true per-pig travel rate with parallelism: when a pumper runs double/triple mode,
several passes are pigged at once, so the elapsed rate reads 2–3× higher than the rate one pig
actually travels. The Valero H-102A/B rows (triple mode) read ~38–40 ft/hr elapsed but a per-pig
rate closer to ~13–15; single-path jobs (H-19/H-20 looped) read their true rate directly. Today the
reader has to de-blend that by hand, and the condition-mean table averages across modes as if they
were comparable. Adding one field fixes both.

## The idea in one line

Record how many passes were pigged **simultaneously** (the mode), and have the generator divide the
elapsed rate by it to report a per-pig rate that is directly comparable to the 100 ft/hr benchmark.

## Schema change — add a `Mode` column (Lane 4, Jesse-gated)

Append **`Mode`** as the **last** column of the Task Durations table (after `Condition`).
Appending — not inserting — is deliberate: the generator pads short rows
(`estimating_rollup.py`, `r = (r + [""] * len(TD_COLS))[:len(TD_COLS)]`), so every existing card
that lacks the column reads it as blank = "unknown" and nothing breaks. **No forced backfill.**

- **Definition:** number of passes pigged simultaneously during the Pig task — the pumping mode
  (single = 1, double = 2, triple = 3), multiplied by the number of pumpers if more than one ran in
  parallel (2 rigs both double = 4). A looped path counts as 1 (it is one continuous pig run).
  Distinct from the existing `Rigs` column, which is the physical pumper-unit count; `Mode` is the
  effective simultaneous-pass count the field crew knows directly.
- **Blank** = not recorded → generator does not normalize that row (raw only).
- **Files carrying the schema:** `04-knowledge/_canonical-heater-card.md` (exemplar, authority),
  `templates/_heater-template.md`, and the Task Durations column mirror inside the
  `usadebusk-vault-ingest` skill (per vault `CLAUDE.md`, the column set lives in the exemplar and is
  mirrored in that skill — update both so they don't drift).
- **Optional backfill to activate normalization now:** set `Mode` on the four cards where it is
  known — Valero `H-102A`/`H-102B` = **3** (triple), HF Sinclair `H19`/`H20` = **1** (looped single
  path). Leave the rest blank until a job records it. P66 `H-28`/`H-29` stay blank (combined-heaters
  rows are already excluded from rate math).

## Generator change — `tools/estimating_rollup.py` (Lane 1/2)

1. **`TD_COLS`** (line ~38): append `"Mode"` to the list. Mode is then `r[11]`.
2. **`build()` rate loop** (lines ~136–145): after the existing `combined` check, parse
   `mode = num(r[11])`. Keep the existing raw `fthr = footage / pig` (unchanged). Add a normalized
   value: `norm = fthr / mode` when `mode` is a positive number and the row is not `combined`,
   else `None`.
3. **Actuals table** (header ~166, rows ~172–178): add two columns — `Mode` and
   `ft/hr per pig (norm)`. Render `norm` with `-` when unknown/combined, mirroring the existing
   `fthr_s` logic. Keep the raw `ft / elapsed pig-hr` column so both are visible side by side.
4. **Condition segmentation** (lines ~180–203): switch the segment aggregation to use `norm` where
   available, so crash rows across different modes are compared on a per-pig basis. Rows with
   unknown mode fall back to raw and are flagged (e.g. a `*` + footnote) rather than silently mixed.
5. **Interpretation caution** (lines ~159–162): rewrite to explain the new column —
   "`ft / elapsed pig-hr` is footage ÷ elapsed Pig hours and reads high on double/triple-mode jobs
   because several passes are pigged at once; `ft/hr per pig (norm)` divides that by `Mode` to
   approximate a single-pig travel rate comparable to the 100 ft/hr benchmark."

### Normalization math and its one caveat

`per-pig rate ≈ (footage / elapsed_pig_hr) / Mode`. Exact when the pass count divides evenly into
sets of `Mode`. When it does not (e.g. 8 passes in triple mode → sets of 3/3/2, average parallelism
2.67 not 3), dividing by 3 slightly **under**-states the rate (~13 vs the exact ~15). For a
tiny anecdotal dataset this approximation is fine; the exact divisor is `passes ÷ ceil(passes ÷
Mode)`, which needs a machine-readable pass count the cards don't yet carry. Note the caveat in the
caution block; revisit only if a structured pass-count field is later added.

## Effort / risk

Small, pure-stdlib. One column added to three schema-carrying files, an optional four-card backfill,
and a localized edit to one generator (no new dependencies, no change to how footage or elapsed
hours are read). Risk is low and contained to a reference report — the rollup never changes a rate
or a skill value. Lane: the generator is Lane 1/2; the `Mode` column on the canonical schema is
Lane 4 (Jesse green-lights the schema addition, as with any card-schema change).

## Verification

1. `python tools/estimating_rollup.py --print` → Valero H-102A/B show `Mode 3` and a normalized
   rate ~13–15; H-19/H-20 show `Mode 1` with normalized == raw; blank-mode rows show `-` in the
   normalized column; P66 combined rows still show `-`.
2. `python tools/vault_lint.py` → 0 errors (the wider Task Durations table stays schema-valid).
3. Hand-check one triple-mode and one single-path row against the source cards before trusting the
   segment means.
