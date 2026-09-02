---
type: review
status: open
review_type: skill-drift
source_authority: primary
confidence: high
created: 2026-09-01
review_after: 2026-10-01
related:
  - "[[vault-skill-drift-loop-spec]]"
  - "[[2026-08-01-skill-drift-review]]"
  - "[[_canonical-heater-card]]"
tags: [review, skill-drift, skills, knowledge-system]
---

# Skill-Drift Review — 2026-09-01

## Trigger

Scheduled fire of the `vault-skill-drift-loop` task. Window: everything since the last `skill-drift:` heartbeat commit `d72d770` (2026-08-01 03:14), which closed the prior run's findings. Read: all 10 skills under `~/.claude/skills/` plus every reference file, the vault knowledge-layer commits in the window (`01-context/`, `04-knowledge/`, `06-reviews/`, `07-llms/`, `08-systems/`, both CLAUDE.md files — roughly 40 commits, 2026-08-01 through 2026-08-25), `04-knowledge/estimating-actuals-rollup.md`, the regression suite (`README.md`, `fixtures/`, `frozen/` frontmatter), and the agent memory directory.

Config repo was clean on `main` at start (`git -C ~/.claude fetch` + `status --porcelain` returned nothing). The prior branch `drift/2026-08` is unmerged, but its review note [[2026-08-01-skill-drift-review]] carries `status: resolved` — a terminal status, so per the loop spec's Branch States table it is a record and not a backlog. Branch creation was **not** skipped. This run's branch is `drift/2026-09`; the name was free.

**Six findings, two memory flags, one open question.** Two of the six touch the regression suite, three touch skills, one is a dead string. No finding is stated without a quoted line.

The count of skills is 10, not the 9 the memory file and `07-llms/claude/code.md` still assume — `skills/adhd/` was added by config commit `e4bb5b8`. See M2.

---

## Part 1 — Regression-suite drift

### F1 · Two frozen baselines require a rule that was struck eight days later — HIGH · **report only, no edit proposed** · Lane 4 (estimating domain truth)

This is the failure mode the loop spec names in its own words: *"A frozen output encoding a retired rule does not fail loudly; it silently redefines a regression as the standard."* It has now happened on the two fixtures that carry the duration model.

`~/.claude/skills/usadebusk-estimating/SKILL.md:62` (current, canonical):

> ⚠ **Dead rule — flag and correct on sight: the "25–40% parallel-friction allowance."** … **Striking it does not reopen the variance problem — zero is more deterministic than a range.** An estimate that marks a parallel set up over the bare coil rate is wrong, not cautious.

and `:98`:

> ⚠ **Removed 2026-08-23 — the whole-shift landing rule and its mid-band diagnostic.** … **Do NOT adjust a project total to a multiple of 12.**

Against that, `~/.claude/regression/frozen/f6-duration-mobdemob-output.md:25` (diff key 4, the thing a replay is judged on):

> (4) parallel-friction allowance stated with reasoning and sitting inside the 25-40% band;

`:24`:

> `friction_factor_note:` The allowance is a written 25-40% band (Jesse, 2026-07-28), not the model's own unsourced figure. This baseline sits at the 40% CEILING … A future run anywhere in 25-40% with a stated reason is a PASS.

`:92` and `:122`, where it is baked into the numerics:

> **Allowance position: 40%, the top of the 25–40% band.**
> `| Pig — one set, all 6 passes, 40% parallel allowance | 17 |`

`~/.claude/regression/frozen/f1-proposal-output.md:19`:

> `friction_note:` The allowance is a written 25-40% band, applied to any pass set carrying more than one circuit … This baseline sits at 30% … A future run anywhere in 25-40% with a stated reason is a PASS.

`:18`, where it is welded into the fixture's most load-bearing arithmetic:

> The rounding sequence is FIXED and explicit … Coil round-up first (1,120 / 85 = 13.18 to 14), then the parallel-friction allowance on that ROUNDED figure (14 x 1.30 = 18.2), then round the set elapsed up (to 19).

