# Process Flow & Pig Travel
**Layer:** 04-knowledge/concepts
**Source:** Master Reference Module 4

---

## Full decoking sequence

**Rig-In** *(fixed event — hours and scheduling belong to the estimate, not this note; see the Duration Model in `usadebusk-estimating`)*
1. Position Trimax pumper, clean tank, dirty tank adjacent to heater
2. Customer's pipe-fitters install the USADebusk launcher/receivers on the coil flanges the job's configuration calls for (adapters as required) — see Role boundary below. Unlooped, that is one at the convection inlet and one at the radiant outlet per pass; **looped, both land at the same end and the loop 180s take the other**
3. Where passes are looped, the fitters install the customer-fabricated 180° spools at the looped end — radiant outlets or convection inlets, per job
4. Route Fig. 200 jetting hoses from Trimax rear ports to launcher/receiver connections
5. Connect filtration circuit *(only when filtration is Elected — read the heater card Job Options)*: dirty tank → 4×3 pump → filter press → clean tank; otherwise effluent drains to coke pit / oily water sewer
6. Fill system and pressure test
7. Confirm valve manifold positions (direction of pig travel)
8. Run BEFORE flow test (RPM vs PSI vs GPM baseline) — must occur before first pig launch

**Pigging Operations (24/7 with shift handovers)**
1. Load pig into launcher, close and pressure up
2. Open launch valve — water pressure propels pig through coil
3. Pig exits at receiver, collected
4. Return water enters Trimax via Fig. 200 port → ceiling pipe → diverter
5. Operator monitors effluent: cloudy → divert to dirty tank; clear → clean tank
6. Filtration loop runs concurrently *(only when filtration is Elected — otherwise effluent drains to coke pit / oily water sewer)*: dirty tank → 4×3 pump → filter press → clean tank
7. Load next pig (same size or next size up), repeat
8. Continue until effluent discharge time ≤ 3–5 seconds and effluent runs clear
9. Run AFTER flow test (same RPM vs PSI vs GPM) — after final pig pass
10. Log all data on service receipt

