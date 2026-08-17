---
type: review
status: open
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-17
related:
  - "[[F-501]]"
  - "[[USA26041-job-sheet]]"
tags: [review, estimating, cost-model, USA26041, pre-staged]
---

# Review — Do any of USA26041's three model-level estimating findings reach `usadebusk-estimating` now, or does n=1 mean all three wait?

## Trigger

Pre-staging loop run 2026-08-17, processing `00-inbox/2026-08-15-usa26041-estimating-feedback.md` — the oldest unprocessed candidate carrying the `vault-loop:` marker without a `vault-prestaged:` marker (two older candidates, `2026-08-10-sharepoint-kb-build-open-items.md` and `2026-08-11-outlook-doc-three-copies.md`, were skipped this run as already covered; a third, `2026-08-11-quote-notes-missing-date-submitted.md`, was skipped as an execution correction).

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-08-15-usa26041-estimating-feedback.md` (read this run) | Observed | Three model-level findings from the first F-501 job (USA26041), explicitly separated from job-level detail: (1) the $103.50 blended pig unit over-recovered — 43 pigs actually ran for $2,742.20 against 25 quoted at $103.50 ($2,587.50), with six real per-size unit costs listed ($8.60–$81.40); (2) rig-out ran 14 hrs against 8 quoted (75% over, needed a second shift) while pigging ran 16 against 24 (a third under) on a coil inspection confirmed clean — net 43 productive hrs against 48 quoted, which the note says hides the shape; (3) per diem should price off calendar days on site (job ran 4 calendar days) rather than shift/person-day count (quote assumed 6×2=12 person-days, 15 T&M person-days actually billed). Note's own "To do" line poses the exact question this row asks. Marker text on this item explicitly routes it to "the on-demand Agent-Review loop" for any write — consistent with this loop's role of proposing, not applying. |
| `50-dashboards/decision-queue.md` (checked this run) | Observed | Four open rows (DQ-016 through DQ-019). None address USA26041, pig-unit cost, rig-out duration, or per-diem basis. Not already queued. |
| `change-log.md:165` (2026-08-15 entry, read this run) | Observed | Records the same actuals independently: "Actuals from receipts 10780–10786: 7 rig-in / 16 pig / 6 smart pig / 14 rig-out = 43 productive hrs against 48 quoted... Condition `first`, n=1, so it does not move the routine baseline." Confirms the rig-out/pigging shape was already filed as a fact on the job card with the n=1 caveat applied — but the entry only records the fact, it does not touch `usadebusk-estimating`'s rig-out or rig-in figures, and it does not address the pig-unit or per-diem questions at all. |
| `change-log.md:167` (2026-08-15 entry, read this run) | Observed | Reconciles the per-diem claim to "24 person-days entitled vs 15 billed = 9 unbilled ($1,350)" — a billing reconciliation on this specific job, not a ruling on whether the estimating model's per-diem basis (shift-count vs. calendar-days) should change. |
| `~/.claude/skills/usadebusk-estimating/SKILL.md:165` (read this run) | Observed | Current per-diem rule: `Per Diem \| Daily per person \| 1 PD per 12-hr shift` — confirms the model prices per diem on a shift-count basis today, matching the note's description of what was quoted, and confirms finding (3) targets a real, currently-unaddressed line in the skill. |
| `~/.claude/skills/usadebusk-estimating/SKILL.md` (grepped this run for "pig unit", "blended", "103.50") | Observed | No company-wide blended pig-unit cost figure or per-size pig cost table found in the skill. The $103.50/$90.00 pair traces only to the DSP26071 quote line (`02-facilities/ExxonMobil/Baytown-TX/DSP26071.md:110`) as a job-specific materials line, not a skill-level default — so finding (1), if actioned, would need to establish whether a size-mix-based pig cost belongs in the skill at all or stays a per-contract quote decision. |
| `01-context/estimating-approach.md` and rig-in/rig-out tier rule (per DQ-009's 2026-08-15 closure, referenced not re-read in full this run) | Observed | The rig-in/rig-out mirroring rule was itself corrected 2026-08-15 (DQ-009) on a *different* defect (a missing third driver — pump mode) than what this note raises (a duration/second-shift risk on a specific equipment profile). The two are not the same question; DQ-009's closure does not cover finding (2). |
| `git log --oneline -i --grep="USA26041" --grep="per.diem" --grep="pig.unit"` (checked this run) | Observed | No commit modifies `usadebusk-estimating` in response to any of these three findings; all USA26041-related commits since 2026-08-15 touch only `02-facilities/` job/card content, `04-knowledge/estimating-actuals-rollup.md`, and the job-report generator — confirms the cost-model question is genuinely unaddressed, not just unfound in prose. |

## The Question

Should any of the three USA26041 model-level findings (pig-unit cost built from a real size mix instead of one blended rate; a rig-out duration correction for the six-launcher/triple-mode/filtration-plus-smart-pig profile; per-diem priced off calendar days on site rather than shift count) modify `usadebusk-estimating` now, or does n=1 (Condition `first`) mean all three sit as tracked, revisit-triggered observations until a second data point exists — and if any should move now, which one(s)?

## Proposed Change

**A. Hold all three at n=1 — no skill change now.** Matches the vault's established pattern (DQ-005 rejected a numeric derate at n=5 for the same reason; the note's own rig-out figure is already filed with "Condition `first`, n=1, so it does not move the routine baseline"). Add a `revisit-trigger:` to the source note (or a successor) keyed to the next comparable job — six-launcher/triple-mode/filtration-plus-smart-pig profile for rig-out, any job with itemized pig receipts for the pig-unit question, any multi-day T&M job for per diem.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**B. Move the per-diem basis now, hold the other two at n=1.** Finding (3) is arguably not a sample-size question at all — "calendar days on site" vs. "shift/person-day count" is a structural billing-model choice, and the note's arithmetic (4 calendar days vs. a 2-day quote assumption) demonstrates the shift-count basis mis-estimates duration risk on jobs that run T&M beyond plan, independent of how many data points exist. Findings (1) and (2) are genuinely single-job cost/duration observations that fit the n=1-hold pattern more cleanly.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**C. Move all three now.** Rejected by the note's own framing (explicitly asks whether n=1 is enough) and by precedent (DQ-005), but included for completeness since the pig-unit real-cost breakdown is unusually well-evidenced (six itemized receipt costs, not an estimate) even at n=1.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

Option A's risk is the one the source note itself flags — three real findings sit unused indefinitely if no comparable job lands soon, and unlike the routine-ft/hr baseline (which has a machine-checked `[machine: routine-rows]` threshold), none of these three has a defined "enough data" trigger beyond "a second data point," which is vaguer than the vault's other n-gated decisions and risks going quiet the way DQ-012's first revisit-trigger did before being pinned harder. Option B's risk is treating a structural-vs-statistical distinction as clean when it may not be — a single job's calendar-days-vs-shift-count gap could itself be job-specific (an unusually long mobilization) rather than a systematic modeling gap, and the note does not establish that calendar-day pricing would have priced this job correctly, only that shift-count pricing under-priced it. Option C's risk is the most direct: acting on n=1 cost/duration data is exactly the pattern DQ-005 rejected, and the pig-unit and rig-out findings, however well-evidenced their arithmetic, are still one job's shape — the note itself calls the rig-out profile a "profile to carry the correction into" (future tense), not a correction to make today. None of the three options resolve the pig-unit question's prerequisite noted in Source Material — whether a size-mix pig cost belongs in the skill at all, or stays a per-contract quote decision — that sub-question is upstream of "does this reach the model" for finding (1) specifically.

## Decision

*(Pending — Jesse to review.)*

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-17 | Note filed by pre-staging loop from `00-inbox/2026-08-15-usa26041-estimating-feedback.md`. Checked for existing coverage: change-log entries from 2026-08-15 record the same actuals as facts on the job card (with n=1/Condition-`first` caveat already applied to the rig-out/pigging figures) but do not touch `usadebusk-estimating`; the per-diem shift-basis rule and the absence of a company-wide pig-unit cost table were confirmed by reading the skill directly; DQ-009's 2026-08-15 rig-in/rig-out fix was confirmed to address a different defect (missing pump-mode driver) than this note's duration-risk finding. `git log` grepped for prior estimating-model commits addressing any of the three findings — none found. `decision-queue.md` checked — not already queued. No vault or config-repo content modified beyond the source marker. | Claude (pre-staging loop) |
