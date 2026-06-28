---
type: review
status: complete
review_type: heater-card-routing
created: 2026-06-27
source_authority: secondary
confidence: medium
related:
  - [[Final Heater Card Output — H-2421]]
tags: [vault-review, heater-card, HF-Sinclair, Navajo-Refinery, H-2421]
---

# Review - H-2421 Heater Card Routing

## Trigger

Daily Vault Review Loop found a new inbox item at `00-inbox/Final Heater Card Output — H-2421.md`. It is labeled final, but its own text preserves residual uncertainty around pass routing confidence and radiant segmentation. Because heater-card facts are operationally sensitive, this should remain a review artifact until Jesse approves an exact destination and edit.

## Evidence

| Claim / signal | Source | Authority | Notes |
|---|---|---|---|
| Source note title identifies HF Sinclair Navajo Refinery / HDU Charge Heater / H-2421. | `00-inbox/Final Heater Card Output — H-2421.md`, heading and Job / Heater Identification table. | Secondary extracted heater-card output. | New inbox item; no existing H-2421 references found elsewhere in the vault during this loop. |
| Source note says state is final with residual uncertainty in pass routing confidence. | `00-inbox/Final Heater Card Output — H-2421.md`, state line. | Secondary extracted heater-card output. | Final wording conflicts with the need to preserve uncertainty before canonical promotion. |
| Tube size, tube quantities, and lengths are mostly anchor/BOM-derived, while pass count and routing interpretation are medium-confidence. | `00-inbox/Final Heater Card Output — H-2421.md`, Convection Section, Radiant Section, Evidence Table, Overall Confidence. | Secondary extracted heater-card output. | Overall confidence is medium; pass count is routing-derived rather than explicit pass labeling. |
| Single pass length is calculated as about 452 ft, crossover excluded. | `00-inbox/Final Heater Card Output — H-2421.md`, Single Pass Length section. | Calculated from secondary extraction. | Should not be copied to a heater card without approval because the calculation depends on routing interpretation. |

## Proposed Action

1. Keep the source note in `00-inbox` until Jesse decides whether it should become a draft/source-derived heater card, remain as inbox evidence, or be routed elsewhere.
2. If approved, create or update the destination heater card as `status: draft`, `source_authority: secondary`, and `confidence: medium` unless stronger source documents are reviewed.
3. Preserve the uncertainty wording for pass routing and radiant segmentation in any approved destination note.
4. Do not treat the 452 ft single-pass length as canonical until the pass routing interpretation is accepted.

## Approval Boundary

This loop run did not move, edit, archive, delete, canonicalize, or promote `00-inbox/Final Heater Card Output — H-2421.md`. Specific Jesse approval is required before editing any source note, canonical heater card, facility note, estimating reference, SOP, field execution note, or customer-facing material.

## Risks / Open Questions

- The note is labeled final, but overall confidence is medium, so retrieval may over-trust it if it is promoted without uncertainty.
- The single-pass length depends on pass routing and radiant segmentation interpretation.
- The source inventory references GA drawing, worksheet, and connection/nozzle diagram, but this loop reviewed only the inbox markdown output, not the original files.
- Destination is not yet established: likely HF Sinclair / Navajo Refinery heater-card area, but no H-2421 note currently exists in the vault search results.

## Decision

- [x] Approve creating a draft/source-derived H-2421 heater card with uncertainty preserved
- [ ] Keep this as inbox evidence only
- [ ] Request review of original GA drawing, worksheet, and connection/nozzle diagram before any heater-card promotion
- [ ] Reject as insufficient for vault heater-card use

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-06-27 | Created review note; no source or canonical notes modified. | Codex | Daily Vault Review Loop. |
| 2026-06-27 | Created draft/source-derived H-2421 heater card with uncertainty preserved. | Codex | Destination: `02-facilities/HF-Sinclair/Artesia-NM/H-2421.md`. |



