---
type: review
status: resolved
review_type: decision-packet
source_authority: researched
confidence: high
created: 2026-09-03
related:
  - "[[idea-job-report-summary-quality]]"
  - "[[17-glossary]]"
  - "[[industry-foundation]]"
  - "[[_canonical-heater-card]]"
  - "[[2026-08-20-syncrude-geometry-per-pass-misread]]"
tags: [review, terminology, job-report, fouling, decision-packet]
---

# Decision packet — fouling and coke terminology

## What this is

A term-by-term list for Jesse to rule on. Nothing here has been implemented anywhere. Phase B — glossary rewrite, report wording standard, enum criteria, skill updates, lint rule — starts only after the rulings below are filled in.

**How to use it:** every table has a `Ruling` column. Fill in keep / drop / reword, or write the term you want instead. Two structural decisions come first because they change which terms even make sense.

**Jesse's stated constraints (2026-09-03):** engineer-grade precision, but it has to sound human; tier terms by what we can actually observe; and no term goes in that the techs would not understand.

## RULED AND APPLIED — 2026-09-03

All six decisions settled in session and implemented the same day. Two overturned the proposal rather than confirming it, and those are the ones worth reading.

**The reframe that governs everything else.** Jesse: *"The pigging tech's have no way of proving / analyzing certain assumptions. We have theories, but most can't be proven."* This generalises past the one term it was asked about — **our evidence is hydraulic and mechanical, not material.** A pig run establishes what the coil did and what the tools did; it never establishes what the deposit *is*. Composition, morphology and formation mechanism are one class of unprovable, not three separate cases, and the packet below was wrong to carry `scale` / `inorganic deposit` in Tier 1 as though we could observe it.

**The three-register split is withdrawn.** Jesse: one vocabulary, the customer already knows the terms, techs can learn them, and the report problems were *"more about verbosity and related concerns."* He is right and Decision 1 below was aimed at the wrong axis. Four of his five CAD26001 corrections are about **how much was said**, not which words were used; the fifth is an invented coinage. The estimating-versus-report tension is real but concerns **detail selection** — estimating needs more facts, not different words. What replaced it:

- **One vocabulary, vault-wide.** A term we would not say in front of the reader who knows it best does not belong in the glossary either.
- **The evidence tiers stay** and do the real work, because they constrain *truth* rather than audience and so apply identically in a shift log, a heater card and a report.
- **Expectation language vs. finding language** — the distinction that does what the register split was reaching for, without splitting by audience. `standard coke` · `hard coke` · `pitch` are predictions from service and history and stay load-bearing in estimating; `Clean ID` · `bore restriction` · `residual fouling` · `return duration` · `recovered fragments` · `pig condition` are observations. An estimate may say we expect hard coke; a report may not say we found it.
- **A report scope rule** written against the five CAD26001 corrections, which is the actual fix for the summaries and is separable from terminology entirely.
- **Carve-out:** raw shift logs preserve the crew's own words — a record of what someone said, not a written document.

**The most valuable thing to come out of the session was Jesse's, not the research.** *"Sometimes large pieces are fractured off the tube wall and collected in the launcher / receiver when the pig enters the receiving end / pigging spool of the circuit. We can visually inspect the larger pieces and see layers of fouling and / or other details."* That moves layered fouling from cited theory into our own evidence — the one place our returns corroborate the published literature (Jegla citing Atkins 1962; Quest's layered-coke case study) rather than borrowing from it. Nothing in `/log` or `/report` asked for it, so it was being seen and discarded. Now captured.

**Applied in:** `04-knowledge/manual/17-glossary.md` (the authority) · `04-knowledge/concepts/industry-foundation.md` (duplicate glossary resolved, `soft coke` retired) · manual `02`, `03`, `09`, `10` · `_canonical-heater-card.md` + `templates/_heater-template.md` (coil-condition criteria) · skills `usadebusk-core`, `-sop`, `-estimating`, `-fieldpm`, `-vault-ingest` · `tools/vault_lint.py` new `DEAD-STRING` rule + fixture.

