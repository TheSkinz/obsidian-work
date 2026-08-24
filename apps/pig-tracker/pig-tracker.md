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

## `buildGeometry()` is a cited dependency — do not move this file casually

`pig-tracker.html:393` defines `buildGeometry()`, and it is **named by approved, unexecuted work**, not just used internally here. [[2026-08-01-coil-visualization-build-owed]] (approved by Jesse 2026-08-01, re-tested and kept in the 2026-08-15 retirement sweep) specifies extracting it into a standalone generator that reads `## Tube Geometry` and `## Connection Info (Facts)` off a heater card and emits an SVG. The full reasoning is in [[2026-07-30-exploration-coil-visualization-for-crews]].

One caveat on that owed note, checked 2026-08-24: its 2026-08-15 re-test justifies keeping the build partly because it "gates [[idea-rig-layout-diagram]], which has been parked on it since 2026-07-30." That seed has since gone `status: closed-unactioned` and now sits in `archive/`, so the downstream item it names is closed, not waiting. The build's own case still stands on its other ground — it is an extraction QA instrument, since a renderer cannot place every tube without forcing unresolved geometry into the open.

So treat this as a **source asset, not a scratch demo.** The line reference is cited by path in at least three notes, and nothing lints it: repo-relative paths written in prose are unprotected (`04-knowledge/vault-capture-loop-spec.md` records this), and POINTER-DEAD only covers recorded absolute paths. Renaming the file, or editing above line 393 so the function moves, silently breaks those citations. If it has to move, grep for `pig-tracker.html` first and fix the references in the same commit.

What the extraction inherits, already written and already correct: serpentine rows with alternating direction, true SVG arc U-bends, pitch auto-scaled to tube count, a crossover bridge between the convection and radiant boxes, and inlet/outlet flange stubs.
