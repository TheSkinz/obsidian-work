# Decoking Method Comparison — Mechanical Pigging vs. Steam-Air
**Layer:** 04-knowledge/concepts
**Source:** Customer-conversion deliverable, 2026-07-22 (DeBusk Services Canada coker-heater leave-behind). External claims web-verified this session — see Verified Sources.

---

## What this is / when to use

Reusable technical + sales positioning for the recurring question "why should we move off steam-air decoking to mechanical pigging?" — most sharply for a **coker heater on heavy / oil-sands feed**. Backs customer conversations, leave-behind documents, and the "why pigging" framing in bids. Originated from a DeBusk Services Canada rep-meeting document (Marshall Douglas request, 2026-07-22). This note is the durable knowledge; the branded deliverable is a rendering of it.

## The two methods

- **Steam-air decoking (SAD).** Oxidation process. Steam spalls coke at elevated temperature, then air is introduced so residual combustible coke burns inside the tubes. Exothermic — tube-metal temperature must be held in a controlled window. Removes what will *burn*.
- **Mechanical pigging.** Studded pigs propelled bi-directionally through the coil on water pressure, run in progressive sizes to bare metal. Removes coke *and* inorganic scale; solids leave in the return water (captured/filtered). Endpoint is measurable (flow test + effluent).

## Comparison (condensed)

| Attribute | Mechanical Pigging | Steam-Air Decoking |
|---|---|---|
| Mechanism | Studded pigs, water pressure; scrapes to bare metal | High-temp oxidation; burns combustible coke in place |
| Deposits removed | Coke + inorganic scale / non-combustibles | Combustible coke only; inorganics remain |
| Cleanliness | Near-bare-metal | Residual inorganics can seed re-coking |
| Tube temperature | Low-temp hydraulic | Elevated; hot-spot / metallurgy risk |
| Wall-thickness inspection data | Yes — post-clean smart-pig (ILI) UT run for the RBI file | None |
| Emissions | No in-tube combustion; contained liquid effluent | Combustion off-gas (PM/NOx/CO), permitting exposure |
| Cleaning window | ~18–24 hr (coker) | Longer offline shutdown sequence |

## Why pigging wins for coker heaters (esp. Canadian oil-sands)

1. **Inorganics steam-air can't remove (lead argument).** Heavy/oil-sands feed carries inorganic, non-combustible material into the coker heater. A burn physically can't remove it; the residue seeds the next coke layer. This is the decisive point for a Canadian coker and is sourced to peer operators, not a vendor.
2. **Bare-metal start-of-run condition** — fewer nucleation sites, protects run length.
3. **Lower thermal risk** — no sustained in-tube combustion, so no hot-spot metallurgy exposure.
4. **Inspection data, not just a clean** — the smart-pig / ILI UT wall-thickness run is the single hardest-to-argue differentiator; SAD produces no wall data. See `process-flow.md` (Smart pig / ILI) for velocities and vendors.
5. **Lower emissions / permitting burden** — closed-loop water process vs. combustion off-gas.
6. **Measurable, verifiable endpoint** — before/after flow test, effluent clarity/discharge-time, pig-condition tracking, final foam run + client sign-off (the USADeBusk 4-point verification protocol).
7. **Frees plant staff** — self-contained specialist service; compatible firebox/maintenance work can proceed in parallel (subject to isolation/confined-space controls).

## Verified sources (web-verified 2026-07-22, direct fetch)

- **AFPM Question 74** — "How effective are online spalling, mechanical pigging, and steam-air decoking in a delayed coker furnace." Coker-specific, and the key statements are attributed to **Marathon Petroleum** (a refiner) and **CH2M Hill** (an engineering firm) — *peer/operator testimony, not vendor marketing*. Verbatim confirmed: SAD "requires a heater shutdown… environmental permitting issues for the emissions… potential for tube damage. If you get a really hot spot, the metallurgy may be affected. It is hindered by any inorganic foulants, and you will have residual foulant in the tubes" (Marathon); tar-sands inorganics "cannot efficiently be removed with steam air decoking. For that reason, many operators switched to the mechanical decoking method" (CH2M Hill); pigging "removes all of the coke" in "18 to 24 hours" (Marathon). URL: afpm.org → data-reports/technical-papers/qa-search/question-74.
- **AIChE "Decoke Tutorial," 2019 Spring Meeting & 15th Global Congress on Process Safety (paper 78d)** — steam-air decoke emissions (PM/NOx/CO) vary by effluent-disposal route (firebox vs. decoke drum). Presenter name not confirmed — cite the paper, not a person.

## Source landmines (do NOT reuse — saves re-checking)

- **Cokebusters** — a direct mechanical-pigging **competitor**. Do not cite as a source or name as a vendor in customer-facing DeBusk material (Jesse's call, 2026-07-22), even though their public "Comparing Decoking Methods" page favors pigging.
- **Oil & Gas Journal (the 2018 Johnson/Wilborn and 1990 Lieberman articles)** — direct fetch showed they do **not** contain the steam-air duration / tube-rupture claims that web-search snippets implied. Do not cite them for those points.
- **US Patent 4,297,147** — real, but it is a 1981 Union Carbide *abrasive particle-gas* method (about avoiding return-bend erosion), **not** a steam-air source. A ChatGPT draft misattributed it. Do not use it to support steam-air claims.
- **"96 hrs → 24–36 hrs / 5 days → 2 days" case-history numbers** — uncorroborated; a ChatGPT draft inflated them. Use only the verified ~18–24 hr pigging figure (AFPM).

## Deliverable

Branded DeBusk Services Canada 3-page leave-behind (`.docx`), technical-only, logo placeholder for self-replace. Not stored in-vault (binary; vault is markdown-first) — regenerate from this note if needed. Related: `industry-foundation.md`, `process-flow.md`, `usadebusk-estimating` Section 6 (verification protocol).
