---
type: review
status: for-review
review_type: decision-packet
source_authority: researched
confidence: medium
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

**Ruling:**

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

**Ruling:**

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

**Ruling on which fields the report should carry:**

---

# Decision 4 — Tier 2: customer-supplied evidence

Legitimate to cite *when the customer gave us the number*, never to assert otherwise. Useful in a report's framing paragraph and in estimating intake.

`TMT` / tube metal temperature · `COT` / coil outlet temperature · pass pressure drop (pass dP) · run length, start-of-run / end-of-run · feed CCR, asphaltene content, sodium and metals.

Grounding (search-summary, not read): API 530's tube-metal-temperature relation is the standard basis for inferring deposit thickness from TMT rise, and recovery toward the clean-tube baseline is the recognised objective measure of decoke effectiveness. We reference both; we generate neither.

**Ruling:**

---

# Decision 5 — Tier 3: do not assert

A pig run cannot evidence any of these. Proposal is that they stay in the manual as background and are banned from job reports.

| Category | Terms | Why banned |
|---|---|---|
| Formation mechanism | pyrolytic · catalytic / filamentous · condensation coking · asphaltene laydown | We cannot see how it formed |
| Deposit morphology | amorphous · graphitic · filamentous | Needs lab characterisation |
| Metallurgical condition | carburization · creep · bulging · ovality | Smart-pig and NDT territory. Asserting it picks a fight with the customer's own inspection data |

**Ruling:**

---

# Decision 6 — terms proposed for retirement

| Term | Problem | Proposal | Ruling |
|---|---|---|---|
| "dirty", "very dirty", "extremely dirty" | Colloquial. Fine on a shift log, wrong in front of a metallurgist | Field register only; never in a report | |
| **"soft coke"** | Lives in exactly one vault file (`industry-foundation.md:40`) and is never defined. In refining, soft/hard coke is a coke-drum VCM term meaning something else entirely — a false friend | Retire, or define explicitly as ours | |
| "90% clean" (USA25025) | A number with nothing behind it | Ban unquantified percentages; use Clean ID | |
| "nominal coking" | Fine but vague | Keep, paired with the defensible form: "consistent with historical run length" | |

---

# Worked examples

The register split is only arguable against real prose. All three are verbatim from delivered reports.

## A. CAD26001 — 7-1 F-1 (Syncrude; readers were metallurgists and engineers)

**Delivered** (`report_input_cad26001.py:125`):

> All eight coils exhibited nominal coking, consistent with historical run times. The heaviest deposits, approximately 1/8 inch thick, were located in the last few radiant tubes of each pass. Post-decoke inspection found a few spots of light fouling in the last three radiant tubes at the outlet in select coils.

**Assessment:** this one is already close to right. "Nominal coking, consistent with historical run times" is defensible — the claim is anchored to run history, not to a grade. Peak thickness is stated with its measurement. The residual is located.

**Proposed:** change little. Optionally "a few spots of light fouling" becomes "localized residual fouling", which names the concentration rather than gesturing at it.

**Ruling:**

## B. USA26041 — F-501 (ExxonMobil Baytown)

**Delivered** (`report_input_usa26041.py:143`):

> Light fouling throughout. The radiant tubes had the majority of soft deposits throughout each pass, though only had light / soft coke, and no pass or coil was notably dirtier than the rest.

**Assessment:** carries three of the problems at once. "Throughout" appears twice in one sentence meaning different things. "Soft deposits" and "light / soft coke" are the undefined false-friend term. "Dirtier" is field register in a customer document.

**Proposed:**

> Light, uniform fouling. Deposits ran the full length of each radiant pass with no pass or coil measurably heavier than the rest.

Same facts, one register, and it drops a term we cannot define.

**Ruling:**

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

**Ruling:**

---

# Open questions

1. **Does "foulant" survive contact with the crew?** It is the highest-value term and the one most likely to sound imported. Fallback is "deposit", which is plainer and nearly as precise.
2. **Do we introduce "scale" at all,** or keep calling everything coke in customer documents and hold the distinction internally? The split is real, but claiming a deposit is inorganic without a lab result is itself an unbacked assertion.
3. **Where does the two-layer deposit structure go?** Strong, defensible, and it explains why progressive pig sizing works. Proposal: `04-knowledge/manual/02-what-mechanical-pigging-is.md`, not a job report.
4. **Is `light | moderate | heavy` worth criteria,** or is it fine as PM judgment? Attaching observable criteria (thickness, Clean ID vs. tube ID, return duration, progression steps) makes it estimating-grade but adds a capture burden.
5. **Do we buy API RP 573?** It is the standard governing fired heater inspection reporting and the most defensible anchor available; it is also the one source this pass could not reach.

# After the rulings

Phase B in order: glossary rewrite and duplicate resolution, then report wording standard, then enum criteria, then skill mirrors, then the lint rule with its fixture. `[[idea-job-report-summary-quality]]` gets folded in and closed; this note is its exploration. Migration precedent and cost model is `[[2026-08-20-syncrude-geometry-per-pass-misread]]`, which re-labeled `crash` vault-wide and lists the six files it touched.
