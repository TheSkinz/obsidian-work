---
type: facility
facility-id: Suncor-Montreal-QC
client: Suncor Énergie (Petro-Canada legacy)
city: Montreal
state: QC
last-updated: 2026-09-08
tags: [facility, Suncor]
---

# Suncor Énergie — Montreal, QC (Raffinerie de Montréal)

Source: 2026 TA RFQ package (Appendices A–G, P&IDs and isometrics), Unit 010 Brut #1 (Crude Unit) and Unit 100 (Viscoreduction) integration. Five heaters bid together: B-101, B-102, B-1001, B-103, B-151.

---

## Site Access

| Field | Value |
|---|---|
| Address | (not recorded) |
| Gate / check-in | (not recorded) |
| Badge / access requirements | (not recorded) |
| Site contact | (not recorded) |
| Site contact phone | (not recorded) |
| Escort requirements | (not recorded) |

---

## Site Equipment and Constraints

| Resource | Detail |
|---|---|
| Decoking truck / filter press laydown | Photo-documented pad adjacent to B-101/B-102 area — see individual heater cards for footprint dims |
| Nitrogen purge | B-102 requires nitrogen purge (100 psig, per croquis) before removing spool sections 1-5 and 11-15 for decoke connection |
| Language | Drawings are bilingual FR/EN; decoke annotations mix "décokage"/"decoking" — no functional difference |

---

## Site Safety and Procedures

- **Soda ash is scoped to B-102 radiant only — corrected 2026-09-08 (Jesse: "I think we over generalized").** The governing document is site directive DI-GE-5-007 Rev.5, particular conditions on furnace B-102: *"DECOKING WITH SODA ASH AND TUBE DRYING WITH NITROGEN for radiant only"*. Its §.6 technical table prints `21000 GAL` against B-102 and `N/A — NO SS IN TUBES` against B-101, B-1001, B-103 and B-151. **This reverses the 2026-07-23 reading that soda ash applied across all five heaters including carbon-steel B-151.** The error is worth naming because the artifact that caused it is still on every card: temporary-spool spec **UD1 rates the spools for "water/soda ash" service on all five heaters, and that is a material rating on a spool, not a process instruction for the coil.** Do not read UD1's appearance on the other four cards as evidence of soda-ash scope, and do not re-derive the all-five reading from it. What survives the correction: soda ash / low-chloride water is **always customer scope** — USADebusk does not provide or mix it — and here Suncor supplies it outright (§.7: a baker tank of fresh 2 wt% solution, a second for used solution, and a vacuum truck on hand). The chemistry limits and monitoring cadence are GM-07 Annexe F, summarized in [[CAD26002-crew-brief]]. The only genuinely stainless section in the package is B-102's 347H radiant outlet header — the section the directive scopes it to, which is consistent rather than coincidental.
- B-102 decoke uses a soda ash / frack tank + filter press + open atmosphere basin arrangement per the site's own decoke croquis (010-067B0001) — distinct from the standard USADebusk filter press setup; confirm scope overlap with customer-provided equipment before quoting.
- B-1001 requires full instrumentation removal from decoke circuits before decoking per site work order 60093250 (thermocouples TE-802-1 through -10, doubled).

---

## Heaters at This Facility

- [[B-101]] — Vacuum Feed Heater, mixed metallurgy (P5 convection / P9 radiant)
- [[B-102]] — Crude Furnace, mixed metallurgy within radiant coil (5Cr upper / 9Cr lower)
- [[B-1001]] — Crude Oil Heater, 2 decoke circuits (passes A+D, B+C)
- [[B-103]] — Preflash Reboiler Furnace, single circuit, extreme elevation (35 ft to exit balcony)
- [[B-151]] — Convection/preheater section, carbon steel tubes, no radiant section

---

## Notes

All five heaters share the same RFQ package and are being bid as one turnaround scope — see each card's Job Options for smart-pig/inspection election status per heater.

---

## Source Files

The 2026 TA RFQ package. Drawing appendices for the five awarded heaters and the governing RFQ text are **copied into this folder** so they open in Obsidian in the field (CAD26002, 2026-09-08); OneDrive remains the store of record.

| In this folder | Covers |
|---|---|
| [RFQ Decoke 2026 TA](<RFQ Decoke 2026 TA - B-101 - B-102 - B-103 - B-151 - B-101 REV.pdf>) | Governing RFQ text, all five heaters |
| [APPENDIX C](<APPENDIX C - B-101 PID and Drawings.pdf>) | [[B-101]] P&ID and drawings |
| [APPENDIX D](<APPENDIX D - B-102 PID and Drawings.pdf>) | [[B-102]] P&ID and drawings |
| [APPENDIX E](<APPENDIX E - B-1001 PID and Drawings.pdf>) | [[B-1001]] P&ID and drawings |
| [APPENDIX F](<APPENDIX F - B-103 PID and Drawings.pdf>) | [[B-103]] P&ID and drawings |
| [APPENDIX G](<APPENDIX G - B-151 PID and Drawings.pdf>) | [[B-151]] P&ID and drawings |

**The RFQ filename is Suncor's and carries their typo** — it reads `B-101 - B-102 - B-103 - B-151 - B-101`, listing B-101 twice and never naming B-1001. Nothing is missing; B-1001 is Appendix E. The name is kept verbatim so it still matches the package as Suncor issued it.

**Store of record — not copied:** Appendix A (`Extract GM-07-000-00-001 rev 7 EN.pdf`), Appendix B (`Plot Plan.pdf`) and the two `Price Matrix template … Option 1/2.xlsx` files remain only at

`C:\Users\Jwuts\OneDrive\USADeBusk\Facilities\Suncor\Suncor Montreal\RFQ Package\RFQ Package\`

Note the folder genuinely nests `RFQ Package\RFQ Package` — that is the estate as it exists, not a transcription error. The parent `Suncor Montreal\` also holds `DSP# 25011CAD Suncor Montreal April 2025.pdf`, a prior Montreal quote with no vault record.

Copying an awarded job's drawing package into the facility folder is a bounded exception to the vault-is-the-index rule — see the carve-out in [[rfq-intake-protocol]].
