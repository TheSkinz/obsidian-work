# Equipment Library
**Layer:** 04-knowledge/equipment
**Source:** Master Reference Module 5

---

## TriMax Pumper Unit

USADeBusk's proprietary trailer-mounted pigging pumper. Transports cleaning pigs bi-directionally through furnace tubes using high-volume, low-pressure water. High volume is the distinguishing characteristic — pigs are propelled by flow, not pressure alone. Not a jetting unit.

**Unit architecture — TRIPLE:** One TriMax trailer contains **3 independent pumping assemblies**. Each assembly has its own engine, gearbox, pump (Waterous CMU Series two-stage centrifugal), and valve manifold. All three share ONE clean tank (3,000 gal) and ONE dirty tank (2,000 gal). Three operator stations in the control cab — one per assembly. Each assembly cleans one circuit independently: direction, flow state, and progress are set per assembly. Scope determines how many of the 3 assemblies are used; unused assemblies sit idle. The three assemblies, left → right: **left (pump 1), center (pump 2), right (pump 3)** — referenced as left/center/right when identifying which assembly/circuit is in use.

**Physical layout (left → right):**
Control cab (3 operator stations) | Dirty tank (2,000 gal, shared) | Clean tank (3,000 gal, shared) | 3× pump/engine assemblies

**Internal routing (per assembly):**
- Feed side: clean tank → suction strainer → pump → flow meter → valve manifold → Fig. 200 CONV port → launcher
- Return water enters via Fig. 200 RAD port at trailer rear, routes via fixed pipe along trailer ceiling toward clean tank
- Diverter (90° plunger, operator-controlled from cab) at junction above the tanks
  - Default: clean tank
  - Thrown (cloudy effluent / pig capture / initial flush): dirty tank

