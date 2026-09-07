# Skill — Proposal Assembly

**Owner Bot:** Scribe
**Source:** ported from `usadebusk-estimating` sections "Proposal Document Structure",
"Section Templates", "Proposal Generation Guardrails", and the pre-send rule from
"Pricing Structure".

## Known deviation, read this first

In the vault, the commercial half of a proposal is produced by a generator — `render_proposal.py`
reads a finished estimating workup `.xlsx` and emits Sections 3, 7 and 9 as a branded draft, with a
back-test harness proving three real quotes reproduce to the cent. **None of that exists here.**

So: this skill covers **document structure, section content and the pre-send gate**. It does not
reproduce the generator, and it must not try to.

**Where this skill says "branded", it means the Brand Standards skill — read it before building any
document.** Fonts, colours, table header and alt-row fills, and the logo and its path all live
there, and the values are deliberately not restated here. Set table styling explicitly; python-docx
defaults to blue, which is not a USADebusk colour. Any figure produced here is hand-tallied — mark it
as such and show the arithmetic. Where a workup `.xlsx` exists, the generator on Jesse's machine is
the right tool and this Bot is not a substitute for it.

## Document structure — 12 to 16 pages

Reproduce this section order exactly unless specified otherwise:

1. Cover Page
2. Table of Contents
3. Requested Service
4. Execution Plan
5. Technical Data
6. Verification of Pass Cleanliness
7. Quotation
8. Requested / Provided Items
9. Hourly Charge Out Rates
10. Time and Material Rate Charges
11. Terms & Conditions
12. USA DeBusk Trimax Pumper (boilerplate)
13. Additional Services (boilerplate)
14. Sample USA DeBusk Customer Profile (boilerplate)

**Use the spaced legal form `USA DeBusk` with its capital B on customer-facing documents.** The
closed house form is `USADebusk`; `USADeBusk` is a dead string.

## Section 3 — Requested Service

Opening: *"USA DeBusk submits this proposal for mechanical decoking services at [Facility Name]
during [Event/Month Year]."*

Then a **Scope of Work** list (job type — Emergency or Planned; heater tags; equipment mobilized)
and a **Commercial Terms** list (Basis T&M; Mob/Demob lump sum; duration estimate basis). Close with
*"USA DeBusk will deliver a safe, flexible, and cost-effective solution in close collaboration with
[Customer] to ensure [turnaround/project] success."* Trimax Pumper photo placeholder.

## Section 4 — Execution Plan

A Gantt table per heater: **Start | End | Hours | Tasks**. Standard rows are rig-in hoses and
launchers, **one Pig row per pass set — not one row for the heater**, rig-over between sets if
applicable, Smart Pig if elected, and rig-out. Bold sub-total per heater and a bold Total Hours row.
Then an Equipment and Manpower Allocation table (equipment left, manpower right) and a Total
Duration block.

**The Project Manager field always reads "Travis Trenholm" — a template default, not an assignment.**
(Jesse, 2026-07-29.) There is no way to assign a PM at bid time, so the ops manager who will dispatch
the project is the standing placeholder on every quotation. **Never flag it, never query it, never
note it as superseded or as a thing to confirm.**

**The Equipment and Manpower Allocation block is the authoritative billable list** — read it per job
to decide whether the person running the project bills as Project Manager or as Day Supervisor
(Jesse, 2026-07-30). The person running the project is always on dayshift; what varies is the slot
they bill in. No PM row means no PM is billed and they take a supervisor slot; a PM row means they
bill as PM. It is not a default either way, and it is **not** inferable from the Total Duration
block's Project Manager name — that is the placeholder above. Worked example: DSP26092 (USA26040,
HF Sinclair Navajo) carries no PM row, so Jesse bills as Day Supervisor.

**A stated execution date is a proposal, not a commitment, and a Gantt that disagrees with the RFQ's
date is not a defect.** (Jesse, 2026-07-29.) Customers routinely name a window and settle the exact
date with the *winning* contractor. **Do not raise the date spread as a discrepancy, an open item, or
a thing to confirm.** This is distinct from a genuine typo — a *wrong year* is worth one mention, a
date sitting inside the customer's own stated window is not.

Standard disclaimer: *"The projected times and durations are estimated based on our extensive
experience and the coil data provided. However, please be aware that the actual project duration may
vary due to factors such as deposit hardness, location, composition, and thickness."*

## Section 5 — Technical Data

One summary table per heater, titled `Furnace: [Heater Tag & Name]`, with convection and radiant
columns: number of coils, total tube footage, average tube + bend length, tube count, tube I.D.,
material, tube arrangement, inlet/outlet flange size and rating, launcher elevation, return bends,
and special notes.

**This table carries facts only.** Filtration and smart pigging are **customer decisions**, read from
the heater card's Job Options as status — never reproduced here as a spec row. Read heater facts from
the card; field meanings defer to the Heater Card Schema.

## Section 6 — Verification of Pass Cleanliness

Boilerplate — the standard 4-point verification protocol (sensor data / effluent monitoring / pig
condition tracking / final foam run with client sign-off). Reproduce verbatim unless customization is
requested.

## Section 7 — Quotation

Header block (company address, date, DSP#, billing method, valid date — 90 days default, prepared-by
name per job, confirm). Bill To block. Special Instructions line summarising contract terms.

Line items (Description | Line Total): Mobilize [equipment] lump sum; Mechanical Decoke per heater
with the hour breakdown (rig-in | pig | smart pig if applicable | rig-out); Labor & Per Diem;
Materials (DEF and decoking pigs); Demobilize [equipment] lump sum. Footer notes, then a right-
aligned Pricing Summary box: Equipment | Manpower | Materials | **Total**.

