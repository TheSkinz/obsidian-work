---
type: review
status: resolved
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-07
related:
  - "[[2026-07-28-instruction-density-second-fixture]]"
tags: [review, knowledge-system, regression, skills, tooling]
---

# Review — Should the F4 (SOP) instruction-density arm test run, and when?

## Trigger

Pre-staging loop run 2026-08-07, processing `00-inbox/2026-07-28-instruction-density-second-fixture.md` — the oldest unprocessed candidate by git first-commit time (`2026-07-28 17:08:32`, ahead of the same-day `f6-rig-tier-decision.md` at `21:53:59` and `quote-notes-go-stale-against-their-own-bid-folder.md` at `22:29:01`).

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-07-28-instruction-density-second-fixture.md` (read this run) | Observed | The F5 (pig sizing) instruction-density arm test found Arm C — `usadebusk-equipment` with corrective/behavioral scaffolding stripped, data and rules retained, 16% smaller — matched the incumbent on every binding numeric and diff key, while Arm B (core only, domain skill withheld) failed outright. States explicitly this is n=1, one fixture, not actionable, and proposes F4 (SOP) as the second fixture needed before any trim pass is licensed. |
| `~/.claude/regression/f5-instruction-density-arm-test-2026-07-28.md` (read this run) | Observed | Full methodology: three arms, identical fixture body/framing/model/delivery, blinded (no Skill tool, no regression/vault access, diff keys withheld). Arm C's one error (misidentifying the convection as Sch 80) traced to a pre-existing gap in core's dimension table, not the ablation — "direct evidence that one run carries enough variance to produce a wrong card value." |
| `~/.claude/regression/runs/claude-opus-5/` directory listing (checked this run) | Observed | Contains `f5-density-a-2026-07-28.md`, `f5-density-b-2026-07-28.md`, `f5-density-c-2026-07-28.md` — no `f4-density-*` files of any kind. `f4-rebaseline-2026-07-28.md` exists but is the standard fixture-replay/rebaseline (verifying F4 still matches current skill content), not the three-arm density ablation; it does not answer this question. |
| `~/.claude/regression/README.md:116` (grepped this run) | Observed | F4's fixture map row: `sop (+core, equipment) + vault formatting standard` — SOP structure, doc numbering, phases, callouts, no-em-dash rule. Confirms F4 loads a different skill (`usadebusk-sop`) and a non-numeric pass bar (structural/formatting conformance, not binding numerics), matching the inbox note's own framing of why it's the right second fixture rather than a repeat of F5. |
| `~/.claude/regression/README.md:39,67,70` (grepped this run) | Observed | F4 is already Opus-5-baselined and was re-swept 2026-07-28 (`be98772`) — the standard regression battery, unrelated to the density-ablation question, is current. |
| `07-llms/prompt-engineering.md` (grepped this run, no line match) | Observed | No mention of a completed F4 density arm test or a trim-pass decision. The file's existing caution (corrective instructions worth keeping are the ones verifying inputs, not re-checking outputs) is the standing counter-consideration the inbox note itself flags — unchanged since 2026-07-28. |
| `change-log.md` (grepped this run, no post-2026-07-28 match) | Observed | No later entry records an F4 arm test, a trim pass, or a decision to drop the finding. The 2026-07-28 entry documents the original F5 test and the mechanized fixture-replay-guard hook, nothing past that date. |
| `00-inbox/2026-08-01-*-owed.md` (three files, read this run) | Observed | The vault's existing pattern for approved-but-unexecuted work: each carries an `approved-unexecuted` tag and a `-owed` filename, created only after a decision-queue row was explicitly closed approving the work (e.g. DQ-004 → `2026-08-01-thesis-v2-rerun-owed.md`). This inbox item carries neither the tag nor that provenance — it has not yet been through a decision, which is why it triages as a genuine open question rather than pre-approved owed work. |

## The Question

Should the F4 (SOP) instruction-density arm test run now — replicating the F5 methodology (incumbent / core-only / corrective-stripped, blinded, 3 model calls) against `usadebusk-sop`'s non-numeric structural pass bar — to get the second data point the F5 result explicitly requires before any trim pass is considered, or is a single n=1 result (plus the inverse-direction architecture finding from the 2026-07-24 `adversarial-review` arm test) enough to leave the finding open and untouched?

## Proposed Change

**A. Run the F4 arm test now, same protocol as F5.** Three blinded Opus 5 calls against the `f4-sop-input.md` fixture: incumbent (`usadebusk-sop` + core + equipment + formatting standard), floor (core only), ablated (corrective/behavioral instructions stripped, data and rules retained). If Arm C matches incumbent on structural conformance the same way F5's did, the finding graduates from n=1 to n=2 across two different skills, two different pass-bar shapes (numeric vs. structural) — the bar the source note itself set for "worth a trim pass." If it doesn't match, the trim idea is closed on evidence rather than left to decay.

- [x] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**B. File as owed work, run opportunistically — no queue decision needed.** Tag it `approved-unexecuted`, rename with a `-owed` suffix matching the three existing precedents (`2026-08-01-baseline-staleness-detector-owed.md`, `2026-08-01-coil-visualization-build-owed.md`, `2026-08-01-thesis-v2-rerun-owed.md`), and let it run whenever a session has spare capacity, same as the thesis v2 re-run. Lowest ceremony, matches the vault's own established pattern for "worth doing, not urgent."

- [ ] Approved
- [ ] Approved with edits
- [x] Rejected
- [ ] Needs more research

**C. Drop it — leave the finding at n=1 and untouched.** The counter-evidence already on file (2026-07-24 `adversarial-review` arm test: architecture ranked in exact inverse order of scaffolding density) points the same general direction as caution, not confidence, and `07-llms/prompt-engineering.md` already carries the standing rule that input-verifying corrective instructions are worth keeping. A second fixture only sharpens a conclusion nobody is currently acting on — no trim pass is scheduled or proposed anywhere in the vault.

- [ ] Approved
- [ ] Approved with edits
- [x] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

Option A's cost is real but bounded — three model calls against an existing, already-staged fixture, not new infrastructure; the F5 run for comparison took under an hour end to end per its `runs/` timestamps (16:07–16:29). Its risk is the same one the source note names for F5: a single additional run is still low-powered, and a second n=1 does not, by itself, license a 165 KB trim across nine skills — it only clears the bar the note set for *starting* that conversation, not for finishing it. Option B's risk is that "owed work" items accumulate without a forcing function — three already sit unexecuted in `00-inbox/`, and this vault's own change-log (DQ-004) shows an "owed" item can go a week or more before anyone runs it, which is fine for low-stakes housekeeping but means the F5 finding stays uncorroborated for an indefinite stretch. Option C's risk is the one already stated in the source note: dropping it means a genuinely encouraging result (Arm C matched every binding numeric and diff key on F5) never gets tested against a second skill shape, and the next time someone reaches for the F5 result to justify a trim, it will still be exactly as thin as it is today.

## Decision

**Resolved 2026-08-15 (Jesse, in session). A approved and executed the same day; B and C rejected.**

B was rejected because the note's own risk paragraph is right about owed work — three `-owed` items already sit unexecuted in `00-inbox/`, and this is three model calls against a fixture that already exists, not a build. Rationing it into a queue that has a demonstrated backlog would have left the F5 finding uncorroborated indefinitely for no saving. C was rejected because the test was cheap enough that "a second fixture only sharpens a conclusion nobody is acting on" stops being an argument once running it costs ~150 seconds.

**Result: F4 replicates F5 exactly.** Full write-up at `~/.claude/regression/f4-instruction-density-arm-test-2026-08-15.md`.

- **Arm B failed**, the same way and for the same reason. Without `usadebusk-sop` and the formatting standard it invented its own document number, its own 11-section order, its own footer boilerplate, and produced no title-block grid and no color scheme.
- **Arm C matched arm A** on every structural conformance key — document number, short-form DOCUMENT NO. cell, 2×4 title block, 9 sections in canonical order, Phase I/II/III procedure, controlled-document footer wording, gold/charcoal scheme — and on every binding numeric, including the 4.250" max pig OD and its 4.026 + 0.250 = 4.276 ceiling arithmetic.
- **C produced *more* judgment-call flags than A** (13 vs 11), so the trap condition — a stripped skill silently dropping flagging discipline — did not fire, replicating F5.
- **Both stripped guardrails held without their instruction text.** The firewater "never surface it as a flag" framing was removed and C still wrote the 2" hose as a plain customer-scope line item rather than an open question. The lodged-pig hard suppression gate was removed and C never referenced `SOP-OPS-LODGE-001`, and correctly omitted the plug-header module on the grounds that this coil has cast 180s.
- **Arm B degraded honestly again** — its opening line names the missing file and its closing line calls that gap "the single biggest risk in this deliverable." Two for two on the standing observation.

**What this changes.** The finding is now n=2 across two skills, two output shapes, and two pass-bar types (numeric on F5, structural on F4), which is exactly the bar the F5 note set. It still does not license a trim pass across nine skills — two clean results are two runs, and F5's own Sch 80 error is on record as evidence that one run carries enough variance to produce a wrong value. The defensible next step is narrower than a trim pass: the strips that proved **redundant with a rule that was retained** (the RFWN corrective, "do not state durations here" alongside the Rig-In/Rig-Out fixed-event labels, "Never assume" alongside the Required Inputs list) are the cheap, low-risk candidates, because in each case the rule already carries the behavior and the corrective only restates it. That is left as an open item, not adopted here.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-15 | Approved and executed. Staged blinded scratchpad copies of the four reference files, built arm C by 29 exact-match strips (each asserted to have matched, so a silent no-op could not pass as a completed ablation), and ran three parallel blinded Opus 5 agents with no Skill tool, no web access, and no read access to `~/.claude/skills/`, `~/.claude/regression/`, or the vault. Arm C is 46,222 bytes against arm A's 51,823 — 10.8% overall, 19.9% on `usadebusk-sop` itself, bracketing F5's 16%. `usadebusk-equipment`'s share of the strip re-applies F5's own documented removal list verbatim so the shared material is ablated identically across both tests. Wrote the full result to `~/.claude/regression/f4-instruction-density-arm-test-2026-08-15.md`. F4's frozen output deliberately **not** re-promoted — promotion is Jesse's call and arm A is a blinded reference, not a standard replay. | Claude (review queue) |
| 2026-08-07 | Note filed by pre-staging loop from `00-inbox/2026-07-28-instruction-density-second-fixture.md`; confirmed via `~/.claude/regression/runs/claude-opus-5/` directory listing, `README.md`'s fixture map, `07-llms/prompt-engineering.md`, and `change-log.md` that no F4 density arm test has run and no trim-pass decision has been made since the source note was filed ten days ago. No vault content modified beyond the source marker. | Claude (pre-staging loop) |