**Rear connections:**
- Two Fig. 200 (3") ports at rear of trailer, side by side — one CONV, one RAD
- Both serve as either feed or return depending on selected pig travel direction
- Valve manifold controls direction from cab — no hose swapping
- Standard conv-to-rad: feed exits CONV, return enters RAD. Reversed: feed exits RAD, return enters CONV.

**Operating pressure:** 100–400 PSI typical; 600 PSI absolute system limit. Over-pressure checklist required above 500 PSI.

## Second TriMax (2× TriMax Configuration)

Terminology: "second TriMax" or "2× TriMax" — never "dual-pumper." Use "Triple" for the unit itself.

- Each TriMax = its own tanks (3,000 gal clean / 2,000 gal dirty) + its own 3 pump/engine assemblies → 2× TriMax = up to **6 simultaneous circuits**
- Filtration scales **conditionally**: 2× filter presses + 2× 4×3 pumps when the customer requires it AND a 2nd press is available; otherwise 1× shared filter press + 1× shared 4×3 pump serving both units
- When shared: T-connections with valve manifolds on both sides link both dirty-tank outlets to shared pump suction; clean filtrate returns to respective clean tanks
- Each assembly runs its own circuit fully independently — direction, flow state, and progress are set per assembly. There is **no cross-assembly direction constraint** (the two units do not have to pig the same direction).

## Double Pumper

Same custom design as the TriMax but on a single trailer with **two** of each major component (engine, gearbox, pump, valve manifold) instead of three. Two independent pump assemblies: **left = pump 1, right = pump 2. No center.** Cleans two circuits simultaneously. Fleet carries two of these (Double 1, Double 2), reserved for special/overseas jobs (~1×/year each) — see [[equipment-fleet]].

**Distinguishing invariant:** assembly count (two vs. three) and the presence/absence of a center assembly. This separates the double pumper from both the TriMax (three assemblies, L/C/R = 1/2/3, one trailer) and the Second TriMax (two trailers, six assemblies total).

**Guardrails:**
- **Don't overwrite:** when a job states it uses the double pumper, do NOT substitute the TriMax. "Double pumper" is accepted terminology for this specific unit — leave it as written.
- **Don't invent:** NEVER infer the double pumper from heater data. Pass count, circuit count, and two-pass geometry do NOT imply a double pumper. The TriMax is the default mobilized unit for essentially all jobs INCLUDING two-pass heaters — one pump side simply goes unused. The double pumper is used only when explicitly stated for that job. It is never a heater-card field.

## Terminology Discipline — Pumper Naming

Three distinct units — do not conflate:
- **TriMax / Triple** — 3 assemblies, 1 trailer, L/C/R = 1/2/3
- **Double pumper** — 2 assemblies, 1 trailer, L/R = 1/2, no center
- **Second TriMax / 2× TriMax** — 2 trailers, 6 assemblies total

**"dual-pumper" / "dual pumper" is BANNED** in any document, internal or customer-facing — customers misread it as a pumper limited to two circuits, and it mischaracterizes the three-assembly TriMax as two-assembly. Flag and correct on sight. Note the deliberate near-homophone guard: *double pumper* (real, rare unit) ≠ *dual-pumper* (banned term).

## Filter Press

- 73 polypropylene plates
- Surface area: 1,243.4 ft²
- Operating pressure: 100 PSI
- Capacity: 400 GPM
- Non-gasketed filter cloths
- Trailer-mounted

## 4×3 Centrifugal Pump (Trash Pump)

- Standalone trailer-mounted centrifugal pump
- 3" camlock inlet and outlet
- Drives dirty water from dirty tank through filter press
- Operates concurrently with pigging — independent process, does not affect coil pressure

## Pig Launchers / Receivers

- Attached directly to convection inlet flanges (launcher) and radiant outlet flanges (receiver)
- Same form factor — labeled by function and location
- Flange size matches heater flange; customer fabricates adapters when flange rating/size differs
- Fig. 200 hose connection at rear of TriMax connects to launcher/receiver via jetting hose

**Inventory (standard across all furnace pigging companies):**
- USADeBusk carries 10+ launchers of each size, sizes 3" through 12"
- 3", 4", 6", 8": 300# connections on barrel and valve
- 10", 12": 150# connections on barrel and valve
- This flange rating standard is consistent industry-wide

## Pig Types

| Type | Description | Use case |
|---|---|---|
| Foam | Soft foam cylinder — no abrasive elements | Opening passes, initial flow establishment, verification |
| TC (Tungsten Carbide Pin) | Urethane body (84A Duro typical, 78A special), TC pins embedded during molding | Primary coke removal — main workhorse pig |
| HR (High-Recovery / Hard Rubber) | Harder durometer body, aggressive cleaning | Heavy fouling, pitch-laden tubes |
| Swab | Oversized soft urethane | Final cleanup, verification, larger tube sections |

**TC Pig mechanics:**
- Pins embedded in urethane body — cast in mold with chemical hardener
- When pig OD ≤ tube ID: pins extend and dig into coke deposits
- When pig OD > tube ID (oversized): urethane body compresses; pins lay back — differential hardness means pins cut coke but deflect off harder tube wall without damage

## Hoses & Connections

| Component | Type | Size | Notes |
|---|---|---|---|
| TriMax to launcher/receiver | Fig. 200 jetting hose | 3" | Connects rear TriMax ports to coil endpoints |
| Filtration circuit (all legs) | Camlock | 3" | Dirty tank → pump → filter press → clean tank |
| Dirty tank vac access | Camlock | 3" | T-branch on dirty tank outlet for vac truck access |

## Support Equipment

| Equipment | Purpose |
|---|---|
| Crew Truck | Crew transport and tool/supply hauling |
| Support Unit | Additional equipment/supply transport trailer |
| DEF (Diesel Exhaust Fluid) | Fuel additive for equipment compliance; billed per shift |
| Vac Truck | Third-party; residual chemical/product disposal from dirty tank |
| Light Plant | Third-party; night lighting for rig-in/out or poorly lit areas |
| Air Compressor | Third-party; pig loading assistance or pneumatic tools |

## Equipment layout (field positioning)

**Option A — No filtration (fire hydrant supply, coke pit discharge):**
```
Fire hydrant → fire hose → each TriMax clean tank
Each TriMax dirty tank → 3" camlock → Coke Pit Drain / Oily Water Sewer
```
1× or 2× TriMax variant.

**Option B — Closed loop with filtration (frac tank supply):**
```
Frac tank → TriMax clean tank(s)
Dirty tank → 4×3 trash pump → filter press → clean tank
```
No hydrant. 1× or 2× TriMax variant. 2× = 2 filter presses, 2 trash pumps (shared or mirrored).

**Physical left-to-right layout (roughly):**
Frac Tank (Option B only) | TriMax unit(s) | Heater | Coke Pit / OWS drain terminus
