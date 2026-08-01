<!-- vault-loop: operational — tools/ build owed; capture loop cannot write this content. -->
---
type: note
status: inbox
created: 2026-08-01
tags: [inbox, field-ops, job-sheet, visualization, tools, approved-unexecuted]
---

# Owed — coil visualization, Tier 2 + Tier 3 + Tier 1

Approved by Jesse 2026-08-01
([[2026-07-30-exploration-coil-visualization-for-crews]]). Scope approved, build
not started.

**Tier 2 — SVG coil elevation.** Extract `buildGeometry()` from
`apps/pig-tracker/pig-tracker.html:393` into a generator that reads `## Tube
Geometry` and `## Connection Info (Facts)` off one heater card and emits an SVG.
The layout engine is already written and already correct — serpentine rows with
alternating direction, true SVG arc U-bends, pitch auto-scaled to tube count, a
crossover bridge, and inlet/outlet flange stubs.

**Tier 3 — terminal and connection layer.** Launcher and receiver boxes at the
stub ends, labeled from `## Connection Info (Facts)` with the real flange spec and
adapter note, plus pass letters and flow arrows. This is the part Jesse named
first: the launcher tied to a tube-count-correct pass. Cheap once Tier 2 exists.

**Tier 1 — Mermaid pig-path block.** launcher → convection pass (n tubes, ID) →
crossover → radiant pass → jumper → receiver. Complementary, not competing:
Mermaid is a graph layout engine and structurally cannot draw a serpentine to
scale, but it covers the circuit view that Tier 2 cannot.

**Build notes carried from the exploration:**

- The vault `tools/` convention is pure standard library, and
  `estimating_rollup.py` already exports the markdown-table parsers
  (`section_lines`, `table_rows`, `num`, `heater_cards`) this should reuse.
- Prove it against H-2421 **and** H-28 — both have independent ground-truth
  records in `04-knowledge/ground-truth/` to check output against.
- Render missing or compound values as visibly indeterminate rather than guessed,
  and stamp every output "schematic — not to scale, not for fabrication." A
  schematic that looks like a drawing gets read as one, and someone will
  eventually try to scale off it.
- Decide standalone file vs job-sheet page 2 only after it works, not before.
- Tier 4 (multi-pass circuit sheet) stays parked — it needs a pass-topology schema
  field and should ride the existing heater-card schema trigger rather than
  opening its own change. Tier 5 is [[idea-rig-layout-diagram]], separate.

**Worth remembering why this earned approval over a park:** it is an extraction QA
instrument, not only a crew aid. A renderer cannot place every tube without
forcing unresolved geometry into the open — `04-knowledge/ground-truth/h-28.md`
row 4 already records "2 tubes cannot split evenly across 4 coils," which today is
a footnote a reader can skip and which a renderer simply could not draw. That
makes it cross-cutting across bids rather than per-job convenience.
