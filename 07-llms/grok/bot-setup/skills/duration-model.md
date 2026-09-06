# Skill — Duration Model

**Owner Bot:** Estimator
**Source:** ported from `usadebusk-estimating` § Duration Model, cross-checked against
`/workspace/vault/01-context/estimating-approach.md`. Both are in the clone; the skill governs where
they differ, and any disagreement is a finding to report, not to resolve.

**Read this first: the rules below are written as "do X, and specifically do NOT do Y."** The Y is
usually a plausible thing a previous estimate actually did. Do not compress a rule to its X half.

---

## The pigging benchmark

**~100 ft/hour per single unlooped coil at nominal fouling.**

**It is a per-pig rate, not a heater-total rate.** It describes one pig travelling one unlooped
coil. It does **not** mean heater-total footage / 100. That arithmetic double-counts circuits pigged
simultaneously and **over-quotes every multi-pass job**. Elapsed pigging time for a pass set is
**one coil's time**, however many circuits the set carries, because the Trimax's pumping assemblies
run independently and in parallel.

**Round the per-coil figure to the NEAREST EVEN HOUR — up or down — once, at the coil level.**
(Jesse, 2026-08-23.) Even hours keep project totals landing cleanly on 12-hour increments. **This is
the only rounding step there is:** do not re-round downstream, and never round per pass, per size,
or at the heater total. **This replaced a former always-round-up rule** — do not reinstate it.

**Do not land the total on a multiple of 12** (removed 2026-08-23). Sum the task lines and report the
total as it falls.

**Parallel is free.** There is no friction allowance, and no pass set is ever marked up for running
multiple circuits (Jesse, 2026-08-23). **A designated pigging tech is assigned to each pass** — that
operator runs the controls on their own pump and their own circuit and changes their own pig, which
takes 30 seconds to 5 minutes. In double mode two operators each do that on their own circuit.
**Double mode does not take longer than single mode.** Do not model this as crew attention splitting
across circuits; that is not what happens on site.

## The rate derate is gated

Apply a derate below 100 ft/hr **only when you have reason to believe the coil is dirty** — prior
actuals on that heater, a recorded fouling history, or hard service Jesse has personally seen on
that unit. **A first-time unknown heater takes the round 100 ft/hr.** Under T&M an overrun goes back
to the customer and gets approved, so under-estimating is recoverable and over-estimating costs the
bid. `first-time clean with no prior data` is **not** a derate trigger — it is the condition under
which the derate does not apply.

**A customer's stated expected condition is a claim, not a fouling history**, and does not open the
gate. "Cleaned 3 years ago, nominal buildup expected" is an expectation on both sides.

## When actuals govern

Heater-specific actuals — the card's Job History / Task Durations, or the actuals rollup — govern
the estimate **only when the coil condition matches the job being quoted**. Read the `Condition`
column: it holds **job class**, and a decoke's hours predict the next decoke's hours only within the
same class.

**`crash` is a callout label, not a fouling grade** (Jesse, 2026-08-20). It means an unscheduled
mobilization — the facility hit trouble and needed a crew on a moment's notice. The coil is usually
dirty but not by definition, and neither the card nor the rollup records how dirty. **Never cite the
crash-vs-routine ft/hr gap as evidence about coil condition**; it is a job-class difference
confounded with mode and service, not a coke measurement.

**Do not price a routine clean from a crash row, or a crash mob from a routine row.** A crash actual
is not a discount to apply to routine work; it is the correct basis for an emergency quote and the
wrong basis for a planned one.

**Match on service AND job class, not job class alone.** The vault carries five routine
mode-normalized rates spanning 47-259 ft/hr per pig, mean ~99. The mean sits on the benchmark, but
the spread is service-shaped — big coker/crude/multi-bore coils at the slow end, short clean single
coils at the fast end.

Rows tagged `hours-blended` or `combined-heaters` are weaker evidence — use the total, not the
per-task or per-heater breakdown. If the only actuals on a heater are the wrong condition for this
job, fall back to the generic default and the 100 ft/hr benchmark, **and say so in the duration
math.**

**Outlier check.** Coils on one heater clean within hours of each other. Before letting any row
govern, check that heater's per-coilset spread and estimate off the clustering coils, never the
outlier.

---

## Rig-in: use the default. Do not build a method for this line.

**Rig-in is 6 hours. That is the answer for the majority of projects** (Jesse, 2026-09-05). Two
departures, and nothing else:

- **8 hrs** when the launcher/receiver connections are elevated **above 40 ft** *and* the pumper is
  running **double or triple** mode. **Both conditions, not either.**
- **12 hrs** only at the extreme Jesse named: pumper roughly **80 ft** from the base of the heater
  *and* connections **40+ ft** in the air. A ceiling and an exceptional case, not a rung reached by
  accumulation.

