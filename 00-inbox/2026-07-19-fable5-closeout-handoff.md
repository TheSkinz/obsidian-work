<!-- vault-loop: operational — heater-card/estimating/regression work orders (04-knowledge, 02-facilities scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
---
type: handoff
created: 2026-07-19
author: claude-fable-5 (final Fable-5 session)
audience: Opus / Codex post-window sessions
status: open
related:
  - "[[h-2421]]"
  - "[[DSP26080]]"
---

# Fable-5 close-out handoff — post-window work orders

Context: written at the end of the final Fable-5 session (2026-07-19), the same
session that produced the regression suite (`~/.claude/regression/`, config repo
7d5eebd), the H-2501 source recovery (vault 4e8ca31), and the H-2421 ground-truth
extraction (`04-knowledge/ground-truth/h-2421.md`, vault a07976f). Five work
orders below, roughly in value order. None are time-critical; all are additive.

**Pending gate first:** H-2421's Stage-4 verification block was presented to Jesse
at session end. If he never responded, the ground-truth note is still
`status: awaiting-jesse-verification` and the heater card still carries its open
flags — the first session that touches H-2421 should re-present the checklist from
the ground-truth note's extraction table (rows 2, 3, 4, 5, 6, 9, 10, 12, 13, 16 are
the load-bearing ones) before any card write.

## (a) Physical-invariant linter for heater cards