## Why it exists

`[[idea-job-report-summary-quality]]` records the CAD26001 revision rounds — *"I'm still not fully happy with any of the job report summaries we do."* Three of its five failure modes are wording problems: invented jargon, SOP-narration instead of findings, and operator-level detail in front of metallurgists.

Underneath that is a genuine gap. The vault's entire formal fouling vocabulary is four terms in `[[17-glossary]]` — Coke, Hard coke, Pitch, Decoking. A second glossary in `[[industry-foundation]]` adds "soft coke" and never defines it. Nothing separates organic coke from inorganic scale, nothing says what `light | moderate | heavy` mean, and nothing assigns a term to an audience. The scatter across five facility cards shows the cost: "very dirty", "15 sec of black", "nominal", "coke ring", "~1/8 inch thick", "90% clean", "Pass 3 >> Pass 4 > Pass 1 ~= Pass 2" — all describing the same class of observation.

## Sources

Read directly, not paraphrased from search results:

- **Quest Integrity, ADCV white paper** v1.0 2020-12-07 — read in full
- **Quest Integrity, Mechanical Decoking of Furnaces the Right Way**, ADCV case study v2.0 2023-05-05 — read in full
- **Jegla, Kohoutek & Stehlik**, *Design and Operating Aspects Influencing Fouling Inside Radiant Coils of Fired Heaters Operated in Crude Oil Distillation Plants*, Heat Exchanger Fouling & Cleaning conference 2011, peer-reviewed — first 6 pages read
- **AFPM Q&A 74** — refiners' own words on spalling vs. pigging vs. steam-air
- **Quest Integrity / Tom Gilmartin**, *Heater Tube Cleaning and Verification*, Hydrocarbon Engineering
- DigitalRefining furnace-coil cleaning article; BIC Magazine on smart-pig heater inspection; API 530 and API RP 573 referenced but paywalled

Provenance note: everything marked **read** comes from a document opened in full. Items marked **search-summary** come from search result text, not the source document — API 530 and API RP 573 are the two that matter and neither was obtainable. RP 573 (5th ed., April 2026) is the actual standard governing fired heater inspection reporting and would be the most defensible anchor we could cite; worth buying if this vocabulary is going to face a customer's inspection group.

---

# Decision 1 — the three-register split

The estimating skill and the report-summary complaint pull in opposite directions, and nobody has written this down.

`usadebusk-estimating/SKILL.md:36` wants a *finer* fouling vocabulary because it drives the ft/hr derate — "harder fouling (coker / crude / vacuum), pitch presence, tube restrictions" — and line 295's RFQ intake asks for "standard coke, hard coke, pitch/resid". Meanwhile the CAD26001 rounds show granularity being cut *out* of the customer summary: "pigged until the return water ran clear" became "pigged until clean."

Both are right. They are different audiences drawing from one undifferentiated word pool.

| Register | Reader | Proposed rule |
|---|---|---|
| Field capture — `/log`, `/report` prompts, Field Notes | Techs and PM | Plainest of the three. Crew's own words preserved (`usadebusk-fieldpm/SKILL.md:244` already requires this). One structured field added, nothing taken away. |
| Internal knowledge — heater cards, manual, estimating | Us | Full precision. Organic vs. inorganic, thickness, mechanism all live here. |
| Customer-facing — job report, proposal | Reliability and process engineers, metallurgists | Precise but plain. Engineer-grade nouns, not engineer-grade jargon. Every claim traceable to something we measured or the customer supplied. |

This is the direct answer to the tech-comprehension concern: **the field register is deliberately the plainest of the three**, and mostly ratifies words the crew already says.

**Ruling: WITHDRAWN.** One vocabulary vault-wide instead. The customer already knows the terms and the techs can learn them; the report problems were verbosity, not vocabulary. Replaced by the evidence tiers plus the expectation/finding split plus a separate report scope rule — see the RULED block at the top. Shift logs keep the preserve-crew-words carve-out.

---

