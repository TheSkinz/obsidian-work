# 2. What Mechanical Pigging Is

**Layer:** 04-knowledge/manual
**Source:** [[industry-foundation]], `~/.claude/skills/usadebusk-core/SKILL.md`
**Manual:** [[00-manual-index]]

---

## 2.1 How coke forms

Fired heater tubes carry process fluid through a zone of high heat flux. Under those conditions the fluid thermally cracks, and a carbon-rich byproduct deposits on the inside of the tube wall. That deposit is petroleum coke, and it accumulates over the course of a run.

Deposition is not uniform. The radiant section sees direct flame radiation and the highest heat flux, and the radiant outlet is the hottest point in the coil. That is where fouling is heaviest and hardest to remove. The convection section, heated indirectly by flue gas, runs at lower tube skin temperatures and generally fouls less severely.

Fouling character varies by service. Standard coke thermally consolidates into a hard deposit that resists removal. Pitch, common in coker and crude service, is a heavy viscous fouling variant that behaves differently and is harder to mobilize.

The deposit is layered rather than homogeneous, and that is why progressive pig sizing works rather than being merely cautious. The published work reports two layers — an outer porous layer over a harder crust against the tube wall (Atkins, 1962, as reported in Jegla, Kohoutek and Stehlík, *Design and Operating Aspects Influencing Fouling Inside Radiant Coils of Fired Heaters*, Heat Exchanger Fouling and Cleaning, 2011). Successive incomplete cleans compound this: material left behind insulates the wall at that point, the area runs hotter, and new deposit forms on top of the old, which hardens with each cycle. Quest Integrity's ADCV case study documents a vacuum furnace where the older layer had hardened past what a metal studded pig could remove, and where sustained overheating had deformed the tube enough that a pig could no longer conform to it.

**We see this ourselves, and that is the stronger evidence.** Where a pig fractures a large piece off the wall and it is recovered in the launcher, receiver or pigging spool, the layering is visible in the piece. Recovered fragments are the only direct look at deposit structure a pig run produces, and they are worth inspecting and photographing every time one comes back — Section 10 treats them as evidence rather than debris. What a fragment cannot tell us is what the deposit is made of; composition, morphology and formation mechanism are not established by looking at it.

## 2.2 What coke costs the operator

Coke on the tube wall is an insulating layer between the flame and the process fluid. Four consequences follow, and they compound.

Heat transfer efficiency falls, so the heater burns more fuel to deliver the same duty. Tube skin temperatures rise, because the fire has to work harder to push heat through the deposit, which consumes tube life and raises the risk of tube failure. Pressure drop across the coil increases as the effective bore shrinks, which loads the charge pumps and can limit unit throughput. Left far enough, the result is an unplanned shutdown on a tube failure or a throughput constraint that forces the unit down anyway.

Operators generally schedule decoking into a planned turnaround, using pressure drop trending and tube skin temperature data to decide when the coil needs cleaning. Emergency decoking, performed when the unit has already reached a constraint, is a different job with a different urgency, but the same method.

## 2.3 What a pig is and what it does

A pig is a cleaning device sized to the tube bore and propelled through the coil by water. It travels the full length of a circuit from the launching spool to the receiving one, removing deposit mechanically as it goes. On an unlooped pass those sit at opposite ends of the coil; on a looped circuit both sit at the same end.

USADebusk uses several pig types across a single job. Foam pigs are soft, carry no abrasive elements, and are used to open the path and establish flow. Tungsten carbide pigs are the primary cleaning tool: a urethane body with tungsten carbide pins embedded during molding. When the pig is at or under tube bore, the pins extend and dig into the deposit. When the pig is deliberately oversized, the urethane body compresses and the pins lay back, and the difference in hardness between coke and tube wall means the pins cut the deposit while deflecting off the steel behind it without damaging the tube. Harder-durometer pigs are used on heavy fouling and pitch-laden tubes, and oversized soft urethane swabs are used for final cleanup and verification.

Cleaning is progressive. The first pass opens a path; each subsequent pass runs a slightly larger pig until the coil takes a pig above tube bore with full wall contact. Section 9 covers the progression in detail.

## 2.4 Why water propulsion

The propelling medium is water, delivered at high volume and moderate pressure. High volume is the distinguishing characteristic of the system: the pig is driven by flow, not by pressure alone. Normal operating pressure sits in a moderate band well below the mechanical limits of the coil, which keeps the coil under conditions comparable to ordinary hydrostatic service rather than exposing it to the thermal cycling and stress that other decoking methods impose.

Water propulsion also produces something no thermal method produces: a physical record. Every pass returns a pig that can be inspected for wear, gouging and appendage loss, and returns effluent whose clarity and discharge duration are observable in real time. It also returns the deposit itself — fines and flakes in the effluent, and sometimes pieces large enough to hold and examine. Combined with the before and after flow tests described in Section 10, that gives an objective basis for declaring a coil clean rather than an inferred one.

What that record does and does not cover is worth stating plainly, because it sets the limit of what we can claim. It is evidence about behaviour: what size passed, where a pig stalled, how long the return ran dirty, what came back, and what the flow test moved. It is not evidence about material. Deposit composition, morphology and formation mechanism, and the metallurgical condition of the tube itself, are outside what a pig run establishes — they belong to the customer's inspection data or a laboratory result.

## 2.5 What mechanical cleaning enables

Once the tube wall is mechanically clean, it can be inspected. In-line inspection tools measure remaining wall thickness, and that measurement is only meaningful against a clean wall. A decoking scope is therefore often the enabling step for a wall thickness survey that informs tube replacement decisions in the same turnaround. Section 14 covers the support USADebusk provides for those runs.

---

Previous: [[01-scope-and-use]] · Next: [[03-heater-and-coil-fundamentals]]