*Why elevation and mode are the two that matter, as background rather than as a calculation:* hoses
run from the pumper to the base of the heater then vertically up the side to the launchers, so
elevated connections add their height to the run rather than sitting beside it. Mode sets how many
of those runs get built — single is two sets of hoses off the blue and red ports, double four,
triple six. **That is the whole picture. Do not turn it into a hose count and do not tier from an
arithmetic result.**

**This line is deliberately not fine-tuned, and that is Jesse's instruction, not an omission**
(2026-09-05): *"Whether it takes a couple of hours more or less isn't something the facility or I
spend a lot of time / effort trying to fine tune."* **Pigging hours are the line that deserves the
complexity** — that is where the money and the schedule risk actually move. **If rig-in reasoning
runs longer than three sentences, it is wrong regardless of the number it lands on.**

**This replaced a four-tier model** (Small 4 / Moderate 6 / Large 8 / Very large 12, tiered from
three multiplying drivers — elevation, run distance, mode). Retired 2026-09-05. Run distance is no
longer an independent driver; it survives only inside the 12-hr extreme. If a source states a tier
in those words, it predates the change.

**Rig-in is ALWAYS one of six values: 2, 4, 6, 8, 10, or 12 hours. Never odd, never fractional.**
(Jesse, 2026-08-15.) That is the complete output space including after the adder. Do not average,
do not interpolate, do not carry a decimal.

**Coil footage and pass count have little to do with rig-in.** A large multi-pass heater with
connections at grade rigs faster than a small heater with connections in the air.

## The pipefitter adder, and the affirmative-trigger rule

Where USADebusk will be waiting on the customer's pipefitters to hang launchers/receivers, **add
~2 hrs**. It stacks **inside** the 12-hour cap — 12 + fitter wait = 12, not 14 — and where the
figure is already at the ceiling the adder is absorbed and stated as a risk instead.

**When the RFQ is silent on pipefitters, the adder does NOT apply.** (Jesse, 2026-07-28.) The
trigger is **affirmative** — something in the job data or the job walk has to say USADebusk will be
waiting. **Silence is not that.** Price the bare figure and put the adder in the proposal's open
items with its swing costed: `+2 hrs rig-in and +2 hrs mirrored rig-out = +4 hrs`, usually the
single largest duration uncertainty on a first-time clean.

*(Written after a replay applied the adder on silence, reasoning that nothing confirmed the
launchers were pre-hung. That inverts the trigger into a default-on.)*

## Rig-out and rig-over

**Rig-out mirrors rig-in including the adders, at the whole figure — not the bare default.** That
holds about 90% of the time (Jesse, 2026-07-25); the exception is a customer who wants rig-out done
differently, not a judgment call about whether the same work recurs. **Do not shave the adder off
the rig-out side** on the reasoning that USADebusk pulls its own pipe and the fitters remove their
own launchers — that was tried and it is wrong. If the customer specified something different, say
so explicitly and price what they specified.

**Flag rig-out as the exposure on multi-rig and large multi-pass jobs** rather than matching
silently. Known counter-example: F-802 (ExxonMobil Baytown, USA26022, 2 rigs, mode 5, routine) ran
rig-in 4 hrs against **rig-out 20** — five times the matched figure. One row does not move the rule,
and the rule still governs the estimate, but on a job of that shape say in the duration math that
rig-out is the exposure.

**Rig-over between pass sets = `ceil(passes / mode) - 1`** (mode = passes cleaned per set: double 2,
triple 3; the last set ends in rig-out). ~1 hr when launchers/receivers are already installed on the
added passes, ~2 hr when waiting on fitters.

**On silence, take the 1-hr figure** — the same affirmative trigger as the rig-in adder, read the
same way on both lines. Reading silence as "waiting" here while reading it as "not waiting" on
rig-in is how one baseline priced a single unknown two different ways in adjacent lines. **Resolve
rig-in, rig-out and rig-over together.**

**Smart Pig: 2 hrs per pass when elected.** (Jesse, 2026-09-06 — replaces a former flat 4 hrs.)

**It is an estimate and nothing more.** Jesse: *"There isn't a specific logic I use to determine the
smart pig hours, because I don't know how long it will actually take."* **Quoted jobs will disagree
with it and that is expected, not a defect** — DSP26085 carries 6 hrs on 4 passes, the F-301 /
F-371A paired line carries 8. **Do not reconcile those figures, do not flag them, and do not reason
from them back toward a rule.** There is no rule behind them to recover. Take 2 hrs per pass, show
it as the estimate it is, and move on.

## Vault rig-in actuals are not a calibration basis

(Jesse, 2026-08-15.) The recorded durations mix sources — some rows carry other salesmen's quoted
figures using their own methods. That is why the actuals column spans 2 to 34.5 hours with eight
rows above the 12-hr cap and many odd values, **none of which this rule would ever produce.** Those
rows are not counter-evidence and must not be averaged, fitted, or used to argue a figure. Read them
as history of what individual jobs took under mixed methods.

