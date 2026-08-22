---
type: idea-seed
status: unexplored
created: 2026-08-21
tags: [idea, estimating, actuals, duration-model, DQ-020]
---

# Does rig-out actually mirror rig-in? Test the rule against every rollup row that carries both

Idea seed captured 2026-08-21 out of the DQ-020 ruling. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** `usadebusk-estimating` says rig-out mirrors rig-in at the whole figure including adders, holding "about 90% of the time" (Jesse, 2026-07-25). USA26041 broke it badly — F-501 quoted 8 hrs of rig-out and ran 14, needing a second shift — and both the source inbox note and the pre-staged review held that at n=1. **They are wrong that it is n=1.** `04-knowledge/estimating-actuals-rollup.md` already carries roughly fourteen rows with both a Rig-In and a Rig-Out figure, and they do not support the mirror rule uniformly: two ExxonMobil Baytown heaters break it hard in the same direction (F-501 7→14, F-802 4→20), HF Sinclair does too (H-19 10→30, H-20 22→38), while four CHS turnaround rows run rig-out *under* rig-in. If that facility-shaped split is real, the mirror rule is not a 90% rule — it is a rule that works at some sites and fails at others, and the estimate should key off which.

**To explore:**
- Read every rollup row carrying both figures back to its source receipt or ticket breakdown, and confirm the pair is real rather than an artifact of how the hours were allocated.
- Does the split sort by facility, by scope type (turnaround vs emergency), by launcher count, or by nothing?
- If rig-out systematically exceeds rig-in at some sites, does the mirror rule get a qualifier, a per-facility override, or a different default — and is that a Lane 4 skill change or a per-bid judgment?
- What does the second-shift threshold look like? F-501's 14 hrs did not fit the single block it was priced in, which is a scheduling failure on top of a duration miss.

**Gate:** Do not derive a numeric correction from the Rig-In column until DQ-017 settles it — that column is **known mixed-method** ([[2026-08-16-idea-research-rollup-rig-in-column-is-mixed-method]], folded into DQ-017 on 2026-08-21), so a spread computed off it today would inherit the same defect that produced the struck ~6 ft/hr Syncrude figure. Reading the rows against their sources is fine now and is exactly what would discharge this gate; fitting a rule to them is not.

revisit-trigger: DQ-017 ruled (per-coilset re-grain + Rig-In column method) — then the numeric half of this becomes derivable.
