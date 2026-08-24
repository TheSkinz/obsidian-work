<!-- vault-loop: operational — tools/ build owed; capture loop cannot write this content. -->
<!-- vault-prestaged: skipped — already covered by [[2026-07-30-exploration-coil-visualization-for-crews]], decision already closed 2026-08-01, this note only tracks owed unexecuted work -->

---
type: note
status: inbox
created: 2026-08-01
tags: [inbox, field-ops, job-sheet, visualization, tools, approved-unexecuted]
---

# Owed — coil visualization, Tier 2 + Tier 3 + Tier 1

> **RESHAPED 2026-08-24 (Jesse). The validator half is built; the renderer is deferred.**
> `tools/coil_geometry_audit.py` → `04-knowledge/coil-geometry-audit.md` now reports which
> heater cards carry coil geometry complete enough to work from — **17 of 44** — and names
> what blocks the other 27. Tier 2/3 (SVG) and Tier 1 (Mermaid) remain approved in principle
> from 2026-08-01 but are **explicitly unscheduled**, pending what the audit shows.
>
> **Three claims in the 2026-08-15 re-test below are now false.** Recorded rather than
> silently corrected, because the re-test was accurate when written and the pattern matters:
>
> 1. **"gates [[idea-rig-layout-diagram]], which has been parked on it since 2026-07-30"** —
>    that seed is `status: closed-unactioned` and sits in `archive/`. Closed, not waiting.
> 2. **"the older of the two surviving owed items"** — the other one
>    ([[2026-08-01-baseline-staleness-detector-owed]]) was built 2026-08-16. This was the
>    only survivor.
> 3. **"extract `buildGeometry()`"** understates the work. That function is 136 lines of
>    JavaScript (`apps/pig-tracker/pig-tracker.html:393-528`) and `tools/` is stdlib Python,
>    so as specified this is a **port**, not a lift. The algorithm is written and correct;
>    the code is not reusable.
>
> **And the flagship QA argument has weakened.** The exploration's case was that h-28's
> "2 tubes cannot split evenly across 4 coils" is a footnote a renderer would force open.
> `02-facilities/P66/Ponca-City-OK/H-28.md` now records it in Config Rollup as
> `4 (+2 heater-wide)` and reconciles arithmetically, so `ROLLUP-SCALE` is satisfied and the
> card surfaces the irregularity itself. What survived is narrower but real, and the audit
> catches it: the card's Tube Geometry row records `Tubes/Circuit` as **`2 heater-wide`** — a
> per-circuit column answered at heater scale, which `num()` reads as `2.0` and understates
> by the circuit count. Six rows across the fleet carry that defect.
>
> **When the renderer is built, the path is a JSON handoff, not a Python port** — a Python
> extractor emits the data object and an HTML file renders it, the pattern
> `apps/rig-diagram/rig-diagram.html` already uses with headless Chrome, already in
> production for `USA26040-job-sheet.pdf`.

> **Re-tested and kept, 2026-08-15** (retirement sweep). Both questions come back yes.
>
> **Still answerable as specified?** Yes, and verified rather than assumed: `buildGeometry()` is still at `apps/pig-tracker/pig-tracker.html:393`, `04-knowledge/ground-truth/` still holds both `h-2421.md` and `h-28.md` to prove output against, and `estimating_rollup.py` still exports the markdown-table parsers this is meant to reuse. Every prerequisite the note names is intact.
>
> **Would the answer change anything?** Yes, on the grounds the note itself argues — it is an extraction QA instrument, not only a crew aid, because a renderer cannot place every tube without forcing unresolved geometry into the open. It also gates [[idea-rig-layout-diagram]], which has been parked on it since 2026-07-30 and cannot move until this does.
>
> Unchanged: this needs scheduling, not re-deciding. It is the older of the two surviving owed items and the one with a downstream item waiting on it.

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
