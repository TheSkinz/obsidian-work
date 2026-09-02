# 5. System and Equipment

**Layer:** 04-knowledge/manual
**Source:** [[equipment-library]], `~/.claude/skills/usadebusk-equipment`
**Manual:** [[00-manual-index]]

---

## 5.1 Trimax pumper unit

The Trimax is USADebusk's trailer-mounted pigging pumper and the core of the system. It is a high-volume, moderate-pressure water system: pigs are propelled by flow rather than by pressure alone.

One Trimax trailer, the standard configuration, is a **Triple**: three independent pumping assemblies, each with its own engine, gearbox, pump, and valve manifold, sharing one clean tank and one dirty tank. Three operator stations sit in the control cab, one per assembly. Each assembly cleans one circuit independently, with its own direction, flow state, and progress; assemblies not in use sit idle. A single Trimax therefore supports up to three circuits simultaneously.

Where a heater has more circuits than one unit can serve, or where schedule requires it, a **second Trimax** is deployed. Each unit carries its own tanks and its own three assemblies, supporting up to six simultaneous circuits.

| Item | Specification |
|---|---|
| Pumping assemblies per unit | 3, independent |
| Clean tank | 3,000 gallons, shared across assemblies |
| Dirty tank | 2,000 gallons, shared across assemblies |
| Pump | Waterous CMU series two-stage centrifugal, one per assembly |
| Normal operating pressure | 150–300 PSI |
| Maximum system pressure | 600 PSI |
| Rear connections | A Blue and a Red 3" Fig. 200 port per pump assembly. The heater section each serves is a per-job assignment, not a property of the port |
| Trailer envelope | 48'-3" L × 8'-6" W × 12'-11" H approximate |

Direction of pig travel is set from the cab through the valve manifold. Reversing direction does not require disconnecting or swapping hoses.

Return water from the receiver enters through the rear Fig. 200 port, routes along a fixed internal pipe toward the clean tank, and passes a diverter at the junction above the two tanks. The diverter is operator-controlled from the cab: default flow is to the clean tank, and the operator throws it to the dirty tank when returning effluent is cloudy. That single control is how the system keeps its working water usable while capturing the solids-laden returns.

A support unit trailer accompanies the pumper carrying additional equipment and supplies.

<!-- GRAPHIC 5-1: Trimax trailer schematic, side elevation, left to right — control cab (3 operator stations), dirty tank 2,000 gal, clean tank 3,000 gal, 3 pump/engine assemblies. Call out the two rear Fig. 200 ports and the internal return path: rear port → ceiling pipe → diverter → clean or dirty tank. This graphic carries the "three independent assemblies, shared tanks" idea, which is the one thing customers consistently misread. -->

## 5.2 Launchers and receivers

Launchers and receivers are the same unit; launcher and receiver name the role a spool plays on a given run. Which coil flange each mounts to is set by the job's configuration — commonly inlet and outlet on an unlooped pass, but on a looped circuit both mount at the same end and the loop spool takes the other. Pigs are loaded at the launcher, and recovered at the receiver after each pass.

USADebusk stocks launchers in sizes 3 inch through 12 inch, in quantity, so that multi-circuit jobs can be equipped without staging between passes. Sizes 3, 4, 6, and 8 inch carry 300 pound connections on barrel and valve; 10 and 12 inch carry 150 pound. This rating convention is consistent across the industry.

Where the heater flange size or rating differs from the launcher, the customer fabricates the required adapter. This is confirmed during engineering, not discovered at rig-in.

Two access requirements govern placement. Launchers need more than 36 inches of working clearance for the valve handle and lid swing, and the working position needs to be within roughly 48 inches of grade or a deck. Dimensional detail by size is in [[18-reference-tables]].

<!-- GRAPHIC 5-2: launcher assembly, sectioned. Show barrel with pig loaded, lid, launch valve, coil flange connection at one end and Fig. 200 jetting hose connection at the other, plus the drain valve. Overlay the two access dimensions: >36" clearance for valve handle and lid swing, working position within ~48" of grade or deck. -->

## 5.3 Pigs

| Type | Construction | Use |
|---|---|---|
| Foam | Soft foam cylinder, no abrasive elements | Opening passes, establishing flow, verification, foam-assist |
| Tungsten carbide | Urethane body with tungsten carbide pins embedded during molding | Primary coke removal, the main working pig |
| Harder durometer | Higher-hardness body, aggressive cleaning action | Heavy fouling, pitch-laden tubes |
| Swab | Oversized soft urethane | Final cleanup, verification, larger sections |

Pigs are consumed by the work. A pig returning heavily worn or damaged is itself information about the condition of the coil, and pig condition is observed and recorded on every pass.

<!-- GRAPHIC 5-3: the four pig types side by side at consistent scale, labeled. Then a second panel showing TC pin mechanics in tube section: pig at or under tube ID with pins extended digging into deposit, and oversized pig with urethane compressed and pins laid back cutting coke but deflecting off tube wall. That second panel explains why an oversized pig is safe, which is the most common customer question on this method. -->

## 5.4 Hoses and connections

| Segment | Connection | Size |
|---|---|---|
| Trimax to launcher and receiver | Fig. 200 jetting hose | 3" |
| Filtration circuit, all legs | Camlock | 3" |
| Dirty tank access for vacuum truck | Camlock | 3" |

The Fig. 200 hammer union used at the pumper ports and coil connections is a 2,000 PSI non-shock cold working pressure fitting, well above the operating band of the system.

## 5.5 Filtration equipment

Where filtration is elected, two additional pieces deploy. A trailer-mounted 4×3 centrifugal pump moves water from the dirty tank through the press, and a trailer-mounted filter press separates solids from the returning water so the filtrate can go back to the clean tank.

| Item | Specification |
|---|---|
| Filter press capacity | 400 GPM |
| Operating pressure | 100 PSI |
| Plates | 73 polypropylene, 1,000 mm |
| Filtration surface area | 1,243 ft² |
| Total cake volume | 60 ft³ |
| Cake thickness | 32 mm |
| Press envelope | 44'-3" L × 8'-7" W, trailer-mounted |
| 4×3 pump connections | 3" camlock inlet and outlet |

Additional filtration capacity is provided by deploying an additional press rather than by a larger unit. The filtration loop runs independently of the pigging circuit and does not influence coil pressure or pig travel. Section 12 covers its operation.

## 5.6 Jumper spools

A jumper spool is a 180 degree spool piece that joins two adjacent passes into one continuous cleaning circuit, connecting the corresponding flanges at the same end of both — outlets or inlets, per job. Spools are fabricated by the customer to the quantity, size, and flange rating identified during engineering.

## 5.7 Supporting equipment

Crew trucks and a support unit transport personnel, tooling, and supplies. Depending on site conditions and scope, third-party equipment may be arranged: vacuum trucks for removal of residual product from the dirty tank, light plants where work occurs in poorly lit areas or outside daylight, and air compressors where pig loading or pneumatic tooling requires them.

## 5.8 Field layout

Two standard layouts cover most jobs.

**Without filtration.** Supply water, commonly from a facility fire hydrant, feeds each Trimax clean tank through fire hose. The dirty tank discharges through 3 inch camlock to the coke pit drain or oily water sewer.

**With filtration.** Supply comes from a frac tank to the clean tanks. The dirty tank routes through the 4×3 pump and filter press and returns filtrate to the clean tank, closing the loop.

Left to right, the footprint is typically frac tank where used, then the Trimax unit or units, then the heater, with the drain terminus beyond.

---

Previous: [[04-project-inputs-and-engineering]] · Next: [[06-safety-and-permit-interface]]
