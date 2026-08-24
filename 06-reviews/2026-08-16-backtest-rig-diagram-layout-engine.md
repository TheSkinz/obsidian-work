---
type: review
status: resolved
review_type: backtest
source_authority: primary
confidence: high
created: 2026-08-16
review_after: 2026-09-16
related:
  - "[[idea-rig-layout-diagram]]"
  - "[[rig-diagram-corpus]]"
  - "[[2026-08-03-idea-research-rig-layout-diagram]]"
tags: [review, backtest, field-ops, visualization, tools]
---

# Back-test — Rig Diagram: computed layout vs frozen template

## Trigger

[[idea-rig-layout-diagram]] was ungated 2026-08-16. Jesse's account of the March 2026 build
threads relocated the problem: pure relabeling was under 5% and genuine authoring 20–25%, but
**the majority of the cost was geometry correction in a screenshot feedback loop** — diagonals
that should have been orthogonal, arrowheads reversed because x1/x2 were swapped, a missing
segment at a T-junction, a 10px gap that needed 20, the filter press at half scale, ports
clustered horizontally that should stack vertically.

Every one of those is a symptom of hand-placed absolute coordinates, which gives two candidate
fixes: **freeze** the coordinates into per-config templates (Jesse's own May-2026 conclusion,
never built), or **never write coordinates at all** and derive them from layout.

## Method

Rebuild F-901 — the simplest instance in [[rig-diagram-corpus]] — and score against criteria
fixed before running, so the comparison could not be talked into a result. Artifact and both
renders are at `apps/rig-diagram/`.

The third approach was not in the original plan and displaced D2: **CSS grid places the blocks,
and connectors are computed from measured element rects at draw time**, emitted as H/V segments
only. It needs no new dependency — Chrome is already the renderer for job sheets.

## Result

| Criterion | Outcome |
|---|---|
| Orthogonal routing | **Pass.** Zero diagonals in any round. `ortho()` cannot represent one. |
| Port order | **Pass.** Pumps and L/R pairs emit from one ordered list; order matches by construction, never nudged. Hoses are routed as a planar fan, so they cannot cross. |
| Domain correctness | **Fail on first pass.** Six errors found by Jesse, four of them domain facts a renderer cannot know. See the correction section. |
| Filtration swap | **Pass.** Two data fields (`filtration: false`, `waterSource: hydrant`) produced the 70H1 hydrant/coke-pit form. No geometry edited. |
| Visual bar | **Close, not equal.** Legible and structurally faithful; still missing the per-port `P1 Out / P1 In` labelling and pump numbering the shipped diagrams carry. |
| Correction rounds | **Five.** See below — the composition matters more than the count. |

**The five rounds were not five geometry chases.** Round 1 rendered; round 2 fixed heater-port
alignment at its root (ports are now drawn at the measured centre of their own L/R box rather
than by a parallel flex container); round 3 was proportions and label placement; round 4 was a
**measurement** that found a single coordinate-space bug; round 5 was cosmetics plus making the
left-hand column data-driven.

Round 4 is the one worth recording. Three rounds of residual misplacement all had one cause: the
SVG's own box measured 691px wide while the content spanned 906px, because percentage sizing on
an SVG resolves against its intrinsic box. Every drawn coordinate was being stretched ~1.5×. I
was two rounds into diagnosing it by eye — which is exactly the March failure loop — before
dumping the actual rects, at which point one fix corrected everything simultaneously. **The
lesson is the standing one: measure through an independent channel instead of inferring from the
render.**

No defect across the five rounds was a diagonal or a coordinate-arithmetic error. **That claim
was originally written to include arrowheads and scale, and Jesse's review proved it wrong on
both** — see the correction below.

## Correction — Jesse's review, 2026-08-16

Jesse reviewed the render and found six errors, four of which I could not have caught myself
because they are domain facts, not drawing defects. They are now recorded as drawing rules in
[[rig-diagram-corpus]]. Summarised:

1. **Frac tank collided with the filtration hoses**, which ran straight through it. It is
   off-system — water is drawn at the start of the job only — and must be separated.
2. **Launchers/receivers were drawn hanging off a second hose run.** They bolt to the heater
   flanges; there is one hose, pumper → L/R.
3. **The frac tank hose runs directly into the Trimax**, which the render did not show clearly.
4. **Scale was wrong.** The pumper was drawn larger than the heater. A Trimax is a trailer,
   roughly frac-tank sized, and must never out-scale the heater. Jesse notes this was a standing
   failure in the chat-built versions too.
