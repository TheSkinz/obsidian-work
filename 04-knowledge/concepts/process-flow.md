# Process Flow & Pig Travel
**Layer:** 04-knowledge/concepts
**Source:** Master Reference Module 4

---

## Full decoking sequence

**Rig-In (fixed event; default 6 hrs, duration varies by pass count and access complexity — see Duration Model in `usadebusk-estimating`. The 12-hour simultaneous Day/Night framing belongs to Mob/Demob, a separate event.)**
1. Position TriMax pumper, clean tank, dirty tank adjacent to heater
2. Install pig launchers on convection inlet flanges (adapters as required)
3. Install pig receivers on radiant outlet flanges (adapters as required)
4. Route Fig. 200 jetting hoses from TriMax rear ports to launcher/receiver connections
5. Connect filtration circuit *(only when filtration is Elected — read the heater card Job Options)*: dirty tank → 4×3 pump → filter press → clean tank; otherwise effluent drains to coke pit / oily water sewer
6. Fill system and pressure test
7. Confirm valve manifold positions (direction of pig travel)
8. Run BEFORE flow test (RPM vs PSI vs GPM baseline) — must occur before first pig launch

**Pigging Operations (24/7 with shift handovers)**
1. Load pig into launcher, close and pressure up
2. Open launch valve — water pressure propels pig through coil
3. Pig exits at receiver, collected
4. Return water enters TriMax via Fig. 200 port → ceiling pipe → diverter
5. Operator monitors effluent: cloudy → divert to dirty tank; clear → clean tank
6. Filtration loop runs concurrently *(only when filtration is Elected — otherwise effluent drains to coke pit / oily water sewer)*: dirty tank → 4×3 pump → filter press → clean tank
7. Load next pig (same size or next size up), repeat
8. Continue until effluent discharge time ≤ 3–5 seconds and effluent runs clear
9. Run AFTER flow test (same RPM vs PSI vs GPM) — after final pig pass
10. Log all data on service receipt

**Rig-Out (fixed event; default 6 hrs, duration varies — see Duration Model)**
- Remove launchers, receivers, all hoses and surface equipment
- Reconnect customer flanges, clean site

## Flow path — standard single pass (convection-to-radiant)

```
TriMax Clean Tank → Waterous Pump → Fig.200 CONV port → Jetting Hose →
Pig Launcher (Conv. Inlet Flange) → Convection Tubes (serpentine) →
Cross-over → Radiant Tubes → Pig Receiver (Rad. Outlet Flange) →
Jetting Hose → Fig.200 RAD port → Internal ceiling pipe →
Diverter → Clean Tank (clear) or Dirty Tank (cloudy)
```

For reversed direction (radiant-to-convection): return water comes back via CONV port. Valve manifold on TriMax controls direction — no manual hose swapping required.

**Filtration loop (concurrent — only when filtration is Elected; see the heater card Job Options):**
```
Dirty Tank → 3" Camlock → 4×3 Pump → 3" Camlock → Filter Press (100 PSI) →
3" Camlock → Clean Tank
```

The filtration loop operates independently from the main pigging process and does not influence process coil pressure or pig travel. When not elected, effluent drains to coke pit / oily water sewer instead.

## Looped circuit (jumper spool configuration)

When two passes are looped via 180° jumper spool:
- Spool connects Radiant Outlet Pass 1 to Radiant Outlet Pass 2
- Pig travels: Conv. Inlet Pass 1 → full Pass 1 coil → Rad. Outlet Pass 1 → Jumper Spool → Rad. Outlet Pass 2 → full Pass 2 coil (reverse direction) → Conv. Inlet Pass 2
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

Run after mechanical cleaning confirms tube walls are clean. USADeBusk provides water propulsion only — vendor controls tool.

- Target velocity: 1.0–2.0 ft/s (slow, constant speed required for UT data quality)
- For 4" ID pipe: approximately 40–70 GPM target range at inspection velocity
- Vendor specifies exact flow envelope in writing before each tool run — do not set pump speed independently of vendor spec
- Common vendors: Quest Integrity, TEAM, Cokebusters, SteadyFlux

## Role boundaries

- **USADeBusk:** All pigging equipment, surface connections, pig propulsion, filtration, service receipts, technical documentation
- **Customer:** Isolation, blinds, PSV protection, permit-to-work, water supply to USADeBusk tanks, fabricated adapters when required
- **Lifting contractor:** All rigging and lifting — USADeBusk does not perform lifts
