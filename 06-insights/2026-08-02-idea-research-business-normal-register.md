---
type: review
status: resolved
review_type: idea-research
source_authority: primary
confidence: high
created: 2026-08-02
review_after: 2026-09-02
related:
  - "[[idea-business-normal-register]]"
tags: [review, knowledge-system, idea-research, estimating]
---

# Idea Research — A Register of Business-Normal Facts

## Trigger

Scheduled nightly run of the Vault Idea Research Loop, 2026-08-02. Oldest `unexplored`
idea-seed by `created` date: `idea-business-normal-register` (2026-07-29), ahead of
`idea-rig-layout-diagram` (2026-07-30).

**Gate check.** The seed's `**Gate:**` line reads "None — researchable now." No hidden
gate found in the "To explore" prose. Proceeded to research (case b).

## Evidence

**1. The seed's core question — register vs. distribution — has direct prior art, and it
points at the status quo, not a new artifact.** Static-analysis tooling has faced the same
tradeoff for years: a centralized "baseline" file (PVS-Studio, PHPStan, RuboCop TODO) that
freezes a point-in-time snapshot of accepted warnings, vs. inline suppression at the point
of use. Industry guidance consistently favors inline/point-of-use for exactly the seed's
use case — a human-judged "this is fine, and here's why" that should be visible to whoever
next encounters the same fact — and reserves the baseline-file shape for one-time mass
suppression of *existing* technical debt at adoption time, which is a different problem
(a snapshot to burn down, not an accreting list of standing judgment calls). Jesse's six
(now more, see below) instances are the latter: ongoing judgment calls arriving one at a
time as new jobs are worked, not a fixed backlog to freeze once.

**2. The vault has already converged on the distributed shape independently, four times,
without anyone designing it.** Grepped the skill and vault for the seed's own examples and
found each fix landed as a single point-of-use sentence, not a lookup elsewhere:

| Instance | Where it lives | Marker phrase |
|---|---|---|
| VP-approved PO / USA# / crew / badging | `01-context/active-jobs.md:27` | "not open items" |
| PM = Travis Trenholm | `02-facilities/ExxonMobil/Baytown-TX/DSP26071.md:44` | "Not a discrepancy." |
| Execution date inside customer's window | `~/.claude/skills/usadebusk-estimating/SKILL.md:379` | "not... a discrepancy" |
| Sea-Can Double Pumper naming (same pattern, different domain — equipment, not estimating) | `01-context/equipment-fleet.md:39` | "not a discrepancy" |

All four use the same shape: one sentence, at the exact file a future reader (human or
agent) would land on, naming the fact and explicitly marking it not-a-finding.

**3. The seed's own cited evidence for "distribution drifts" was already fixed the same
day the seed was written, before the seed makes its case.** The seed argues distribution
failed because "the DSP26071 note describe[d] the Trenholm default as *superseded*, which
actively generated a flag." True as of earlier in the day — but `change-log.md:135` (dated
2026-07-29, same day) records that exact defect being caught and rewritten *and* promoted
into a standing `usadebusk-estimating` guardrail so the identical instance can't recur.
Read today, `DSP26071.md:44` already says "Not a discrepancy" — the drift case is closed,
not open.

**4. "Is six a genuine pattern or the tail of one unusual day?" — confirmed genuine, by a
seventh instance the very next day that cost exactly the round trip the seed predicted.**
`change-log.md:141` (2026-07-30, one day after this seed was filed) records a *new*
normal-by-design fact — a shared PO covering both hydroblast and pigging scope under one
agreement across divisions — read as a broken-rule finding and struck down, in the exact
same shape as the original six: "I read exactly that shared PO as evidence the decoke-scope
rule was broken and raised it as a finding when it wasn't." This is now written into
`usadebusk-core`. The pattern is real and ongoing, not a single session's noise — and it
continued to recur even with the six prior fixes already in place, because each fix closes
one instance, not the category.

**5. A register-shaped artifact already exists for the category itself — just not in the
vault.** This assistant's own cross-session memory system (`~/.claude/projects/.../memory/`,
outside the vault) already carries `feedback-someone-elses-pending-work.md`, titled
"Normal-by-Design Isn't a Finding," summarizing exactly this class: "USA#/crew/badging
belong to other queues, VP-approved POs are closed, PM always reads 'Travis Trenholm',
customer-window dates aren't discrepancies." That file is, functionally, the register the
seed is asking whether to build — written the same week, independently, by a different
persistence mechanism, because the category needed a home *somewhere* the moment it stopped
being one-off. It just isn't visible to Jesse and is coupled to this specific harness (a
different tool, a different machine, or a fresh memory reset would lose it).

## Interpretation

**Already covered, in a working three-tier form the seed didn't have visibility into when
it was written.** The vault is not missing a home for business-normal facts; it has three,
each serving a different consumer, and all three are already in active use:

1. **Point-of-use vault note** (one sentence, e.g. `DSP26071.md:44`) — for a fact specific
   to one job, read by a human or agent who lands on that exact file.
