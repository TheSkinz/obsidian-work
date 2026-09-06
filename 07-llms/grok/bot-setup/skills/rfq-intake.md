# Skill — RFQ Intake

**Owner Bot:** Intake
**Source:** ported from `usadebusk-estimating`, sections "RFQ Intake — Required Inputs" and
"Contract Terms & Bid Instructions Review". That skill is the authority; re-read it in
`/workspace/vault` if anything here looks stale.

## Two standing rules that set the posture

**Every RFQ gets bid. There is no no-bid analysis, and it is not a question to raise.**
(Jesse, 2026-08-16: *"I don't believe it's worth bidding, but we will anyway. We don't turn down
opportunities to bid."*) Low expected win probability is not a reason to decline, to reduce effort,
or to suggest spending estimating hours elsewhere — including where the site is known to bid for
procurement compliance with a preferred contractor already in place. Build the bid properly
regardless. The only thing that stops a submission is a hard disqualifier such as the wrong form or
a missed deadline, which is a mechanics failure and not a judgment call.

**Competitor outcomes are unknowable — do not ask who won or why.** (Jesse, 2026-08-16: *"I won't
be able to give answers like 'DDT actually took this award'."*) Award results, competitor pricing
and the customer's stated reason for a loss are not information available to Jesse, so a loss reason
is inference at best. Do not open it as a question, an open item, or a thing to chase. `lost-reason`
on a quote note is a best-available label, never a measurement.

## The 17 required inputs

Confirm all of these before any proposal is built:

1. Facility name and customer
2. Heater tag and service name
3. Scope type (Planned / Emergency / Turnaround)
4. Pass/circuit count and coil pairing
5. Tube ID — convection and radiant (OD and schedule if available)
6. Total footage per pass
7. Inlet/outlet flange size and rating (e.g. 4" 300#, 6" 150#)
8. Tube arrangement (horizontal / vertical / helical)
9. Tube metallurgy (carbon steel or stainless)
10. Expected fouling type (standard coke, hard coke, pitch/resid) — ask for the customer's
    expectation **and their basis for it**; it is a prediction on both sides, not a measurement.
    One informal grade pairing "soft" with the coke noun was retired 2026-09-03 (DQ-030) and is not
    vault vocabulary — if a customer uses it, record their words verbatim and ask what they mean
    rather than mapping it to a grade yourself. The fouling vocabulary is in
    `/workspace/vault/04-knowledge/manual/17-glossary.md`.
11. Water source (BFW / fresh condensate / demineralized / firewater)
12. Launcher access and elevation constraints
13. Jumper spool requirements
14. Execution dates (or estimated window)
15. Equipment profile — Trimax count (1x / 2x / 3x) **and** support-equipment count (filter press,
    4x3 pump). A customer election constrained by room at the unit and by fleet availability across
    concurrent jobs; supplied per bid, never derived from heater data.
16. Applicable contract rates
17. Applicable customer standards

## Derive vs ask — the load-bearing part

This skill computes from supplied data; it does not infer the situation. Anything in the right-hand
column is a per-bid input from Jesse. **Asking for it is correct behavior, not a failure to be
thorough, and a plausible-looking assumption in its place is worse than an open question.**

| May derive from supplied data | Must ask — never infer |
|---|---|
| Duration from footage / rate, per the Duration Model | Support-equipment count (filter press, 4x3 pump), and whether a second unit is available |
| Rig-over count, `ceil(passes / mode) - 1` | Customer elections — filtration, smart pigging (status only, read from the card's Job Options) |
| Mob/demob **cost** from a **stated** piece count — internal margin only | Contract rates and the third-party markup tier; the **billable** mob/demob lump sum, which the contract caps and which is never the workup's built-up cost |
| All line-item arithmetic — hours x rate, extensions, totals | Site real-estate: whether the unit has room for the equipment being quoted |
| Pig cost via the quantity method | Water source (item 11) |

The right-hand column exists because those values are set outside the heater's data — by the
customer, by the governing contract, by what physically fits at the unit, and by what equipment is
uncommitted that month across concurrent jobs. **No amount of heater detail determines any of them.**

**Incomplete-input gate:** if inputs are incomplete, list exactly what is missing and ask for it.
Do not estimate or assume missing technical data.

## Deriving for the estimate does not license writing to the card

The estimate and the heater card are separate containers with opposite rules. An estimate is
*supposed* to compute — derive footage, hours, wall thickness or anything else it needs, and show
the math. A **heater card carries stated values only**: if the source document does not state a
field, it stays blank, even when it is trivially computable. Carry the computed value in the
estimate's working note, never into the card's Tube Geometry.

## Contract terms and bid instructions — a separate pass, run before pricing

This is what loses bids on technicalities rather than on price. Confirm and record:

- Submission platform — ARIBA, GED, or direct email per customer requirement
- Due date **with time zone**
- Required forms and attachments
- Insurance and safety-qualification requirements
- Whether pricing must be submitted on the customer's own sheet or workbook
- Any page-count or format constraints

**A technically perfect proposal submitted on the wrong form is a no-bid.**

## Output

A checklist marking each of the 17 inputs **supplied / missing / assumed**, plus the submission
mechanics above. For anything marked assumed, say what was assumed and why. A plausible default for
an unknown field is actively misleading — leave it blank and flag it rather than filling it in.

Save to `/workspace/bids/<DSP or facility>/intake.md` and name that path when handing off.

## Safety boundaries

Never reply to a customer — not to acknowledge, not to clarify, not to confirm receipt. Anything
needing a customer answer goes in Unresolved questions for Jesse to send. Do not price anything.
Do not raise a no-bid. Do not ask who won a prior award.
