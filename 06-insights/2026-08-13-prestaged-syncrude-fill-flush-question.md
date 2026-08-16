---
type: review
status: resolved
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-13
superseded-by: "DQ-017 (2026-08-15) — the reproduce-first ordering moved into the queue row's ask verbatim; `revisit-trigger:` retired, see the Apply Log"
related:
  - "[[2026-07-28-idea-research-rollup-per-rig-coilset-grain]]"
tags: [review, knowledge-system, estimating, actuals, syncrude]
---

# Review — Does the Syncrude ~6 ft/hr per-coilset figure include fill/flush time, and does it matter today?

## Trigger

Pre-staging loop run 2026-08-13, processing `00-inbox/2026-07-29-syncrude-6-ft-hr-fill-flush-question.md` — the oldest unprocessed candidate carrying the `vault-loop:` marker without a `vault-prestaged:` marker (previously tied with, and passed over in favor of, the 2026-08-11 run's `build-workup-quotation-regression-check` item, which that run's own note flagged as remaining queued).

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-07-29-syncrude-6-ft-hr-fill-flush-question.md` (read this run) | Observed | Split out of the per-rig-coilset-grain idea-research note when Jesse parked that note 2026-07-29. Asks whether the Syncrude ~6 ft/hr figure includes fill/flush time before it "is allowed to enter any service-class benchmark." Explicitly does not gate the parked schema decision. |
| `06-insights/2026-07-28-idea-research-rollup-per-rig-coilset-grain.md` (read this run) | Observed | Origin of the ~6 ft/hr figure: "item 2" of the researched idea, describing a per-rig-coilset breakdown as one of two example cards used to argue the actuals rollup should be re-grained below the heater-job level. Decision: **parked**, "next time the card schema is opened for a reason carrying its own weight" — bundled with the still-parked Pig Specifications `Condition` column. The fill/flush question was carved out as a separate, non-gating ask at Jesse's own direction. |
| `02-facilities/Syncrude/Fort-McMurray-AB/7-1-F-1.md:138-151` (read this run) | Observed | The only structured per-coilset split in the vault for this heater: CND25004 — Trimax 5 (coils 2/3/4, triple mode) 6/48/6/3=63 hrs; Trimax 6 (coils 5/6/7, triple mode) 6/35/4/3=48 hrs; Trimax 6 (coils 1 & 8) 2/36/8/7=53 hrs. The card's own "ft/hr note" already states pig hours on both Task Durations rows are "2-rig sums across asymmetric coil-sets, so the rollup's ft/elapsed-pig-hr is NOT a valid per-pig travel rate for either" — but that exclusion is reasoned from the multi-rig blending, not from any determination about fill/flush content. The card documents 47 tubes / 2,311 ft as **uneven per-coil** (some coils 3 radiant tubes, some 4), so no clean heater-footage-÷-8 per-coilset figure exists to check "~6 ft/hr" against. |
| `04-knowledge/estimating-actuals-rollup.md:33-34,42-45` (read this run) | Observed | Both Syncrude rows (CND24002, CND25004) carry `Mode: ?` and `ft/hr per pig (norm): -` — already excluded from the condition-mean tables (`routine` mean 99 ft/hr over 5 rows) at the heater-job grain the rollup currently tracks. Neither row's elapsed-only rate (34, 19 ft/hr) is close to 6. |
| Vault-wide search for "fill/flush", "fill and flush" (read this run) | Observed | No note anywhere resolves whether the Syncrude per-coilset hours include fill/flush; the phrase appears on other, unrelated heater cards (Flint Hills, HF Sinclair) describing their own de-inventory delays, not this question. |

## The Question

Should Jesse's read on whether the Syncrude per-coilset pig-hour figures include fill/flush time be captured now (recorded on the heater card regardless of current exposure), or is the question moot today and better bundled with the already-parked per-coilset re-grain schema decision, since no current mechanism lets a per-coilset figure enter any benchmark?

## Proposed Change

**A. Ask Jesse now and record the answer in `7-1-F-1.md`'s Field Notes or ft/hr note, independent of the parked schema decision.** Cheap to capture while the job is still recent memory; avoids re-deriving or re-asking when the schema decision eventually reopens. Narrow ask: for CND25004's per-coilset splits (Trimax 5: 63 hrs / Trimax 6 coils 5-7: 48 hrs / Trimax 6 coils 1&8: 53 hrs), do the "Pig" hours in each sub-total include fill/flush/dewater time, or only pig-travel time?

- [ ] Approved
- [ ] Approved with edits
- [x] Rejected
- [ ] Needs more research

**B. Bundle and defer — no per-coilset figure feeds any benchmark today** (heater-total rows are already excluded from the norm mean via blank `Mode`; per-coilset rows don't exist as rollup data at all, only as Field Notes prose). Close this inbox item as moot until the per-coilset re-grain schema decision from the 2026-07-28 idea-research note reopens, and answer the fill/flush question at that point, in context, rather than banking an isolated fact now.

- [ ] Approved
- [x] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**C. Needs more research before either A or B: reproduce the "~6 ft/hr" figure itself.** This review could not reconstruct it from what's in the card — heater footage is documented as unevenly split across coils (some 3 radiant tubes, some 4), so no per-coilset footage exists to divide by the 63/48/53-hour sub-totals and check against "~6 ft/hr." The figure may rest on data (a specific per-coilset footage split) that was never ingested into the card, in which case the fill/flush question is secondary to a missing-footage question.

- [ ] Approved
- [ ] Approved with edits
- [x] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

Option A's "cheap now" framing assumes Jesse can still recall or look up the fill/flush split for a September 2025 job; if not, this becomes a research task disguised as a quick question. Option B's "moot today" claim is only as solid as the current schema staying unchanged — if the per-coilset re-grain schema decision is approved at some future point without anyone re-checking this note, the ~6 ft/hr figure could enter a benchmark table with the fill/flush question still unanswered, silently reintroducing the exact risk the original inbox note flagged. Option C is the most defensible next step given this run's finding that the figure can't be reproduced from card data, but it delays Jesse's decision behind a data-reconciliation task nobody has scoped yet.

## Decision

**Resolved 2026-08-15 (Jesse, in session). B approved with edits. A and C rejected.**

**A is rejected on its own stated risk.** It asks Jesse to recall the fill/flush split on a September 2025 job — that is a research task wearing a quick question's clothing, and it buys nothing today because no per-coilset figure can reach a benchmark under the current schema.

**B is right that it is moot today, and wrong that "close as moot" is enough.** B's own risk paragraph names the failure exactly: if the per-coilset re-grain decision is ever approved without anyone rereading this note, ~6 ft/hr enters a benchmark with the question still open. Closing a note as moot is precisely how that happens. The edit is therefore a `revisit-trigger:` on this note, tied to the same event that unparks the schema decision, so the dormant-triggers table on the health dashboard carries it and it cannot go quiet.

**C is rejected as an option but its finding is the most important thing in this note, and it reorders the question.** This run could not reproduce ~6 ft/hr from card data at all — the 47 tubes / 2,311 ft are documented as unevenly split across coils, so there is no per-coilset footage to divide by the 63 / 48 / 53-hour sub-totals. The figure rests on a split that was never ingested. That inverts the priority: asking whether the hours include fill/flush is asking for a qualifier on a number nobody can currently derive. Reproduce first, qualify second. C is rejected only because scoping a data-recovery task now, for a figure with no consumer, is work with no deadline attached to it — the requirement is instead written into the trigger so it fires when the figure actually acquires a consumer.

Recorded on the heater card as well as here, because the card is where anyone would land while doing the re-grain work, and a caution that lives only in `06-insights/` is a caution nobody reads at the moment it matters.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-15 | Ruled. Added `revisit-trigger:` to this note's frontmatter, event-shaped and tied to the per-coilset re-grain decision parked at [[2026-07-28-idea-research-rollup-per-rig-coilset-grain]], requiring the figure be reproduced from recovered per-coilset footage BEFORE the fill/flush question is asked and barring it from any benchmark until both are answered. Added a paragraph to `02-facilities/Syncrude/Fort-McMurray-AB/7-1-F-1.md`'s ft/hr note recording that ~6 ft/hr is not reproducible from card data and why (uneven per-coil tube counts, no per-coilset footage ingested). Heater-card content is Lane 1 in full per the governance facility-data note, so no gate was needed for that edit; no rollup, schema, or benchmark value was touched, and no new domain figure was asserted. | Claude (review queue) |
| 2026-08-15 | **Trigger retired one day later and replaced by [[decision-queue\|DQ-017]]** (Jesse, retirement sweep). This reverses yesterday's mechanism but not yesterday's ruling, and the distinction matters because DQ-012 chose a trigger *specifically* so the question could not go quiet. The premise it rested on has changed: the gating event — a heater-card schema change carrying its own weight — has not occurred since 2026-07-28, and three separate triggers were queued behind it, so waiting was itself the risk. Jesse ruled the bundle gets its own scheduled session instead. **The reproduce-first constraint is not weakened and is carried verbatim in DQ-017's ask:** reproduce ~6 ft/hr from per-coilset footage BEFORE asking the fill/flush question, and no benchmark entry until both are answered. The decision queue is the stronger carrier — it is capped, counted on the health dashboard, ages out at 60 days, and pauses proposal-generating loops when full, none of which a dormant-trigger row does. | Claude (retirement sweep) |
| 2026-08-13 | Note filed by pre-staging loop from `00-inbox/2026-07-29-syncrude-6-ft-hr-fill-flush-question.md`. Confirmed both Syncrude rows are already excluded from the actuals rollup's normalized per-pig means (blank `Mode`), for a different reason (multi-rig blending) than the fill/flush question asks about. Attempted to reproduce the "~6 ft/hr" figure from the heater card's per-coilset hour splits and heater-total footage; could not, because per-coil footage is documented as uneven and no per-coilset footage breakdown exists in the card — flagged as Option C. No heater-card, rollup, or schema content modified. | Claude (pre-staging loop) |
