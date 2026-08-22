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

STATUS: APPROVED — Phase 2.0 field set approved by Jesse 2026-07-22 (config/skill-system audit). This file is the governing schema authority; treat its field set as settled, not tentative.
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

| Section | Arrangement | Metallurgy | OD (in) | Sched | Wall (in) | ID (in) | Tubes/Circuit | Avg Length (ft) | Length/Circuit (ft) | Return Bend Type |
|---|---|---|---|---|---|---|---|---|---|---|
| Convection | Horizontal | <e.g. A106 Gr.B> | | | | | | | | <e.g. 180° U-bend A234 WPB> |
| Radiant <add suffix if multi-segment, e.g. "Radiant — segment 1 of N"> | <Horizontal/Vertical — required> | | | | | | | | | |

<!-- Add additional Radiant rows in flow order for multi-segment radiant sections. -->

**Tube geometry notes.**

**<Section — exactly as written in the table's first column>.** <Provenance, confirmation
reasoning, or dimensional caveat for that row.>

<!--
NO Notes COLUMN (changed 2026-07-27, Jesse). The table is 11 columns and carries atomic
values only. Anything explanatory — how a tube count was confirmed, which drawing a length
came from, why a schedule looks odd — goes in the keyed block directly above this comment,
one paragraph per row, led by the Section name exactly as it appears in column 1.

Why: a 12th prose column pushed the table past the render width, so it scrolled sideways and
squeezed every numeric column. 75 notes across 39 cards were moved out on 2026-07-27; the
text was relocated verbatim, not rewritten.

This is NOT Field Notes. Field Notes is the per-job operational record (pigs ran, obstacles,
facility procedures) and is scoped to a job number. Tube geometry notes are card-level facts
about the tubing itself and do not belong there. Omit the block entirely when no row needs one.
-->


---

## Config Rollup — Estimating Reference

