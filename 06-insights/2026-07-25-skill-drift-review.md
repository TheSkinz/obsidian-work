---
type: review
status: open
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

**Evidence:** the vault carries two Canadian sites under exactly this convention — `02-facilities/Suncor/Montreal-QC/` and `02-facilities/Syncrude/Fort-McMurray-AB/` — and the same skill supports Canada elsewhere: `SKILL.md:412` has `job_number: [USA##### or CND##### or null]` and `:413` has `job_region: [US | CA | null]`. The rule as written covers neither `QC` nor `AB`, and its example list "(TX, LA, OK, CA, etc.)" now carries a live ambiguity, since `CA` reads as California in a US list and as Canada in the `job_region` field two sections down.

**Proposed:** widen the format to state-or-province, name the Canadian abbreviations explicitly with a pointer to `job_region`/`CND#####`, add `Fort-McMurray-AB` and `Montreal-QC` to the examples, and drop the bare `CA` from the US example list.

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

- [ ] **F1–F6:** merge `drift/2026-07b` as-is
- [ ] **F1–F6:** merge partially — note which findings to drop in the Apply Log
- [ ] **F4 held back** (Lane 4 — answer open question 1 first), rest merged
- [ ] Discard the branch — reason in the Apply Log
- [ ] **V1:** resolution 1 (keep scheduled, add heartbeat + fix spec) / resolution 2 (disable the task)
- [ ] **V2–V4:** approve the vault-side fixes as proposed
- [ ] **M1–M2:** run `/consolidate-memory`

---

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| | | | |
