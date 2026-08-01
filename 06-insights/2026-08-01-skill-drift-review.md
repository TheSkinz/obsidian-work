---
type: review
status: resolved
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

Five findings and one open question: one regression-suite (F1, proposed on the branch), three vault-side (V1–V3), one memory-side (M1, read-only, flagged only). No finding is proposed without a quoted line.

**The loop itself wrote only this note and the branch.** V1 was raised as a finding with no edit proposed, per the loop's zero-authority-over-vault-content rule. Jesse then ruled on it in the same session, and V2 and V3 were found and applied by that interactive session under his ruling — not by the loop. The Apply Log distinguishes them.

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

### V1 · process-flow.md states Rig-In/Rig-Out durations the SOP skill explicitly forbids stating — MEDIUM · Lane 4 (estimating/domain-truth) — **RESOLVED**

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

**RESOLVED 2026-08-01, in session.** Jesse ruled: *"No need to mention durations for a document / concept intended to give a general explanation on a task. Giving a specific number would imply all scopes / rig-in times are the same. They are not."* Both lines now carry the SOP skill's own construction with no figure. The ruling is general, so a sweep applied it to one sibling instance and corrected one factual descendant of the same root cause — see the Apply Log.

### V2 · industry-foundation.md states a passivation circulation duration — LOW · Lane 2

`04-knowledge/concepts/industry-foundation.md:59` (before this session):

> - Duration: typically 4–6 hours

Same defect class as V1, in the stainless passivation parameter list. **Evidence it is stale rather than deliberate:** `04-knowledge/manual/15-ancillary-passivation-stainless.md:27-33` carries this same parameter table — target pH, circulation velocity, final condition, governing specification — and drops the duration row entirely, consistent with `00-manual-index.md:21`'s explicit no-durations rule. The concepts note was never updated when the manual was built. **Applied 2026-08-01** under V1's ruling; the remaining four bullets now match the manual.

### V3 · _cost-model.md asserts a fixed 6-hr rig-out on every job — MEDIUM · Lane 4 (pricing analysis)

`04-knowledge/pricing/_cost-model.md:113` (before this session):

> Rig-out is a fixed ~6 hr event on essentially every job, so the error is small per job but systematic across all of them.

Not a general-explanation document, so V1's ruling does not reach it — but it carries the same claim in its strongest, most universalizing form, and it is wrong on the merits against `usadebusk-estimating/SKILL.md:68`'s current fallback tiers (Small 4 / Moderate 6 / Large 8 / Very large 12) and the launcher-elevation tiering that replaced the flat default. Same root cause as V1: both predate the tiered model.

The sentence is sizing the dollar impact of the rig-out/stand-by rate-link anomaly, so the argument had to survive. **Reworded, not deleted,** 2026-08-01 — the anomaly finding itself is untouched.

---

## Part 2b — Deliberately not changed

`04-knowledge/concepts/decoking-method-comparison.md:26` states `| Cleaning window | ~18–24 hr (coker) |`. This surfaced in the same sweep and was **left alone deliberately.** It is a third-party attributed benchmark — Marathon Petroleum via AFPM Question 74, web-verified 2026-07-22 and quoted verbatim at that file's line 40 — not USADebusk stating its own scope duration, and it is load-bearing for the pigging-vs-steam-air argument. That file's line 48 explicitly directs "Use only the verified ~18–24 hr pigging figure (AFPM)" as a guard against uncorroborated inflated case-history numbers. Removing it would gut the document's purpose and re-open the door that guard closes. Recorded here so a future sweep does not re-litigate it.

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

**1. Does USADebusk ever supply the soda ash?** Surfaced while editing the passivation block for V2, and not settleable from files. `04-knowledge/concepts/industry-foundation.md:56`:

> Customer typically provides soda ash or pre-mixes. **USADebusk can supply if required.**

Against `~/.claude/skills/usadebusk-core/SKILL.md:105`:

> USADebusk doesn't supply the soda ash or perform the passivation, and does not provide or mix the soda ash / low-chloride water — **it's customer scope, end to end.**

And `04-knowledge/manual/15-ancillary-passivation-stainless.md:29`: `| Solution | Soda ash, customer-supplied and customer-mixed |`.

Two recent and deliberate surfaces say customer-only; one older surface, inherited from the Master Reference decomposition, says USADebusk can supply. This is Lane 4 domain truth, so **no edit was made** — the duration removal (V2) landed regardless, since it is independent of who supplies the material. If customer-only is correct, `industry-foundation.md:56` needs its last sentence dropped. If USADebusk genuinely can supply on request, then `usadebusk-core`'s "end to end" overstates it and the fix runs the other direction, as a config-repo branch change rather than a vault edit.

