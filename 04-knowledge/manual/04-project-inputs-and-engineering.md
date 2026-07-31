# 4. Project Inputs and Engineering

**Layer:** 04-knowledge/manual
**Source:** `~/.claude/skills/usadebusk-sop/SKILL.md` (Required Inputs), `04-knowledge/concepts/industry-foundation.md` (Key variables)
**Manual:** [[00-manual-index]]

---

Every job is engineered against confirmed heater data before any equipment moves. This section states what that data is, why each item drives a decision, and what USADebusk produces from it. For a client preparing a scope of work or responding to a data request, this is the working chapter of the manual.

## 4.1 Information required

USADebusk does not begin a job SOP until the following are confirmed. Where a value is genuinely unknown, it is recorded as unknown and resolved before execution rather than assumed.

| # | Input | What it determines |
|---|---|---|
| 1 | Facility and unit | Site requirements, permitting interface, applicable customer specifications |
| 2 | Heater tag and service | Expected fouling character, process context |
| 3 | Pass / circuit count | Equipment quantity, launcher and receiver sets, number of simultaneous circuits |
| 4 | Coil pairing and loop configuration | Which passes can be looped through a jumper spool, and therefore circuit length |
| 5 | Tube ID, convection and radiant | Pig sizing, launcher and receiver size, adapter requirements |
| 6 | Total footage per pass | Scope of the cleaning effort |
| 7 | Inlet and outlet flange size and rating | Launcher and receiver selection, and whether customer-fabricated adapters are required |
| 8 | Tube arrangement, horizontal or vertical | Equipment placement, launcher access, rig-in approach |
| 9 | Expected fouling type | Pig progression strategy and pig selection |
| 10 | Tube metallurgy, per section | Whether passivation applies, and water chemistry constraints |
| 11 | Water source | Supply arrangement, and on stainless work, chloride control |
| 12 | Launcher access and elevation | Whether a working deck exists, and whether scaffolding is required |
| 13 | Jumper spool requirements | Quantity, size, and flange rating of spools the customer fabricates |
| 14 | Applicable standards and customer specifications | Any facility procedure, industry standard, or client specification governing the work |

Return bend type, including whether any section uses plug-type headers, is recorded per section and affects the procedure written into the SOP.

## 4.2 Where the data comes from

Heater general arrangement drawings, coil detail drawings, and data sheets are the primary source. Where a drawing gives outside diameter and schedule, inner diameter is derived and cross-checked rather than read from a note. Where field measurement is the only available source, it is recorded as such.

Two cautions apply to drawing-sourced data. General notes on a drawing are frequently generic boilerplate carried across a whole drawing set and do not necessarily describe the heater in front of you. And where extracted values disagree between sources, the discrepancy is raised and resolved with the customer rather than silently reconciled.

Where inputs are taken from a drawing or data sheet, USADebusk presents the extracted values back to the customer in a confirmation table before drafting the SOP. That confirmation step exists because pig sizing is derived from these numbers, and a wrong inner diameter is a field problem, not a paperwork problem.

## 4.3 Pig sizing derivation

Two numbers come out of the input data and govern the whole progression.

The **governing tube ID** is the smallest inner diameter present anywhere in the circuit, across all sections and all size segments. It is normally a convection dimension.

The **maximum pig OD** is the governing tube ID plus 0.250 inches. No pig above that figure is run in that circuit. Where a heater carries multiple sections of different sizes, the smallest governs the entire circuit, not just the section it belongs to.

Looped circuits are the one case where the final pig may be taken to the larger end of the permitted range, because a longer combined circuit requires more positive wall contact to finish. That remains inside the maximum, not above it.

## 4.4 What USADebusk produces

From confirmed inputs, USADebusk prepares the heater-specific execution SOP and the process flow diagram, and on jobs where the customer's engineering review requires it, a full pre-execution technical package. Section 16 lists the contents.

<!-- GRAPHIC 4-1: annotated tube cross-section showing OD, wall thickness, and ID as three distinct dimensions, with a callout that ID is the figure pig sizing keys off and OD + schedule are how it gets verified. Small and diagrammatic; this is a vocabulary graphic, not a drawing reproduction. -->

## 4.5 What the customer confirms

Beyond the technical data, four practical items are settled in planning because they determine what can physically be done on site: the water supply arrangement and its point of connection, the effluent disposal route, whether filtration is elected, and whether the coil requires the initial flush described in Section 13 to remove residual hydrocarbon before decoking begins.

---

Previous: [[03-heater-and-coil-fundamentals]] · Next: [[05-system-and-equipment]]
