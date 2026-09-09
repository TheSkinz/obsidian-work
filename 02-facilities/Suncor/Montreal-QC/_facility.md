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

- **Soda ash here is a customer-instruction override, not a USADebusk metallurgy trigger** (Jesse 2026-07-23). The Suncor rep's decoke spec (UD1 "water/soda ash" temp-spool spec) calls for soda ash across all five heaters — including carbon-steel B-151 — regardless of tube metallurgy. Soda ash / low-chloride water is always customer scope: USADebusk does not provide or mix it, and follows the customer rep's RFQ/bid instructions as default (which may follow NACE or a facility-specific passivation method rather than the stainless-only default). The only genuinely-stainless section in the package is B-102's 347H radiant outlet header. Read the RFQ for the governing passivation method before scoping.
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
