# Industry Foundation
**Layer:** 04-knowledge/concepts
**Source:** Master Reference Modules 2 & 3

---

## What furnace decoking is

Fired heater tubes in refineries and chemical plants accumulate petroleum coke deposits over time from process fluid passing through them. Coke is a carbon-rich byproduct of thermal cracking — it builds up on tube walls as the process fluid is heated.

Why refineries need it: coke reduces heat transfer efficiency, increases tube skin temperatures (tube failure risk), increases pressure drop across the coil, and eventually causes unplanned unit shutdowns. Refineries schedule decoking during planned turnarounds or when pressure drop/temperature data indicates cleaning is needed.

## Heater types

| Type | Description |
|---|---|
| Cabin / Box | Rectangular structure; burners on floor or sides; common in crude/VDU service |
| Vertical Cylindrical (VC) | Cylindrical shell; burners on floor; coil arranged in circular pattern around center |
| Arbor / Wicket | Coil hangs in loops; less common |

## Coil sections

**Convection section:** Upper section. Horizontal tube arrangement standard. Heated by flue gas convection only. Lower tube skin temps. Convection tube ID is the same size as or smaller than radiant tube ID on virtually all heaters USADebusk services (confirmed across 23+ years of field experience — exceptions exist but are extremely rare, less than 1%).

**⚠ FLAG BEHAVIOR:** If heater data shows convection tube ID *larger* than radiant tube ID, flag it immediately before proceeding with any SOP, proposal, or pig sizing work. Anomalous — must be confirmed before continuing.

**Radiant section:** Lower section. Direct flame radiation. Highest heat flux. Heaviest fouling typically found here. Radiant outlet is the hottest and most fouling-prone location.

**Cross-over:** External piping between convection outlet flange and radiant inlet flange. Contains the tube size reducer when convection and radiant tube IDs differ.

## Key variables driving job approach

| Variable | Why it matters |
|---|---|
| Pass / circuit count | Determines equipment qty, launcher/receiver sets, job duration |
| Tube ID (convection and radiant) | Sets pig sizing, launcher/receiver size, required adapters |
| Inlet/outlet flange size & rating | Determines launcher model and customer-fabricated adapters |
| Total tube footage per pass | Primary driver of pigging duration estimate |
| Tube arrangement (H vs. V) | Affects equipment placement, launcher access, rig-in complexity |
| Expected fouling type | Standard coke, hard coke or pitch — affects pig progression strategy. Expectation language: what we predict from service and history, never a finding. See [[17-glossary]] |
| Tube metallurgy | Carbon steel = standard; Stainless steel = requires soda ash passivation |
| Coil pairing / loop config | Which passes can be looped via 180° jumper spools |

## Tube dimensions — common reference

- 4" Sch 40: OD = 4.500", ID = 4.026"
- 5" (convection typical in some units): ID ~5.047"
- 6" Sch 40: OD = 6.625", ID = 6.065"
- 8" Sch 40: ID = 7.981"
- 10" Sch 40: ID = 10.020"

## Metallurgy — passivation

**Carbon steel:** Standard process, no modification needed.

**Stainless steel:** Requires passivation. Soda ash solution circulated through coil after mechanical cleaning to restore passive oxide layer. pH monitoring required throughout.
- Target pH: maintained above ~10.0 during circulation
- Circulation velocity: ~1–2 ft/s
- Final flush to neutral pH before job closeout
- Chloride limits: fresh solution ≤250 ppm, spent solution ≤500 ppm, verify <0.5 ppm before fill

## Terminology

**The glossary is [[17-glossary]].** It is the single authority for USADebusk terminology, including the fouling vocabulary and the expectation-versus-finding split that now governs it. This section used to duplicate it and had drifted — it was the only place carrying "soft coke", a term defined nowhere in the vault and naming a coke-drum property in refining, so it has been retired. Only the terms 17-glossary does not carry are kept below.

| Term | Definition |
|---|---|
| Stand-by | Time on site but not actively pigging — may be billable depending on cause |
| Plant Down Time (PDT) | Facility-caused downtime — generally billable as stand-by |
| Ticket Breakdown | Per-job Excel file tracking all billable resources, durations, and rates |
| Service Receipt | Handwritten daily field document completed by PM for each 12-hour shift |
