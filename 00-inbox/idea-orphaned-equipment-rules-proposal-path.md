---
type: idea-seed
status: resolved
created: 2026-07-24
resolved: 2026-07-25
tags: [idea, vault-system, future, estimating, skills]
---

# Are other equipment-skill rules unreachable from the proposal path?

Idea seed captured 2026-07-24 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** A proposal build loads `usadebusk-core` + `usadebusk-estimating`. It does not load `usadebusk-equipment`. So any rule that lives only in the equipment skill but is load-bearing on a *proposal* is invisible at the moment it is needed. This was confirmed once, not theorised: the 2" minimum firewater hose rule (Jesse, 2026-07-23) lived only in `usadebusk-equipment`, and the F1 regression proposal duly asked CITGO for "firewater at the required volume and pressure" with no size — the exact failure the rule exists to prevent. Fixed 2026-07-24 by adding a Section 8 trigger in the estimating skill (config commit `902fae8`). The open question is whether that was the only orphan or the first one found.

Jesse was offered a wider audit at the time and chose the direct fix, deliberately — this is the deferred half of that call, not a re-litigation of it.

**To explore:** Sweep `usadebusk-equipment` for rules whose consumer is a proposal section rather than a field operation — hose and connection minimums, launcher/receiver access constraints, pressure limits that belong in a customer-facing spec table, anything phrased as "request from the customer" or "flag on the RFQ." For each, check whether `usadebusk-estimating` can reach it. Open questions: is the right fix per-rule cross-references in estimating (what was done for firewater, cheap but drift-prone — two files to keep in sync), a single "customer-provided items" list that estimating owns outright, or making the proposal path load equipment as a third skill (simplest, but costs context on every bid and pulls in a lot of irrelevant field detail)? Also worth asking whether the same orphaning runs the other way — core or estimating rules that field work needs and cannot see — and whether `usadebusk-sop` has the same exposure, since SOP builds load equipment but not estimating.

Related: the same session's arm test found this via three independent reviewers all flagging the omission; the general lesson (cross-skill reachability is not guaranteed by a rule existing somewhere) may be worth a lint rule rather than a one-time sweep.

---

## Resolution — 2026-07-25

Explored and closed. The seed's framing was wrong in a useful way: the sweep found four more candidates, but three were not reachability problems at all. They were **situational facts only Jesse can supply** — support-equipment count, second-press availability, pig quantities — that had leaked into the estimating skill's *derive* column. Handing the skill more knowledge would have made it more confidently wrong; the fix was to make it refuse to guess and route those through the incomplete-input gate that already existed.

Decisions (Jesse, 2026-07-25): fleet availability is not tracked in the vault, always ask. No site-laydown field on the card schema. The flange-rating adapter check was considered and dropped — reps build adapting spools, and the role boundary already lives in always-loaded `usadebusk-core`. The three-skill proposal path was proposed and withdrawn.

The seed's closing suggestion — a lint rule for cross-skill reachability — is **not** taken up. A linter can detect a dangling `usadebusk-*` pointer but cannot tell a genuinely orphaned rule from one that correctly lives in a single skill, and this sweep showed the interesting failures aren't reachability at all. The one thing a linter could catch cheaply is the three dangling pointers from `usadebusk-sop` to `usadebusk-estimating` (`:12`, `:38`, `:128`) from a path that doesn't load it — left open, low severity.

Detail and revert path in `change-log.md`, 2026-07-25. Config commit `bb78eb8`.