**RESOLVED 2026-08-01, in session — and neither branch of that guess was right.** Jesse: *"In a generalized document, don't mention who provides it. Context: We've provided it in the past, but it's not something I want to do. I made the rule that the customer always supplies it because when the rule wasn't in place you flagged or questioned it in almost everything we worked on. The instances where we supply and mix the soda ash is so rare with complications over the customer's preferences that I wanted to avoid the conversation all together."*

Three things follow, and the middle one is the reason this finding was worth raising:

1. **`industry-foundation.md:56` drops the provider question entirely** — both the "customer typically provides" sentence and the "USADebusk can supply if required" sentence. A generalized document does not name a provider at all. Applied.
2. **`usadebusk-core:105` is a behavioral rule, not a factual claim, and it is correct as written.** USADebusk *has* supplied soda ash historically. The rule exists because without it the model flagged or questioned supply in nearly every piece of work, and the real-world cases are rare enough — and tangled enough in customer preference — that Jesse wants the conversation avoided rather than surfaced. **A future drift run that finds historical evidence of USADebusk supplying soda ash must not read that as core being wrong.** The skill is deliberately stating the operating rule, not the full factual picture.
3. **The manual's `| Solution | Soda ash, customer-supplied and customer-mixed |`** (`manual/15-ancillary-passivation-stainless.md:29`) was **left alone** — it is a customer-facing deliverable, which per global CLAUDE.md is not modified without explicit confirmation, and there it functions as a scope statement to the customer, which serves the same avoid-the-conversation goal. Raised with Jesse separately rather than changed.

---

## Decision

- [x] **F1:** merge `drift/2026-08` (single README.md hash correction) — approved and merged 2026-08-01
- [x] **V1:** ~~decide the reframing approach~~ — **ruled 2026-08-01:** general-explanation documents state no task durations at all. Applied to process-flow.md, and swept to V2 and V3.
- [x] **V2 + V3:** applied under V1's ruling — see Apply Log
- [x] **Open question 1 (soda ash supply):** ruled 2026-08-01 — generalized documents name no provider; `usadebusk-core`'s rule is behavioral and stands. See Part 4.
- [x] **M1:** `/consolidate-memory` run 2026-08-01 — index corrected to six loops, and the pass retired 2 merged-away files, closed a stale "open item" in the harness-audit memory that today's ruling had overtaken, and captured both of this session's rulings as new memories

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-01 | **V1 applied** — process-flow.md lines 9 and 31 | Claude | Both headers now read `*(fixed event — hours and scheduling belong to the estimate, not this note; see the Duration Model in usadebusk-estimating)*`, mirroring `usadebusk-sop/SKILL.md:12` verbatim so the two surfaces read as one rule. Dropped the "6 hrs" figures, the rejected pass-count driver, and the Mob/Demob 12-hour disambiguation, which existed only to guard a number that no longer appears. |
| 2026-08-01 | **V2 applied** — industry-foundation.md:59 | Claude | `- Duration: typically 4–6 hours` deleted. The remaining four passivation bullets now match `manual/15-ancillary-passivation-stainless.md`'s parameter table exactly. |
| 2026-08-01 | **V3 applied** — _cost-model.md:113 | Claude | Reworded, not deleted, so the rate-link anomaly's impact argument survives: "Rig-out runs a handful of hours on any job (the no-job-walk fallback tiers span 4 to 12 hrs)". The anomaly finding itself is untouched. Flagged as Lane 4 because it sits in the cost model, though no rate or margin figure changed. |
| 2026-08-01 | **decoking-method-comparison.md:26 left unchanged** | Claude | Deliberate. Third-party AFPM/Marathon benchmark, web-verified, load-bearing for the steam-air comparison, and protected by that file's own line 48. Recorded in Part 2b so a future sweep does not re-litigate it. |
| 2026-08-01 | **Soda-ash supply contradiction flagged, not fixed** | Claude | Lane 4 domain truth, not settleable from files. Filed as Part 4 open question 1. V2 landed independently of it. |
| 2026-08-01 | **Open question 1 ruled; industry-foundation.md:56 stripped of provider language** | Claude | Both provider sentences removed — a generalized document names no provider. `usadebusk-core:105` left unchanged and recorded as a *behavioral* rule rather than a factual claim, so a future run does not "correct" it on historical evidence. Manual left alone (customer-facing deliverable). |
| 2026-08-01 | **`drift/2026-08` merged to config `main`** | Claude | Jesse approved. Single-commit branch (`db558d3`, F5 hash correction). Merged, not rebased; branch retained per the vault-wide deletion ban. |
