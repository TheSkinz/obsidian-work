---
type: review
status: open
review_type: heater-card-routing
created: 2026-06-28
source_authority: secondary
confidence: high
review_after: 2026-07-05
related:
  - [[Final Heater Card Output — HF Sinclair Navajo Refinery - H-2501]]
  - [[HF-Sinclair-Artesia-NM]]
tags: [vault-review, heater-card, HF-Sinclair, Navajo-Refinery, H-2501]
---

# Review - H-2501 Heater Card Routing

## Trigger

Daily Vault Review Loop found the next unreviewed heater-card inbox item at `00-inbox/Final Heater Card Output — HF Sinclair Navajo Refinery - H-2501.md`. It is labeled final and says all primary values are explicit anchors from a source Excel heater card. Because the content is still a heater-card fact package, it should remain behind approval before creating or updating any canonical heater card.

## Evidence

| Claim / signal | Source | Authority | Notes |
|---|---|---|---|
| Source note identifies HF Sinclair Navajo Refinery / H-2501. | `00-inbox/Final Heater Card Output — HF Sinclair Navajo Refinery - H-2501.md`, heading and Job / Heater Identification table. | Secondary extracted heater-card output. | Search found no existing `H-2501` heater note outside the inbox during this loop. |
| Source note is marked `OUTPUT STATUS: FINAL`. | Same source note, status block. | Secondary extracted heater-card output. | The note states no unresolved variables affect calculations. |
| Facility, heater, service, convection/radiant lengths, pass count, tubes per pass, and coil lengths per pass are described as anchor values from source Excel. | Same source note, status block and Source Inventory. | Secondary extracted heater-card output from stated Excel source-of-record. | Higher confidence than H-2421 because the note does not preserve routing uncertainty. |
| Likely destination exists at HF Sinclair Artesia facility area. | `02-facilities/HF-Sinclair/Artesia-NM/HF-Sinclair-Artesia-NM.md`; existing `02-facilities/HF-Sinclair/Artesia-NM/H-2421.md`. | Existing vault structure. | Destination should be approved before creating `H-2501.md`. |

## Proposed Action

1. Keep the inbox source note unchanged until Jesse approves routing.
2. If approved, create `02-facilities/HF-Sinclair/Artesia-NM/H-2501.md` as a draft/source-derived heater card unless Jesse explicitly approves reviewed/canonical status.
3. Preserve the source note's anchor/final claims and source Excel caveat in the destination note.
4. Do not use H-2501 geometry in estimating, SOP, field execution, or customer-facing material until the heater card status is approved.

## Approval Boundary

This loop run did not move, edit, archive, delete, canonicalize, or promote `00-inbox/Final Heater Card Output — HF Sinclair Navajo Refinery - H-2501.md`. Specific Jesse approval is required before editing any source note, canonical heater card, facility note, estimating reference, SOP, field execution note, or customer-facing material.

## Risks / Open Questions

- The source note says the values are final and anchor-based, but the loop reviewed only the markdown output, not the original Excel file.
- The correct facility display name should be kept consistent with existing `HF-Sinclair/Artesia-NM` records before creating the heater note.
- The radiant section uses mixed 4 inch and 6 inch diameters; that fact should be preserved clearly if routed because it affects pigging assumptions.

## Decision

- [ ] Approve creating a draft/source-derived H-2501 heater card
- [ ] Approve creating a reviewed H-2501 heater card from this final output
- [ ] Keep this as inbox evidence only
- [ ] Request review of the original Excel heater card before promotion
- [ ] Reject as insufficient for vault heater-card use

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-06-28 | Created review note; no source or canonical notes modified. | Codex | Daily Vault Review Loop. |
