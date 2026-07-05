# Equipment Library
**Layer:** 04-knowledge/equipment
**Source:** Master Reference Module 5

---

## TriMax Pumper Unit

USADeBusk's proprietary trailer-mounted pigging pumper. Transports cleaning pigs bi-directionally through furnace tubes using high-volume, low-pressure water.

**Physical layout (left to right):**
- Control cab (operator station, far left)
- Dirty tank (2,000 gallons)
- Clean tank (3,000 gallons)
- Waterous CMU Series Two-Stage Centrifugal Pump (far right end)

**Internal routing:**
- Return water from receiver enters via Fig. 200 RAD port at trailer rear
- Routes via fixed pipe along trailer ceiling toward clean tank
- Diverter (90° plunger, operator-controlled from cab) sits at junction above dirty/clean tank
  - Default: water flows to clean tank
  - Thrown (when effluent cloudy): water diverts to dirty tank
- Pump inlet: right side of clean tank
- Pump discharge: right side of pump → out to launcher via Fig. 200 CONV port

**Rear connections:**
- Two Fig. 200 (3") ports at rear of trailer, side by side — one CONV, one RAD
- Both serve as either feed or return depending on selected pig travel direction
- Valve manifold on TriMax controls direction from cab — no hose swapping

**Operating note:** High-volume / low-pressure system. High volume is the distinguishing characteristic — pigs are propelled by flow, not pressure alone.

**Discharge pressure specs:**
- Normal operating: 150–250 PSI
- Maximum: 600 PSI

**Physical dimensions (trailer):**
- Pumper unit: 48'-3⅜" L × 8'-6" W × 12'-10⁷⁄₁₆" H
- Support unit: 48'-5⅞" L × 8'-5¹⁵⁄₁₆" W × 9'-3⅞" H

**Engine — Cummins QSL9 (config D563019CX03, CPL 3823-93996):**
- Rated power: 333 BHP (248 kW) @ 2,100 RPM
- Maximum power: 345 hp (257 kW) @ 2,000 RPM
- Peak torque: 1,050 lb-ft (1,424 N·m) @ 1,500 RPM
- Minimum engine speed for full-load sustained operation: 1,500 RPM
- Displacement 543 in³ (8.9L), turbocharged and charge-air-cooled
- Emissions: CARB Tier 4(f), EU Stage IV, U.S. EPA Tier 4(f)

**Pump — Waterous CMU multi-stage centrifugal:**
- NFPA performance ratings: 1250/1500/1750/2000/2250 GPM @ 150 PSI
- Max pressure: 600 PSI @ 2,250 GPM
- Two-piece, horizontally-split casing; bronze wear rings and impellers; heat-treated stainless steel two-piece impeller shaft (separates from transmission without disassembly)
- Ball-type bronze transfer valve, floating seal, switches PRESSURE/VOLUME without sticking
- Braided flexible graphite (BFG) packing standard; self-adjusting mechanical seals optional
- Transmission: C20 series, drive ratios 1.27–2.46, pneumatic in-cab shift with PUMP/ROAD lock

## Second TriMax (2× TriMax Configuration)

When running 2x TriMax simultaneously:
- Each unit has its own clean tank (3,000 gal) and dirty tank (2,000 gal)
- One shared 4×3 pump and one shared filter press
- T-connections with valve manifolds on both sides link each dirty tank outlet to shared pump suction
- Clean filtrate returns to respective clean tanks
- Both units pig the same direction — B→R means convection-inlet-to-radiant-outlet (standard direction)

## Filter Press

USADeBusk Filter Press #1 specs:
- Dimensions: 44'-3" L × 8'-7" W, trailer-mounted
- 73 polypropylene plates, 1,000 mm plate size
- Surface area: 1,243.4 ft²
- Total volume: 60 ft³
- Operating pressure: 100 PSI
- Capacity: 400 GPM
- Non-gasketed filter cloths
- Cake thickness: 32 mm

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

**Launcher dimensions (RF flanges, inches):**

| Size | Valve handle swing radius (A) | Lid swing radius (B) | C | Length (D) |
|---|---|---|---|---|
| 3" | 24" | 12" | 16" | 42"± |
| 4" | 24" | 12" | 16" | 46"± |
| 6" | 36" | 12" | 20" | 63"± |
| 8" | 36" | 24" | 36" | 82"± |
| 10" | 42" | 24" | 40" | 120"± |
| 12" | 42" | 24" | 40" | 120"± |

- Launcher access requires >36" clearance
- Positioned within 48" of grade or deck
- Fig. 200 hammer union supplies water to the system; drain valve empties water once pig has returned

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

**Fig. 200 hammer union spec (Kemper):** 2,000-psi NSCWP (non-shock cold working pressure), available 1" through 10", butt-weld Schedule 40/80, color-coded blue nut / gray subs, stainless steel subs available. Compact, popular for low-pressure rig piping; meets medium-pressure requirements for air/water/oil/gas service. Kemper's full union line spans other pressure classes (Fig. 100 through 2202, up to 22,500 psi) not currently used in USADeBusk's fleet — see source PDF if a job ever needs a different figure.

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

---

## Source Documents

Manufacturer/company spec sheets backing the figures above, kept at `04-knowledge/equipment/spec-sheets/`:

| File | Covers |
|---|---|
| `Cummins TriMax.pdf` | Cummins QSL9 engine performance data (FR93996) |
| `DEBUSK Pumper & Support Dims.pdf` | TriMax pumper and support unit trailer dimensions |
| `Filter Press # 1.pdf` | USADeBusk Filter Press #1 dimensions and specs |
| `Pump Curve CMUPigging.pdf` | Waterous CMU pump specifications and performance curves |
| `USA PIG LAUNCHER Dim with flanges explained.pdf` | Pig launcher dimensions by size, flange notes |
| `Fig 200 Spec sheets.pdf` | Kemper oilfield hammer union catalog (Fig. 200 and other pressure classes) |