# Decision 2 — how much of Quest's vocabulary to adopt

Quest is the reference standard here, so their published wording was read directly rather than characterised. Four findings.

**Their master term is "internal fouling," not "coke."** Across both documents "fouling" carries the load. The case study writes internal fouling "coke" — coke in scare quotes, as the informal gloss. They pair the verbs consistently: "mechanical decoking or descaling," "decoke and descale."

**They publish a structured schema for one fouling indication.** The single most adoptable thing in the research pass — Table 1 of the case study:

| Fouling Details | Piping Information |
|---|---|
| Internal / External · Location (distance from end of previous fitting) · Axial Length · Circumferential Width · Fouling Thickness · Avg. Fouling Thickness | Material · Nominal OD · Nominal ID · Nominal Wall Thickness |

Reported values on that job: `3.4 mm` peak thickness against `0.6 mm` average, `0.60 m` axial length, `0.10 m` circumferential width, on `A335-P5`.

**"Over-cleaning" is a named failure mode with an observable signature, and we have no word for it.** Quest reports "horizontal grooving patterns on the inside tube walls" and "damage (wall loss) to the tube walls" left by a prior cleaning vendor. We already record the neighbouring facts — pig appendage wear across sections on F-501, restrictions that "gouged the pigs" on USA26041 — with nothing connecting them.

**Their layered-coke account corroborates yours.** From the case study: leftover coke "acted as an accelerate for the rapid formation of new coke"; coke "acts as an insulator"; the older layer became "so hard over time that even a metal studded decoking pig could not remove it"; and "prolonged overheating from the internal fouling deformed the tube, making it difficult for the cleaning pig to conform to the shape of the tube." That is the same phenomenon recorded in `usadebusk-estimating/SKILL.md:102-106` — first-ever-pigged heaters at facilities with long steam-air histories yielding layered fouling. Independent corroboration from the leading inspection vendor, alongside the peer-reviewed two-layer deposit structure (Jegla, citing Atkins 1962: an outer porous layer and a hard crust against the tube wall).

## The catch

Quest's vocabulary arrives welded to an argument against our method.

> The cleaning process continues until fouling is no longer removed from the coil, as evident by the color of the water and lack of particulates at the coil output. As further evidence that a coil is clean, some companies may also run an oversized light-colored foam pig... A decrease in pressure and increase in flow after the final cleaning runs indicates a reduction in fouling, although whether the coil is completely clean is unknown.

Those three are precisely our completion criteria (`usadebusk-sop/SKILL.md:97-101`). They also attribute tube grooving and wall loss to "oversized cleaning pigs, extra hard cleaning appendages and excessive cleaning pig runs" — an accurate description of TC and HR progression.

Counterweight: on many jobs Quest is not the competition but the smart-pig vendor on the same heater. USA26038's own summary cites a Quest smart pig confirming minimal residual coke, and CAD26001 lists "Smart Pigging: Yes - Quest Integrity, all 8 coils." Shared nouns make the two reports reconcile instead of talk past each other.

| Option | What it means |
|---|---|
| **A — Adopt descriptive vocabulary, reject the verification framing** | Take *internal fouling*, the indication schema, *residual fouling*, *over-cleaning*. Keep our completion criteria stated in measured terms. Speaks the customer's language without conceding the argument. |
| **B — Adopt, and answer the argument head-on** | As A, plus make the three-criteria logic explicit in the report. Our own manual already concedes more than Quest does — `10-verification-and-completion.md:50`: "each criterion alone can be satisfied by a coil that is not clean." Stating why the three together are sufficient is a stronger position than avoiding the topic. |
| **C — Stay clear of their terms** | Use plainer equivalents wherever a term carries their framing. |

**Ruling: B.** Adopt the descriptive nouns and answer the verification argument rather than avoiding it. Applied at `usadebusk-sop/SKILL.md` § Cleaning Completion Criteria and `04-knowledge/manual/10-verification-and-completion.md` § 10.3 — the criteria are sufficient together, none is sufficient alone, and where a document states a result it states that joint basis plus the Clean ID reached.

