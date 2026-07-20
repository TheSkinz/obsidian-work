---
type: heater
heater-id: <UNIT>-<TAG>-<ShortName>
heater-tag: <e.g. F-802, 210-1401A>
unit: <e.g. PS8, Unit 210, HU9 — omit if not applicable>
facility: <Client>-<City>-<ST>
  # ↑ JOIN KEY — must exactly match the facility-id in this site's _facility.md.
  #   Commands use this to find the facility record for any heater.
client: <Client name>
heater-type: <crude | vacuum | reboiler | other>
service: <e.g. Crude Heater, Splitter Reboiler — descriptive, optional if heater-type covers it>
configuration: <e.g. Looped-at-Radiant-outlet-flanges, Individual-Passes>
last-updated: <YYYY-MM-DD>
tags: [heater-card, <Client>, <heater-type>]
---

<!--
CANONICAL EXEMPLAR — NOT A LIVE CARD.
This file is the schema authority for all heater cards in the vault. It is never a record
of an actual heater's data; it exists to be stable while live cards mutate. Templates and
the vault-ingest internal template derive their structure FROM this file.

Annotations like this one explain field purpose / required-vs-optional / format. They stay
in the exemplar and are stripped (or left as guidance comments) when a real card is created
from this template — Jesse's call on whether comments survive into real cards or are removed
at creation time.

STATUS: DRAFT — Phase 2.0, pending Jesse's review and field-set approval.
Validated against: F-802, 210-1401A, 210-1402B, 210-1403A, 210-1404B, F-301, F-371A.

