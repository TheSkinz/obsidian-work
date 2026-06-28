# Estimating Approach
**Layer:** 01-context — loads every session
**Source:** usadebusk-estimating skill

---

## Commercial structure

Most jobs (95%+): T&M on execution, Lump Sum on Mob/Demob.

Mob/Demob is estimated as Day shift cost bucket only: total drive hours + per diem per travel day per person + equipment travel costs. Presented as two separate lump sum line items.

Third-party markup rate is contract-specific.

---

## Duration calculation

Baseline pigging rate: 100 ft/hr per pass.

Adjust the rate downward (more hours required) for:
- Coker or crude service
- Pitch presence
- Hard fouling history
- Tight tube ID (under ~3")

Use prior job data when available for the same facility or service type.

Standard fixed durations:
- Rig-in: 6 hrs
- Rig-out: 6 hrs
- Smart Pig run: 4 hrs (when applicable)

All tasks run on 12-hr shift cycle. Pigging runs 24/7.

---

## Equipment profile

| Config | Assets | Crew impact |
|---|---|---|
| 1x TriMax | 1 pumper, 1 support unit | Smaller crew |
| 2x TriMax | 2 pumpers, 2 support units | Larger crew, dual-shift standard |
| 3x TriMax | 3 pumpers | Major TA scope |

Filter Press is billed concurrently at Pumping rate when TriMax is actively pigging, Non-Pumping (stand-by) rate otherwise.

---

## Pricing rules

- Rate-application discipline (no prior-job rates without confirmation) lives in `usadebusk-estimating` — not duplicated here.
- Never assume tube footage, pass count, or equipment profile — always derive from provided data.
- When generating the Execution Plan, show duration math explicitly so Jesse can verify before the document is finalized.
- When generating the Quotation, show line item (hours × rate) calculations in a working note before producing the final table.

---

## Proposal document structure

**Canonical authority: `usadebusk-estimating` skill** (config-repo commit `025578c`, 2026-06-15). Do not maintain a parallel section list here. The skill holds the authoritative 14-section order, full section templates (Sections 3–9 detail, boilerplate 10–14), merged intake checklist (17 items + drawing rule + incomplete-input gate), and proposal generation guardrails.

Document number format: DSP##### YYYY-MM
