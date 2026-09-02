---
type: review
status: decided-blocked
review_type: skill-drift
source_authority: primary
confidence: high
created: 2026-07-25
review_after: 2026-08-25
related:
  - "[[vault-skill-drift-loop-spec]]"
  - "[[2026-07-12-skill-drift-review]]"
  - "[[_canonical-job-sheet]]"
  - "[[quote-lifecycle]]"
  - "[[estimating-actuals-rollup]]"
tags: [review, skill-drift, skills, knowledge-system]
---

# Skill-Drift Review — 2026-07-25 (Second Run)

## Trigger

Automated fire of the `vault-skill-drift-loop` scheduled task at 2026-07-25T18:05Z. Window: everything since the last `skill-drift:` heartbeat commit `bdd33fe` (2026-07-18), which closed the first run's 13 findings. Read: all 9 skills under `~/.claude/skills/` plus every reference file, the vault layers changed in the window, `04-knowledge/estimating-actuals-rollup.md`, both CLAUDE.md files, and the agent memory directory.

Config repo was clean on `main` at start. The prior `drift/2026-07` branch is **merged** into `origin/main` (`git log origin/main..origin/drift/2026-07` is empty), so it is not a stale outstanding branch and branch creation was not skipped. Because this is the second run inside the same calendar month and `drift/2026-07` is taken, this run's branch is **`drift/2026-07b`** — a deliberate deviation from the spec's `drift/YYYY-MM` naming, flagged here rather than reusing a merged name.

Twelve findings: six skill-side (proposed on the branch), four vault-side, two memory-side. No finding is proposed without a quoted line.

---

## Part 1 — Skill drift (proposed on branch `drift/2026-07b`)

### F1 · vault-ingest still says the job-sheet type is unformalized — MEDIUM · Lane 2

`usadebusk-vault-ingest/references/document-routing.md:10`:

> `doc_type:` `other` until the job-sheet type is formalized (see the `job-sheet-type-formalization` idea seed).

And the `doc_type` enum at `usadebusk-vault-ingest/SKILL.md:413` has no `job-sheet` value:

> `doc_type: [job-note | heater-card | facility-overview | sop | change-order | pre-job-package | procedure | policy | inspection-report | data-sheet | proposal | quote | reference | field-report | other]`

**Evidence:** the type was formalized 2026-07-18. `04-knowledge/_canonical-job-sheet.md:2` opens `type: job-sheet` and its header comment reads "This file is the schema authority for all job sheets in the vault"; `templates/_job-sheet-template.md` exists; `04-knowledge/concepts/quote-lifecycle.md:57` states "Schema authority: [[_canonical-job-sheet]]; template: `templates/_job-sheet-template.md`". The seed `00-inbox/2026-07-11-job-sheet-type-formalization.md:3` carries `status: researched`, and the research note's Apply Log records both files created on 2026-07-18.

**Proposed** (routing line): `doc_type:` `job-sheet`. Schema authority: `04-knowledge/_canonical-job-sheet.md`; template: `templates/_job-sheet-template.md` (formalized 2026-07-18). **Proposed** (enum): insert `job-sheet` after `heater-card`.

### F2 · estimating's billing-math block points at the live instance, not the canonical — MEDIUM · Lane 2

`usadebusk-estimating/SKILL.md:361`:

> Conventions for reading or building a per-heater work-up billing table (established USA26038, 2026-07; live exemplar: `02-facilities/HF-Sinclair/Artesia-NM/USA26038-job-sheet.md` in the vault):

**Evidence:** the same six billing rules now live as authoritative field-generation rules in the schema authority, `04-knowledge/_canonical-job-sheet.md:117-129` ("WORK-UP BILLING MATH (authoritative — derived from the USA26038 work-up, 2026-07-11)"). The two copies agree on all six rules — this is a stale pointer, not a value conflict. The canonical carries one rule the skill omits, `_canonical-job-sheet.md:131`:

> Filter Unit appears only when filtration was elected. Omit the row on non-filtered jobs rather than carrying it at zero.

**Proposed:** repoint the parenthetical to `04-knowledge/_canonical-job-sheet.md` as canonical home with the USA26038 sheet named as the live instance, and extend the equipment-lines bullet with the filtration-election condition.

### F3 · fieldpm's dormancy banner carries the wrong demob date — LOW · Lane 1