FOLDER STRUCTURE (locked 2026-06-22):
  02-facilities/<Client>/<City-ST>/<HeaterTag>.md — flat, no per-heater subfolders.
  _facility.md lives alongside heater cards at the site level.
  Jobs are not separate files — job actuals dissolve into each heater card (## Job History + ## Task Durations).
  Folders are for human navigation; frontmatter is for programmatic access.
-->

# <Unit/Tag> <ShortName> — <Client> <City>, <ST>

<!--
STAINLESS / SPECIAL METALLURGY WARNING BLOCK — conditional, include only if any section's
metallurgy is stainless or another passivation-requiring alloy. See 210-1403A for the live
example. Omit this block entirely on carbon-steel-only heaters (e.g. F-802, Marathon crude
cards) rather than leaving an empty warning shell.

> ⚠ STAINLESS METALLURGY — Soda ash passivation required (customer-performed unless noted
> otherwise). Monitor pH ≥ 10.0 throughout passivation. Firewater avoided by default due to
> chloride content unless facility has tested and confirmed acceptable hydrant chloride levels.
-->

---

## Identity

<!--
Card-level facts only. Anything that can legitimately differ BY SECTION (metallurgy, return
bend type) does NOT belong here — see Tube Geometry. This table answers "what heater is this"
not "what is it made of."
-->

| Field | Value |
|---|---|
| Client | <value> |
| Facility | <City, ST> |
| Unit ID | <Unit / Tag> |
| Heater type | <Crude / Vacuum / Reboiler / etc.> |
| Configuration | <Looped at outlets / Individual Passes / etc.> |

---

## Tube Geometry

<!--
ATOMIC FACTS ONLY. Per-circuit measurements, never totals/sums — those are derived and live
in Config Rollup below. One row per physical segment: a heater with a single-ID radiant
section gets one Radiant row; a heater with multiple radiant pipe sizes in series (e.g.
210-1403A, 210-1404B) gets one row PER segment, in flow order.

Metallurgy and Return Bend Type are PER-SECTION, not card-level — confirmed 2026-06-22 after
recon showed mixed-metallurgy heaters exist (e.g. carbon convection / stainless radiant).
Do not promote these to Identity or a card-level Connection Info row.

Arrangement: Convection defaults to Horizontal (true in ~98% of cases) — only override if a
specific card is confirmed otherwise. Radiant has NO default; state explicitly every time —
it is genuinely ~50/50 horizontal vs vertical depending on heater type.

"Not recorded" is an expected, valid value — customers don't always supply full tube specs.
Use it explicitly rather than leaving a cell blank, so a missing fact is distinguishable from
an unfilled-in card.
-->

| Section | Arrangement | Metallurgy | OD (in) | Sched | Wall (in) | ID (in) | Tubes/Circuit | Avg Length (ft) | Length/Circuit (ft) | Return Bend Type | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Convection | Horizontal | <e.g. A106 Gr.B> | | | | | | | | <e.g. 180° U-bend A234 WPB> | |
| Radiant <add suffix if multi-segment, e.g. "Radiant — segment 1 of N"> | <Horizontal/Vertical — required> | | | | | | | | | | |

<!-- Add additional Radiant rows in flow order for multi-segment radiant sections. -->

---

## Config Rollup — Estimating Reference

<!--
DERIVED, NEVER HAND-ENTERED. This section expresses the heater's FIXED physical loop
arrangement at two scales, not a "current job configuration" — corrected 2026-06-22 after
F-802 migration surfaced the wrong model.

CORRECTED MODEL: A heater's coil/loop arrangement (e.g. "10 coils looped to 5 passes") is a
PERMANENT physical fact about the heater, not something that changes per job. It is set once,
physically, with temp loops or permanent piping — not reconfigured between decokes. The earlier
"current config only, overwrite on change" framing was wrong for heaters where the loop count
is fixed; it only applies in the rare case Jesse described — a flaw found on a prior decoke
forces an actual physical reconfiguration. That case is the exception, not the norm, and when
it happens it's a dated, logged event (see Field Notes), not a routine overwrite.

Two rows, always both present, not alternatives:
  - "Per circuit" — the single-coil/circuit base unit (matches Tube Geometry's
    Tubes/Circuit and Length/Circuit exactly — this row is the estimating multiplication base).
  - "Heater total" — the full installed total, accounting for the actual loop arrangement
    (e.g. 10 physical coils looped to 5 passes still totals 10 coils' worth of tube footage,
    even though they're plumbed as 5). State the loop arrangement in the Notes column.

If a heater is ever physically reconfigured (the rare flaw-driven case), update the "Heater
total" row's Notes to state the new arrangement and the job/date it changed, and log the prior
arrangement as a dated note in Field Notes. Do not add a third row — the table still reflects
current physical reality, just update it in place.
-->

| Scale | Section | Pipe ID(s) (in) | Total Tubes | Total Length (ft) | Notes |
|---|---|---|---|---|---|
| Per circuit | Convection | | | | |
| Per circuit | Radiant | | | | |
| Heater total | Convection | | | | <e.g. "10 coils looped to 5 passes"> |
| Heater total | Radiant | | | | |

---

## Connection Info (Facts)

<!--
Card-level connection facts that do NOT vary by section. Return Bend Type moved to Tube
Geometry (per-section) — do not duplicate it here.
-->

| Field | Value |
|---|---|
| Launcher flange | |
| Receiver flange | |
| Water supply source | |
| Max pig OD (in) | <governing tube ID + 0.250" — compute from the SMALLEST ID across all sections/segments, typically radiant> |

---

## ⚠ Job Options — Customer Decisions (Quarantined)

> Status only — never facts. This section tracks customer-elected choices, not equipment specs.

| Option | Status (Optional / Elected / Declined / TBD) | Vendor / Notes |
|---|---|---|
| Filtration | | |
| Smart pigging / inspection | | |

---

## Pig Specifications

<!--
Own section — confirmed 2026-06-22, not folded into Connection Info. This is estimating/
tooling reference data: what pig sizes and types this heater has historically used, at what
cost, billed how, sourced from which quote.
-->

| Size | Type | Qty | Unit Cost | Billed As | Source |
|---|---|---|---|---|---|
| | | | | | |

---

## Job History

| Job # | Quote | Date | Notes |
|---|---|---|---|
| | | | |

---

## Task Durations
<!-- Wall-clock ELAPSED hours per decoke, one row per job (Date = job START, YYYY-MM-DD;
multi-day span lives in Job History). ACTUALS ONLY — what the job really took, keyed by
Job #; estimates live in the estimating workflow, never as a row here. Rigs = number of
TriMax on the job; task hours are ELAPSED, so labor ≈ task hrs × Rigs (per-rig split stays
in Field Notes, never averaged into this table). Stand-By is tracked but EXCLUDED from Total
(Total = productive task hours: Rig-In + Pig + Smart Pig + Rig-Over + Rig-Out). Total is
DERIVED but hand-entered (no formula layer) — re-sum on any edit, do not trust a stale Total.
  Rig-Over attaches to the heater the equipment moved TO (destination heater; never split
        or double-counted across heaters on a multi-heater job).
  Pig includes flow-test hours — before/after flow tests are NOT a separate column; fold
        into Pig. Add a Flow Test column only when a real receipt breaks the hours out.
  "–" = task confirmed did NOT occur (e.g. no smart pig on this job).
  "?" = task occurred-status unrecorded / unknown — distinct from "–".
  CONDITION (last column) — what state the coil was in, because a decoke's hours are only
        evidence for the NEXT decoke of the same condition. Vocabulary:
          `routine`  = normal service fouling, planned/TA scope.
          `crash`    = furnace was crashed/upset; significantly dirtier than routine.
                       Classification rule (Jesse, 2026-07-19): if the job details say
                       "emergency" (emergency mob / emergency project), it is a crash.
          `first`    = first-ever clean on this heater, no prior baseline.
          `unknown`  = scope condition not recoverable from the source documents.
        Append `, hours-blended` when the source report did not separate task hours
        cleanly and the split across columns is an allocation, not a measurement.
        Append `, combined-heaters` when the job pigged more than one heater and the
        recorded hours are the JOB total, not this heater's share — the same row then
        appears on each heater's card. Suppresses ft/hr in the rollup, which would
        otherwise charge the full combined hours against one heater's footage.
        NEVER estimate a routine job from crash rows — see usadebusk-estimating. -->
| Date | Job # | Rigs | Rig-In | Pig | Smart Pig | Rig-Over | Rig-Out | Stand-By | Total | Condition |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

---

## SOPs

<!-- Card-specific procedural notes/links, if any. Leave header present even if empty. -->

---

## Field Notes

<!--
Per-job operational record: pigs ran, obstacles, facility procedures learned, and (multi-TriMax
jobs only) the per-rig split backing the Task Durations table. Never restate the Task Durations
table's numbers here as prose — the table carries the numbers, Field Notes carries the "why."
"Difficulty"/challenges content (formerly a frontmatter key, dropped 2026-06-22) belongs here,
scoped to the job it occurred on — not as a card-level rating.
-->

### <Job # — Month Year>

**Pigs Ran:**

**Obstacles:**

**Facility Procedures:**

**Per-rig split (multi-TriMax only):**

---

## Notes

<!-- General card-level notes that don't fit elsewhere. -->
