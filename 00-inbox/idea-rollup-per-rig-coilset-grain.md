---
type: idea-seed
status: unexplored
created: 2026-07-25
tags: [idea, vault-system, future, estimating, actuals, schema]
related:
  - "[[idea-pig-actuals-maturation]]"
---

# Re-grain the actuals rollup to one row per rig-coilset

Idea seed captured 2026-07-25 for a future session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** `04-knowledge/estimating-actuals-rollup.md` holds 22 job rows but only **11 carry a usable normalized rate** (5 routine, 6 crash). The rest are blanked because `Mode` is empty — and the blanks are correct, not gaps. They were ruled blank deliberately, because on those jobs the pig hours are not a single-rig elapsed measurement and no single mode applies. The thin routine sample that results (n=5, two clients) is what forces a stated-but-unquantified parallel-friction judgment call into **every multi-pass estimate**, and it was hedged on in all six fixture runs of 2026-07-25.

The clean measurements already exist one level down, inside the heater cards. `7-1-F-1.md` records CND25004 as three separate single-rig runs — TriMax 5 on coils 2/3/4 at triple mode for 48 pig hrs, TriMax 6 on coils 5/6/7 at triple for 35, TriMax 6 on coils 1 & 8 looped for 36 — each of which *is* a clean elapsed measurement at a known mode. `HF-0011.md` similarly records 96 pig hours as 62 triple + 34 double. So the proposal is not to backfill Mode (which would divide blended sums by a number that does not apply and manufacture false precision) but to **change the rollup's grain from one-row-per-heater-job to one-row-per-rig-coilset**, reading the splits the cards already carry.

Rough scale: Syncrude alone would go from 2 dead rows to ~6 live ones across its two jobs, and they would be 6" bore in resid service — a service class the rollup currently has zero coverage of.

**To explore:**

1. **The HF-0011 conflict, and it needs Jesse first.** The card records Mode blank per Jesse 2026-07-22 because the 96 pig hours mix modes (62 triple + 34 double). Asked again on 2026-07-25 he answered "4 looped to 2, so double" — which is the *coil configuration* and is correct as such, but the job did not run at one mode. **Does the 62/34 split map to specific passes and footage?** If yes it is two clean rows; if not it stays blended and the row stays blank. Do not write Mode 2 onto this row — it computes 26 ft/hr per pig on a routine job, below the crash mean.
2. **The Syncrude rate is a 16× outlier and must be understood before it enters any benchmark.** Split per coilset it lands near 6 ft/hr per pig against a routine mean of 99. The card gives plausible cause — coils full of resid on arrival, pitch, Kicksolve, 6" multi-bore, smart pig on all 8 — but the prior question is whether fill and flush time is sitting inside those pig hours. If the number is real, Syncrude is its own service class and must not be averaged with Gulf Coast crude; the rollup would need a service dimension, not just condition.
3. Does `tools/estimating_rollup.py` read structured enough card data to do this, or do the per-coilset splits currently live only in prose Row-notes and Field Notes? If prose, this is a card-schema change (Lane 4) before it is a script change.
4. Is a re-grained rollup still comparable to the existing rows, or does it need both grains side by side during transition?
5. Honest ROI check, in the shape the pig-actuals seed used: the payoff is removing a judgment call from every multi-pass estimate and — via the 2026-07-25 whole-shift rule, which is gated on *that heater* having no historical pigging times — removing the shift pad on repeat heaters. Repeat heaters are where it pays: H-19, H-20, H-28, H-29 and 7-1 F-1 already carry two rows each. A new heater's ticket breakdown improves the benchmark slightly and does nothing for its own next estimate.

**Gate:** None — researchable now, and item 1 needs only a decision from Jesse rather than new data.
