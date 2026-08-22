---
type: idea-seed
status: unexplored
created: 2026-08-21
tags: [idea, estimating, actuals, duration-model, DQ-020]
---

# Does rig-out actually mirror rig-in? Test the rule against every rollup row that carries both

Idea seed captured 2026-08-21 out of the DQ-020 ruling. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** `usadebusk-estimating` says rig-out mirrors rig-in at the whole figure including adders, holding "about 90% of the time" (Jesse, 2026-07-25). USA26041 broke it badly — F-501 quoted 8 hrs of rig-out and ran 14, needing a second shift — and both the source inbox note and the pre-staged review held that at n=1. They are right that it is not n=1, but the original count was far too generous.

> **⚠ REVISED 2026-08-21 — the HF Sinclair pillar is struck, and the usable count is 5 pairs, not ~14.**
>
> Jesse, 2026-08-21: *"That 25051 project was chaotic. This is not a great project to get reliable data from. The H20 had a different configuration."* Both HF Sinclair heaters are now quarantined for rule-derivation on their own row notes ([[H19]], [[H20]]) — four separate contaminations: USA25051's H-20 hours have two sources that do not reconcile under any concurrency assumption (flagged on the card since 2026-07-22); H-20 is a **vertical** 4-coil hydro heater against H-19's **horizontal** 2-coil charge heater, so they were never two samples of one configuration; H-20's radiant looping is a per-job election that changed between its own two jobs; and H-19's USA26038 rig-out of 2 h is truncated because the rigging moved to H-20 rather than demobbing.
>
> **Recount of the rollup, my derivation not a stated figure:** of the 25 rows, only **5** carry a clean numeric pair with no disqualifying marker — HF-0012 11→6, HP-0002 2→6, HP-0025 6→6, F-501 7→14, F-802 4→20. The rest are excluded by `hours-blended` (2-rig sums), `combined-heaters` (two-heater totals, and the P66 rows are the same job written on two cards), bundled rigging figures (`H-102A/B`), an unrecorded cell, or the HF Sinclair quarantine.
>
> **So the "facility-shaped split" framing does not survive the recount.** What is left is three CHS rows from a **single** turnaround (USA25025) running rig-out at or under rig-in, against two ExxonMobil rows — one of them `first` condition, the other a 2-rig job — running it well over. That is a difference between three jobs, not between sites, and it is equally consistent with job shape, condition, or rig count. Do not write it up as a per-facility rule.

If the split were real it would mean the mirror rule is not a 90% rule but a rule that works in some situations and fails in others, and the estimate should key off which. The recount says the vault cannot yet say which.

**To explore:**
- Read the **five clean pairs** back to their source receipts and confirm each is real rather than an artifact of how the hours were allocated. This is now a short read, not a survey — and three of the five are one job.
- With HF Sinclair struck, does anything sort by facility at all, or was that always job shape? Test scope type (turnaround vs emergency), rig count, and condition before facility — F-802 is 2-rig and F-501 is `first`, so both ExxonMobil rows have a candidate explanation that is not "Baytown."
- **The honest possibility: the vault cannot answer this yet.** Five pairs from three jobs may simply be too thin, in which case the finding is "the mirror rule is unmeasured," not "the mirror rule is wrong." Say so rather than fitting.
- If rig-out systematically exceeds rig-in at some sites, does the mirror rule get a qualifier, a per-facility override, or a different default — and is that a Lane 4 skill change or a per-bid judgment?
- What does the second-shift threshold look like? F-501's 14 hrs did not fit the single block it was priced in, which is a scheduling failure on top of a duration miss.

**Gate:** Do not derive a numeric correction from the Rig-In column until DQ-017 settles it — that column is **known mixed-method** ([[2026-08-16-idea-research-rollup-rig-in-column-is-mixed-method]], folded into DQ-017 on 2026-08-21), so a spread computed off it today would inherit the same defect that produced the struck ~6 ft/hr Syncrude figure. Reading the rows against their sources is fine now and is exactly what would discharge this gate; fitting a rule to them is not.

revisit-trigger: DQ-017 ruled (per-coilset re-grain + Rig-In column method) — then the numeric half of this becomes derivable.
