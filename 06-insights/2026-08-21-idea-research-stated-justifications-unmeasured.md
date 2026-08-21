---
type: review
status: open
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-08-21
review_after: 2026-11-21
related:
  - "[[idea-stated-justifications-are-unmeasured-claims]]"
  - "[[2026-08-17-triage-job-report-generator-layout-gaps]]"
  - "[[2026-08-19-idea-research-backtest-visually-broken-document]]"
  - "[[_canonical-job-sheet]]"
  - "[[job-report-generator-build-spec]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, idea-research, generator, validation, cross-cutting]
---

# Idea Research — A Design's Stated Justification Is a Claim, and Ours Go Unmeasured

## Trigger

Scheduled nightly run of the Vault Idea Research Loop, 2026-08-21. Two unexplored seeds share the
oldest `created:` date of 2026-08-17. The other one,
[[idea-generator-owns-marked-spans-not-layout]], carries a `**Gate:**` line that was settled shut
from files — see [[2026-08-21-idea-research-generator-owns-marked-spans-gated]] — so this seed came
up next. Its own gate reads "None — researchable now," so it was researched.

The seed generalises from one incident: the Pigs Used table was split 2-up "to fit the page," that
reason was written in the renderer and two spec documents, and when it was finally rendered and
measured on 2026-08-17 against USA25025 — the 26-size job the split existed for — it was false. The
split had never once delivered the fit it existed for. The seed's claim is that the failure is not
about pig tables: **a decision that ships with a stated reason reads as checked, and writing a reason
down does nothing to make it true.**

## Evidence

