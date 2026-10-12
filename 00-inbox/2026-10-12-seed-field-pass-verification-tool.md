---
type: idea-seed
status: unexplored
created: 2026-10-12
tags: [idea, field-ops, future]
---

# Field tool to verify which inlet flange feeds which outlet flange

Idea seed captured 2026-10-12 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** On Valero Port Arthur B-301 (DSP26115) the rebuilt heater carried no pass tags and its crossovers are internal, so pairing the four convection inlets with the four radiant outlets took an hour of drawing reading, a hand sketch, and phone-compass readings on each flange. Even then the result was only "likely": a 4-pass vertical cylindrical heater's outlet pattern looks the same rotated 180°, so compass headings fix the geometry but can't choose between the two pass maps. Only a fill test settled it. A repeatable on-site method or tool would turn this into minutes on any heater that comes without tags.

**Framing (Jesse, 2026-10-12):** the goal is to know the inlet↔outlet pairing **before** any flow goes in, not to find out through an incident. Nothing heater-specific will exist, so the method is general tools — drawings, his body position and flange-face bearings, phone compass, GPS, Google Maps satellite imagery, and other apps — combined to infer the map.

**Key finding from B-301:** geometry alone can't break a heater's rotational symmetry, and neither can grid-aligned features such as pipe racks (they're symmetric too). The chain needs one *directional* reference that ties the drawing to the world: the drawing's orientation note ("0° axis = west"), plus **which way plant north points**, taken from the plot plan's north arrow or from a Valero operator pointing to it. Then flange compass bearings → drawing angles → pass map. On B-301 the main map predicts plant north ≈ 306° true and the alternate ≈ 126°, so one question to an operator separates them.

**To explore:**
- **Method ranking:** fill or air test per inlet (definitive), skin-temperature or thermal-camera survey during a warm fill, acoustic tapping, plant-north offset from the GA's axis note, and P&ID thermocouple tables (B-301's Detail "A" tied pass to coil letter).
- **Where it would live:** a step in the fieldpm `/setup` checklist, a section in the SOP template, or a small browser tool beside `apps/pig-tracker/` that takes flange headings plus the plan-view angles and draws the candidate maps.
- **Prior art:** a quick search on 2026-10-12 found nothing built for this. Inspection checklists cover tube ID against a sketch, and Tracerco-type tracer methods are for leak detection. A deeper power-user and forum search is still owed.
- **Frequency:** how often a heater actually arrives untagged — revamps, crash jobs, first cleans.

Source case: [[B-301]], `02-facilities/Valero/Port-Arthur-TX/files/B-301-pass-map.png`.
