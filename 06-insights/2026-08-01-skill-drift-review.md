---
type: review
status: open
review_type: skill-drift
source_authority: primary
confidence: high
created: 2026-08-01
review_after: 2026-09-01
related:
  - "[[vault-skill-drift-loop-spec]]"
  - "[[2026-07-25-skill-drift-review]]"
  - "[[estimating-actuals-rollup]]"
tags: [review, skill-drift, skills, knowledge-system]
---

# Skill-Drift Review — 2026-08-01

## Trigger

Scheduled fire of the `vault-skill-drift-loop` task. Window: everything since the last `skill-drift:` heartbeat commit `d85236f` (2026-07-25), which closed the prior run's 12 findings. Read: all 9 skills under `~/.claude/skills/` plus every reference file, the vault knowledge-layer commits in the window (`04-knowledge/`, `06-insights/`, `07-llms/`, `08-systems/` — roughly 45 commits, 2026-07-25 through 2026-08-01), `04-knowledge/estimating-actuals-rollup.md`, both CLAUDE.md files, the regression suite (`README.md`, `fixtures/`, `frozen/` frontmatter), and the agent memory directory.

Config repo was clean on `main` at start (`git -C ~/.claude fetch` + `status` confirmed). The prior `drift/2026-07b` branch's review note carries `status: decided-blocked` with nothing pending (F1/F2/F5/F6 applied to `main` by hand, F3 rejected, F4 held-then-resolved via `f2b87e4`) — per the loop spec's Branch States table, a terminal-status note means the branch is a record, not a backlog, so branch creation was **not** skipped. This run's branch is `drift/2026-08`.

Three findings: one regression-suite (proposed on the branch), one vault-side (no branch — this loop does not edit vault content beyond this note), one memory-side (read-only, flagged only). No finding is proposed without a quoted line.

---

## Part 1 — Regression-suite drift (proposed on branch `drift/2026-08`)

### F1 · README's per-fixture commit table names the wrong hash for F5 — MEDIUM · Lane 2

`~/.claude/regression/README.md:47` (before this branch):

> F2 @ `f20db13`, F3 @ `4ec2d76`, F4 @ `396d8b2`, F5 @ `589fb1e`.

`frozen/f5-pig-sizing-output.md`'s own frontmatter (authoritative per this file's own stated rule at README.md:50-51, "the frontmatter, not this table, is authoritative"):

> `skills: usadebusk-core, usadebusk-equipment (claude-config @ 2026-07-28, core Common Tube Dimensions 5" row filled to \`5" Sch 40 | 5.563" | 5.047"\`)`
> `supersedes: | claude-opus-5 baseline captured 2026-07-28 @ 589fb1e (the firewater ruleswrite run), recoverable at commit 361ff91's successor.`

`589fb1e` is the baseline F5 **superseded**, not its current one. The commit that actually matches the frontmatter's description — "fill core 5\" row" and a same-day F5 re-promotion — is `28827d3` ("regression: mechanize trigger #2; fill core 5\" row; re-promote F5"), confirmed against `~/.claude/skills/usadebusk-core/SKILL.md`'s Common Tube Dimensions table, which currently reads exactly `5" Sch 40 | 5.563" | 5.047"`.

**Evidence:** `git -C ~/.claude log --oneline` shows `28827d3` sits directly after `589fb1e` in history and its commit message names both actions the F5 frontmatter describes. The README's own text at line 47-51 already documents this exact failure mode happening once before (F1/F6 in this same table) and states the fix rule; the table just wasn't updated for F5's second same-day promotion.

**Applied on the branch:** `regression/README.md:47` corrected to `F5 @ \`28827d3\`` (commit `db558d3` on `drift/2026-08`). No other file touched.

---

## Part 2 — Vault-side drift (no branch; this loop does not edit vault content)

### V1 · process-flow.md states Rig-In/Rig-Out durations the SOP skill explicitly forbids stating — MEDIUM · Lane 4 (estimating/domain-truth)

`04-knowledge/concepts/process-flow.md:9`:

> **Rig-In (fixed event; default 6 hrs, duration varies by pass count and access complexity — see Duration Model in `usadebusk-estimating`. The 12-hour simultaneous Day/Night framing belongs to Mob/Demob, a separate event.)**