---

# Decision 3 — Tier 1 terms: what a pig run actually evidences

Defensible in a customer report because we watched it happen. Most are already in field use; the change is defining them, not introducing them.

| # | Term | Means | Status today | Techs know it? | Ruling |
|---|---|---|---|---|---|
| 1.1 | **Coke** | Carbon-rich *organic* deposit from thermal cracking of the process fluid | Defined; proposal is to scope it to organic only | Yes | |
| 1.2 | **Scale** / **inorganic deposit** | Non-combustible deposit — iron oxide, iron sulfide, salts, silica | New. Today everything is called coke | Introduce carefully | |
| 1.3 | **Foulant** / **deposit** | Neutral cover term when we have not established which | New. Biggest single precision win; Quest's master term | Likely new | |
| 1.4 | **Internal fouling** | Quest's master term for the whole phenomenon | New as a formal term | Adjacent — "fouling" already used | |
| 1.5 | **Bore restriction** / **reduced bore** | Deposit narrowing the flow path, stated with the size that would not pass | Replaces "restricted", "severely restricted" | "Restriction" yes | |
| 1.6 | **Clean ID** | Largest pig OD that passed the full circuit unobstructed | Exists at `usadebusk-ops/SKILL.md:17`. Our best hard number — proposal is to promote it into the report | Yes | |
| 1.7 | **Deposit thickness** | Measured, stated with the measurement | Already used on 7-1-F-1 (`~1/8"`) and H-102B (`0.25"`) | Yes | |
| 1.8 | **Localized** vs. **general / uniform** | Whether fouling concentrated or ran the length | Replaces "throughout", "the majority of" | Plain enough | |
| 1.9 | **Circumferential ring** | A band of deposit at one axial location | Already on H-102B: "0.25 inch thick circumferential coke ring" | Yes | |
| 1.10 | **Residual deposit** / **residual fouling** | What remains after cleaning. AFPM and Quest both use it | Replaces "minimal residual coke" — keep, define | Yes | |
| 1.11 | **Return clarity / return duration** | Seconds of discoloured return per pass | Formalises "15 sec of black" without discarding it | Yes — this IS their term | |
| 1.12 | **Obstruction / lodgment / hang-up** | Pig stopped or slowed, with location | Already field vocabulary | Yes | |
| 1.13 | **Pitch** | Heavy viscous fouling variant, coker and crude service | USADebusk-specific and real — retain | Yes | |
| 1.14 | **Hard coke** | Thermally consolidated coke requiring progressive sizing | Retain current definition | Yes | |
| 1.15 | **Layered fouling** | Distinct deposit layers from successive incomplete cleans; older layer hardens | Your own observation; now has vendor and literature backing | Yes | |
| 1.16 | **Over-cleaning** | Excess runs or oversizing causing tube wall loss, seen as grooving | New. Quest's term, and a live risk in our own method | New but immediately legible | |

## The indication schema — which fields can we actually fill?

Honest question attached to Quest's Table 1. A pig run is not a UT tool, so some of these we can populate and some we cannot.

| Field | Can a pig run populate it? |
|---|---|
| Internal / external | Yes — always internal for us |
| Location | Partly. USA26041 located and mapped restrictions from digital chart recorders, explicitly "not visually identified" |
| Axial length | Rarely. A chart-recorder trace gives an extent, not a measurement |
| Circumferential width | No — needs UT or a cut-out |
| Peak thickness | Only where measured directly (7-1-F-1's 1/8 inch and H-102B's 0.25 inch both came from a smart pig, not from us) |
| Average thickness | No |
| Nominal OD / ID / wall / material | Yes — from the heater card |

**Ruling: carry only what we populate.** Location, nominal geometry from the card, and thickness *where it was actually measured* — a smart pig, a cut-out, or a recovered fragment thick enough to measure. Axial length, circumferential width and average thickness are not ours and are not estimated to fill the shape of Quest's table.

---

# Decision 4 — Tier 2: customer-supplied evidence