`usadebusk-fieldpm/SKILL.md:5`:

> description: Dormant — no active mobilization (last active: USA26038, HF Sinclair Navajo H19/H20, demobbed 2026-07-20).

**Evidence:** `02-facilities/HF-Sinclair/Artesia-NM/USA26038-job-report.md:9` — `execution: 2026-07-10 to 2026-07-17`; the report body at `:32` reads "July 10–17, 2026, two TriMax pumpers (3 & 5) with filtration." `01-context/active-jobs.md:17` records the job Completed `2026-07-17`.

**Proposed:** `demobbed 2026-07-17`. **Open question if 07-20 was deliberate:** if the equipment physically returned on the 20th and the 17th is only the last shift, say so and the banner should read `job complete 2026-07-17, demobbed 2026-07-20` rather than being silently changed.

### F4 · two skills disagree on whether a second filter press exists — MEDIUM · **Lane 4** (equipment/commercial domain truth)

`usadebusk-estimating/SKILL.md:111`:

> It is never a given: a second press is conditional on room at the unit and on one being uncommitted that month across concurrent jobs, and there is no larger press — the filter press in `usadebusk-equipment` is the only unit.

`usadebusk-equipment/SKILL.md:124`:

> Filtration scales conditionally: 2× filter presses + 2× 4×3 pumps when customer requires it AND a 2nd press is available; otherwise 1× shared filter press + 1× shared 4×3 pump serving both TriMax units

**Evidence:** three surfaces presuppose more than one physical press — the equipment skill's "a 2nd press is available", the estimating skill's own "one being uncommitted that month across concurrent jobs", and `04-knowledge/equipment/equipment-library.md:69` which is headed "USADeBusk Filter Press **#1** specs". Read strictly, "the only unit" contradicts all three. The sentence almost certainly means there is no larger-capacity *model*, but as written it reads as a fleet count of one, and an estimator reading only the estimating skill would conclude a second press is impossible rather than conditional.

**Proposed:** "…and there is no larger press — the filter press spec'd in `usadebusk-equipment` is the only model in the fleet, so more capacity means a second press, not a bigger one." This preserves both stated facts and removes the count reading. **Lane 4 — do not treat the reword as settled until Jesse confirms the fleet actually holds more than one press** (see Open Questions).

### F5 · vault-ingest's city-state rule has no province case, but the vault has Canadian sites — LOW · Lane 2

`usadebusk-vault-ingest/SKILL.md:82-88`:

> Format: `[City-hyphenated]-[2-letter-state-abbrev]`
> - Use standard 2-letter state abbreviation (TX, LA, OK, CA, etc.)
> - Never spell out the state name
> - Examples: `Ponca-City-OK`, `Garyville-LA`, `Port-Arthur-TX`, `Corpus-Christi-TX`

**Evidence:** the vault carries two Canadian sites under exactly this convention — `02-facilities/Suncor/Montreal-QC/` and `02-facilities/Syncrude/Fort-McMurray-AB/` — and the same skill supports Canada elsewhere: `SKILL.md:412` has `job_number: [USA##### or CAD##### or null]` and `:413` has `job_region: [US | CA | null]`. The rule as written covers neither `QC` nor `AB`, and its example list "(TX, LA, OK, CA, etc.)" now carries a live ambiguity, since `CA` reads as California in a US list and as Canada in the `job_region` field two sections down.

**Proposed:** widen the format to state-or-province, name the Canadian abbreviations explicitly with a pointer to `job_region`/`CAD#####`, add `Fort-McMurray-AB` and `Montreal-QC` to the examples, and drop the bare `CA` from the US example list.

### F6 · core lists Jesse's role as PM; global CLAUDE.md calls that title stale — MEDIUM · Lane 1

`usadebusk-core/SKILL.md:13`:

> - **Key roles:** Jesse (technical sales, PM, proposals, estimation); Jason VP (named on some customer-facing docs)

**Evidence:** global CLAUDE.md, "Who I am": "Jesse Utsey — technical specialist at USADeBusk… I run the full workflow cycle: technical sales, proposals, estimating, engineering-document analysis, and field ops. Treat me as a high-autonomy operator who wants direct, correct answers, not a 'Project Manager' who needs hand-holding (that title is stale)."

