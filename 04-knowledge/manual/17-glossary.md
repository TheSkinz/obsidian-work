# 17. Glossary

**Layer:** 04-knowledge/manual
**Source:** `~/.claude/skills/usadebusk-core/SKILL.md` (Core Terminology), `04-knowledge/concepts/industry-foundation.md` (Terminology)
**Manual:** [[00-manual-index]]

---

Terms defined here are those the manual actually uses. Where local facility usage differs, these are the meanings intended in this document and in USADebusk job SOPs.

## Heater and coil

| Term | Definition |
|---|---|
| Fired heater / Furnace | Process vessel containing the tube coil. Used interchangeably. |
| Coil | The complete tube assembly for one heater — individual tubes joined in series by return bends. |
| Pass / Circuit | One continuous tube path through the heater. A heater may have several. Each is cleaned as its own circuit. |
| Tube | An individual straight pipe section within a coil. |
| Return bend | A cast 180 degree fitting joining adjacent tubes. |
| Plug header | A box header with removable plugs at the tube ends. An older design; tube-to-tube traversal is less direct than through a cast return bend. |
| Convection section | The upper coil section, heated indirectly by flue gas. Lower tube skin temperatures. |
| Radiant section | The lower or inner section, exposed to direct flame radiation. Highest heat flux and where fouling is heaviest. |
| Cross-over | External piping connecting the convection outlet to the radiant inlet. Contains the size reducer where section bores differ. |
| Tube ID | Tube inner diameter. The dimension pig sizing keys off. |
| Governing tube ID | The smallest inner diameter present anywhere in a circuit. Sets the maximum pig OD for that entire circuit. |
| Serpentine | Horizontal parallel tube rows with return bends alternating ends, so a pig reverses direction at each tube. |
| Helical | A coil wrapping the shell circumference, found in radiant sections of vertical cylindrical heaters. |

## Fouling

> **This section is the authority for fouling vocabulary, and it is deliberately mirrored.** Copies live in `04-knowledge/_canonical-heater-card.md` and `templates/_heater-template.md` (the coil-condition criteria), and in the `usadebusk-core` and `usadebusk-vault-ingest` skills — skills cannot simply point here, because a subagent may have to read them from disk without vault access. **Keeping them in step is the point: a change to the rules below edits this file and every mirror in the same commit.** Same contract as `DURATIONS_HEADER` in `tools/vault_lint.py`. The mirrors are unlocked by any tool, so the monthly skill-drift review is what actually catches a lapse — this file drifting from `04-knowledge/concepts/industry-foundation.md` for months is what made `soft coke` possible.

Our evidence is hydraulic and mechanical. A pig run establishes what the coil did and what the tools did — what size passed, where a pig stalled, how long the return ran discoloured, what came back, how many progression steps it took, and what the flow test moved. It does not establish what the deposit is made of. Composition, morphology and formation mechanism are not observable from a pig run and are never asserted from one; where they matter they come from the customer's inspection data or a laboratory result. `Fouling` and `deposit` are therefore the default nouns, and `coke` is used where composition was actually established rather than as a general synonym.

Two vocabularies do different jobs. **Expectation language** describes what we predict going in, from service type and unit history, and belongs in estimating and bid intake. **Finding language** describes what we observed coming out, and belongs in job reports, Field Notes and heater-card actuals. Neither does the other's work: an estimate may say we expect hard coke, and a report may not say we found it.

### The material

| Term | Definition |
|---|---|
| Fouling / Deposit | The default nouns. Any accumulation on the tube wall, composition unstated. |
| Internal fouling | The same accumulation named as a whole phenomenon. The general industry term. |
| Coke | Carbon-rich deposit formed on the tube wall by thermal cracking of the process fluid. Used where composition was established — a laboratory result, a cut-out, or the customer stating it. |
| Decoking | Removal of deposits from the tube interior. Retained as the name of the service regardless of the default-noun rule; it is what the work is called. |
| Descaling | The same operation named for non-carbon deposits. Paired with decoking in industry usage. |

### Expectation language — what we predict going in

| Term | Definition |
|---|---|
| Expected fouling type | The fouling anticipated from service type and unit history, before any pig is run. An estimating input, never a finding. |
| Standard coke | The baseline expectation on most heater service. |
| Hard coke | Coke expected to have thermally consolidated, requiring progressive pig sizing to remove. Drives the ft/hour derate. |
| Pitch | A heavy, viscous fouling variant expected in coker and crude service, harder to mobilize than standard coke. |
| Layered fouling | Deposit expected to carry distinct layers from successive incomplete cleans, the older layer harder. Anticipated where a heater has a long steam-air history or has never been pigged. |

### Finding language — what we observed coming out

| Term | Definition |
|---|---|
| Clean ID | The largest pig OD that passed the full circuit without obstruction. The primary evidence of the result. |
| Bore restriction | Deposit narrowing the flow path, stated with the pig size that would not pass. |
| Localized / General | Whether fouling concentrated at identifiable locations or ran the length of the pass. |
| Circumferential ring | A band of deposit at one axial location. |
| Residual fouling | Deposit remaining after cleaning. |
| Return clarity / Return duration | The colour of the return and the seconds it ran discoloured per pass. |
| Recovered fragments | Pieces fractured off the tube wall and collected in the launcher, receiver or pigging spool. Large pieces can be inspected directly, and layering visible in them is the one direct evidence of deposit structure a pig run produces. Described using the three axes below. |
| Pig condition on return | Wear, gouging, appendage loss. Evidence of what the pig met. |
| Progression steps | The sequence of pig sizes run to reach the Clean ID, and any size that stalled. Hours and steps are the record of how hard the coil was to clean; they are not evidence of what the deposit was, because slow progress also follows from bore restriction, pig fit, flow, or tube deformation. Describe a deposit from a fragment you handled, never from how long it took. |
| Localized hard spot | A confined section where the last of the wall fouling resists removal — several pigs run in one area for very little progress, at the end of the job. It can account for a significant share of total pig hours. **It does not occur on every heater** (Jesse, 2026-09-03), and its absence is not recorded. Location varies and is written as free text: pass, section, approximate tube position. |
| Over-cleaning | Tube wall loss caused by excess runs or oversizing, seen as grooving on the inside wall. A failure mode of the method, not a condition of the coil. |

