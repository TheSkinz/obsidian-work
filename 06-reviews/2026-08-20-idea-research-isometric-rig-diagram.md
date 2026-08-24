---
type: review
status: resolved
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-08-20
review_after: 2026-09-20
related:
  - "[[idea-isometric-rig-diagram-from-debusk-renders]]"
  - "[[rig-diagram-corpus]]"
  - "[[2026-08-16-backtest-rig-diagram-layout-engine]]"
  - "[[idea-rig-layout-diagram]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, idea-research, field-ops, visualization, tooling]
---

# Idea Research — Isometric Site Plan Built From DeBusk's Existing Equipment Renders

## Trigger

Scheduled nightly run of the Vault Idea Research Loop, 2026-08-20. Five seeds sat at
`status: unexplored`; the oldest by `created` is
[[idea-isometric-rig-diagram-from-debusk-renders]] (2026-08-16).

**Gate handling.** The seed states no `**Gate:**` line. Its "To explore" opens with an ordering
instruction — "Answer the source-models question first; everything else is downstream of it" —
which reads as a hinge rather than a gate, and in either reading it is not settleable from files:
whether DeBusk holds source 3D models for its equipment is a fact about the company, held by a
person, recorded in no vault note. Per [[vault-idea-loop-spec]] step 3 outcome (c), the seed was
researched normally and the unresolved hinge is named in the Interpretation below.

## Evidence