Legitimate to cite *when the customer gave us the number*, never to assert otherwise. Useful in a report's framing paragraph and in estimating intake.

`TMT` / tube metal temperature · `COT` / coil outlet temperature · pass pressure drop (pass dP) · run length, start-of-run / end-of-run · feed CCR, asphaltene content, sodium and metals.

Grounding (search-summary, not read): API 530's tube-metal-temperature relation is the standard basis for inferring deposit thickness from TMT rise, and recovery toward the clean-tube baseline is the recognised objective measure of decoke effectiveness. We reference both; we generate neither.

**Ruling: approved as written.** Citable when the customer gave us the number, attributed to them, never asserted otherwise.

---

# Decision 5 — Tier 3: do not assert

A pig run cannot evidence any of these. Proposal is that they stay in the manual as background and are banned from job reports.

| Category | Terms | Why banned |
|---|---|---|
| Formation mechanism | pyrolytic · catalytic / filamentous · condensation coking · asphaltene laydown | We cannot see how it formed |
| Deposit morphology | amorphous · graphitic · filamentous | Needs lab characterisation |
| Metallurgical condition | carburization · creep · bulging · ovality | Smart-pig and NDT territory. Asserting it picks a fight with the customer's own inspection data |

**Ruling: approved, and widened.** Deposit **composition** joins this tier — the `coke` vs. `scale` split proposed in Tier 1 is not observable from a pig run either, and treating it as though it were was the packet's own error. All four categories are one class: not assertable from our work, sourced to the customer's inspection data or a lab result, or not stated.

---

# Decision 6 — terms proposed for retirement

| Term | Problem | Proposal | Ruling |
|---|---|---|---|
| "dirty", "very dirty", "extremely dirty" | Colloquial. Fine on a shift log, wrong in front of a metallurgist | Field register only; never in a report | **Accepted**, restated as the raw-capture carve-out rather than a register: shift logs are a record of what someone said and are exempt; anything written as a document is not |
| **"soft coke"** | Lives in exactly one vault file (`industry-foundation.md:40`) and is never defined. In refining, soft/hard coke is a coke-drum VCM term meaning something else entirely — a false friend | Retire, or define explicitly as ours | **Retired.** Migrated to zero and armed as a `DEAD-STRING` lint error, on the `HEATER-TYPE-VOCAB` precedent — zero backlog, so a hit can only mean reintroduction |
| "90% clean" (USA25025) | A number with nothing behind it | Ban unquantified percentages; use Clean ID | **Accepted.** Clean ID promoted into the completion criteria and named as the hardest number the job produces |
| "nominal coking" | Fine but vague | Keep, paired with the defensible form: "consistent with historical run length" | **Accepted**, kept as written on CAD26001 |

---

# Worked examples

The register split is only arguable against real prose. All three are verbatim from delivered reports.

## A. CAD26001 — 7-1 F-1 (Syncrude; readers were metallurgists and engineers)

**Delivered** (`report_input_cad26001.py:125`):

> All eight coils exhibited nominal coking, consistent with historical run times. The heaviest deposits, approximately 1/8 inch thick, were located in the last few radiant tubes of each pass. Post-decoke inspection found a few spots of light fouling in the last three radiant tubes at the outlet in select coils.

**Assessment:** this one is already close to right. "Nominal coking, consistent with historical run times" is defensible — the claim is anchored to run history, not to a grade. Peak thickness is stated with its measurement. The residual is located.

**Proposed:** change little. Optionally "a few spots of light fouling" becomes "localized residual fouling", which names the concentration rather than gesturing at it.

**Ruling: accepted.** This one was already close to right — the claim is anchored to run history rather than to a grade, and the thickness is stated with its measurement.

## B. USA26041 — F-501 (ExxonMobil Baytown)

**Delivered** (`report_input_usa26041.py:143`):

> Light fouling throughout. The radiant tubes had the majority of soft deposits throughout each pass, though only had light / soft coke, and no pass or coil was notably dirtier than the rest.