### Describing recovered material

What comes back in the spool is described on three independent axes. All of it is observation — someone looked at the material, or handled it — and none of it is a claim about composition or about why the deposit formed that way. **Record the form; do not explain it.** Jesse, 2026-09-03: *"I can't give an informed opinion for why and the different circumstances for the different types of fouling we see and the reason for it."* The types are real and worth recording; the explanation is not ours to give, and a described-form record across enough jobs is what would eventually support one.

| Axis | Values | Notes |
|---|---|---|
| Form | `hard` · `brittle` · `powdery` | How the material behaves when handled. A piece that resists breaking, one that fractures readily, one that crumbles. |
| Size | `chunks` · `chips` · `fines` | Independent of form — a deposit can come back as hard fines or brittle chunks. |
| Condition | `wet` · `oily` · `tarry` | The return is not dry material on pitch and resid service. |
| Structure | `layered` | Visible strata in a piece large enough to inspect. See § 2.1. |

**`hard` appears on both sides of the expectation/finding line, and that is not a contradiction.** `hard coke` in the expectation table above is a *prediction* from service type and history, made before a pig is run — it drives the ft/hour derate. `hard` here is a *description of a piece somebody picked up*. The first is an input to an estimate; the second is an observation from a job. Say which one is meant, and never let the second be inferred from cleaning hours.

## Method and equipment

| Term | Definition |
|---|---|
| Pig | A cleaning device sized to the tube bore and propelled through the coil by water pressure. |
| Pigging | Driving pigs through the coil to clean the tubes. |
| Foam pig | A soft foam pig with no abrasive elements. Used for opening passes, flow establishment, verification, and foam assist. |
| TC pig | Tungsten carbide pig — a urethane body with tungsten carbide pins embedded during molding. The primary cleaning pig. |
| Swab | An oversized soft urethane pig used for final cleanup and verification. |
| Maximum pig OD | The largest pig permitted in a circuit: governing tube ID plus 0.250 inches. |
| Launcher | The vessel mounted on the coil inlet flange from which pigs are launched. |
| Receiver | The vessel mounted on the coil outlet flange in which pigs are recovered. Same form factor as a launcher, distinguished by function. |
| Jumper spool | A temporary 180 degree spool joining two passes into one continuous circuit, connecting the corresponding flanges at the same end of both passes. The end is a per-job election — radiant outlets or convection inlets — and the looped end carries no launcher or receiver. |
| Trimax | USADebusk's trailer-mounted pigging pumper. The standard unit is a Triple, carrying three independent pumping assemblies sharing one clean and one dirty tank. |
| Second Trimax | A second pumping unit deployed on the same job, each unit carrying its own tanks and assemblies. |
| Clean tank | The tank supplying water to the pump. Receives return water when effluent runs clear. |
| Dirty tank | The tank receiving return water when effluent runs cloudy. |
| Diverter | The operator-controlled valve directing return water to the clean or dirty tank. |
| Fig. 200 | The hammer union connection type used at the pumper ports and coil connections, 3 inch on this system. |
| Camlock | The quick-connect fitting used throughout the filtration circuit, 3 inch standard. |
| Jetting hose | Hose running between the pumper ports and the launcher or receiver. |
| Filter press | Plate-and-frame press separating solids from return water, allowing filtrate to be reused. |
| Filter cake | The separated solids discharged from the filter press. |

## Operations

| Term | Definition |
|---|---|
| Rig-in | Setup of all surface equipment prior to pigging, ending at the baseline flow test. |
| Rig-out | Removal of all surface equipment after cleaning is complete. |
| Rig-over | Movement of the equipment spread to another set of passes or another heater within the same job. |
| Effluent | Return water exiting the receiver. Its clarity and discharge duration indicate cleaning progress. |
| Flow test | A pump curve measurement taken before and after cleaning at matched flow rate. The pressure differential demonstrates the improvement. |
| Completion criteria | The three conditions that must all be met before a circuit is declared clean. See Section 10. |
| Hang-up | A pig that has stopped advancing while circuit flow remains fully established. Recovered by controlled reversal, bumping, or foam assist. |
| Kicksolve | A chemical additive used to mobilize hardened residual product and pitch. |
| Passivation | Restoration of the passive oxide layer on stainless steel following mechanical cleaning. Customer scope. |
| Smart pig / ILI tool | An in-line inspection tool carrying ultrasonic transducers to measure remaining tube wall thickness. Run after mechanical cleaning. |
| SIMOPS | Simultaneous operations — other work proceeding in or around the heater at the same time, addressed in the permit and the JSA. |
| PTW | Permit to work, issued by the facility. |
| JSA | Job safety analysis, completed and reviewed with the crew before work begins and at each shift change. |

---

Previous: [[16-documentation-and-deliverables]] · Next: [[18-reference-tables]]
