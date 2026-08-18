# 14. Smart Pig and In-Line Inspection Support

**Layer:** 04-knowledge/manual
**Source:** `~/.claude/skills/usadebusk-sop/SKILL.md` (Smart Pig / ILI), [[process-flow]]
**Manual:** [[00-manual-index]]

---

## 14.1 What this scope is

A smart pig, or in-line inspection tool, carries ultrasonic transducers that measure remaining tube wall thickness as it travels the coil. The measurement informs tube replacement decisions, and it is one of the few ways to obtain wall data across a full coil without pulling tubes.

The tool has to be moved through the coil, and water propulsion is how that is done. On these jobs USADebusk provides the propulsion and the inspection vendor provides and controls the tool.

## 14.2 Role boundary

This boundary is stated plainly because it is the item most often assumed rather than agreed on inspection-supported jobs.

**USADebusk provides** the pumping unit, the circuit, the launcher and receiver, the connections, and controlled water propulsion at the flow rate the vendor specifies. USADebusk operates the pump to the vendor's stated envelope.

**The inspection vendor provides and controls** the tool itself, its configuration, its launch and recovery handling, the data acquisition, and the interpretation and reporting of the data. The vendor specifies the flow envelope required for valid data.

**USADebusk does not** configure the tool, operate it, acquire data, interpret data, or make any representation about wall thickness results. Nothing in the USADebusk scope constitutes inspection.

## 14.3 Prerequisite: a mechanically clean coil

The inspection run follows mechanical decoking and does not precede it. Ultrasonic wall measurement requires acoustic coupling to the tube wall, and a coke deposit between the transducer and the steel degrades or invalidates the reading.

Mechanical cleaning is therefore confirmed complete against the criteria in Section 10 before the tool is introduced. Running a tool through a coil that has not met those criteria risks producing a dataset the vendor cannot certify, which puts the whole scope back.

## 14.4 Propulsion parameters

An inspection run is a different operation from a cleaning pass. Cleaning drives a pig at working flow; inspection requires a slow, constant, controlled speed, because data quality depends on a steady traverse.

| Parameter | Specification |
|---|---|
| Target tool velocity | 1.0–2.0 ft/s |
| Approximate flow for a 4" bore at that velocity | 40–70 GPM |
| Speed control | Constant velocity throughout the run |
| Governing authority | The inspection vendor's written flow envelope |

> **CAUTION.** The pump is not set independently of the vendor's specification. The vendor states the required flow envelope in writing before each tool run, and USADebusk operates to that figure. Velocity above the vendor's envelope degrades data quality, and inconsistent velocity through a run can invalidate it.

The flow figures above are typical values for orientation during planning. The vendor's written envelope for the specific tool and coil governs the run.

## 14.5 Sequence

1. Mechanical decoking is confirmed complete on the circuit to be inspected.
2. The vendor's flow envelope is received in writing.
3. The vendor prepares and launches the tool; USADebusk configures the circuit and establishes flow at the specified rate.
4. The tool traverses the coil at controlled velocity, with USADebusk holding flow constant.
5. The vendor recovers the tool and downloads the data.
6. The vendor confirms whether the run produced a valid dataset. Where it did not, the run is repeated before the circuit is broken.

## 14.6 Approval gate before dewatering

> **WARNING.** On inspection-supported scopes, the customer's written acceptance of the inspection data is required before dewatering or circuit breaking begins. Rig-out follows dewatering and is not itself gated.

The acceptance is given against the vendor's preliminary digital report, not the final report, which arrives well after demobilization. That report answers two questions at once: whether the vendor captured the data it needs, and whether any fouling remains. **A non-acceptance does not end the job — pigging continues and the tool is run again until the customer has the data.**

The reason for the gate is practical. A re-run is straightforward while the circuit is intact and the equipment is in place. Once the coil has been dewatered and the launchers and receivers removed, a re-run requires a complete re-rig. The gate exists so that a data quality problem is discovered while it is still inexpensive to fix.

## 14.7 Common vendors

Inspection vendors encountered on this work include Quest Integrity, TEAM, Cokebusters, and SteadyFlux. USADebusk works to whichever vendor the customer engages, and to that vendor's stated requirements.

---

Previous: [[13-ancillary-initial-flush-and-pitch-removal]] · Next: [[15-ancillary-passivation-stainless]]