**Rig-Out** *(fixed event — hours and scheduling belong to the estimate, not this note; see the Duration Model in `usadebusk-estimating`)*
- Dewater and depressurize; confirm zero pressure at every circuit *(on inspection-supported scopes this waits on the customer's acceptance of the inspection data)*
- USADebusk breaks the jetting hoses from the 3" connections on the launchers/receivers
- Customer's pipe-fitters break the coil flanges, remove the launchers/receivers, and help place them back on the USADebusk support unit; the fitters then reconnect the heater piping
- Remove all hoses and surface equipment; clean the tanks and filtration equipment
- Clean site

> **Role boundary — who bolts the coil flanges.** USADebusk supplies and owns the launchers and
> receivers, but does **not** bolt or unbolt the facility's heater flanges, and does not handle spool
> pieces. The customer's pipe-fitters offload them from the USADebusk support trailer, hang them at
> rig-in — usually while USADebusk is running hoses — remove them at rig-out, and reconnect the heater
> piping afterward. The units weigh over 400 lbs and the fitters have crane and forklift access
> USADebusk does not. **USADebusk's connection boundary is the 3" Fig. 200 connection on the
> launcher/receiver:** we make and break the hose, they make and break the flange. Who the fitters are
> is the customer's call and usually not known until arrival — call them "the customer" in
> customer-facing documents. See [[07-roles-and-responsibilities]] §7.1. (Jesse, 2026-08-17.)

## Flow path — standard single pass (convection-to-radiant)

```
Trimax Clean Tank → Waterous Pump → Fig.200 BLUE port → Jetting Hose →
Launcher/receiver (Conv. Inlet Flange) → Convection Tubes (serpentine) →
Cross-over → Radiant Tubes → Launcher/receiver (Rad. Outlet Flange) →
Jetting Hose → Fig.200 RED port → Internal ceiling pipe →
Diverter → Clean Tank (clear) or Dirty Tank (cloudy)
```

**This is the standard unlooped hookup, not a fixed mapping.** Blue is the feed port and Red the return; which coil flange each serves is a per-job assignment following where the spool is bolted. CONV and RAD name heater *sections*, never ports (Jesse, 2026-09-02). For reversed direction (red to blue): return water comes back via the Blue port. Valve manifold on Trimax controls direction — no manual hose swapping required.

**Filtration loop (concurrent — only when filtration is Elected; see the heater card Job Options):**
```
Dirty Tank → 3" Camlock → 4×3 Pump → 3" Camlock → Filter Press (100 PSI) →
3" Camlock → Clean Tank
```

The filtration loop operates independently from the main pigging process and does not influence process coil pressure or pig travel. When not elected, effluent drains to coke pit / oily water sewer instead.

## Looped circuit (jumper spool configuration)

When two passes are looped via 180° jumper spool:
- Spool connects the corresponding flanges at the **same end** of both passes. **The end is a per-job election with no default** — CAD26001 and ExxonMobil F-901/F-802 loop at the radiant outlets; Valero Three Rivers and ExxonMobil F-501 loop at the convection inlets
- **Both the launcher and the receiver land at the unlooped end, and the looped end carries no spool at all** — the 180s take their place. That is the consequence most easily missed when reading a rig-in sequence written for unlooped passes
- Pig travels (loop at the outlets): Conv. Inlet Pass 1 → full Pass 1 coil → Rad. Outlet Pass 1 → Jumper Spool → Rad. Outlet Pass 2 → full Pass 2 coil (reverse direction) → Conv. Inlet Pass 2. Loop at the inlets and the path mirrors — launch and recover at the radiant outlets
- Creates longer circuit — extended pig transit, a function of footage, pipe ID, and GPM (observed ~6–30 min across looped jobs, not a fixed range)
- Longer blind period between launches requires careful monitoring
- Final pig size may need to be larger (e.g., 6.5" vs. 6.25") to achieve full wall contact on long combined circuits

## Pig progression strategy

- Start with foams or undersized TCs to open the path
- Progress by 1/8" increments per successful pass
- Line-size pig (tube ID): removes bulk of coke
- Oversized pig (tube ID + 0.125" to 0.250"): final cleanup, wall contact for residual removal
- Example (6.065" ID tube): start 6.0" TC → 6.25" TC (final standard) → 6.5" TC if heavy fouling or looped circuit
- Maximum pig OD = tube ID + 0.250" (governs all passes; use the smaller governing tube ID)

**Crossover reducer note:** The reducer between convection outlet and radiant inlet sits on the cross-over piping. Significant obstruction point — has been encountered as a blockage location when transitioning from 5" convection pigs to 6" radiant pigs. Must be addressed explicitly in pig progression planning for mixed-ID heaters.

## Cleaning completion criteria

All three must be met before stopping:
1. Effluent discharge time ≤ 3–5 seconds per pig pass
2. Effluent runs consistently clear
3. Before/after flow tests show measurable pressure drop improvement at equivalent GPM

## Smart pig / ILI inspection (post-decoking)

Run after mechanical cleaning confirms tube walls are clean. USADebusk provides water propulsion only — vendor controls tool.

- Target velocity: 1.0–2.0 ft/s (slow, constant speed required for UT data quality)
- For 4" ID pipe: approximately 40–70 GPM target range at inspection velocity
- Vendor specifies exact flow envelope in writing before each tool run — do not set pump speed independently of vendor spec
- Common vendors: Quest Integrity, TEAM, Cokebusters, SteadyFlux

## Role boundaries

- **USADebusk:** All pigging equipment, surface connections, pig propulsion, filtration, service receipts, technical documentation
- **Customer:** Isolation, blinds, PSV protection, permit-to-work, water supply to USADebusk tanks, fabricated adapters when required
- **Lifting contractor:** All rigging and lifting — USADebusk does not perform lifts
