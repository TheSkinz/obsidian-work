---
type: review
status: open
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
| Port order | **Pass.** Pumps and L/R pairs emit from one ordered list; order matches by construction, never nudged. |
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

Not one defect across all five rounds was a diagonal, a swapped arrowhead, or a scale error.
Those failure classes were eliminated by construction rather than by care.

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

## Recommended Action

Prove dual-Trimax on F-802 before committing to anything. If it holds, adopt computed layout as
the path and retire the twelve-template plan; if it does not, the freeze approach is still
sitting there and nothing has been lost but this session.

Do **not** wire this to heater cards yet. The data object is currently hand-filled, and whether
it should read `## Connection Info (Facts)` off the card is a separate decision that overlaps
the coil-visualization build's parser work.

## Decision

**Mutually exclusive — pick one.**

- [ ] Prove dual-Trimax on F-802, then decide (recommended)
- [ ] Adopt computed layout now on the single-Trimax evidence
- [ ] Install D2 and run the comparison the plan originally named
- [ ] Revert to the twelve frozen templates
- [ ] Park — the five hand-made diagrams are sufficient

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-16 | Back-test run; prototype filed to `apps/rig-diagram/` | Claude (Opus 5) | F-901 rebuilt, filtration swap verified. D2 not evaluated (not installed). Dual-Trimax not implemented. |