2. **Skill guardrail rule** (e.g. the date-window paragraph, the cross-division PO note) —
   for a fact-shape that will recur across *any* future job, promoted once the first
   instance shows it's not job-specific.
3. **Assistant memory** (`feedback-someone-elses-pending-work.md`) — for the meta-heuristic
   itself ("owned by someone else's queue isn't an open item"), which doesn't belong in any
   one skill because it's a rule about how to *evaluate* a fact, not a fact.

This is not a coincidence arrived at by design — it emerged from four independent
instances converging on the same shape, plus a fourth mechanism (memory) covering the
one gap distribution can't: a category-level "stop pattern-matching this as a finding"
rule that no single skill file is the right owner for.

The seed's third question — "is the failing distinguishable from a real finding by any
mechanical rule at all" — has a partial answer already in production, also from Jesse's
own words captured in `change-log.md:133` (2026-07-29): *owned by Jesse and actionable now
is an open item; owned by someone else or already ruled on above him is one factual line
naming the owner.* That's a real, usable test for the "someone else's queue" subclass. It
does not cover every instance in the six/seven (the date-window and PM-default cases are a
different subclass — "template default, not an assignment" — with their own, separately
stated test), so the seed's question is answered per-subclass, not by one universal rule.

**The one real gap: the memory-tier register is invisible to Jesse and not vault-durable.**
If Jesse switches tools, resets memory, or wants to hand this category to someone else (a
new hire reading the vault cold), tier 3 disappears with it — the vault-side tiers 1 and 2
persist, tier 3 does not. That's a narrower, cheaper problem than "design a register from
scratch."

## Recommended Action

**Do not build a new register artifact — the three-tier system is working and a fourth
artifact would compete with, not replace, the existing three.** Bounded one-shot
alternative, much smaller than the seed's original framing:

1. Write down the convention itself, once, in `01-context/estimating-approach.md` or the
   `usadebusk-estimating` guardrails intro (a few sentences, not a new file): when a
   struck-down flag's reasoning is job-specific, it stays a one-line point-of-use note;
   when the *shape* will recur across future jobs, promote it to a skill guardrail; when
   it's a meta-rule about evaluating flags rather than a fact about a job, it belongs in
   assistant memory. This makes explicit what has so far only existed as observed behavior
   across four independent instances.
2. Optionally mirror the memory-tier content (`feedback-someone-elses-pending-work.md`) as
   a short, human-readable note in the vault — not a new taxonomy, just making the one
   tier that currently has no vault footprint durable and visible to Jesse. Candidate home:
   `04-knowledge/concepts/` alongside the other cross-cutting estimating concepts, or a
   short addition to `01-context/estimating-approach.md`.

Both are documentation-only, no schema, no tooling, no new note type. This is a much
smaller ask than the seed originally framed ("is a standing register the right shape") —
the answer is that a register-shaped thing already exists split across three mechanisms,
and the only real work left is naming the convention and giving the one ungrounded tier a
vault-visible copy.

## Decision

- [x] Approved — write the convention paragraph + mirror memory content (items 1–2 above)
- [ ] Approved with edits
- [ ] Rejected — leave as-is, three tiers with no written convention
- [ ] Needs more source material

**Resolved 2026-08-15 (Jesse, in session).** Both items approved and applied. The recommendation to *not* build a new register artifact stands — what landed is documentation of what already exists, not a fourth mechanism competing with the three.

Placement decision: both items went into one new note, `04-knowledge/concepts/business-normal-facts.md`, rather than being split across `01-context/estimating-approach.md` and `04-knowledge/concepts/`. Two reasons. `estimating-approach.md` declares itself duration-model-only ("does not restate the skill's pricing or section content"), so the convention would have been a foreign body there. And the convention and the register explain each other — the register is the thing tier 3 was holding, and the convention is why it needed a vault copy; separating them costs a second file open to understand either. A pointer was added to `knowledge-system-governance.md` under Core Loops as a new "Struck-Down Flags" subsection, sited next to Contradiction Handling since it is the mirror case.

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-15 | Approved and applied. Created `04-knowledge/concepts/business-normal-facts.md` carrying both the three-tier convention (item 1) and the mirrored register content (item 2). Added the "Struck-Down Flags" subsection to `04-knowledge/knowledge-system-governance.md`. | Claude (review queue) | Re-verified all four cited instances before writing, since this note is 13 days old. `DSP26071.md:44` and `equipment-fleet.md:39` still exact. The SKILL.md rule drifted 379 → 384, content unchanged. **`01-context/active-jobs.md:27` no longer exists as cited** — that instance has since evolved rather than regressed: USA26041 now carries an assigned USA#, and both the badging status and the cross-division shared PO read as plain fact in the job row with no flag framing. The convention is visibly holding in the live file. Cited `change-log.md` lines 133/135/141 have also drifted; the underlying entries are at 141–142 (2026-07-29) and the 2026-07-30 row. Line numbers were not carried into the new note for this reason — instances are cited by file and content. |