**Critical: never apply a default third-party markup rate.** Always confirm the applicable rate from
the governing contract before populating the field.

## Generation guardrails

**Flag immediately if provided data is internally inconsistent** — footage that does not match tube
count x tube length, for example.

**An enumerated list that contradicts its own stated count is a flag, not a rounding error.** Where
the RFQ enumerates items and also states a total — most often the equipment profile, e.g.
`1x Trimax + support unit + 2 filter presses + 6x4 pump + 3 crew trucks (7 pieces traveling)`, which
enumerates eight against a stated seven — **count the enumerated items, compare against the stated
count, and stop on any mismatch.** Do not silently adopt either figure. Name both readings, price the
swing, state which you carried and why, and put it in the open-items list. The same check applies to
crew headcount against enumerated roles, pass count against enumerated circuits, and drivers against
pieces traveling. **Drivers = pieces traveling is an identity**, so a driver count disagreeing with
the piece count is the same defect surfacing on the labor side.

**Price the swing correctly: crew total is fixed, so an added piece converts a non-driver into a
driver — it does not add a person.** Worked on a shape of 9 crew / 7 pieces / 2 non-drivers at 220
one-way miles with 4 hours of non-driver travel: reading eight pieces gives **8 drivers and 1
non-driver, still 9 crew**. The swing per end is four terms, not one — `+ mileage for the piece
+ one driver per diem - that person's non-driver travel labor - their non-driver per diem` — netting
**+$428 per end and $856 across mob and demob**, not the $1,620 that counting only the additive terms
produces. **Never reject a reading on the ground that it "would need another crew member"; it would
not**, and that reasoning has been used to discard the right answer for the wrong reason.

**Never document the absence of something that was never in scope.** (Jesse, 2026-09-03: *"There's no
need to add details about equipment that isn't or wasn't ever supposed to be sent on the project."*)
If filtration was not sold, the proposal is silent about filtration — no "no filtration required"
line, no reassuring N/A row. The absence of out-of-scope equipment is not a clarification; it makes
the reader wonder what they missed. **This is the easiest rule to break while feeling thorough.** It
does not touch **stated requirements**, which are line items we do tell the customer (the 2"
firewater hose) — the distinction is whether the thing is in scope, not whether it is interesting.

**Show duration math explicitly** before finalizing the Execution Plan so it can be verified, and
**show line-item hour x rate calculations in a working note** before producing the final Quotation
table.

**Never assume tube footage, pass count, or equipment profile** — derive from provided data.

**"Use the same rates as [prior DSP#]"** → confirm which DSP# is referenced and verify those rates
against the *current* contract before use.

## The pre-send gate — compare scope before dollars

Run this before anything goes out. It is judgment, not arithmetic, and it is the most valuable rule
in this skill.

Once mob/demob is set aside (see Work-Up Billing Math — a gap equal to a whole number of mob/demob
units is expected, not an error), a remaining gap between the workup's total and the quotation's
total **carries no information in its size.**

**DSP26026's $39,548.16 gap is correct and DSP25142's $90,090 gap is a defect, and no dollar
threshold separates them.** Never reason about whether a gap is "large enough to worry about" — that
question has no answer. What separates the two cases is that both documents state their scope in
structured form, so compare that first:

| Quotation scope vs workup | Reading | Action |
|---|---|---|
| **Matches** — same heaters, same task hours | A totals gap here is a dropped, mistyped or miscarried line. Nothing explains it | **Block.** Do not send until resolved. This is the DSP25142 shape |
| **Narrower** — fewer heaters, or fewer task hours | Ordinary scope narrowing; the workup was built for a wider turnaround and the bid went out for part of it | **Re-price and check.** Take the quotation's own hours at the workup's own rates, add its other lines, compare against the quotation's stated total. Match → pass, and say in one line that a narrowing was detected and what it was. Mismatch → block; the narrowing is hiding an error |
| **Wider** — heaters or hours the workup does not cover | Quoting work the estimate never costed | **Block unconditionally.** This direction is never legitimate |

**Worked case — DSP26026 (Marathon Detroit)**, the reason this rule exists: the workup's `TA Heaters`
row carries **12 / 36 / 12** hours and $75,240 equipment against a total of $153,715.40, while the
submitted quotation covers the **70H1 Coker alone at 6 / 24 / 6**, decoke $58,287.24, total
$114,167.24. The gap is not a mob/demob multiple, so the lump-sum exemption does not apply — but the
hour figures disagree on their face, which is the narrowing signature. Confirmed 2026-07-25 that
nothing was quoted short.

**Narrowing is occasional — a few times a year**, so the matched-scope path is the normal one and the
re-price path is the exception. That is what makes a pass-with-note tolerable rather than noisy: a
gate firing for confirmation on every narrowed bid would train the reviewer to click through it,
which is the same failure the mob/demob rule was written to fix.

**The re-price is a human step.** Jesse's `presend_gate.py` deliberately does not compute it, because
guessing it produces a confident wrong pass on the one branch where the estimate and the bid
legitimately disagree. If you reach the narrowing branch, lay out the re-price for Jesse rather than
declaring a verdict.

## Safety boundaries

Produce drafts only. Never send, publish, or submit anything. Hand over one file, never a source and
its generated output together. Mark every hand-tallied figure as hand-tallied and show its
arithmetic. Never apply a default third-party markup. Prose is the Project Manager's voice — keep
drafted narrative short and mark it clearly as a draft for Jesse to replace.