**1. The hinge could not be settled — but research relocated where to ask it.** The seed assumes
the models, if they exist, sit with whoever produced the marketing video. USA DeBusk's own
Automated Tube Cleaning Division page says the company "utilize[s] the latest sophisticated design
software, perform[s] rapid prototyping, and use[s] techniques such as 3D printing to create parts
and tools in various materials." That describes an in-house CAD practice building the equipment
itself, which is a better and closer source of source geometry than a marketing vendor's render
files — and a different person to ask. Nothing on the public site names the group or publishes a
model.
[USA DeBusk — Automation & Technology](https://usadebusk.com/service/automation-technology/)

**2. If the models exist, the pipeline is documented, free, and standard.** The seed's "genuinely
easy" branch is not an assumption — it is a known workflow. Blender renders with an orthographic
camera (no vanishing point, objects at true scale regardless of distance), and Freestyle emits the
result as line art exported directly to **SVG**, which is the flat, vector, matched-angle asset the
seed wants. Every piece rendered at one fixed camera yields a set that composites cleanly by
construction. This is exactly the property the seed identifies as missing from the existing
perspective renders.
[Blender for technical drawing (Freestyle → SVG)](https://www.blender3darchitect.com/blender-2-8-for-technical-drawing/) ·
[Isometric scenes in Blender](https://www.3dblendered.com/learning-blender/how-to-create-isometric-scenes-in-blender/) ·
[Orthographic camera setup](https://yelzkizi.org/set-camera-to-render-in-orthographic-mode-in-blender/)

**3. A fallback the seed did not consider exists, and it is weak.** Free CAD models of the generic
equipment classes are downloadable — GrabCAD carries multiple frac tank models, 3D Warehouse
carries frac tanks, and STLFinder indexes frac pump trucks. Any of these renders orthographically
through the same pipeline and produces a matched set without DeBusk's own geometry. But a generic
frac tank is not a *DeBusk* frac tank, and recognizability is the entire case for this idea — the
side benefit the seed names is that a viewer can tell which box is the press and which is the pump.
A stock model buys the matched angles and forfeits the point.
[GrabCAD — Frac Tank 80m3](https://grabcad.com/library/frac-tank-80m3) ·
[3D Warehouse — Frac Tank](https://3dwarehouse.sketchup.com/model/338cf3e35c51a4aade0ddeecf587a6d0/Frac-Tank)

**4. The editor half is already solved, free, and cheaper than the seed's plan.** The seed proposes
porting the router in `apps/rig-diagram/` from two axes to three. That work is unnecessary:
**FossFLOW** (MIT-licensed fork of Isoflow) is a purpose-built isometric diagram editor with an
isometric grid, custom icon import accepting **PNG / JPG / SVG**, an isometric-vs-flat toggle for
imported art, automatic scaling, and PNG/SVG export. It runs as a local PWA, from Docker, or from
source, with data stored locally. Known limitation: issue #49 — exported files embed every icon as
a base64 SVG string, producing 2MB+ files that version poorly.
[FossFLOW on GitHub](https://github.com/LuxWise/fossflow) ·
[FossFLOW overview](https://ostechnix.com/fossflow-create-isometric-diagrams/) ·
[Isoflow](https://isoflow.io/) ·
[FossFLOW export/TODO notes](https://github.com/stan-smith/FossFLOW/blob/master/FOSSFLOW_TODO.md)

This is the same argument the seed already makes for draw.io — a flaw costs a drag instead of a
conversation — but it lands harder here, because draw.io still has **no snap-to-isometric-grid**
(the seed's own tooling notes record it as an open feature request). For an isometric artifact
specifically, FossFLOW is the better editor and draw.io is the better general one.

**5. Commercial isometric icon sets are abundant but off-target.** IconScout, Vecteezy, Flaticon
and Icograms all carry large isometric oil-and-gas and industrial libraries under commercial
licenses, and Icograms Designer is a purpose-built isometric factory-map tool that accepts uploaded
graphics. None of them contain a Trimax, a decoking launcher/receiver, or a plate-and-frame press
in DeBusk livery. They solve the generic-icon problem, which is not the problem.
[Icograms — factory maps](https://icograms.com/usage-factory-maps) ·
[IconScout — oil & gas](https://iconscout.com/icons/oil-gas-industry)

**6. Vault and skill check — nothing covers this, and there is no site-plan corpus.** No skill under
`~/.claude/skills/` mentions isometric or site plans. In the vault, "isometric" appears only in this
seed and in `02-facilities/Suncor/Montreal-QC/B-101.md`, where it means *piping isometrics*
(customer drawings M10D031/M10D033 cited for scaffolding scope) — a different artifact entirely.
Most importantly: [[rig-diagram-corpus]] inventories **five hand-built topology schematics and zero
site plans.** The artifact this seed targets has never been produced.

## Interpretation

**Sound, unrefuted, and still ROI-gated — with the gate held by a person, not by evidence.**
Nothing found kills the idea, and two of its premises firmed up: the orthographic-render pipeline is
real and free, and the editor problem is already solved off the shelf. The seed's own framing that
"the art exists and has already been paid for" survives *conditionally* — it holds if the source
geometry is reachable and collapses to a mismatched-compositing job if only finished images exist.
That question is unanswered and unanswerable from here.

**What research did not relieve is the constraint the seed already concedes.** The 2026-08-16
back-test closed the flat generator because domain correctness — frac tank off-system, launchers
bolted to the heater flange, a Trimax never out-scaling the heater — is not derivable by any
renderer, so every regeneration reopens Jesse's review. The template decision worked because five
already-reviewed, already-shipped diagrams existed to relabel. **A site plan has no such corpus.**
Every one would be authored fresh and reviewed fresh. Better assets change how the drawing *looks*,
not what the review *costs*, and looks were never the binding constraint.

**The one genuinely useful decoupling.** Gathering a matched asset set is a one-time cost whose
value does not depend on any tool ever being built — the assets improve a hand-made one-off exactly
as much as a generated one. So "get the assets" and "build a site-plan tool" are separable, and only
the second is expensive. The first is worth doing if and only if the source models turn out to
exist; if they don't, the honest answer is that this stays parked, because the fallback paths
(stock models, purchased icon packs, compositing the existing perspective renders) all forfeit the
recognizability that is the whole argument.

**Naming caution.** "Isometric" already means piping isometrics to a refinery customer. Whatever
this artifact becomes, call it a site plan in customer-facing text.

## Recommended Action

**Bounded, in order — and step 1 is not a research task.**

1. **Ask internally whether source 3D models exist** for the Trimax, frac tank, and filter press —
   STEP, SolidWorks, or Blender, any format. Ask the Automated Tube Cleaning Division / whoever
   owns the design-software and rapid-prototyping work first, and the marketing-video producer
   second. One email. This is the hinge and no amount of further research moves it.
2. **If yes** — one-shot, time-boxed: render three pieces orthographically at one fixed isometric
   camera via Blender + Freestyle → SVG, place them in FossFLOW, and look at whether the set reads
   as matched. Stop there and decide with the picture in hand. Do not build a generator.
3. **If no** — park the seed. Do not composite the perspective marketing renders, and do not
   substitute stock or purchased isometric icons; both give up the recognizability that is the case
   for the idea, and a generic tank icon is worth no more than the green box that ships today.
4. **Regardless of the answer** — do not port the `apps/rig-diagram/` router to three axes. That
   work is superseded by an off-the-shelf editor and runs against the 2026-08-16 decision that
   editable masters beat regeneration.

## Decision

**Mutually exclusive — pick one.**

- [ ] Run step 1 (ask internally about source models), then re-decide
- [x] Park the seed now — the site plan is not worth the ask — **ruled 2026-08-21.** Overtaken by the 2026-08-16 ruling on the rig diagram: use the four shipped diagrams, build no generator. Asking internally for source models reopens a question already closed.
- [ ] Drop entirely
- [ ] Something else / needs discussion

**Separable, non-exclusive — check if wanted alongside the above:**

- [ ] Record FossFLOW in the tooling notes as the isometric-editor option, independent of this idea

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-21 | Closed as overtaken. Jesse ruled "park the seed now." | Claude | The 2026-08-16 ruling — use the four shipped diagrams, build no generator — already closed this. FossFLOW was not recorded separately; if an isometric editor is ever wanted, the seed carries the reference. |
|  |  |  |  |