and `:123` / `:146`, the struck shift-landing rule as a line item:

> `shift-landing adj.       +2      [stated as its own step, never folded into a task line]`
> `| Trimax Pumper | 48 | Rig-in 6 + Pig 33 + Rig-over 1 + Rig-out 6 + shift-landing 2 | $500.00/hr | $24,000.00 |`

**Evidence and consequence.** A replay that correctly applies the current skill — no allowance, no landing adjustment — fails F1 diff keys 4 and 8 and F6 diff key 4, and misses the frozen numerics on the Pig line, the Trimax line and the project total. The detector is inverted: correct behavior now reads as a regression, and the only way to "pass" is to reproduce a rule the skill flags as dead. F1's inversion is the worse of the two because the allowance sits inside the rounding sequence the file calls "the single most load-bearing arithmetic in this fixture," so the error propagates into every downstream dollar figure rather than sitting on one line.

Third, smaller: `frozen/f6-duration-mobdemob-output.md:16` cites a skill passage that no longer exists —

> usadebusk-estimating's **shift-landing section** carries a worked example naming this fixture and its answer ("Read the same connection description as Very large - which is how Jesse reads that heater shape, at rig-in 12")

There is no shift-landing section in the skill any more, and that quoted sentence is absent from it. The multiply illustration it also cites *did* survive, at `SKILL.md:80`.

**No edit is proposed to anything under `frozen/`.** Re-cutting a baseline is your call and requires a judged clean replay first, per the suite's own "When to re-cut frozen/". What the loop can say is that both fixtures are unjudgeable against the current skill until that happens, and the health dashboard's `behind` rows for f1 and f6 understate it — this is not "unverified," it is "verified wrong."

Recommended sequence if you take it: replay F6 first (smaller, one struck rule, one line moves), judge, re-cut; then F1 (two struck rules, rounding sequence changes, most numerics move).

**Decision:**
- [ ] Re-cut F6 and F1 from judged replays against current skills
- [ ] Re-cut F6 only for now; leave F1
- [ ] Leave both; the README caveat below is enough of a warning
- [ ] Something else: ______

### F2 · README's per-fixture commit table names F6's promotion commit, not its skill commit — MEDIUM · Lane 2 · **proposed on branch**

`~/.claude/regression/README.md:52-53`:

> …always read the `model:` and `skills:` frontmatter of the specific file you are diffing against — F1 @ `a8cc6fd`, F6 @ `ebb1217`, F2 @ `f20db13`, F3 @ `4ec2d76`, F4 @ `396d8b2`, F5 @ `28827d3`.

`frozen/f6-duration-mobdemob-output.md:5-6`, authoritative per this same README's rule at `:56-57` ("the frontmatter, not this table, is authoritative"):

> `skills:` usadebusk-core, usadebusk-estimating (claude-config @ `60e86c7` — `4f34b94` added mode as the third rig-in driver and the 12-hr cap, `60e86c7` confirmed the per-mode hose counts).
> `baseline_commits:` claude-config @ `60e86c7` -- skills/usadebusk-core, skills/usadebusk-estimating

**Evidence.** `git -C ~/.claude log -1 ebb1217` returns *"regression: promote F6 from the 2026-08-15 judged run — rig lines corrected, quote unchanged"* — the commit that wrote the frozen file, not the skill state it was cut against. `60e86c7` is *"rig-in tier: per-mode hose counts confirmed"*, which is what the frontmatter names. Every other entry in the table matches its file's frontmatter; F6 is the only mismatch. This is the third instance of the same defect in this one table (F1/F6 before 2026-07-28, F5 corrected 2026-08-01), and the README documents the fix rule at `:54-58` already.

**Proposed:** `F6 @ \`60e86c7\``.

**Decision:**
- [ ] Accept
- [ ] Reject — reason: ______

### F3 · README H1 carries the dead string `USADeBusk` — LOW · Lane 2 · **proposed on branch**