<!--
DERIVED FROM TUBE GEOMETRY — hand-entered (no formula layer), so re-derive on any edit and
never invent a value Tube Geometry can't back. This section expresses the heater's FIXED
physical loop arrangement at two scales, not a "current job configuration" — corrected
2026-06-22 after F-802 migration surfaced the wrong model.

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
Trimax on the job; task hours are ELAPSED, so labor ≈ task hrs × Rigs (per-rig split stays
in Field Notes, never averaged into this table). Stand-By is tracked but EXCLUDED from Total
(Total = productive task hours: Rig-In + Pig + Smart Pig + Rig-Over + Rig-Out). Total is
DERIVED but hand-entered (no formula layer) — re-sum on any edit, do not trust a stale Total.
  Rig-Over attaches to the heater the equipment moved TO (destination heater; never split
        or double-counted across heaters on a multi-heater job).
  Pig includes flow-test hours — before/after flow tests are NOT a separate column; fold
        into Pig. Add a Flow Test column only when a real receipt breaks the hours out.
  "–" = task confirmed did NOT occur (e.g. no smart pig on this job).
  "?" = task occurred-status unrecorded / unknown — distinct from "–".
  CONDITION (second-to-last column) — the JOB CLASS this decoke belongs to, because a decoke's
        hours are only evidence for the NEXT decoke of the same class. Vocabulary:
          `routine`  = normal service fouling, planned/TA scope.
          `crash`    = UNSCHEDULED MOBILIZATION. The facility hit operational trouble and
                       needed a crew cleaning on a moment's notice. It is a callout label,
                       NOT a fouling grade (Jesse, 2026-08-20) — the coil is usually dirty,
                       but not by definition, and this column does not record how dirty.
                       Classification rule (Jesse, 2026-07-19): if the job details say
                       "emergency" (emergency mob / emergency project), it is a crash.
          `first`    = first-ever clean on this heater, no prior baseline.
          `unknown`  = job class not recoverable from the source documents.
        NAMING NOTE: the column is called `Condition` and the name is now a slight misnomer —
        it holds job class, not coil condition. Kept as-is deliberately for schema stability
        (the header is lint-locked by DURATIONS-HEADER across every card). Whether callout
        type and coil condition become separate columns is DQ-017's call, bundled with the
        per-coilset re-grain; do not rename or split this column ahead of that ruling.
        Append `, hours-blended` when the source report did not separate task hours
        cleanly and the split across columns is an allocation, not a measurement.
        Append `, combined-heaters` when the job pigged more than one heater and the
        recorded hours are the JOB total, not this heater's share — the same row then
        appears on each heater's card. Suppresses ft/hr in the rollup, which would
        otherwise charge the full combined hours against one heater's footage.
        Append `, rig-quarantined` (added 2026-08-21, DQ-017 Q3) when this job's RIG
        figures must not feed a duration rule — the job's own sources disagree, the
        configuration changed mid-job, or the rig moved to another heater rather than
        demobbing. The hours stay in the table as billing actuals; the token blocks
        derivation only, and the card's row note carries the reason. In use on all four
        HF Sinclair rows (Jesse, 2026-08-21: USA25051 "was chaotic… not a great project
        to get reliable data from"). Reach for it when the reason is job-specific and
        the numbers are otherwise real — not for a figure you merely doubt.
        THESE QUALIFIERS ARE APPENDED AFTER A COMMA and never replace the job class:
        `estimating_rollup.py` keys job-class segmentation on the text BEFORE the first
        comma, so `crash, rig-quarantined` still counts as `crash`. Writing a qualifier
        into the first position would silently move a published mean.
        NEVER estimate a routine job from crash rows, or a crash mob from routine rows —
        they are different job classes and their hours are not interchangeable. That
        prohibition stands on its own; it does not rest on a claim that crash coils are
        dirtier, which is not something this table measures. See usadebusk-estimating.
  MODE (last column) = passes pigged SIMULTANEOUSLY during the Pig task: single 1 / double 2 /
        triple 3, ×rigs if more than one pumper ran in parallel; a looped path counts as 1.
        Blank = unrecorded. The estimating rollup divides ft/elapsed-hr by Mode to report a
        single-pig travel rate comparable to the 100 ft/hr benchmark. -->
| Date | Job # | Rigs | Rig-In | Pig | Smart Pig | Rig-Over | Rig-Out | Stand-By | Total | Condition | Mode |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

---

## Coilset Durations

<!-- Added 2026-08-21 (Jesse, DQ-017 Phase 1). OPTIONAL section — omit it entirely on cards
with no per-coilset data; it is not a lint-locked fixture and its absence is not a gap.

WHAT THIS IS. One row per COILSET as actually run — the grain at which a decoke is really
measured. `## Task Durations` stays authoritative at the heater level and is NOT changed by
this section; these rows SUM to the parent row of the same Job #. Where they do not sum, the
parent row carries `hours-blended` and that marker is what says so.

WHY IT EXISTS. A heater-level row cannot show that one coilset ran 13 hours off its siblings,
and cannot yield a per-pig travel rate without the ÷Mode approximation. Both were real
failures: the struck ~6 ft/hr Syncrude figure was built on an outlier coilset that nothing on
the card marked as one (DQ-027), and the ÷Mode column is an approximation the parent table
labels as such. This section fixes both by recording what one pig actually did.

  COILS — the set as run: `2/3/4`, `1&8 (looped)`. Name the coils, not a rig-internal label.

  RIG — which Trimax ran this set (`TM5`, `TM6`). Blank on single-rig jobs is fine.

  MODE — SIMULTANEOUS CIRCUITS in this set, which CAN DIVERGE FROM THE TICKET'S LABEL.
        CND25004's 1 & 8 set was written "double mode" because two passes were handled, but
        the pair was LOOPED into ONE circuit — Mode is 1 here. Read the ticket's mode word as
        a passes-handled count and record what actually ran in parallel.

  CIRCUIT FT — FOOTAGE ONE PIG TRAVELS. NOT the set total. A triple-mode set of coils 2/3/4
        is three pigs each traversing one coil (2,237 ft on 7-1-F-1), NOT one 6,711 ft
        circuit. A looped pair is one pig traversing both coils (4,474 ft). Reading this as a
        set total is the same per-pass-vs-heater-total error that produced the struck ~6 ft/hr
        figure — the definition is load-bearing, not pedantry.
        This is what makes the rate a MEASUREMENT: `ft/hr per pig = Circuit ft ÷ Pig`, with no
        ÷Mode approximation. On CND25004 it reproduces 47 / 64 / 124 ft/hr exactly.

  TASK HOURS — same conventions as `## Task Durations`: elapsed, `–` = confirmed did not
        occur, `?` = unrecorded. Total = Rig-In + Pig + Smart Pig + Rig-Over + Rig-Out.

  NO STAND-BY COLUMN, deliberately. Stand-by is a PER-RIG figure, not a per-set one — on
        CND25004 the 192 hrs split 84 (TM5) / 108 (TM6), and TM6 ran two sets with the 108
        unallocated between them. Stand-By stays on the parent Task Durations row.

  COIL CONDITION — how dirty the coil actually WAS. Vocabulary (Jesse, 2026-08-21):
          `light` · `moderate` · `heavy` · `unknown`
        This is the column `Condition` on `## Task Durations` is NOT. That one holds JOB CLASS
        (crash / routine / first) and stays unrenamed and unsplit — DQ-026 kept it that way
        because splitting moves the lint-locked DURATIONS-HEADER across every card and most
        historical rows would land `unknown`. Recording condition HERE costs neither. Expect
        it blank on migrated historical rows; fouling was recorded at job level, not per set.

  FLAG — the per-set data-quality marker DQ-027 had nowhere to put:
          `clean`   = a real, cleanly-separated measurement for this set.
          `outlier` = this set ran well off its siblings (12–24 hrs) on the same heater, same
                      rig config, same mode. Coils on one heater clean within a few hours of
                      each other (Jesse, 2026-08-20), so a spread that wide means a problem
                      specific to that coil on that decoke, or corrupt data. ESTIMATE OFF THE
                      SETS THAT CLUSTER, NEVER THE OUTLIER, and say in the duration math which
                      set you excluded — an unstated exclusion is indistinguishable from
                      cherry-picking. Worked case: CND25004's 48-hr set against its 35/36 hr
                      siblings, which agree within 3%.
          `blended` = the source allocated these hours rather than measuring them.
          `unknown` = quality not recoverable from the source documents.
-->
| Job # | Coils | Rig | Mode | Circuit ft | Rig-In | Pig | Smart Pig | Rig-Over | Rig-Out | Total | Coil condition | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

---

## SOPs

<!-- Card-specific procedural notes/links, if any. Leave header present even if empty. -->

---

## Field Notes

<!--
Per-job operational record: pigs ran, obstacles, facility procedures learned, and (multi-Trimax
jobs only) the per-rig split backing the Task Durations table. Never restate the Task Durations
table's numbers here as prose — the table carries the numbers, Field Notes carries the "why."
"Difficulty"/challenges content (formerly a frontmatter key, dropped 2026-06-22) belongs here,
scoped to the job it occurred on — not as a card-level rating.
-->

### <Job # — Month Year>

**Pigs Ran:**

**Obstacles:**

**Facility Procedures:**

**Per-rig split (multi-Trimax only):**

---

## Notes

<!-- General card-level notes that don't fit elsewhere. -->