Build as a leverage-repo-style exec gate (`C:\Users\Jwuts\leverage`): manifest per
`schemas/gate-manifest.json` (kind `exec`, target_type `heater-card`, entrypoint
exposing `check(target_path)`), and it may not gate anything until it classifies
≥3 pass + ≥3 fail fixtures at 100% (the repo's deployment rule). Real fixtures
exist: H-2421.md / H-2501.md / H-30.md as pass cases once verified; fail fixtures
by mutating one value each.

Invariants to check, from this session's proven catches:
1. ID = OD − 2×wall within ±0.005" wherever all three are recorded.
2. (OD, wall) pair matches a standard schedule when Sched is claimed (6.625/0.432
   = Sch 80, 6.625/0.280 = Sch 40, 4.5/0.237 = Sch 40…). Keep the lookup table small
   and explicit.
3. Tubes/Circuit × Avg Length ≈ Length/Circuit (tolerance ~2% — cut vs effective
   lengths differ; see caveat below).
4. Per-circuit × circuit count = heater-total rows in the Config Rollup.
5. Max pig OD ≤ governing (smallest) ID + 0.250, and governing ID = min of all
   section/segment IDs on the card.
6. Serpentine sanity when return count is recorded: returns = tubes − 1 per circuit.

**Lane 4 rule, Jesse gates:** the invariant CONSTANTS (0.250 pig rule, schedule
table, tolerances) live in one reviewed config block that only Jesse changes —
the linter code is Lane 1/2, the constants file is Lane 4. Do not let a code
session "fix" a failing card by loosening a constant.

Caveat the linter must encode, not fight: cards legitimately mix cut lengths
(BOM) and effective lengths (datasheet incl. return development ≈ π × NPS/2 per
SR return). H-2421 proved both figures true simultaneously (192.9 vs 210 conv).
Rule 3 must accept either interpretation and flag only when NEITHER reconciles.

## (b) Cross-reference checker — top 3 rules

Scope: card ↔ quote note ↔ `01-context/active-jobs.md`. Run as a propose-only
report (Lane 1), not auto-fix.
1. **Quote status consistency:** a quote note's `status:` (pending/won/lost) must
   agree with the active-jobs table row and with every heater card whose Job
   History cites it. (DSP26058-lost vs directory drift was a real instance.)
2. **Validity dates:** quote `date-submitted` + validity period vs active-jobs
   "Valid Through" — flag "Not recorded" pairs older than 30 days and any expired
   quote still listed as pending. DSP26080 currently has both unrecorded.
3. **Job/quote number linkage:** every Job # in a card's Job History exists as a
   quote note or job sheet; every heater a quote's frontmatter `heaters:` lists has
   a card whose Job History cites that quote back. Catches one-sided edits.

## (c) Duration-model adjudication brief (Lane 4 memo for Jesse)

> **DONE 2026-07-22.** Picked up this session. Jesse stated the duration model directly, which
> dissolved the adjudication (the 82-vs-128 "paradox" is one per-coil rate near 100 that only
> differs after looping/service/bore). Captured in `06-insights/2026-07-22-duration-model-capture.md`
> with proposed gap-fills A–F to the three estimating sources; queued as `DQ-002` for Jesse's call.
> The generator's combined-heaters defect noted below was already fixed before this pass (emits `-`).

Question to settle: what does the 100 ft/hr benchmark actually apply to —
total coil footage as one number (the skill's worked example) or per-pass with
parallelism across TriMax assemblies (the benchmark's own phrasing)? The two
readings diverge hard on multi-pass heaters (F6 fixture in the regression suite
freezes the tension deliberately; H-2421's DSP26080 plan quotes 12 pig-hours for
980 ft looped — 82 ft/hr single-path — while H-2501 quotes 48 hr for 6,167 ft =
128 ft/hr with 6 passes on 3 assemblies).

Method: pull every footage row from `04-knowledge/estimating-actuals-rollup.md`
(8 rows as of today), normalize each to (a) ft/hr-total and (b) ft/hr-per-pass ×
assemblies-used, against the 6-hr rig-in default.

**Do not take the four P66 rows at face value — they are arithmetically wrong.**
Adding verified footage to the H-28/H-29 cards on 2026-07-19 caused
`estimating_rollup.py` to compute ft/hr for jobs 24012 and USA25041, but both
jobs pigged H-28 and H-29 *together* and the recorded task hours are combined,
not per-heater. The generator attributes the full combined hours to each heater
while using only that heater's footage, so the resulting 13/16/17/20 ft/hr
figures understate the true rate by roughly half. The correct normalization for
those two jobs is combined: 4,238 ft against 143 hrs (24012) and 117 hrs
(USA25041) — about 30 and 36 ft/hr, which is still far below the 100 ft/hr
benchmark and is the real signal (hard coker coke, bend-restricted 2.6" bends).
The combined-job caveat lives in prose on both cards; the generator cannot see
it. **Fixing this is part of the job:** either give the rollup a way to recognize
a multi-heater job (a shared job-number key, or a `combined-with:` field) or have
it emit "(combined — see card)" instead of a computed rate. Same defect will hit
any future job spanning two heaters. Include quote-vs-actual deltas —
USA25041 ran 117 pig-hours actual vs 80 quoted (46% over). Output: a one-page
Lane-4 memo with a recommended benchmark statement + a written duration decision
procedure (when to use total-footage, when per-pass-parallel, when heater actuals
override — the skill already says actuals govern). Jesse decides; the skill text
changes only after his call.

## (d) Model-regression diff procedure

Everything needed is in `~/.claude/regression/README.md` (config repo 7d5eebd):
replay each fixture verbatim on the target model, diff against `frozen/` on the
three-tier bar (exact numerics → behavioral flags → structure). Patch ONLY skills
whose fixture fails, by making the implicit rule explicit in skill text, then
re-run that fixture. Don't re-freeze references on a new model — the frozen set
stays Fable-5 until Jesse decides to re-baseline.

## (e) Reasoning traces worth harvesting

Two worked examples from this session deserve extraction into
`07-llms/` (or wherever the methods library lands) as reusable patterns:
1. **Stage 3 cross-source reconciliation** (session transcript, 2026-07-19; result
   in `04-knowledge/ground-truth/h-2421.md`): BOM piece-counting → returns = n−1
   identity → per-circuit totals → weight-column back-computation to distinguish
   finned/bare and verify wall thickness → template-legend detection by cross-file
   cell comparison (the "Ubend to Plug-Head / Unknown. Validate" cells identical in
   two different heaters' workbooks = template artifact, not data). The general
   lesson: an Excel cell is only data if it varies across instances.
2. **Length-conflict reconciliation:** when two sources disagree on tube length,
   test "cut length + return development ≈ effective length" before declaring
   conflict (Δ0.25% radiant, Δ1.6% conv on H-2421). Generalizes to any
   BOM-vs-datasheet dispute.
Item (c)'s normalization, once done, is a third trace.

## Bonus pointer — P66 H-28/H-29 (repeat client, cards empty of geometry)

Reachable and probed this session, NOT extracted (Stage 4 gate took precedence):
- Files: `C:\Users\Jwuts\OneDrive\Desktop\Facilities\Active Work\Job Report\24012 P66 Ponca City H-28 Jan 2024 TA Job Report.docx` (+ H-29 twin, PDFs alongside).
- The geometry lives in embedded images, not text. H-28 `word/media/image4.png`
  is a clean TUBE & PIPE BILL OF MATERIAL: 3" (3½" OD) Sch 80 SMLS, rows
  8× 44'-2 + 8× 45'-4¼ (SA-106 Gr B), 4× 46'-6 + 52× 44'-1 + 20× 44'-1 + 4× 44'-1
  (B407 UNS N08811 = Incoloy 800H/HT), plus 2× 8" Sch 80 extruded manifolds
  (MK 03-03A/03B). image5.png shows the coil GA with pass labels "A"/"B"/"C"/"D"
  at the tube sheet. H-29 media includes a 17 MB EMF (image4.emf) that is likely
  the full vector GA — render it before trusting any raster.
- Method: identical to Stage 3 (region crops, identity checks, ground-truth note
  per `h-2421.md`'s format, cards untouched until Jesse verifies). Mixed
  SA-106/Incoloy metallurgy split across tube positions will be the interesting
  flag — don't average it into one metallurgy value.
