---
type: review
status: resolved
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-08
related:
  - "[[2026-07-28-f6-rig-tier-decision]]"
tags: [review, knowledge-system, regression, estimating, fixture]
---

# Review — Should F6's rig-in tier ambiguity be closed by amending the fixture or by ruling the tier?

## Trigger

Pre-staging loop run 2026-08-08, processing `00-inbox/2026-07-28-f6-rig-tier-decision.md` — the oldest unprocessed candidate by git first-commit time (`2026-07-28 21:53:59`, ahead of the same-day `quote-notes-go-stale-against-their-own-bid-folder.md` at `22:29:01`).

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-07-28-f6-rig-tier-decision.md` (read this run) | Observed | States the fixture is synthetic (ExxonMobil Beaumont F-42 does not exist; every real ExxonMobil card in the vault is Baytown), so there is no live commercial exposure. Frames the open item as a fixture-authoring miss, not a knowledge gap: the launcher-access paragraph added 2026-07-25 in `98ac964` was meant to make the rig tier derivable but instead reads two ways (Large vs. Very large). Proposes two closing options — amend the fixture to a run distance in feet, or rule the tier as judgment — and recommends amending, but explicitly defers the choice ("it is not mine to do unasked") since it changes a quoted duration. |
| `~/.claude/regression/fixtures/f6-duration-mobdemob-input.md:21-25` (read this run) | Observed | The job-walk paragraph in question: connection points "approximately 8 ft above grade — no crane required," but "TriMax set-out is well back from the heater; a long hard-pipe and hose run is needed to reach all six launcher positions." Elevation reads low-tier; run distance across six positions reads high-tier — confirms the inbox note's description of the ambiguity verbatim. |
| `~/.claude/regression/frozen/f6-duration-mobdemob-output.md:14` (read this run) | Observed | The frozen baseline's own `open_tier_selection_question` field: "NARROWED, still not closed. Jesse's figure for this heater shape is rig-in 12; this baseline computes 10 (Large 8 + fitter 2). Across four post-patch readings the tier has come back Large three times and Moderate once." Confirms the inbox note's four-replay, three-to-one split and the Jesse-vs-baseline mismatch (12 vs. 10) exactly. |
| `~/.claude/regression/frozen/f6-duration-mobdemob-output.md:82-101` (read this run) | Observed | The frozen reasoning for landing on Large (8 hrs): "One driver low, one driver high... Above Moderate (6) because the run length and six discrete launcher positions are real build work; below Very large (12) because there is no crane and no elevated hanging." This is the specific judgment call the ambiguity forces on every replay. |
| `50-dashboards/decision-queue.md` (checked this run) | Observed | DQ-002 (closed 2026-07-22) captured the general rig-in tier scale (4/6/8/12) from Jesse, but nothing in the closed or open rows addresses this specific F6 fixture-wording ambiguity — not already covered. |
| `04-knowledge/vault-skill-drift-loop-spec.md:39` (grepped this run) | Observed | Confirms the regression suite is an audited-but-never-edited surface for the skill-drift loop and that F6 has drifted before (a 2026-07-25 finding on retired equipment in its frozen output) — establishing this fixture as one the vault already tracks for staleness, though tier wording specifically has not been flagged there. |
| `change-log.md` (grepped this run, no post-2026-07-28 F6 entry) | Observed | No decision recorded since the note was filed; the tier question is still open eleven days later. |

## The Question

Should F6's ambiguous launcher-access paragraph be **amended** to make the rig-in tier deterministic (e.g. stating a run distance in feet, at the cost of the fixture no longer exercising tier *selection*), or should the tier be **ruled as judgment** (recording which tier the current wording should select, so F6 keeps testing judgment under acknowledged ambiguity) — or is a third option, leaving it as an accepted source of noise, preferable to changing a fixture that also drives a quoted duration?

## Proposed Change

> **RESOLVED 2026-08-15 — none of A/B/C. All three rejected; see the Decision section.** All three options assume the ambiguity lives in the fixture's wording. It does not: the tier *rule* was missing its dominant driver. Fixing the rule made the fixture derivable without amending it.

**A. Amend the fixture — replace the qualitative run-distance language with a stated figure (or state the tier outright).** Matches the source note's own recommendation and finishes what `98ac964` (2026-07-25) set out to do: make the rig tier derivable from the rule rather than left to free judgment. Removes a documented four-hour swing between replays that the regression battery cannot currently detect as a defect. Cost: F6 stops exercising tier-selection judgment, one of the few fixtures that currently does.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**B. Rule the tier as judgment — record the expected reading and let F6 keep testing it.** Requires deciding, on the existing wording, whether Large (8, matching 3 of 4 replays and the frozen baseline) or Very large (12, matching Jesse's own stated figure for this heater shape) is the correct reading, then encoding that as the expected diff key. Preserves F6 as a judgment-under-ambiguity fixture but leaves the Jesse-vs-baseline mismatch (12 vs. 10) unresolved unless Very large is the ruling.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**C. Leave it open, no fixture change.** The swing is bounded (Large vs. Very large, never wider) and already documented in the frozen output's own `open_tier_selection_question` field with instructions not to fail a future run for reading it either way, provided both drivers are named and reasoning requirements hold. Zero cost, but the note's own framing — this is the largest remaining source of legitimate re-diff in the duration fixture — argues against leaving a known, fixable ambiguity as permanent noise.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

Option A's risk is the one the source note names directly: it changes what F6 measures, trading a judgment-call fixture for a deterministic one, and the fixture also underlies a quoted duration, so amending it is not purely a testing-infrastructure decision. Option B's risk is that it requires Jesse to adjudicate Large vs. Very large on a synthetic, non-existent heater (Beaumont F-42) — a real-sounding judgment call with no real job walk behind it, which may not be worth his time relative to just fixing the wording. Option C's risk is the note's central point: a fixture whose whole job is duration arithmetic currently carries a rig line that can swing four hours between runs for a reason the battery cannot tell apart from a genuine model error, which erodes the value of F6 as a regression signal. All three options are low operational risk (synthetic fixture, no live commercial exposure per the note's own confirmation) but the choice does determine what F6 continues to measure going forward.

## Decision

**Resolved 2026-08-15 (Jesse, in session). A — Rejected. B — Rejected. C — Rejected.** The premise shared by all three was wrong. The fixture wording is fine; the rig-tier rule in `usadebusk-estimating` was incomplete, listing only two drivers (elevation, run distance) when there are three. The missing driver is **mode** — pumps utilized, which sets circuit-line and spool count, which sets how much hose gets built.

That gap is the entire 12-vs-10 divergence. Under the two-driver rule F6 reads as one driver low (8 ft walk-up) and one high (long run), so every replay split the difference at Large 8 + fitter 2 = 10. F6 is 2× Trimax — six pumps, twelve circuit lines, six launchers and six receivers, the largest hose build the fleet runs. Counting mode, the drivers do not offset; they multiply, and the tier is Very large.

Three domain facts recorded this session, all Jesse:

1. **Mode is the third tier driver.** A circuit line is a run of connected hoses from a pumper port to one launcher or receiver connection. Single = 1 pump / 2 lines / 2 spools; double = 2 pumps / 4 lines / 4 spools; triple = 3 pumps / 6 lines / 6 spools. Hoses are 17 ft, hard pipe 20 ft, a 60 ft run takes ~4–5 hoses **per line**.
2. **The three drivers multiply, they do not offset.** Elevation adds to run length (60 ft out + 60 ft up = a 120 ft run, doubling hose per line); mode multiplies the result by line count.
3. **Rig-in never exceeds 12 hrs and rarely exceeds 8.** Very large is a ceiling, not a rung reached by accumulation. The pipefitter adder therefore stacks *inside* the cap — a Very large tier with a fitter wait is 12, not 14.

**F6's figures under the corrected rule:** rig-in 12, rig-out 12 (full mirror), pigging 17, rig-over 0, smart pig 4 → raw 45, landing 48 with a +3 adjustment. The mid-band shift-landing diagnostic no longer fires (45 sits 3 below the boundary, outside the middle third), which independently corroborates the read — the tier was doing the work the +7 pad was covering for. Mob/demob are unaffected.

**Triple-mode hose count — flagged, then closed.** Jesse first gave triple as 12–15, which contradicted his own primitives (6 lines × 4–5 hoses at a 60 ft run = 24–30); single and double were both internally consistent at 4–5 per line, so only the triple row broke the pattern. Raised in session as a likely arithmetic slip and the disputed total was withheld from the skill pending confirmation. **Jesse confirmed the slip same session — 24–30 is correct.** The per-mode figures at a 60 ft run are now written into the skill: single 8–10, double 16–20, triple 24–30, each doubling when the run doubles.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-15 | Resolved. A/B/C all rejected; root cause was a missing driver in the tier rule, not fixture wording. Edited `~/.claude/skills/usadebusk-estimating/SKILL.md` in three places: added mode as the third rig-tier driver with the circuit-line/hose primitives and the multiply-don't-offset framing; added the 12-hr rig-in cap with the "rarely above 8" calibration; amended the pipefitter-adder rule to stack inside the cap. Fixture left untouched. **Consequence not yet actioned: F6's frozen baseline is now stale** — rig-in 10→12, rig-out 10→12, raw 41→45 — and needs a replay and re-promotion; the regression suite is audited-but-never-edited, so this was not done unasked. | Claude (with Jesse in session) |
| 2026-08-08 | Note filed by pre-staging loop from `00-inbox/2026-07-28-f6-rig-tier-decision.md`; confirmed via `~/.claude/regression/fixtures/f6-duration-mobdemob-input.md` and `~/.claude/regression/frozen/f6-duration-mobdemob-output.md` that the ambiguity, the four-replay split, and the Jesse-vs-baseline (12 vs. 10) mismatch are all as described in the source note. `50-dashboards/decision-queue.md` checked — DQ-002 covers the general tier scale, not this fixture-specific ambiguity, so not already covered. No vault or config-repo content modified beyond the source marker. | Claude (pre-staging loop) |