5. **Jetting hoses crossed** between the pump ports and the launchers.
6. **Return-flow arrowheads pointed the wrong way** on the receiver legs (my own find, before
   his review).

**This falsifies part of the result above and the claim is withdrawn.** Arrowhead direction and
scale were *not* eliminated by construction — direction is a semantic property the router has no
opinion about, and scale was a CSS value I chose badly. What survives is narrower and should be
read as the actual finding: **orthogonality and hose crossings are eliminated structurally;
correctness of direction, scale and domain semantics is not, and still needs a domain reviewer.**

All six were fixed in two rounds. The crossing fix generalises — hoses are now routed as a planar
fan with one lane per run ordered by launcher height, so crossings are impossible rather than
avoided, and that holds at F-802's ten launchers without change. The others were data and CSS.

Still unrepresented: the **diverter** and the **loop/jumper** on looped passes. Both appear in
the hand-made originals and neither is in the generated version.

## Interpretation

**The computed-layout approach does what the freeze approach was meant to do, and covers a case
the freeze approach cannot.** Freezing coordinates needs one template per config cell — the
corpus already spans 1-vs-2 Trimax × mode × filtration-or-not, which is roughly where May's
estimate of twelve came from. Computing them collapses that to zero: a new config is new data,
not a new file. The filtration swap demonstrates this directly.

It also inherits the discipline the heater cards enforce. The rendered `Max Pig OD` reads the
rule-correct **5.25"** rather than the 5.5" the shipped F-901 diagram and SOP both carry in
error, because the value came from the card. That is the same extraction-QA argument that earned
the coil visualization its approval, and it applies here without the coil renderer existing.

**What is not proven.** Dual-Trimax is unimplemented and untested, and both F-802 and 70H1 need
it — that is precisely where the freeze approach gets expensive and where a computed layout
should pull ahead, so the decisive case is the missing one. D2 + ELK, the candidate the plan
named, was **not evaluated**: it is not installed, and installing it was not worth doing
unasked. The comparison is therefore against the freeze approach only.

**Honest counterweight.** Five rounds is not free, and a chunk of it was my own plumbing bug
rather than anything intrinsic. A fair reading is that the approach front-loads cost into
machinery that then holds, whereas the freeze approach front-loads it into templates that also
hold but do not generalise. The evidence favours computed layout; it does not make it obvious.

## Recommended Action — reversed 2026-08-16, after the review

**Do not build the generator. Use the four shipped diagrams as the template set.**

The back-test measured correction rounds, and the honest reading is that the loop did not
collapse. Five rounds got to something that looked right; Jesse's review then found six more
errors, four of them domain facts; and he called the remaining tail at another two-plus hours of
explaining adjustments and hand-fixing outside the tool. That is the same loop the March 2026
threads ran, which is exactly what this was supposed to avoid.

**What the structural guarantees actually bought.** Orthogonality and hose crossings are
genuinely eliminated — they cannot recur. But those were the cheap failures. The expensive one
is domain correctness, and it is not derivable from any drawing engine: that the frac tank is
off-system, that launchers bolt to the heater flange, that a Trimax never out-scales the heater.
A generator re-derives geometry on every run and therefore **re-opens domain review on every
run**, and Jesse is the only domain reviewer. No rendering technology changes that, D2 included.

**A frozen template does change it.** Review happens once per config and then carries forward;
per-job work is find-and-replace on already-reviewed geometry. That was Jesse's own May-2026
conclusion, and this session is evidence for it rather than against it.

**The template set already exists and does not need building.** [[rig-diagram-corpus]] holds four
shipped diagrams spanning single vs dual Trimax and filtration vs none — already domain-correct,
already customer-accepted. The unbuilt piece was never the templates; it is only the habit of
picking the closest one and relabeling.

`apps/rig-diagram/` stays filed as back-test evidence, not as a path. Do not wire it to heater
cards.

## Decision

**Mutually exclusive — pick one.**

- [x] **Use the four shipped diagrams as the template set; no generator** (2026-08-16)
- [ ] ~~Prove dual-Trimax on F-802, then decide~~
- [ ] ~~Adopt computed layout on the single-Trimax evidence~~
- [ ] ~~Install D2 and run the comparison the plan originally named~~

**Revisit trigger:** a job whose configuration none of the four existing diagrams covers. Until
then this is closed.

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-16 | Back-test run; prototype filed to `apps/rig-diagram/` | Claude (Opus 5) | F-901 rebuilt, filtration swap verified. D2 not evaluated (not installed). Dual-Trimax not implemented. |