**Assessment:** carries three of the problems at once. "Throughout" appears twice in one sentence meaning different things. "Soft deposits" and "light / soft coke" are the undefined false-friend term. "Dirtier" is field register in a customer document.

**Proposed:**

> Light, uniform fouling. Deposits ran the full length of each radiant pass with no pass or coil measurably heavier than the rest.

Same facts, and it drops a term we cannot define.

**Ruling: accepted.** The clearest case for the whole exercise — one sentence carried the doubled "throughout", the retired `soft coke`, and "dirtier" as a comparative with nothing behind it.

## C. USA26038 — H-20 (HF-Sinclair Artesia)

**Delivered** (`report_input_usa26038.py:113`, result and callout):

> Fouling severity ran Pass 3 >> Pass 4 > Pass 1 ~= Pass 2.
>
> Pass 3's radiant section was severely restricted with three separate heavy restrictions. Trimax 3 forced it open using its own pumps; 2 inch pigs run to establish flow returned badly damaged...

**Assessment:** the ranking chain is compact and genuinely informative, but the math notation is unusual in a report. "Severely restricted with three separate heavy restrictions" repeats itself. The strongest evidence in the whole passage — 2 inch pigs returning badly damaged in a 3.068 inch radiant — is buried as colour when it is the hardest number available.

**Proposed:**

> Fouling was heaviest in Pass 3, then Pass 4; Passes 1 and 2 were comparable and lighter.
>
> Pass 3's radiant carried three separate bore restrictions. Trimax 3 forced it open using its own pumps; 2 inch pigs run to establish flow returned badly damaged against a 3.068 inch radiant ID.

**Ruling: accepted.** Promoting the damaged-pig detail out of the callout is the substantive change — pig condition on return is Tier 1 evidence and was being written as colour.

---

# Open questions — all answered

1. **Does "foulant" survive contact with the crew?** **Answered by falling back.** `fouling` and `deposit` are the default nouns; `foulant` is not adopted as a required term. Plainer, and it was the term most likely to sound imported.
2. **Do we introduce "scale" at all?** **No.** This was the question that produced the whole reframe — claiming a deposit is inorganic without a lab result is an unbacked assertion, and so is calling it coke. Composition moved to the not-assertable tier entirely.
3. **Where does the two-layer deposit structure go?** **`04-knowledge/manual/02-what-mechanical-pigging-is.md` § 2.1, and it is stronger than proposed.** It went in citing Jegla/Atkins and Quest, *and* our own recovered fragments — which are the better evidence, because they are ours.
4. **Is `light | moderate | heavy` worth criteria?** **Yes.** Criteria added to `_canonical-heater-card.md` and mirrored to the template and `usadebusk-vault-ingest`, ordered so the two measurements (Clean ID against tube ID, progression steps) outrank the corroborating observations. The bands are calibration, deliberately not a formula. `unknown` over an inferred grade, same rule as job class.
5. **Do we buy API RP 573?** **No** (Jesse, 2026-09-03): *"There's enough info on the internet about the subject."* The vocabulary is grounded in Quest's published wording, the peer-reviewed Jegla paper, and our own observations. RP 573 would add citable authority, not new terms. Revisit only if a customer challenges our condition language.

# After the rulings

All of Phase B was applied the same session — glossary and duplicate resolution, report scope rule, capture prompts, enum criteria, skill mirrors, and the `DEAD-STRING` lint rule with its fixture. Verified: lint self-test 20/20 rules fire, vault lint 0 errors, `assert_structure.py` self-test passes, and the renderer and back-test configs show an empty diff, so no re-render was owed.

## Round 2 — same day, three more rulings

Jesse added two field observations after the first round shipped, prefaced *"I don't know if this is worth taking into consideration."* Both were, and answering the follow-up questions produced a third item larger than either.

