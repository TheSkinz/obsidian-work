---
type: note
status: open
created: 2026-07-25
tags: [inbox, skill-drift, lane-4, awaiting-decision]
related:
  - "[[2026-07-25-skill-drift-review]]"
  - "[[2026-07-25-f6-divergences-awaiting-adjudication]]"
---

# Skill-drift 2026-07 — four items held for Jesse

The 2026-07-25 skill-drift review is adjudicated and its Decision block is closed (`status: decided-blocked`), so `health.md` no longer counts it. These four items were deliberately not applied and would otherwise have gone quiet with it. Each is either Lane 4 or unverifiable from files.

**1. Does the fleet hold more than one filter press?** (F4, the highest-value question here.) `usadebusk-estimating:111` ends "there is no larger press — the filter press in `usadebusk-equipment` is the only unit." Three other surfaces presuppose more than one physical press: the equipment skill's conditional "when a 2nd press is available", estimating's own "one being uncommitted that month across concurrent jobs", and `equipment-library.md:69` headed "Filter Press **#1** specs". The loop proposed rewording "only unit" to "only model in the fleet, so more capacity means a second press, not a bigger one" — which preserves both facts. That reword sits unmerged on `drift/2026-07b` and was **not** applied. If the fleet really does hold exactly one press, the fix runs the other way and it is the *equipment* skill's conditional 2× filtration that is wrong. This one matters because an estimator reading only the estimating skill concludes a second press is impossible rather than conditional, and press capacity against 2× TriMax is the configuration that generated $25,628.17 of billable stand-by on USA26022.

**2. Was USA26038's demob 07-17 or 07-20?** (F3.) `usadebusk-fieldpm`'s dormancy banner says demobbed 2026-07-20. The job report gives execution 2026-07-10 to 2026-07-17 and `active-jobs.md` records Completed 2026-07-17. Nothing in the vault records the physical equipment-return date, so this is not settleable from files — which is why the proposed change to 07-17 was rejected rather than applied. If the last shift was the 17th and the equipment came home on the 20th, both are true and the banner should say so: `job complete 2026-07-17, demobbed 2026-07-20`. One line either way; the skill is dormant so nothing depends on it until the next mobilization.

**3. ~~`estimating-pricing.md:68` names the $58.00 line "Driver Travel".~~ — APPLIED, not held.** (V3.) Initially held as Lane 4 pricing, then released on recon: `change-log.md`'s 2026-07-24 entry already records this rename as your decision — "the `$58.00/hr Driver Travel` rate line was unreachable … it is renamed **Crew Travel (non-driver)**" — and lists `04-knowledge/concepts/estimating-pricing.md` among the files that entry touched. The rename landed in the skill and in `estimating-approach.md` but never in this row. So it is a half-landed approved fix like V2, not a new pricing decision, and it was applied on that basis. Flagging it here anyway because it is a pricing row and you should know it moved. If you disagree, revert that one line.

**4. F1 regression fixture now fails diff key 4.** The post-adjudication replay missed the equipment-piece-count contradiction in intake item 15 — six items enumerated against "(5 pieces traveling)" — and priced five pieces without flagging it, where the frozen baseline catches it, reconciles it, and prices the swing. Not caused by any change in this adjudication: nothing has touched estimating or core intake logic since F1's baseline commit `bb78eb8` except a role line and a billing-math pointer. It reads as model variance against a rule that is implicit rather than written. The README's remedy is to make the implicit rule explicit in the skill, but that is a new commercial-skill edit, so it was left alone. `frozen/` was **not** re-cut. Decide whether to write an intake-consistency rule into `usadebusk-estimating`.

Items 2 and 3 are one-liners. Item 1 is the one with real downstream reach.