**Proposed:** "- **Key roles:** Jesse (technical specialist — technical sales, proposals, estimating, engineering-document analysis, field ops); Jason VP (named on some customer-facing docs)".

**Scope guard — do not over-apply.** The field **PM** who completes service receipts per 12-hour shift (`usadebusk-ops/SKILL.md:9`, `usadebusk-fieldpm` `/setup` and `/report`) is a different role held by a different person (USA26038's PM was Dacorey Slater). Only the Jesse line changes. The vault carries the same stale title at `01-context/company-context.md:17` — "Jesse Utsey (jutsey@usadebusk.com): Technical sales, project management, proposal development…" — which is vault content and outside this loop's edit authority; listed in Part 2 as V4.

---

## Part 2 — Vault-side drift (no branch; this loop does not edit vault content)

### V1 · The loop spec says this loop is unscheduled and unmonitored; the scheduler says otherwise — HIGH

`04-knowledge/vault-skill-drift-loop-spec.md:28`:

> **On-demand only** — say "run the Skill-Drift Loop" in a session. Runbook prompt: `~/.claude/scheduled-tasks/vault-skill-drift-loop/SKILL.md` (the task is registered but disabled, so it can still be started manually).

`:30`:

> Because it is no longer scheduled, it is not heartbeat-tracked in `tools/vault_health.py` — a silent scheduler is not a failure for an on-demand loop.

**Evidence:** the scheduler reports `vault-skill-drift-loop` as `"enabled": true`, `"cronExpression": "0 3 1 * *"`, `"nextRunAt": "2026-08-01T08:02:05.000Z"` — and this review exists because the task fired automatically at `"lastRunAt": "2026-07-25T18:05:49.051Z"`. Meanwhile `tools/vault_health.py:51` still reads "The review/agent and skill-drift loops are on-demand by design and not listed", and its `LOOPS` table at `:61-66` carries only Capture, Idea-research and Consolidation — confirmed by `50-dashboards/health.md`, which shows three loop rows, not four.

**Why it matters:** this is not a documentation nit. An *enabled monthly* loop with no heartbeat row is the exact blind spot the run ledger was built to close — if it silently stops firing, nothing in the vault notices, and the spec tells a future reader that silence is expected. Note also the scheduler's own task description still reads "run manually — needs config-repo write access that is deliberately not pre-granted", which the automated fire has now falsified.

**Two coherent resolutions, Jesse's call — this loop proposes neither:**
1. **Keep it scheduled.** Update the spec's Trigger and the "Why not scheduled (2026-07-19)" paragraph to say scheduled-monthly, add the loop to `vault_health.py`'s `LOOPS` (heartbeat prefix `skill-drift:`, cadence 31 d), fix `:51`/`:371` and the scheduler task description.
2. **Restore on-demand.** Disable the scheduled task so the spec becomes true again.

The 2026-07-19 reasoning behind option 2 is still sound on its own terms (git mutation authority is scoped to the vault; permission rules cannot be scoped to a branch). What is not tenable is the present state, where the task is enabled and the spec says it is disabled.

### V2 · Half of an already-approved fix never landed — MEDIUM

`04-knowledge/equipment/equipment-library.md:181`:

> No hydrant. 1× or 2× TriMax variant. 2× = 2 filter presses, 2 trash pumps (shared or mirrored).

**Evidence:** finding V3 of `06-insights/2026-07-12-skill-drift-review.md` quoted both this line and line 61, and proposed "replace **both** spots with the conditional rule"; the decision block records "V1–V8: approve vault-side fixes as proposed — applied 2026-07-18". Line 63 now carries the conditional rule correctly — "Filtration scales conditionally: 2× filter presses + 2× 4×3 pumps when the customer requires it AND a 2nd press is available" — but line 181 still asserts it unconditionally, which is the original self-contradiction the finding was raised to remove.

**Proposed:** "No hydrant. 1× or 2× TriMax variant. On 2×, filtration scales conditionally — see the Second TriMax section above."

### V3 · estimating-pricing.md names the $58.00 line "Driver Travel"; the skill says drivers have no travel-labor line — LOW

`04-knowledge/concepts/estimating-pricing.md:68`:

> | Mob/Labor | Driver Travel | $58.00 | Hour |

**Evidence:** `usadebusk-estimating/SKILL.md:136` labels the same rate "| Mob/Labor | Crew Travel (non-driver) | $58.00 | Hour |", and `:66-69` states "The $3.00/mile includes driver labor (drivers carry no separate travel-labor line)" with `:77-80` making the $58.00 line explicitly the non-driver rate and "the only travel-labor rate on it, since drivers are covered by the mileage line above." Applying the vault's label would double-bill driver travel.

**Proposed:** rename the row to "Crew Travel (non-driver)".

### V4 · company-context.md carries the stale "project management" title — LOW

`01-context/company-context.md:17`:

> - **Jesse Utsey (jutsey@usadebusk.com):** Technical sales, project management, proposal development, cost estimation, field ops support

Same evidence as F6 (global CLAUDE.md: "that title is stale"). Fix alongside F6 so the two surfaces do not diverge again.

---

## Part 3 — Agent-memory drift (read-only; flagged, never edited by this loop)

Both findings sit in the same file, `~/.claude/projects/C--Users-Jwuts-obsidian-work/memory/project-vault-five-loop-system.md`. **Recommended action: run `/consolidate-memory`** — this loop has no authority to edit memory files.

### M1 · Memory claims four heartbeat-tracked loops; there are three

`:19`:

> `vault_health.py` (heartbeats for all 4 scheduled loops + "review notes awaiting decision" metric…)

`:27`:

> health.md (generated 2026-07-21) shows all four scheduled-loop rows ok, no heartbeats overdue.

**Evidence:** `tools/vault_health.py:61-66` defines three `LOOPS` entries (Capture, Idea-research, Consolidation) and `:51` states the skill-drift loop is deliberately not listed. `50-dashboards/health.md:25-27` renders three rows. This is the same underlying confusion as V1 and should be reconciled in whichever direction Jesse decides there.

### M2 · Memory carries a stale lint-rule count

`:19`:

> `vault_lint.py` (9 rules incl. ORPHAN; REVIEW-OVERDUE + SUPERSEDED added 2026-07-18 as the "self-obsolescence detection" mechanical slice…)

**Evidence:** `tools/vault_lint.py:538-541` enumerates eleven rules — `OP-FRONTMATTER, DEAD-LINK, SECRET, STATUS-VOCAB, CONF-CONFLICT, INBOX-AGE, ORPHAN, REVIEW-OVERDUE, SUPERSEDED, DURATIONS-HEADER, POINTER-DEAD`. `POINTER-DEAD` was added 2026-07-23 (commit `708c6ba`). The vault's own CLAUDE.md already rules against carrying this number anywhere but the script — "rule set defined by and authoritative from the script itself — no count here to drift" — so the fix is to drop the count from memory, not to update it to 11.

---

## Part 4 — Open questions (not settleable from files; no edits proposed)

1. **Does the fleet hold more than one filter press?** Three surfaces presuppose yes, one clause says no (F4). The proposed reword assumes "only model, not only unit." If the fleet genuinely holds exactly one press, then `usadebusk-equipment:124`'s conditional 2× filtration and estimating's "uncommitted that month across concurrent jobs" are both wrong instead, and the fix runs the other direction.
2. **Was USA26038's demob 07-17 or 07-20?** (F3.) The job report gives execution as 07-10 to 07-17; the skill banner says demobbed 07-20. If both are true — last shift on the 17th, equipment home on the 20th — the banner should say both.
3. **Scheduled or on-demand for this loop?** (V1.) A judgment call about where config-repo write authority should sit, not a fact this loop can look up.

**Already tracked elsewhere — no action here:** the two F6-fixture divergences in `00-inbox/2026-07-25-f6-divergences-awaiting-adjudication.md` (rig tier Large vs Moderate; non-driver travel $64 vs $58) are open Lane 4 adjudications from the Opus 5 regression battery, not drift. This run deliberately proposes nothing that touches the rig tier or the travel-rate precedence rule.

---

## Decision

- [ ] ~~**F1–F6:** merge `drift/2026-07b` as-is~~ — rejected; two findings did not survive verification
- [x] **F1–F6:** merge partially — F1, F2, F5, F6 applied to `main` by hand; **F3 rejected**, **F4 held**. Details in the Apply Log.
- [x] **F4 held back** (Lane 4 — answer open question 1 first), rest merged
- [ ] ~~Discard the branch~~ — branch retained, unmerged, as the record of what was proposed
- [x] **V1:** resolution 1 (keep scheduled, add heartbeat + fix spec) — *and* the stated reason for resolution 2 was found to be factually false; see Apply Log
- [x] **V2–V4:** approve the vault-side fixes as proposed — V2 and V4 applied; **V3 held as Lane 4** (pricing-table label)
- [x] **M1–M2:** ~~run `/consolidate-memory`~~ — corrected directly instead; both were single-line factual fixes

**Adjudicated 2026-07-25 by Claude (Opus 5), in session, against live files.** Every "current text" quote in Part 1 was re-read on `main` before its proposal was considered; all six matched verbatim, as did every piece of supporting vault evidence. Nothing was accepted on the note's word alone.

---

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-07-25 | **F1 + F5 applied** to config `main` (`9c8068a`) | Claude | Cherry-picked `32b96e5` whole — the only branch commit accepted unchanged. Job-sheet `doc_type` + enum, and the state-or-province rule. |
| 2026-07-25 | **F2 applied** to config `main` (`dad1c06`) | Claude | Hand-applied, not cherry-picked: branch commit `7ab4ee5` carried F2 and F4 together and F4 is held. Billing-math block repointed to `_canonical-job-sheet.md`; filtration-election rule added. |
| 2026-07-25 | **F6 applied partially** to config `main` (`9c020bd`) | Claude | Role line applied as proposed. The branch commit also appended a sentence disambiguating the field-PM role — never proposed in the note, and contrary to its own scope guard ("Only the Jesse line changes"). Dropped. |
| 2026-07-25 | **F3 REJECTED** | Claude | Not verifiable from files. The vault gives last shift and job completion (both 07-17); the physical equipment-return date appears nowhere. The finding's own open question 2 said as much and warned against a silent change — the branch made one anyway. Moved back to an open question for Jesse. |
| 2026-07-25 | **F4 HELD — Lane 4** | Claude | Filter-press fleet count is domain truth. Not applied, not reworded. Remains on the branch only. |
| 2026-07-25 | **V2 + V4 applied** to vault (`a0d6591`) | Claude | V2 repointed line 181 to the Second TriMax section instead of restating the rule, so it holds under either answer to open question 1. V4 title matched to global CLAUDE.md. |
| 2026-07-25 | **V3 applied** to vault | Claude | Held as Lane 4 first, then released on recon: `change-log.md`'s 2026-07-24 entry already records the rename as Jesse's decision ("the `$58.00/hr Driver Travel` rate line was unreachable … it is renamed **Crew Travel (non-driver)**") and names this very file among those the entry touched. It landed in the skill and in `estimating-approach.md` but not in this row — a half-landed approved fix, same shape as V2. Applied on that basis, not as a new pricing call, and flagged to Jesse regardless. |
| 2026-07-25 | **V1 resolved — resolution 1** (`a0d6591`) | Claude | Spec Trigger rewritten to scheduled-monthly; `vault_health.py` now tracks the loop (62 d heartbeat, loose because it commits only on findings); `health.md` regenerated, 4 loop rows, all ok; scheduled-task description updated. |
| 2026-07-25 | **V1 premise found false** | Claude | The spec's reason for staying manual — config-repo write authority "deliberately not pre-granted" — never existed. `settings.json` runs `defaultMode: auto`; `git add`/`commit`/`push` are in neither `allow` nor `deny`; the git-guard hook matches only `USADEBUSK[\\/]`, not `C:\Users\Jwuts\.claude`. That is why the unattended run pushed successfully instead of stalling. Recorded in the spec; the containment is procedural, not permissional. |
| 2026-07-25 | **Loop Scope extended** (`a0d6591`) | Claude | Added `~/.claude/regression/` as drift class 6, with `frozen/` explicitly flag-only — re-cutting a baseline stays Jesse's call and requires a judged clean replay first. Also recorded the `drift/YYYY-MMb` second-run branch-naming convention this run had to improvise. |
| 2026-07-25 | **M1 + M2 corrected** | Claude | `project-vault-five-loop-system.md`: heartbeat count now four and self-describing; lint-rule count dropped rather than updated, per the vault CLAUDE.md rule against carrying it outside the script. |
| 2026-07-25 | **Regression battery replayed** — 5 of 6 pass | Claude | Core changed, so all six ran, fresh-context subagents with frozen output and expected numbers withheld. F2/F3/F4/F5/F6 pass on their own diff keys. **F1 fails diff key 4.** Frozen `frontmatter` note filed below. `frozen/` NOT re-cut. |

## Regression battery — 2026-07-25 post-adjudication

Method per `~/.claude/regression/README.md`: one fresh-context subagent per fixture, regression framing given, `frozen/` and expected numbers withheld, judged against each frozen file's own `notes:` diff keys rather than word identity.

| Fixture | Skills | Verdict | Basis |
|---|---|---|---|
| F1 | estimating, core | **FAIL** | Diff key 4 missed — see below |
| F2 | vault-ingest, core | PASS (1 divergence) | Config Rollup on 6 circuits not 3 passes (60/2,280, 72/2,736, 5,016 ft) exact; max pig OD 4.276; Job # blank; Task Durations left blank per actuals-only; passivation omitted. Job-sheet guard correctly evaluated and *not* matched on a DSP — the F1 skill change behaves. `Borger-TX` normalized cleanly. **Divergence:** derived wall 0.237" was written to the card (marked "(derived)" and flagged) where the baseline requires it deliberately not written. Not caused by this adjudication. |
| F3 | fieldpm, core | PASS | All five diff keys hold — both roster corrections, the 4.1→4.125 autocorrect, the Clean ID conflict surfaced not silently resolved, missing customer signature, refusal to guess the illegible operator. All three required new behaviors present (per-pass split, standby overrun flag, hours reconciliation with math shown). |
| F4 | sop, core, equipment | PASS | All seven diff keys. RFWN correctly omitted per the amended standard. Phase III named "Pass 4 Rig-Over" — permitted; no smart-pig phase inserted. Em-dashes only in the phase headings the standard prescribes. |
| F5 | equipment, core | PASS | Both ID computations exact (5.047", 6.065"); governing ID 5.047"; max OD 5.297" computed and rounded to the stocked 5.250"; two-section ladder split; six judgment calls flagged. Footages 336/610/946/3,784/1,892 all match. |
| F6 | estimating, core | PASS | Mode 6 derived, sets 1, rig-overs 0, per-coil 900/75 with the 5,400/75 serial figure explicitly rejected, friction allowance stated and reasoned, smart pig as one event, per-diem `ceil(2/10)=1`, demob mirrors mob, contradicting actuals flagged not substituted. **Non-driver travel came out at $64.00 → Mob/Demob $3,774.00 each — which the frozen frontmatter's `rate_precedence_correction` states is the correct answer**; the frozen body's $3,738 is preserved-but-wrong. Rig tier Large (8 hrs) vs the baseline's Moderate (6 hrs) remains the open adjudication already tracked in `00-inbox/2026-07-25-f6-divergences-awaiting-adjudication.md`. The 38-vs-31 hour delta is fully accounted for by that tier question plus the permitted friction-figure variance. |

**F1 failure detail.** Intake item 15 enumerates six equipment items (TriMax, support unit, filter press, 4×3 pump, two crew trucks) while stating "(5 pieces traveling)", and the crew note sets drivers equal to pieces at five. Six enumerated against five stated cannot all be true. The frozen baseline catches this, reconciles it (the 4×3 pump rides on the support unit as a skid), prices mob/demob at five pieces, and states the swing if that assumption is wrong ($450 per direction, $900 across both). This replay wrote "No internal inconsistency in the supplied data. All 17 intake items are present" and priced five pieces without noticing the contradiction — absorbing it silently, which is the specific behavior diff key 4 exists to catch. Everything else on F1 matched, including the headline arithmetic exactly (31 pigging hrs, 45 project hrs, 4 shifts) and the serial-basis rejection.

**Not attributable to this adjudication.** The only changes to `usadebusk-estimating` or `usadebusk-core` since F1's baseline commit `bb78eb8` are this run's two edits — the role line and the billing-math pointer — neither of which touches RFQ intake validation. This reads as model variance against an implicit rule. Per the README's own guidance the fix is to make the implicit rule explicit in the skill text, but that is a new commercial-skill edit rather than drift remediation, so it is **left for Jesse's call, not applied here**. `frozen/` was not re-cut.