**1. The general failure has a name and a literature, and the seed's diagnosis matches it.** The
field calls these design rationale and assumptions, and the documented pathology is exactly the
seed's: an assumption that is documented but never tested is a more legible risk, not a resolved one,
and rationale silently expires while continuing to read as authoritative. The survey figures are
blunt — 74% of practitioners report forgetting the reasons behind their own design decisions and 80%
report being unable to reconstruct the reasons for others'. Parnas's classic framing is adjacent and
useful here: the written rationale is a *rational reconstruction*, produced after the fact, and it is
honest only if someone maintains it against the artifact.
[Hidden Assumptions: The Silent Killers of Software Systems](https://medium.com/from-code-to-systems/hidden-assumptions-the-silent-killers-of-software-systems-f91998e5f154) ·
[Assumptions in Design and in Design Rationale (Brown, WPI)](http://web.cs.wpi.edu/~dcb/Papers/DCC06-DR-wkshp.pdf) ·
[A Rational Design Process: How and Why to Fake It (Parnas)](https://users.ece.utexas.edu/~perry/education/SE-Intro/fakeit.pdf)

**2. The seed's proposed standing form — "if a design carries a because-clause about the output, the
back-test has to assert that clause" — is a named, mature practice: the architectural fitness
function.** The definition is almost a restatement of the seed: *any mechanism that performs an
objective integrity assessment of some architecture characteristic*, checking that the system still
matches the architect's *intent* rather than its behaviour. That distinction is the whole point here.
The generator's numbers-only back-test was a behaviour test; "the split fits the page" is an intent
claim, and no behaviour test was ever going to touch it.
[Architectural fitness function — Thoughtworks Radar](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function) ·
[The Up-and-Running Guide to Architectural Fitness Functions](https://mikaelvesavuori.se/blog/2023-08-20_The-Up-and-Running-Guide-to-Architectural-Fitness-Function)

**3. The cheap version of the same practice is also prior art, and it is closer to the right size for
this vault.** The ADR literature converged on a `Last verified` date in the header, *separate from
the original date*, precisely because a rationale's authorship date says nothing about when anyone
last sanity-checked it, and an ADR whose status never changes becomes actively misleading. That is a
convention, not machinery, and it is what "the reason was written in three places and repeated for
months" needed.
[Maintain an architecture decision record — Azure Well-Architected](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record) ·
[Architecture Decision Records: A Practical Guide for 2026](https://www.john-pratt.com/architecture-decision-record)

**4. This vault already has the convention that should have caught it — and it explicitly carves out
the exact class of claim that got through.** `04-knowledge/_canonical-job-sheet.md:21-27` splits
rules into two classes, added 2026-07-30 after the H-2421 scaffold error:

> LAYOUT rules — page budget, table merges, the connbox, render pipeline, naming. Design decisions,
> **verifiable by rendering the page, safe to change on judgment. No attribution needed.**
> DOMAIN rules — … A domain rule MUST carry either `(Jesse, YYYY-MM-DD)` or a cited source.

The pig-table split is a layout rule. It was exempted from attribution *because* layout rules are
"verifiable by rendering the page" — and then nobody rendered the page, on any job, for months. The
convention's own justification is the seed's thesis in miniature: **verifiable is not verified**, and
the exemption treated the two as the same thing. This is a small, precise amendment to an existing
convention, not a new system.

**5. Running the seed's own sweep on its four named candidates: one is materially unmeasured and the
arithmetic disagrees with the stated reason; two are better hedged than the seed remembered; one has
no live target.**

| Candidate | Where it is stated | Status after checking |
|---|---|---|
| `_widths()` column figures "sampled once from a shipped PDF" | `render_job_report.py:413` — `# 6.90" — full text width` | **Contradicted by arithmetic.** See below. |
| Rig hours pooled at project level because "rigging is fungible" | `report-structure.md:97-99`, `scripts/README.md:44`, `extract_ticket_breakdown.py:118` | Hedged, and self-aware. |
| Per-heater pig/smart allocation safe wherever a pumper stays on one heater | `report_input_template.py:41-43`, `render_job_report.py:266` | Enforced, not merely asserted. |
| Equivalent reasoning in the workup-to-proposal transfer step | `usadebusk-estimating/scripts/render_proposal.py` | Live target — see item 7. |

**The widths finding.** Both renderers set `left_margin = right_margin = Inches(0.8)` on a Letter
page, so the true text width is **6.9"**, and `_widths()` sets `table.autofit = False`
(`render_job_report.py:147`), so these are fixed column specs rather than hints. Summing every
`_widths()` call site in the job-report renderer: the Project Duration table is specified at
**7.7"** in its pooled form (`[2.9, 1.4, 1.0, 1.2, 1.2]`, line 333) and **7.5"** in its per-scope-rig
form (`[2.5, 1.2, 0.8, 0.8, 1.1, 1.1]`, line 332). Every other table sums to exactly **7.0"** (lines
240, 251, 362, 434, 454, 536), as does every table in `render_proposal.py` (lines 188, 267, 307, 326,
427, 468). Exactly one call site sums to 6.9" — line 413, the one carrying the comment that asserts
6.9" is the standard.

So the stated justification is wrong at the level of the file: 7.0" is the de facto house convention,
not 6.9", and the comment describes only itself. And the Project Duration table matches neither
convention, sitting 0.6–0.8" wider than the page can hold. **What this does not establish** is that
the delivered documents are visibly broken — Word can absorb an over-wide fixed spec in ways that are
not predictable from the numbers, and USA26038 shipped and was accepted. It establishes that nobody
has ever measured it, which is precisely the seed's claim. Resolving it costs one render and one
look, not a build.

**The two that came out better than expected.** The fungibility claim is stated with its own
limitation attached — `report-structure.md:98-99` says outright that "the per-heater rig split is an
allocation convention, not a measured fact," which is a hedge, not a false because-clause; and the
`duration_rows` escape hatch with a `"rig"` key exists and is exercised by a real fixture
(`back-test/report_input_usa25025.py`). The pumper-heater claim is not left as an assertion at all:
when a pumper roams, `extract_ticket_breakdown.py` flags it UNMAPPED rather than guessing, and the
renderer asserts supplied rows reconcile to the workbook totals. Both are the *right* shape already —
a claim with its falsifier attached.

**6. The corpus is genuinely small, which answers the seed's last question.** A sweep for
because-clauses across `usadebusk-fieldpm` (`because`, `so that`, `in order to`, `to fit`, `which is
why`) returns seven hits, two of which are the pig-table post-mortem itself; across
`usadebusk-estimating/scripts`, four. Roughly a dozen because-clauses exist in total, and three of
the four the seed named are already checked or hedged. That is a read-and-list afternoon, not a
standing harness.

**7. One correction to carry forward.** [[2026-08-19-idea-research-backtest-visually-broken-document]]
concluded that the workup-to-proposal transfer step "is not built" and therefore had "no live
target." `usadebusk-estimating/scripts/render_proposal.py` exists and renders Sections 7, 9 and 3 of
the proposal as a branded docx draft. It shares the job report's brand core "verbatim" by its own
docstring, and it inherits the same 7.0"-on-a-6.9"-page pattern at all six of its table call sites.
So the standard set for the job report does have somewhere to land today.

## Interpretation

**Sound, and cheaper than it looks — but the standing-machinery half is the trap.**

The diagnosis is right and it is well-supported prior art: a stated reason is an unverified claim
wearing the costume of a verified one, and that is a recognised, named failure with an equally
recognised fix. The seed's instinct that the fix belongs in the back-test is also right in principle —
that is exactly what a fitness function is.

What the sweep changes is the *sizing*. The seed frames this as possibly needing "a cheap standing
form," a rule that every because-clause about the output must be asserted by the back-test. Three of
the four candidates it named turned out to be already hedged, already enforced, or previously
mis-scoped. The one that failed, failed to a sum — the cheapest possible measurement, requiring no
harness, no render and no tooling. Building standing machinery to catch roughly a dozen clauses, most
of which are already fine, is the same over-build the 2026-08-19 note warned against when it declined
an automated pixel-diff with a tolerance knob. The failure mode is identical: machinery nobody
maintains, guarding a corpus small enough to read.

The durable half is not a harness at all — it is the two-word amendment to a convention that already
exists and already governs this material. `_canonical-job-sheet.md` exempts layout rules from
attribution on the grounds that they are "verifiable by rendering the page." That exemption is the
hole the pig-table split went through, and it closes by requiring the *date it was last verified*
rather than requiring a source. Layout rules do not need provenance; they need a "last looked at"
stamp, which is exactly what the ADR literature converged on for the same reason.

Naming the residual risk honestly: the widths finding is arithmetic, not observation. It is possible
every table renders fine and the 7.0" convention is harmless slack that Word silently clamps. If so
that is still worth knowing once, and writing down *with a date*, so the next person does not
rediscover it — which is the seed's entire point.

## Recommended Action

**One-time sweep now; one convention amendment; no standing machinery.**

1. **Measure the widths claim** — render one fixture, convert, and look at the Project Duration table
   and the right margin. It is one render and one look, the same mechanism the 2026-08-17 triage
   already used. Then either correct the specs to sum to 6.9", or correct the comment at
   `render_job_report.py:413` to record what the convention actually is and that it was checked.
   Whichever way it lands, stamp the date.
2. **Amend the layout-rule class in `_canonical-job-sheet.md:23`** — keep "no attribution needed,"
   add that a layout rule carrying a because-clause about the *output* records the date it was last
   verified against a rendered artifact. Verifiable is not verified. This is a Lane 4-adjacent edit
   to a canonical schema file and is Jesse's call, not this loop's.
3. **Sweep the remaining because-clauses once** — roughly a dozen across both renderers, listed in
   evidence item 6. Read them, mark each measured / hedged / unmeasured, fix or date-stamp. An
   afternoon, one pass, no recurrence.
4. **Do not** add a back-test rule requiring every because-clause to be asserted. Fold the useful
   part into the tier-one structural assertions the 2026-08-19 note already recommends: if a claim is
   cheap to assert mechanically (a width sum, a border element), assert it there; if it is not, date
   it instead.
5. **Carry the correction** from evidence item 7 into the workup-to-proposal work — the proposal
   renderer exists and inherits the same pattern, so whatever standard the job report adopts applies
   to it on the same day, not "when that generator is built."

**Scope note.** Items 1, 3 and 5 are skills-side changes under `~/.claude/skills/`, and item 2 is
canonical `04-knowledge/` content. This loop is barred from all of them. Nothing here was
implemented — this note is evidence for a decision, not the decision.

## Decision

- [ ] Approved — run the one-time sweep and amend the layout-rule convention
- [ ] Approved, measurement only — render and settle the widths question, skip the convention change
- [ ] Approved with edits
- [ ] Rejected — the because-clauses are fine as they stand
- [ ] Needs more source material

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
|  |  |  |  |