`~/.claude/regression/README.md:1`:

> `# USADeBusk Skill Regression Suite`

`~/.claude/skills/usadebusk-core/SKILL.md:9`:

> **Name:** USADebusk — house spelling of the closed form, **never `USADeBusk`** (dead string; Jesse, 2026-07-27, reversing the 2026-07-12 skill-drift ruling).

**Proposed:** `# USADebusk Skill Regression Suite`.

**Not touched, deliberately:** `fixtures/f4-sop-input.md:36` and `fixtures/f6-duration-mobdemob-input.md:13,25` also carry `USADeBusk`, and `fixtures/f1-rfq-input.md:25` / `f6:14` carry `TriMax`. Those are **replay inputs** — editing them changes what a run reads and would silently alter the spelling delta the README rules an expected pass at `:195-206`. The README H1 is prose with no replay consequence, so only it is proposed.

**Decision:**
- [ ] Accept
- [ ] Reject — reason: ______

### F1-side · README caveat naming the two stale baselines — LOW · Lane 2 · **proposed on branch, separable**

A factual note added under the README's existing "Known spelling diff" pattern, stating that F1 and F6 encode the struck allowance and landing rules, naming the affected diff keys, and pointing at "When to re-cut frozen/" for the decision. It touches no file under `frozen/` and takes no position on whether to re-cut. Drop this commit if you would rather the README stay silent until F1 is decided.

**Decision:**
- [ ] Accept
- [ ] Reject — reason: ______

---

## Part 2 — Skill-vs-vault and skill-vs-skill drift

### F4 · `usadebusk-fieldpm` still teaches "crash means a dirtier coil" — MEDIUM · Lane 4 (domain truth) · **proposed on branch**

`~/.claude/skills/usadebusk-fieldpm/SKILL.md:206`:

> **Coil condition — always capture, it is the highest-value field the report carries.** Heater coils foul about the same way decoke to decoke under routine service, so a job's hours predict the next job's hours *only when the condition matches*. **A crashed/upset furnace runs significantly dirtier**, and its hours must never be used to estimate a routine clean.

`:207`:

> 1. **Job condition** — routine (normal service fouling) or crash (furnace was crashed/upset). An emergency mobilization is a crash. This becomes the `Condition` column on the heater card's Task Durations row.

The canonical home corrected this on 2026-08-20 under DQ-026. `04-knowledge/_canonical-heater-card.md:241-244`:

> `crash` = UNSCHEDULED MOBILIZATION. The facility hit operational trouble and needed a crew cleaning on a moment's notice. **It is a callout label, NOT a fouling grade** (Jesse, 2026-08-20) — the coil is usually dirty, but not by definition, and this column does not record how dirty.

`:272-275`:

> NEVER estimate a routine job from crash rows, or a crash mob from routine rows — they are different job classes and their hours are not interchangeable. **That prohibition stands on its own; it does not rest on a claim that crash coils are dirtier**, which is not something this table measures.

Two defects, both in `:206-207`. First, the retired mechanism — fieldpm asserts as fact ("runs significantly dirtier") the exact claim the canonical card says the prohibition does *not* rest on, and which `usadebusk-estimating:96` and `04-knowledge/estimating-actuals-rollup.md:47` both retired. Second, the vocabulary: fieldpm offers the field as a two-value choice, while the canonical column is four — `routine` | `crash` | `first` | `unknown` (`_canonical-heater-card.md:240-248`). A `/report` run following fieldpm has no way to record a first-ever clean or an unrecoverable class, and `_canonical-heater-card.md:334` is explicit that `unknown` must be written rather than `routine` inferred.

This is class (d) — corrected in its canonical home while the restatement in the skill that *feeds* that column still carries the old version. It matters more than most pointer drift because `/report` is the upstream of the `Condition` value, not a downstream reader of it.

**Proposed:** rewrite `:206-207` to carry the callout-label reading and the four-value vocabulary, pointing at `04-knowledge/_canonical-heater-card.md` as canonical. Full text on the branch.