**1. The hardness rule from round 1 was too broad.** Jesse: *"There are hard deposits and soft brittle deposits we remove from heater coils… Both types can be fractured from the tube wall and collected in the pigging spools for visual analysis. Sometimes the coke is hard coke fractured from the tube wall, sometimes it's a 'powdery' form of coke."* Round 1 wrote *"difficulty is recorded as effort, never as a claim about the material"* and *"`heavy` does not say the deposit was hard"* — which collapsed three separate things. Corrected to: describing a fragment somebody **handled** is an observation and is allowed; inferring deposit hardness **from cleaning slowness** is not a finding, because slow progress also follows from bore restriction, pig fit, flow or tube deformation; composition and mechanism stay Tier 3. **Describe from the piece, never from the clock.** Ruled vocabulary, three axes: form `hard | brittle | powdery`, size `chunks | chips | fines`, condition `wet | oily | tarry`. `flakes / plates / sheets` was proposed and rejected — not a distinction the crew makes. Jesse on why the types differ: *"I can't give an informed opinion for why and the different circumstances for the different types of fouling we see and the reason for it."* That is the rule, not an apology — record the form, do not explain it.

**2. Localized hard spot — a phenomenon the vault did not mention anywhere.** Jesse: *"Sometimes at the end of the decoking project, we'll run several pigs in a certain area and make very slow progress… A significant portion of the pigging can be attributed to cleaning this one section."* A grep for last-layer / slow-progress / terminal-phase language across `04-knowledge/`, `02-facilities/` and every skill returned **zero hits** before this. Named `localized hard spot`; location captured as free text because it varies. **It does not occur on every heater**, so its absence is never recorded. Explicitly *not* the `outlier` Flag: an outlier coil is a fluke or corrupt data, a hard spot within a coil is normal. Recorded against the ~100 ft/hr benchmark as an **open question, not a derate** — the benchmark is a footage rate and a hard spot is not footage-driven, so if it is real at that scale, some of the ft/hr spread now read as service severity is structural instead. One observation, so it stays a hypothesis; capture first, revisit when several jobs carry data. Researching *why* fouling concentrates where it does was ruled out of scope: *"the heater tubes have to be cleaned regardless of the location of the fouling and the reason for it"* — which is also the cleanest statement of why the Tier 3 ban costs nothing.

**3. Negative-scope reporting — a standing complaint, and the largest of the three.** Jesse: *"You have a habit of adding specific details about things that aren't related to the specific project… Sometimes you'll add 'No Filtration' to project reports or job sheets that don't require Filtration and weren't sold or mobilized to the project."* Verified rather than taken on faith — `CAD26001-job-sheet.html:183`, `CAD26001-job-sheet.md:98` and `CAD26001-flow-tests.md:52` all carry it. Added as a **sixth report scope rule**, and it is the most general of the six: *do not document the absence of something that was never in scope*. Its corollary governs everything in round 2 — **an observation nobody made is absent from the document, never reported as absent.** Mirrored into `usadebusk-estimating`'s proposal guardrails, since the same habit would land on a bid. It does not touch stated requirements like the 2" firewater hose, which are line items we do tell the customer; the test is whether the thing is in scope, not whether it is interesting.

**Deliberately not done:** retro-editing the CAD26001 artifacts. The job sheet was delivered and the job is closed, editing the HTML would trip `JOBSHEET-PDF-STALE` against a PDF nothing regenerates (`render_job_sheet.py` deferred 2026-07-18), and the standing rule is to fix the canonical source rather than chase sent documents. `7-1-F-1.md:138`'s `Filtration | Not used — settled` also stays: it is the internal record of a settled decision and what stops filtration being estimated into the next Syncrude bid, not a deliverable. Flagged to Jesse as his call.

**Still open, and deliberately not closed here:** `[[idea-job-report-summary-quality]]`'s other half — the three-move summary structure (scope executed → condition found → what it means next). That is arguably the bigger lever on verbosity than the scope rule is, and it needs the standing back-test against two structurally different delivered reports before it governs anything. The seed stays open for it. Migration precedent and cost model is `[[2026-08-20-syncrude-geometry-per-pass-misread]]`, which re-labeled `crash` vault-wide and lists the six files it touched.
