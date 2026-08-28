---
type: reference
status: active
source_authority: primary
confidence: high
created: 2026-08-24
related:
  - "[[2026-08-01-coil-visualization-build-owed]]"
  - "[[2026-07-30-exploration-coil-visualization-for-crews]]"
tags: [reference, visualization, field-ops, tools]
---

# Pig Travel Tracker

`pig-tracker.html` — a self-contained browser tool for tracking a pig's position through a coil in real time. No build step and no server: open the file directly in any browser.

## What it does

A circuit is defined in the builder as an ordered list of segments, each carrying a zone (convection, crossover, radiant), a tube count, and a length. Circuits are named for the heater and site (`F-201 — Site, Unit`), saved locally, and can be exported and re-imported as a file, so a circuit built once at the desk survives to the job.

From that data it renders an SVG coil elevation and runs a live readout against it: ETA and arrival clock, the zone and tube the pig is currently in, current and next segment, distance covered and remaining, percent complete, velocity, elapsed time, and a copyable log.

## Flow direction — the crossover enters the radiant at the TOP (fixed 2026-08-28)

Jesse, 2026-08-28: **the crossover pipe connects the bottom of the convection to the top of the
radiant.** The engine had it entering the radiant at the *bottom*: `radRowY` was built inverted
(`nRad - 1 - j`), so `radRowY[0]` was the bottom row, and the bridge dropped below both banks to
climb into it — line 457's own comment read *"up into radiant bottom row."*

A second error followed from the same inversion. Entering at the bottom and serpentining upward
means the coil **exits out the top**, which put the receiver at elevation and contradicted
[[7-1-F-1]]'s Connection Info: *"All launchers and receivers are at grade. Nothing on this heater is
rigged at elevation."* Entering at the top and exiting at the bottom corrects both, and on a looped
circuit it puts the temporary 180 at the radiant outlet flanges, which is where the real one is.

This was an **engine** fix, so it changed the drawing for every circuit, not just the CND26001
presets. That is correct — the old direction was wrong for any fired heater. The tube numbering in
`drawStatic` mirrored the same inversion and was flipped to match, so radiant tube 1 now sits at the
top and 31 at the bottom, running with the flow rather than against it.

**Bearing on the owed extraction.** [[2026-08-01-coil-visualization-build-owed]] justifies itself
partly on the premise that *"the layout engine is already written and already correct."* That was
half true — correct as serpentine mechanics, wrong as heater flow, and it went unnoticed for the
seven months the tool has existed because nothing in the vault checked the drawing against a real
coil. Anything extracted from `buildGeometry()` must take the post-2026-08-28 version.

## Looped circuits — the mirrored-leg model (added 2026-08-28)

A circuit carrying a `legs: ["Coil 1", "Coil 8"]` array is **looped**: its `segments` describe ONE
coil, and `legs` names the coils the pig runs through in order. Everything the loop needs is defined
at or below line 528 on purpose — see the citation constraint below.

The reason it is modelled this way is a real defect in the drawing engine, not a preference.
`buildGeometry()` lays tubes out **by zone** — all convection into the left bank, all radiant into
the right — while the ft→px lookup (`knots`) is built in **segment** order. A looped circuit runs
conv → rad → 180 → rad → conv, so the trailing convection run sits last in segment order while
holding pixels from the left bank; the lookup goes non-monotonic there and the pig marker teleports.
The numeric readout was never affected, since it reads `state.distance_ft` against `segments[]`.

Rather than rework the layout into four banks, the two coils in a loop are identical, so the drawing
of coil A *is* the drawing of coil B. `buildGeometry()` is fed one leg and never learns about the
loop: the pig sweeps the picture forward on leg 1 and backward on leg 2, which is also what it
physically does, since it returns outlet → inlet through the second coil. Tube identity falls out
correct for free — entering leg 2 puts the pig in radiant tube 31, where it really is. `units`,
`zoneCounts` and `geoSegments` are leg-scoped; `segments`, `cumStart` and `totalLength` cover the
whole circuit.

Unlooped circuits take the `legCount === 1` path and behave exactly as before.