**Decision:**
- [ ] Accept
- [ ] Reject — reason: ______

### F5 · `/report` never captures the per-coilset hours three other surfaces read it for — MEDIUM · Lane 3 · **proposed on branch**

Class (b) — two skills contradicting each other about what the job report contains.

`~/.claude/skills/usadebusk-estimating/SKILL.md:34`:

> The rollup carries per-job heater totals, so the spread is not visible there: **go to the card's Field Notes or the job report for per-coilset hours.**

`~/.claude/skills/usadebusk-vault-ingest/SKILL.md:389`:

> **Capture per-coilset hours AT INGEST, while the source's own duration tables are still structured** — this is the one step that cannot be recovered later. **When the job report or ticket breakdown breaks hours out by coilset or by rig-and-coilset**, fill `## Coilset Durations` in the same pass…

And the schema section they both serve, `04-knowledge/_canonical-heater-card.md` `## Coilset Durations` (added 2026-08-21, DQ-017), whose columns are Coils / Rig / Mode / Circuit ft / per-task hours / Coil condition / Flag.

Against all three, `usadebusk-fieldpm/SKILL.md:204-210` — the `/report` input list and its explicit "always capture" block — asks for exactly two things beyond the ticket breakdown: job condition and a prose **Per-coil abnormality** narrative at `:208`:

> 2. **Per-coil abnormality** — which specific coils, if any, were abnormally coked, plugged, or notably cleaner than the rest, and how that showed up (pig sizes that stalled, stuck pigs, hours spent). **Per-coil elapsed durations alone don't say *why* one coil took twice another.**

`grep -rn -i "coilset" skills/usadebusk-fieldpm/` returns nothing: not in `SKILL.md`, not in `references/report-structure.md`, not in `scripts/README.md`. So the skill that produces the job report never asks for the per-set hours, while the ingest skill is told to harvest them from that report and warned the step is unrecoverable, and the estimating outlier check (`SKILL.md:34`, Jesse 2026-08-20) is told to go read them there. The Syncrude 48 / 35 / 36 spread that rule was written from was recovered by hand, not from a structured table.