**The same caution does NOT extend to the pigging columns**, where condition- and mode-matched rows
remain the right cross-check.

## First heater vs subsequent heaters on one mobilization

(Jesse, 2026-08-23.) The first heater takes the full rig-in figure; **subsequent heaters in close
proximity take a reduced one**, because the pumper is already partially rigged in. DSP#26100 ran
6 hrs on the first and 4 on the other two — 4 being enough to clean the tanks, add hoses, and give
the fitters time to hang launchers.

**This is why `Rig-Over` reads 0 on a job where the equipment physically moves twice.** A
same-mobilization move between nearby heaters is priced as a **reduced rig-in plus a mirrored
rig-out on the destination heater**, not a rig-over line. Rig-over stays the right line for moving
between pass sets *within* one heater. Rig-out still mirrors rig-in on each heater individually —
DSP#26100 runs 6/6, 4/4, 4/4.

## Stand-by: the test is who controls the cause

**Customer-caused stand-by is NOT an estimating input.** (Jesse, 2026-08-21.) Plant readiness —
de-inventory, draining, blinding, temporary spools and 90s, releasing the heater — is outside
USADebusk's control and **is not forecastable**. *"We will have to clean the heater when they are
ready whenever that may be. We don't control the stand-by, and we can't anticipate it."* So: **do not
price it, do not pad for it, do not carry it as a proposal open item, and do not raise it as a thing
to confirm with the customer.** A customer's own schedule note — "the plant is running ahead," "we
expect to be ready Tuesday" — is a note, not evidence. On-time, a shift early and a shift late are
the same job.

**The counter-case: stand-by that USADebusk's own equipment profile causes IS foreseeable and stays
statable.** One filter press against 2x Trimax on F-802 produced 20 hrs of stand-by and $25,628.17 —
a consequence of the profile we brought, knowable at bid time, and naming it in the proposal is
correct. Do not read the customer-caused rule as licence to drop that flag, and do not read the
filter-press rule as licence to forecast the plant's schedule.

## Pre-inspection pigging is a task allowance, not footage / rate

(Jesse, 2026-08-23.) When a customer says the heater was *recently steam-air decoked, so it should be
clean*, they mean they completed their routine method and **assume** it was thorough. They have no
way to visualize residual coke and no way to verify it. Jesse has pigged first-ever-pigged heaters
at facilities with long steam-air histories and pulled out **layered fouling** — one layer left
behind, the heater returned to service, another cooked on top. Sometimes they do get an optimal
decoke; the layering is not universal but it is observed and repeated.

**The commercial asymmetry runs OPPOSITE to a normal decoke.** If the allowance is short, USADebusk
tells the customer more pigging is needed and the customer decides — and because the coil must be
clean for the inspection to be valid, **the rep always approves.** If the coil really is clean the
crew goes straight to inspection and the hours are never worked. The job is T&M, so USADebusk does
not charge what it does not work. **Under-estimating is recoverable; over-estimating inflates the
bid against competitors on hours that may never exist.** Do not pad this line, and do not reason
about it as though the residual risk pointed upward.

## Mob/demob in the schedule vs mob/demob in the price

The Duration Model governs how mob/demob **occupies the schedule**. It does not set price. The
costing build-up lives in the Work-Up Billing Math skill, and what may be *billed* is whatever the
governing contract allows — frequently less than the built-up cost. Never carry a schedule figure
into a quotation line.

## Presentation

**Shifts and days are a PRESENTATION rounding, never an hours adjustment.** The Total Duration block
reports whole shifts and days — DSP#26100's 94 hrs renders as "8 Shifts" and "4 Days" — but **no
hours are added to reach them.** `Days = total hrs / 24`; shifts round up from `total hrs / 12`.
Reporting 8 shifts and quoting 94 hours is correct and is not a discrepancy.

All tasks run a 12-hr shift cycle; pigging runs 24/7.

**Workup conventions** (DSP#26100, DSP#26094): `Man-hrs = total hrs x 3` where the crew is 3 on
shift. A 6-person crew is 1 supervisor + 2 operators per shift, day and night.
`Composite rate = (total - mob - demob - per diem) / project hours`. DEF and per diem both key off
the **shift count**, not the hour count.

**SIMOPS:** multi-heater jobs need overlapping heater timeline visibility — resource stacking and
scheduling commitments visible across all heater cards at once.

## Safety boundaries

Show the duration math explicitly so it can be checked. Never invent an actual. If the only actuals
available are the wrong condition or the wrong service, say so and fall back to the benchmark rather
than stretching a row to fit. Never price customer-caused stand-by. Propose-only: nothing leaves for
a customer without Jesse reading it.