On a looped circuit the drawn `R` end is the **temporary 180**, not the receiver — both the launcher
and the receiver land at the B end. The stubs are labelled accordingly (`180 / 180 LOOP` and
`LAUNCHER / RECEIVER`) rather than telling a crew the outlet is a receiver.

## Built-in circuits for CND26001

Five presets ship for Syncrude 7-1 F-1 — the four looped circuits of the August 2026 campaign
(**1&8 · 2&7 · 3&6 · 4&5**, 4,474 ft each) plus a single unlooped coil (2,237 ft) as a field
fallback. Geometry is from [[7-1-F-1]]'s Config Rollup, verified 2026-08-20. The app opens on
Circuit 1 & 8 rather than the synthetic test.

**They omit the crossover and the loop spool.** No length for the convection-to-radiant crossover or
the temporary 180 at the radiant outlet is recorded anywhere in the vault — the card's 2,237 ft is
tube footage only. ETA therefore runs slightly short and the pig lands a little after the app says.
The B-103 preset shows the `crossover` segment shape to add if either is ever measured.

## Field deployment

Published as a private Artifact for phone use on shift:
**https://claude.ai/code/artifact/af8fa7ea-444e-4ca2-bf69-15ddbde634b6**

**This file stays canonical.** The Artifact is a projection of it with the `<!doctype>`/`<head>`/
`<body>` wrapper stripped (the Artifact runtime supplies those); republish from here rather than
editing the published copy. Two known limits in that environment: the builder's **Export JSON**
button is inert, because the artifact viewer blocks page-initiated downloads, and **keep screen on**
depends on Wake Lock surviving a sandboxed iframe. Both degrade quietly — the app feature-detects
Wake Lock already — and neither affects the presets.

## `buildGeometry()` is a cited dependency — do not move this file casually

`pig-tracker.html:393` defines `buildGeometry()`, and it is **named by approved, unexecuted work**, not just used internally here. [[2026-08-01-coil-visualization-build-owed]] (approved by Jesse 2026-08-01, re-tested and kept in the 2026-08-15 retirement sweep) specifies extracting it into a standalone generator that reads `## Tube Geometry` and `## Connection Info (Facts)` off a heater card and emits an SVG. The full reasoning is in [[2026-07-30-exploration-coil-visualization-for-crews]].

One caveat on that owed note, checked 2026-08-24: its 2026-08-15 re-test justifies keeping the build partly because it "gates [[idea-rig-layout-diagram]], which has been parked on it since 2026-07-30." That seed has since gone `status: closed-unactioned` and now sits in `archive/`, so the downstream item it names is closed, not waiting. The build's own case still stands on its other ground — it is an extraction QA instrument, since a renderer cannot place every tube without forcing unresolved geometry into the open.

So treat this as a **source asset, not a scratch demo.** The line reference is cited by path in at least three notes, and nothing lints it: repo-relative paths written in prose are unprotected (`04-knowledge/vault-capture-loop-spec.md` records this), and POINTER-DEAD only covers recorded absolute paths. Renaming the file, or editing above line 393 so the function moves, silently breaks those citations. If it has to move, grep for `pig-tracker.html` first and fix the references in the same commit.

**Honored 2026-08-28.** The grep found **ten** citations, not three — across `CLAUDE.md`, both review notes, two inbox notes, this file, and two `change-log.md` entries. Both `:393` and the `:393-528` range are cited. Two of those are records that should not be rewritten to accommodate a code change, so the looped-circuit work was built entirely **below line 528** instead: `BUILTIN_CIRCUITS` is mutated from the bottom of the script with `push()` rather than extended at its declaration on line 279, and the leg-indicator element is injected at runtime rather than added to the markup. `buildGeometry()` still starts at 393 and ends at 528. Check that with `grep -n "^function buildGeometry"` before and after any future edit — it is the cheapest gate available until [[idea-lint-repo-relative-paths]] is built.

What the extraction inherits, already written and already correct: serpentine rows with alternating direction, true SVG arc U-bends, pitch auto-scaled to tube count, a crossover bridge between the convection and radiant boxes, and inlet/outlet flange stubs.