**Proposed:** add per-coilset hours (as a table, with each set's `Coil condition` on the `light | moderate | heavy | unknown` vocabulary) as a third mandatory capture item in `/report`, alongside the existing abnormality narrative — the numbers and the "why" are complementary, and `:208`'s own sentence says so. Full text on the branch.

**Decision:**
- [ ] Accept
- [ ] Reject — reason: ______

### F6 · `usadebusk-vault-ingest` hardcodes `USA#####` where the vault uses any job number — LOW · Lane 3 · **proposed on branch**

`~/.claude/skills/usadebusk-vault-ingest/SKILL.md:190` states the contract:

> `<!-- Derived from 04-knowledge/_canonical-heater-card.md. Keep in sync. -->`

The exemplar's Field Notes heading is generic:

> `### <Job # — Month Year>`  (`04-knowledge/_canonical-heater-card.md`, `## Field Notes` block)

The skill's is not. `:373` (template body), `:388` and `:411` (the ingest rules):

> `### [USA#####] — [Month Year]`
> Job report ingest fills one `## Task Durations` row (actuals) AND appends a `### USA##### — Month Year` Field Notes subsection…
> Append a new `### USA##### — Month Year` subsection under `## Field Notes` for the narrative only…

and `:398`:

> Job reports (USA#####) are dissolved into heater cards…

Live cards already disagree. `02-facilities/Syncrude/Fort-McMurray-AB/7-1-F-1.md:259` and `:283`:

> `### CAD24002 — April 2024 TA`
> `### CAD25004 — September 2025`

The skill knows about CAD# elsewhere — `:85` ("`CAD#####` job numbers in the Frontmatter Template"), `:104` ("Same for `USA#` and `CAD#`"), `:451` (`job_number: [USA##### or CAD##### or null]`) — so this is internal inconsistency, not an unrecorded fact. It becomes live in the next few weeks: CAD26001 mobilized 2026-08-25 and its actuals land on the same card that already carries two CAD Field Notes subsections.

**Proposed:** generalize the four `USA#####` occurrences at `:373`, `:388`, `:398`, `:411` to the job number. `:391` ("Field Notes entries require a real job number") is already correct and is untouched.

**Decision:**
- [ ] Accept
- [ ] Reject — reason: ______

---

## Part 3 — Agent memory (read-only; this loop never edits memory)

Both flagged only. Recommended action for both: run `/consolidate-memory`.

### M1 · The memory asserts six live loops; three are deprecated

`~/.claude/projects/C--Users-Jwuts-obsidian-work/memory/project-vault-five-loop-system.md`, description line:

> "Vault now runs SIX loops (Capture, Agent/Review, Idea Research, Pre-Staging, Skill-Drift, Consolidation) — schedules, heartbeats, and the first-run approval caveat"

body:

> The obsidian-work vault runs six governance loops (three → five on 2026-07-07, → six on 2026-07-28) … **Capture Loop** — scheduled **daily ~5am** … **Idea Research Loop** — scheduled nightly ~2am … **Pre-Staging Loop** — scheduled daily ~6am

Contradicted by the vault. `04-knowledge/vault-capture-loop-spec.md`, `vault-idea-loop-spec.md` and `vault-prestaging-loop-spec.md` all carry `status: deprecated` (commit `93d85dd`, 2026-08-24, *"Mark the three stopped loop specs deprecated"*), and commit `46c0771` (2026-08-21) is *"schedule the review loop monthly; retire the six-loop story from context."* `50-dashboards/health.md` renders three loop rows — Consolidation, Review, Skill-drift — not six.

### M2 · The memory says 9 skills; there are 10

`memory/project-usadebusk-claude-arch.md`:

> **9 skills** in `~/.claude/skills/` … usadebusk-core, -equipment, -estimating, -fieldpm (dormant between mobilizations), -ops, -sop, -vault-ingest, plus adversarial-review and idea-triage.

`ls -d ~/.claude/skills/*/ | wc -l` returns **10**. The missing one is `adhd`, added by config commit `e4bb5b8` (*"output-styles: thin reinforcer style; vendor adhd as a command-only skill"*). Same file also carries the dead string `USADeBusk` four times, including in its description and its **How to apply** line.

Not a memory finding but worth carrying with it: `07-llms/claude/code.md:191` makes the same nine-skill assumption — *"fieldpm is still the longest description — 806 chars against `usadebusk-estimating`'s 577, **checked across all nine***." That is vault content and outside this loop's write authority; it is noted here, not proposed.

---

## Open question

**OQ1 · `usadebusk-fieldpm`'s dormancy banner names a job two mobilizations back.**

`~/.claude/skills/usadebusk-fieldpm/SKILL.md:5`:

> "Dormant — no active mobilization (last active: USA26038, HF Sinclair Navajo H19/H20, demobbed 2026-07-17)."

Since then the vault records USA26041 (ExxonMobil Baytown F-501, completed 2026-08-14, Jesse ran the job) and CAD26001 (Syncrude 7-1 F-1, mob 2026-08-25, rig-in 08-26) — `01-context/active-jobs.md`.

I did not propose an edit, for two reasons. First, "last active" is ambiguous between *the last job* and *the last job this skill was used on*, and `07-llms/claude/code.md:189` records that the skill's lifetime invocation counter was zero because its frontmatter would not parse until 2026-07-28 — so under the second reading the string may be literally correct and there is no file that settles which was meant. Second, the same note at `:191` rules explicitly against touching this field: *"Not trimmed: editing the exact field that silently disabled the skill for three weeks is not worth 17 tokens."*

What would settle it: your reading of the phrase. If it means the last mobilization, the string is two jobs stale and CAD26001 raises the separate question of whether `status: dormant` is still right at all.

---

## Apply Log

*(empty — for Jesse)*