and `:31`:

> **Rig-Out (fixed event; default 6 hrs, duration varies — see Duration Model)**

`~/.claude/skills/usadebusk-sop/SKILL.md:12` and `:38`:

> **Rig-In** *(fixed event — hours and scheduling belong to the estimate, not the SOP; do not state durations here)*
> **Rig-Out** *(fixed event — hours and scheduling belong to the estimate, not the SOP; do not state durations here)*

Two separate problems, not one. First, the plain contradiction: the vault note states a duration in exactly the place the skill says never to. Second, even as a citation to the estimating model, it's wrong on the merits — current `usadebusk-estimating` (`SKILL.md:61-68`) explicitly rejects "pass count" as the rig-in driver ("**Tier from the launcher/receiver connection points, not from the heater.** ... Coil footage and pass count have little to do with rig-in") and replaced the flat "6 hrs default" with a four-tier fallback (Small 4 / Moderate 6 / Large 8 / Very large 12) keyed on launcher/receiver elevation and pumper run-distance, settled at the job walk. `process-flow.md` predates both the SOP no-durations rule and the tiered rig-in model and was never updated after either landed.

**Evidence this is already known and open, not new:** `change-log.md`'s 2026-07-31 entry (manual-creation commit `1f5ccbd`) states verbatim: *"Still open: `process-flow.md` lines 9 and 31 keep the 'default 6 hrs' language that contradicts the SOP skill — the manual sidesteps it by omitting durations, but the contradiction is live in the vault and reframing those lines as estimating-model data needs a separate go-ahead."* This finding restates that open item with current line numbers and the additional pass-count problem, since it survived the manual build unresolved.

**Not proposed as an edit** — this is vault content, which is outside this loop's writes, and the change-log entry itself flags it as needing Jesse's go-ahead on the reframing approach (strip entirely vs. reframe as a pointer with no numbers, matching the SOP skill's own phrasing). Surfacing it here so it doesn't keep aging past the person who already flagged it.

---

## Part 3 — Agent-memory drift (read-only; flagged, never edited by this loop)

### M1 · MEMORY.md's index line for the five/six-loop memory is stale against its own topic file

`MEMORY.md`:

> - [Vault Five-Loop System](project-vault-five-loop-system.md) — Capture + Agent/Review + Idea Research + Skill-Drift + Consolidation; heartbeats in health.md; all five have now had a successful run (Consolidation cleared 2026-07-19)

`project-vault-five-loop-system.md`'s own `description:` frontmatter (already correct):

> "Vault now runs SIX loops (Capture, Agent/Review, Idea Research, Pre-Staging, Skill-Drift, Consolidation) — schedules, heartbeats, and the first-run approval caveat"

and its body opens: "The obsidian-work vault runs six governance loops (three → five on 2026-07-07, → six on 2026-07-28)..." — the Pre-Staging Loop (added `d44857c`, 2026-07-28) has its own bullet with schedule and heartbeat detail.

The topic file itself is current. Only the one-line index restatement in `MEMORY.md` still carries the pre-2026-07-28 "five loops" count and doesn't mention Pre-Staging at all — a class-4 (correction-landed-in-canonical-home, pointer-elsewhere-still-stale) pattern surfacing on the memory surface. **Recommendation:** run `/consolidate-memory` to refresh the index line; no edit made from this loop.

---

## Part 4 — Open questions (not settleable from files; no edits proposed)

None this run — the process-flow.md reframing (V1) already has an owner and an explicit "needs a separate go-ahead" flag from the 2026-07-31 change-log entry, so it's carried as a finding rather than a new open question.

---

## Decision

- [ ] **F1:** merge `drift/2026-08` (single README.md hash correction)
- [ ] **V1:** decide the process-flow.md reframing approach (strip durations entirely to match the SOP skill's silence-on-hours convention, vs. reframe as a bare pointer to the Duration Model with no numbers) and apply in the vault
- [ ] **M1:** run `/consolidate-memory`, or dismiss if the index staleness is judged too minor to bother with

## Apply Log

*(empty — awaiting Jesse's decisions above)*
