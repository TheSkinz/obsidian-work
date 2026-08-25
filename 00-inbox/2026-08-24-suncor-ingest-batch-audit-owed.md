---
type: note
status: inbox
created: 2026-08-24
tags: [inbox, heater-cards, data-quality, suncor, owed]
---

# Owed — audit the other four cards from the 2026-07-07 Suncor ingest

B-102 was found on 2026-08-24 to have carried **heater totals in per-circuit columns across seven cells**, contradicting its own Config Rollup, from its ingest in `7798d54` ("Add Suncor Montreal 5-heater RFQ package"). It came in with four siblings that nobody has re-checked: **B-101, B-103, B-151, B-1001** (`02-facilities/Suncor/Montreal-QC/`).

**Why this is not already covered.** The cross-check added the same day (`bdf6d52`) compares Tube Geometry per-circuit tube counts against Config Rollup by zone, and reports all four clean. But that tests **one field**. B-102's defect was systematic across tube counts *and* lengths, and nothing has verified metallurgy, schedule, wall, bore, or arrangement on any of the five against the source RFQ package.

A batch that produced one card that wrong deserves one deliberate pass over the rest, against the original package rather than against the cards' own internal consistency.

**Known already, so not a finding:** B-1001 and B-151 were flagged by the audit and cleared as correct — B-1001 records `18/circuit (36 heater-total ÷ 2 circuits)`, which is right, and B-151 is a single-pass heater where both scales coincide. B-103 carries `46 (2 + 44)` as a compound tube count, which is a legibility gap rather than a known error.

**Start with:** the source RFQ package path recorded on the cards, and `04-knowledge/coil-geometry-audit.md` for what the fleet check already knows.
