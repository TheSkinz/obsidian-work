# Fable 5.1 build prompt — Steady Flux pipeline inspection visualization

Source data: Steady Flux Technologies document **25-0532-006 Rev. C**, *Intelligent Pig Inspection
Report, 1611-X002-005 Line (8 Wharf)*, prepared for Chevron Richmond, inspection 2025-04-17, issued
2025-07-25, 56 pp. Held at `C:\Users\Jwuts\Downloads\25-0532-006C Chevron Richmond Line Long Wharf Line No 8 REVC.pdf`
— not in the vault; it is Chevron's document, supplied informally by the Steady Flux CEO.

The data block below was extracted and reconciled in a Claude Code session on 2026-09-06.

The customer is not named in the paste-in payload, but the GPS route is real and geolocates the
line, so treat the result as identifiable rather than anonymous. That is a deliberate call (Jesse,
2026-09-06): this is an internal demo and a model test, not a customer deliverable and not for any
official use. Do not forward the built page to Chevron or present it as work product.

## How to run it

Open a **new** Claude Code session in the desktop app, set the model to **Claude Fable 5.1**, set
effort to **`high`**, and paste everything below the `---` as a single message.

**Use `high`, not `xhigh` or `max`.** Counterintuitive for a build this size, and documented: at the
top effort settings Fable 5.1 drafts a long deliverable inside its thinking and then writes it out
again as the reply, doubling the turn for no quality gain. Anthropic's guidance is that a single
request asking for one long deliverable runs at `high`, and you move up only where you have
measured a gain.

## What to expect while it runs

Fable 5.1 writes fewer user-facing updates during long tool chains than Fable 5 did, and the effect
strengthens at higher effort. Minutes of silence is normal, not a hang. The prompt asks for brief
progress notes, which helps but does not eliminate it.

If it starts rewriting the whole HTML file to make small changes — expensive at this file size, and
a known Fable 5.1 tendency — paste this once:

> The number of tokens used to edit files is best minimized, all else being equal. Therefore, when
> it will not affect the end result, try to surgically edit a file rather than rewrite the entire
> thing.

## What to watch for as a capability read

1. Does it hit the four platform walls in the "Environment" section without being told how to solve
   them, or does it re-lose the day?
2. Does it label its own interpolation honestly, unprompted? The data is 115 points across 5,600 ft
   and everything between them is invented smoothing.
3. Does it actually open the page and look at it, or declare done from the code?
4. Does it notice the two distance systems disagree by 5% and handle it, rather than silently
   picking one?
5. **Does it use the latitude?** The form is left completely open and the prompt says so twice. If
   it builds the 3D camera tour anyway, that is a legitimate answer — but a *chosen* one, and it
   should say why it chose it. If it reaches for something else and the something else is better,
   that is the most interesting outcome available from this run.

## What the extraction found, and what does not reconcile

Read from the flaw table (pages 10–40): **401 rows — 286 girth welds, 115 anomalies.** The anomaly
count reconciles exactly with the Executive Summary's stated 115, and the type split (103 metal
loss, 9 metal-loss-with-dent, 2 dent, 1 pitting) reconciles exactly with the Anomaly Summary's type
totals. Girth-weld relative distances are internally consistent to within 0.01 ft across all 285
intervals (58 of them differ by exactly 0.01 ft — a rounding artifact, not a data problem). The flaw
table's measured columns are clean and are the authority.

Its *label* columns are not. See item 7 below and the note above the data block.

Eight things in the report do **not** reconcile. All but the last two sit in derived summaries
rather than in the measured data:

1. **Two distance systems, 5.0% apart.** The girth-weld chain runs 0 → 5,612.69 ft. The surveyed GPS
   route (Table 1) sums to 5,343.8 ft, and the Project Summary states line length 5,344 ft. That is
   +268.9 ft. Odometer distance and surveyed route length are not the same measurement, so divergence
   is expected in kind — but 5% is larger than the ±1% locating accuracy Steady Flux advertises on
   their website (that figure is website copy, not a claim made anywhere in this report). The prompt
   tells the model to state the mapping it uses rather than hide it.
2. **The 6-inch anomaly count.** Project Summary (p3): "Anomalies 82 (6in), 32 (8 in)". Executive
   Summary (p4): "83 were located in the 6" section and 32 in the 8" section." Rev C added P-1, the
   0.060 in pit, and p3 was not updated — so **115 total** is settled and p3's 82 is simply stale.
   Which side of the reducer that 115th record belongs on is a different question, and item 3 says it
   is open. Do not read this item as endorsing p5's split.
3. **The 8-inch Anomaly Summary contradicts itself.** Its bin rows give Metal Loss 21 + 5 = 26 and
   its Total row says 25, so the section total reads 32 where its own bins sum to 33. My extraction's
   8-inch bins match the report's bin rows *exactly* (10–35%: ML 21, Dent 1, ML w/Dent 5; 35–50%:
   ML 5, ML w/Dent 1). Splitting the flaw table at the reducers gives 33 in the 8-inch segments and
   82 in the 6-inch segment, against the summary's 32 / 83. Grand total is 115 either way, so exactly
   one record's section assignment is in dispute. Unresolved — do not assert either split as correct.
4. **The report states two different bases for percentage loss.** Reporting Thresholds (p9): "Metal
   loss anomaly percentage is calculated based on apparent anomaly depth in reference to the nominal
   pipe wall thickness." Appendix B glossary (p56): "When given as a percentage, loss is relative to
   the median wall thickness." All `loss_%` figures in the data block below are derived against
   **nominal** and marked as derived.

   The sharpest evidence that this matters: binning the 82 6-inch records against nominal puts all
   three metal-loss-with-dent records in the 35–50% row and none in 10–35%. The report's 6-inch rows
   read 2 and 1. The counts agree at 3 total, so this is a *basis* disagreement, not a section
   assignment — which is why item 3's residual is better explained here than by a misfiled record.
5. **The Executive Summary's distances match nothing in the flaw table.** p4 places the 8-inch minimum
   "approximately 1 ft from the land-side weld, 43.7 ft from the start of the line" — the table has
   IML-2 at 66.95 ft. p4 puts the 0.176 low spot at "22.4 ft from the land-side weld, 887.3 ft from
   the land-side end" — the table has EML-43 at rel 27.66, abs 1018.44. p4 puts the largest dent at
   "2.2 ft from the land-side weld and 4086.8 ft" — the table has D-2 at rel 1.69, abs 4154.80.
   Rev C's own history line reads "Updated known pipe lengths to flaw table," so p4's distances look
   pre-Rev-C. **The flaw table wins; ignore p4's positions entirely.**
6. **Appendix A's narrative captions carry copy-paste errors.** It says IML-2 is "approximately 2.79
   feet past GW 11" — the table puts IML-2 at 1.12 ft past GW-11, and 2.79 ft is IML-1's offset past
   GW-10. It says MD-4 "is 9 inches long, 6 inches wide" — the table says 4.39 × 4.76, and "9 inches
   long, 6 inches wide" is the wording of the EML-43 paragraph three pages earlier, where it rounds
   correctly. Appendix A's *wall readings* do match the table in both cases; only the geometry and
   offsets are wrong.
7. **The flaw table's own girth-weld label columns are internally inconsistent.** 19 of the 286 weld
   rows carry a land-side column number that contradicts their own `GW-n` id — several are simple
   transpositions (GW-164 is labelled 165 and GW-165 labelled 164, likewise 167/168 and 211/212/213).
   Two anomalies inherit this: see the note above the data block. This does not affect any measured
   value, only the labels, and absolute distance is unaffected throughout.
8. **52 of the 56 page headers carry the wrong document number.** The title page and Project Summary
   say `25-0532-006 Rev. C`, and pages 1–4 match. Page 5 reads `Document 22-0532-005 Rev. B` — wrong
   number *and* wrong revision. Pages 6–56 read `Document 22-0532-006 Rev. C` — right revision, wrong
   prefix. Found 2026-09-07 while assembling the defect list Jesse sent the Steady Flux CEO; it
   affects nothing in the data but it is a controlled-document defect.

These are worth a note to the CEO independently of this build — the same friend-of-a-friend channel
used for the F-501 findings on 2026-08-16.

## Repair ladder

Send one at a time, in this order, only for what actually broke. Each names a failure, not a fix.

1. *"The page renders but the layout doesn't match the data. Re-derive it from the route and
   girth-weld tables and verify your totals before continuing."*
2. *"Nothing is legible at the default zoom. Look at your own screenshot and fix the contrast and
   type sizes."*
3. *"Motion between points of interest reads as a series of cuts rather than one continuous move.
   Make the transitions continuous."*
4. *"You reported this done without opening it. Open it, screenshot it, read the console, and tell me
   what is actually wrong with it."*
5. *"This is a competent chart, not something anyone will remember. You were told to pick the most
   visually impressive form for this data and you picked the safe one. Try again."*

---

Build a single-file interactive web visualization of a real pipeline intelligent-pig inspection,
branded for the company that performed the inspection.

## What this is being judged on

**Visual impact, first and mostly.** This page is going in front of the inspection company's CEO. The
bar is that he stops, looks, and wants to show someone. A page that is accurate, careful and
forgettable is a failure here. Accuracy is the floor, not the goal — it is what makes the impact
mean something, and the data has already been reconciled for you so that staying accurate costs you
almost nothing.

Spend your effort on the picture. Where you have a choice between a safe presentation and an
ambitious one, take the ambitious one.

Someone who knows nothing about pipeline inspection should open this, watch without touching
anything, and come away with three things: where this pipeline is losing wall, how much is left at
the worst places, and roughly how much of it was actually measured. Someone who *does* know pipeline
inspection should find the numbers they'd want and no claim the data doesn't support.

### What is actually dramatic in this data

Use this. It is why the dataset was chosen, and a picture that buries it is not doing its job.

- **A pit at 0.060 in.** Nominal wall is 0.280 in. Seventy-nine percent of the steel is gone at one
  spot, 2.4 inches long, halfway out the line. Every other reading in 5,600 ft of pipe is between
  0.157 and 0.287 in — this one is off the scale by a factor of two and a half, and the first release
  of the report missed it entirely. It was recovered only by re-analysis. It is the single most
  arresting fact available to you.
- **Full-bore internal thinning.** Eleven records in the first 450 ft, nine of them 12 to 23 ft long,
  wrapping the entire inner circumference. Not spots — long tunnels of thinned pipe.
- **A clear pattern and its exceptions.** 94 of 115 anomalies sit between 5:00 and 8:00 — the bottom
  of the pipe, where water and debris sit. The 21 that don't are the interesting ones.
- **Density that varies enormously.** One 38 ft joint carries 16 separate flaws; thousands of feet
  elsewhere carry none. The line is not uniformly bad, it is bad in specific places.
- **The line changes size twice** and doubles back on itself at a wharf, so the run is a loop, not a
  straight shot.

### Two ways this fails

Fair warning about the two failure modes, so you can steer away from both:

- **Timid.** A clean chart, a tidy table, a competent diagram. Correct and unmemorable. This is the
  likelier failure and the one to actively resist.
- **Decorative.** Effects, particles and motion that aren't carrying anything. If a viewer asks
  "what does that mean" and there's no answer, it's noise. Every striking thing on the page should
  be striking *because of what the data says*.

## How to work

You are operating autonomously. The user is not watching in real time and cannot answer questions
mid-task, so asking "Want me to…?" or "Shall I…?" will block the work. For reversible actions that
follow from this request, proceed without asking.

Before you end your turn, check your last paragraph. If it is a plan, an analysis, a question, a list
of next steps, or a promise about work you have not done ("I'll…", "next I'll…"), do that work now.
That includes retrying after errors and gathering missing information yourself. Do not stop because
the session is long. End your turn only when the build is complete and you have looked at it, or you
are blocked on something only the user can provide.

The request sets the scope and the scope is the deliverable — don't quietly narrow it. Read ambiguity
the way a careful colleague would and make routine judgment calls yourself. If you see a real problem
with the task as specified, say so in a sentence or two and keep building under stated assumptions.

Say in one line what you're about to do before you start, and drop a brief note as you finish each
major stage so the user can follow along. Close with a short recap that stands on its own.

First privately list what you need next; then request every item that doesn't depend on another's
result in the same response.

## The form is yours, not just the styling

**The single most important instruction in this prompt: choose the presentation you believe will be
most visually impressive and most useful for this data, and build that.**

What prompted this request was an automatic cinematic 3D tour — a to-scale model of the line with a
camera that orbits, dollies in to each significant defect, holds, and drifts on to the next. That is
a direction, not a specification. It is the thing to beat, not the thing to reproduce. If you judge
that a different form serves this dataset better — an unrolled cylinder map where 5,600 ft of pipe
wall becomes one continuous surface, a C-scan-style thickness field, a strip chart married to a
spatial view, a scrubable inspection timeline, something 2D, something hybrid, something nobody has
named — take it. You will not be second-guessed for departing from the tour idea. You will be
second-guessed for building something less impressive than the tour because you assumed the tour was
required.

Dimensionality, rendering technique, whether there is a camera at all, geometry construction, motion
and choreography, layout, type scale and hierarchy, how condition maps to color, lighting, materials,
how the supporting information is presented and where it sits, whether there is a timeline or a
minimap or neither, how a viewer navigates — all of it is your call. Do not ask which approach to
take. Pick the one you think is best and build it. If you consider more than one form seriously, say
in a sentence which you chose and why; that reasoning is useful, and it is the only thing owed on
this decision.

**Three things are constraints and not choices, so that the rest can genuinely be free.** They are
stated in full further down; named here so you don't mistake them for design latitude you've been
given and then had taken back:

- **Brand palette and typeface** come from Steady Flux's live site, because the page is branded for
  them. Everything about how you *use* that palette and type — hierarchy, weight, scale, what carries
  color and what doesn't — is yours.
- **Certain information has to appear**: provenance, the interpolation disclaimer, the percentage
  basis, and the absence of a fitness-for-service verdict. Where it sits and how it looks is yours.
- **The data is what it is.** The measured extents, positions and clock orientations are not
  adjustable to suit a composition.

Two things the form has to deliver, whatever it is:

- **It rewards watching.** A viewer who opens the page and touches nothing should still be shown the
  story of this pipeline. Interaction should deepen that, not be the price of admission.
- **It handles the whole run.** 5,600 ft, 115 anomalies, two pipe sizes and 285 joints. A form that
  only works for the four dramatic defects and gives up on the rest is not solving the problem.

There is a prior build of this concept for a different subject. You are not being shown it, on
purpose. Solve the presentation your own way.

## What an intelligent pig inspection is

A pipeline is a long steel tube carrying product. Over years the wall thins — internal corrosion from
what's flowing through it, external corrosion from what's around it, mechanical damage where
something struck or settled on it. The wall is what holds the pressure, so how much is left is the
question that matters.

An intelligent pig is an instrumented tool that travels inside the line, carried by the product flow,
measuring remaining wall thickness continuously and recording where it was for each reading. It comes
out the far end and the data comes off it.

This inspection was performed by **Steady Flux Technologies** using their **WiLBR Intelligent Pig** —
an ultrasonic pulse-echo tool. On this run it averaged **6,178 readings per linear foot**. Their
published specifications put flaw detection "as low as 0.185"" and location "within ±1% of the tube or
pipe length" using a proprietary internal mapping system, and the tool reports internal and external
corrosion, pitting, erosion, manufacturing deformations, bulging, ovality and swelling.

Two details of this particular run matter to the picture:

- **The tool distinguishes internal from external damage** by whether the inner-radius data changes at
  the flaw. Where the bore moves, the loss is internal; where the bore is unchanged and the wall is
  thin, the loss is external. Both are in the data as separate types, and the distinction is real
  information a viewer should be able to see.
- **The line was fouled.** Cleaning ran before the inspection and swab pigs were run to clear air that
  would interfere with the ultrasound, but debris still degraded signal in places. The report's own
  C-scans render dropped or low-grade signal as white, and it recommends manual UT where large white
  areas appear. Absence of a reading is not absence of a flaw, and the page must not let a viewer
  conclude otherwise.

What lands in the report is not 6,178 readings per foot. It is a table of 115 discrete anomalies: per
anomaly, one remaining-wall figure at one recorded position and clock orientation. That distinction
matters and the page must not obscure it — see "Honesty" below.

## The asset

A looped pair of pipelines at a marine wharf, inspected in a single run. The tool launched from the
land-side site, ran out to the wharf, reversed at the far end, and returned to the same site.

- **Total run: 5,344 ft (1.01 miles).** Carbon steel, Schedule 40.
- **8-inch NPS, nominal wall 0.322 in** for the first 452 ft out of the launcher, and again for the
  last ~1,477 ft on the return.
- **6-inch NPS, nominal wall 0.280 in** for the long middle section, roughly 453 ft to 4,135 ft.
- Two **6-to-8 reducer pairs** mark the transitions: girth welds at 452.23 / 452.90 ft and at
  4,134.91 / 4,135.84 ft on the odometer scale.
- **286 girth welds** — 285 pipe joints, mean 19.7 ft, ranging 0.49 to 56.74 ft.
- Four surveyed bends, at 1,108.2 / 4,038.9 / 4,064.7 / 4,428.6 ft on the route scale.
- Grade, minimum yield strength, operating temperature, class location, longitudinal joint factor,
  fill volume, product and age are all recorded as "(TBD)" in the report's Project Summary, and MAOP
  as "Not calculated at this time." **The report never states a minimum allowable wall thickness** —
  not as a value and not as an explicit absence. Treat it as unavailable, which is what the missing
  inputs above imply, and do not report it as a finding that none exists.

### Two distance systems, and they disagree

This is the one geometric problem in the data, and you have to make a decision about it rather than
let it pass silently.

- The **GPS route table** below is a surveyed centerline: 41 waypoints in latitude/longitude with
  cumulative distance, totalling **5,343.8 ft**. This is the path's real shape.
- The **girth-weld chain and every anomaly position** are on the tool's **odometer**, which runs
  0 → **5,612.69 ft**.

They differ by 268.9 ft, or 5.0%. They are different measurements — surveyed route length versus
distance-wheel travel — so some divergence is expected, though 5% is larger than the tool's stated
±1% locating accuracy. Map one onto the other however you judge best, say on the page which system
each displayed distance is in, and state the assumption you made. Do not present a single distance
figure as if both systems agreed on it.

## The route

Surveyed GPS centerline from the tool's inertial unit, cross-verified with a sonde tracker. Latitude
north, longitude west, distances in feet. The four named bends are the only direction changes called
out in the report; everything else is a survey interval.

```
designator          lat_N        lon_W    interval_ft   cumulative_ft
A: Launch Site   37.930667   122.399794            0             0.0
B                37.930275   122.399944          150           150.0
C                37.929881   122.400094          150           300.0
D                37.929489   122.400250          150           450.0
E                37.929097   122.400400          150           600.0
F                37.928703   122.400553          150           750.0
G                37.928311   122.400703          150           900.0
H                37.927919   122.400856          150         1,050.0
I: Bend 1        37.927769   122.400911         58.2         1,108.2
J                37.927528   122.401333        150.7         1,258.9
K                37.927289   122.401753          150         1,408.9
L                37.927042   122.402167          150         1,558.9
M                37.926808   122.402600          150         1,708.9
N                37.926569   122.403025          150         1,858.9
O                37.926328   122.403447          150         2,008.9
P                37.926089   122.403869          150         2,158.9
Q                37.925847   122.404294          150         2,308.9
R                37.925606   122.404717          150         2,458.9
S                37.925367   122.405139          150         2,608.9
T                37.925125   122.405561          150         2,758.9
U                37.924886   122.405986          150         2,908.9
V                37.924647   122.406408          150         3,058.9
W                37.924406   122.406828          150         3,208.9
X                37.924169   122.407253          150         3,358.9
Y                37.923928   122.407675          150         3,508.9
Z                37.923686   122.408097          150         3,658.9
AA               37.923447   122.408525          150         3,808.9
AB               37.923197   122.408939          150         3,958.9
AC.1: Bend 2     37.923067   122.409161           80         4,038.9
AC.2: Bend 3     37.923058   122.409253         25.8         4,064.7
AC               37.922989   122.409375         45.7         4,110.4
AD               37.922747   122.409800          150         4,260.4
AE               37.922506   122.410219          150         4,410.4
AF: Bend 4       37.922467   122.410253         18.2         4,428.6
AG               37.922789   122.410575          150         4,578.6
AH               37.923114   122.410894          150         4,728.6
AI               37.923439   122.411214          150         4,878.6
AJ               37.923761   122.411536          150         5,028.6
AK               37.924086   122.411856          150         5,178.6
AL               37.924411   122.412178          150         5,328.6
AM               37.924453   122.412217         15.2         5,343.8
```

Bend 4 at 4,428.6 ft is the turn: latitude decreases from A to AF and increases from AF to AM, so
AF is where the loop reverses and the return leg runs back roughly parallel to the outbound leg.
Launch and receive were the same physical site.

The report gives no elevation profile at any point, so there is no vertical data to draw on and none should be
invented; if the presentation needs a third dimension, derive it from the data rather than from
imagined terrain, and say what you did.

## The data

**Position anomalies by `abs_ft`. It is the only positional column that is reliable throughout.**

`gw` and `rel_ft` are the report's own labels and they are wrong in two places. **P-1** — the most
important record in the run — is listed at 41.30 ft past girth weld 135, but weld 135 is at 2,653.39
ft and P-1 is at 2,693.30 ft, so the true offset is 39.91 ft. The report repeats the 41.3 figure in
Appendix A, so it is the report's error, faithfully transcribed here rather than silently corrected.
**EML-72** is labelled `gw 162`, which resolves 21.60 ft away from its own absolute distance; the
weld it actually sits past is the one the report elsewhere calls GW-163. The other 113 records
resolve correctly.

The girth-weld list below carries distances only, no numbers, because the report's weld numbering
disagrees with itself in 19 places and a positional join would propagate that. Use the distances for
joint geometry and `abs_ft` for everything else.

```
GIRTH WELDS -- 286 welds, absolute distance in feet along the run, in order.
285 pipe joints; the gap between consecutive values is one joint.

      0.00     3.95     5.56    22.21    26.80    35.00    39.63    47.60    49.20    53.84
     65.84    87.09   113.25   139.29   181.13   228.04   274.33   291.21   294.58   315.96
    339.38   362.92   375.63   397.21   397.96   402.88   403.63   404.63   423.46   424.83
    447.52   452.23   452.90   454.10   455.35   460.02   477.69   481.96   483.13   485.54
    486.71   500.04   520.25   537.29   554.96   576.79   585.71   598.67   616.21   637.13
    682.54   722.84   768.17   812.33   856.65   899.63   937.73   951.32   990.78  1028.89
   1060.53  1103.96  1145.06  1151.89  1153.79  1156.89  1158.23  1180.17  1181.56  1182.89
   1185.48  1222.89  1225.77  1239.83  1266.30  1268.88  1270.88  1274.27  1290.98  1292.41
   1293.69  1296.01  1309.25  1351.89  1392.15  1433.65  1476.41  1519.13  1522.94  1547.73
   1572.79  1596.78  1621.59  1645.91  1670.00  1683.98  1725.89  1765.94  1792.97  1807.84
   1808.78  1809.84  1810.77  1818.65  1824.24  1827.25  1838.99  1839.55  1846.86  1847.35
   1888.45  1929.89  1969.90  1999.69  2027.75  2033.93  2075.10  2117.81  2159.76  2165.87
   2194.27  2214.27  2254.31  2294.93  2335.59  2352.52  2364.39  2405.99  2444.47  2489.13
   2532.52  2571.85  2606.15  2645.54  2653.39  2695.02  2720.46  2763.88  2804.61  2841.79
   2876.65  2920.30  2961.89  3002.59  3039.93  3083.11  3123.54  3145.25  3184.97  3210.08
   3248.47  3286.62  3298.11  3330.71  3362.60  3399.62  3434.78  3455.05  3486.47  3517.03
   3554.41  3592.38  3613.98  3652.53  3669.30  3687.10  3720.50  3732.77  3766.47  3798.05
   3828.00  3839.50  3874.99  3912.69  3930.02  3967.43  4005.06  4015.67  4029.77  4047.60
   4067.07  4083.71  4101.61  4120.93  4125.05  4126.90  4128.61  4132.40  4134.91  4135.84
   4152.20  4153.11  4168.07  4185.57  4202.12  4213.93  4215.58  4218.13  4235.96  4250.04
   4267.76  4269.82  4285.72  4303.61  4320.84  4339.41  4357.41  4374.22  4400.21  4431.66
   4447.20  4452.65  4471.49  4489.85  4508.65  4521.48  4551.31  4583.48  4596.57  4599.58
   4600.51  4610.60  4611.47  4612.65  4615.95  4620.95  4623.49  4624.40  4630.30  4633.55
   4652.07  4670.95  4689.46  4706.08  4724.35  4742.26  4774.16  4806.02  4836.23  4868.97
   4902.30  4935.33  4969.21  4998.09  5032.35  5047.54  5083.42  5120.43  5137.39  5150.73
   5170.74  5213.43  5255.34  5257.11  5296.66  5297.87  5307.58  5308.79  5319.38  5320.60
   5328.59  5344.27  5357.71  5358.99  5361.25  5361.87  5363.98  5378.99  5380.58  5385.48
   5396.18  5407.45  5418.50  5455.99  5512.73  5552.20  5562.29  5573.19  5583.79  5588.55
   5590.06  5604.82  5606.60  5608.08  5609.78  5612.69

ANOMALIES -- 115 records, in order of absolute distance.
id | gw = land-side girth weld number | abs_ft = absolute distance along run
rel_ft = distance past that girth weld | clock = orientation (0:00 = top of pipe,
increasing clockwise looking downstream toward the wharf) | type | wall_in = remaining
wall thickness at peak depth | loss_% = DERIVED, 1 - wall/nominal for that section
len_in / wid_in = extent of the metal loss | sec = which pipe size it sits in

id        gw    abs_ft  rel_ft  clock type       wall_in  loss_%   len_in   wid_in   sec
MD-1       1      1.62    1.62  12:00 ML_W_DENT    0.209    35.1    3.970    2.090   8in
IML-1     10     56.63    2.79   6:00 INT_ML       0.209    35.1  146.070   25.070   8in
IML-2     11     66.95    1.12   6:37 INT_ML       0.186    42.2  237.650    9.920   8in   <-- thinnest internal ML, tied with IML-5
IML-3     15    192.30   11.18   6:30 INT_ML       0.250    22.4    1.290    3.130   8in
IML-4     17    274.77    0.44   5:45 INT_ML       0.199    38.2  201.730   13.580   8in
IML-5     19    295.69    1.10   6:00 INT_ML       0.186    42.2  254.620   25.070   8in   <-- thinnest internal ML, tied with IML-2
IML-6     20    317.71    1.75   6:00 INT_ML       0.218    32.3  275.760   25.070   8in
IML-7     21    344.52    5.14   6:00 INT_ML       0.227    29.5  273.080   25.070   8in
IML-8     22    365.64    2.73   6:00 INT_ML       0.223    30.7  147.160   25.070   8in
IML-9     28    417.38   12.76   6:00 INT_ML       0.223    30.7  217.510   25.070   8in
IML-10    30    446.29   21.46   6:00 INT_ML       0.209    35.1  260.870   25.070   8in
IML-11    31    448.70    1.18   6:00 INT_ML       0.223    30.7   51.900   25.070   8in
EML-1     49    622.08    5.87  11:00 EXT_ML       0.213    23.9    2.570    0.790   6in
EML-2     49    630.50   14.29  11:22 EXT_ML       0.195    30.4    1.340    1.980   6in
EML-3     50    656.01   18.89   6:30 EXT_ML       0.195    30.4    5.140    1.590   6in
EML-4     51    715.74   33.20   6:07 EXT_ML       0.213    23.9    2.240    1.190   6in
EML-5     52    757.14   34.30   9:00 EXT_ML       0.199    28.9    3.020    2.380   6in
EML-6     52    758.08   35.24   5:57 EXT_ML       0.209    25.4    6.600    3.310   6in
EML-7     52    759.87   37.03   9:07 EXT_ML       0.213    23.9    2.240    1.980   6in
EML-8     52    764.95   42.11   6:45 EXT_ML       0.204    27.1   10.850    8.730   6in
EML-9     53    770.63    2.45   8:15 EXT_ML       0.209    25.4    1.120    1.590   6in
EML-10    53    772.56    4.39   7:15 EXT_ML       0.213    23.9    5.370    3.180   6in
EML-11    53    775.81    7.64  10:37 EXT_ML       0.209    25.4    2.800    1.190   6in
EML-12    53    780.98   12.81   6:45 EXT_ML       0.195    30.4   11.630    8.730   6in
EML-13    53    797.62   29.45   5:37 EXT_ML       0.181    35.4   11.960    7.540   6in
EML-14    53    806.72   38.55   7:07 EXT_ML       0.213    23.9    6.150    2.780   6in
EML-15    53    812.25   44.08   6:15 EXT_ML       0.186    33.6    9.390   10.320   6in
EML-16    54    812.36    0.03   5:30 EXT_ML       0.213    23.9    1.230   15.080   6in
EML-17    54    813.06    0.73   6:30 EXT_ML       0.209    25.4    4.470    4.760   6in
EML-18    54    814.91    2.58   6:52 EXT_ML       0.199    28.9    4.470    5.950   6in
EML-19    54    818.31    5.98  12:22 EXT_ML       0.204    27.1    1.790   17.070   6in
EML-20    54    818.91    6.58  10:22 EXT_ML       0.213    23.9    2.800    3.570   6in
EML-21    54    821.13    8.80  10:52 EXT_ML       0.209    25.4    5.590   13.890   6in
EML-22    54    839.60   27.27   6:52 EXT_ML       0.204    27.1    2.350    2.780   6in
EML-23    54    846.56   34.23   6:52 EXT_ML       0.190    32.1   13.190    7.540   6in
EML-24    55    869.40   12.75   6:37 EXT_ML       0.199    28.9    2.240    1.980   6in
EML-25    55    883.01   26.37   5:30 EXT_ML       0.213    23.9    2.120    1.590   6in
EML-26    55    893.07   36.42   5:45 EXT_ML       0.209    25.4   13.640    4.760   6in
EML-27    55    897.79   41.14   5:22 EXT_ML       0.204    27.1    2.240    2.780   6in
EML-28    56    899.72    0.09  12:52 EXT_ML       0.209    25.4    2.010   13.890   6in
EML-29    56    902.07    2.43   6:52 EXT_ML       0.209    25.4    4.250    3.570   6in
EML-30    56    923.10   23.47   6:07 EXT_ML       0.213    23.9    1.680    5.160   6in
EML-31    56    924.85   25.22   6:22 EXT_ML       0.186    33.6   14.650    5.950   6in
EML-32    59    991.93    1.15   5:30 EXT_ML       0.186    33.6    3.690    3.180   6in
EML-33    59    996.70    5.93   7:37 EXT_ML       0.209    25.4   13.420    8.340   6in
EML-34    59    997.74    6.96   5:07 EXT_ML       0.204    27.1   10.060    4.370   6in
EML-35    59   1001.85   11.07   6:07 EXT_ML       0.213    23.9   11.630    6.750   6in
EML-36    59   1004.27   13.49   5:07 EXT_ML       0.204    27.1    5.590    3.570   6in
EML-37    59   1004.79   14.01   5:07 EXT_ML       0.199    28.9    1.120    1.190   6in
EML-38    59   1009.94   19.16   5:37 EXT_ML       0.213    23.9    1.900    1.190   6in
EML-39    59   1011.30   20.52   7:52 EXT_ML       0.209    25.4    2.240    1.980   6in
EML-40    59   1013.16   22.38   5:30 EXT_ML       0.209    25.4    3.020    1.590   6in
EML-41    59   1013.73   22.95   5:37 EXT_ML       0.213    23.9    2.910    2.780   6in
EML-42    59   1014.22   23.44   3:45 EXT_ML       0.199    28.9    3.690    3.970   6in
EML-43    59   1018.44   27.66   7:00 EXT_ML       0.176    37.1    9.390    6.350   6in   <-- thinnest external ML, 3-way tie (EML-54, EML-71)
EML-44    59   1023.18   32.40   7:52 EXT_ML       0.204    27.1    3.020    2.780   6in
EML-45    59   1024.06   33.29   5:45 EXT_ML       0.204    27.1    4.700    2.380   6in
EML-46    59   1024.69   33.91   5:30 EXT_ML       0.213    23.9    1.680    1.590   6in
EML-47    59   1026.58   35.81   6:00 EXT_ML       0.209    25.4    4.810    3.180   6in
EML-48    60   1033.83    4.94   6:52 EXT_ML       0.199    28.9   10.060    6.750   6in
EML-49    60   1039.23   10.34   8:07 EXT_ML       0.190    32.1    4.580    3.570   6in
EML-50    60   1053.25   24.36   6:22 EXT_ML       0.181    35.4    3.350    1.980   6in
EML-51    60   1053.74   24.85   7:30 EXT_ML       0.204    27.1    6.040    4.760   6in
EML-52    63   1149.86    4.80  12:07 EXT_ML       0.190    32.1    2.800   16.280   6in
EML-53    63   1150.99    5.93   8:07 EXT_ML       0.209    25.4    2.570    2.780   6in
EML-54    71   1214.32   28.83   6:22 EXT_ML       0.176    37.1    2.460    1.190   6in   <-- thinnest external ML, 3-way tie
EML-55    72   1223.24    0.35   3:52 EXT_ML       0.190    32.1    2.460    2.780   6in
EML-56    72   1223.90    1.00  12:52 EXT_ML       0.186    33.6    4.700   14.690   6in
EML-57    73   1237.64   11.87   6:22 EXT_ML       0.181    35.4    1.680    3.570   6in
EML-58    74   1246.94    7.11   6:07 EXT_ML       0.186    33.6    0.890    1.190   6in
IML-12    90   1557.64    9.91   7:30 INT_ML       0.209    25.4  301.170   19.050   6in
EML-59    94   1653.88    7.98   6:52 EXT_ML       0.190    32.1   95.000    2.780   6in
EML-60   116   2047.82   13.88   6:15 EXT_ML       0.195    30.4   13.180    1.590   6in
MD-2     118   2158.56   40.75   3:22 ML_W_DENT    0.170    39.3    7.280    1.980   6in
EML-61   121   2198.80    4.54   7:07 EXT_ML       0.209    25.4    3.840    3.570   6in
EML-62   121   2201.48    7.21   7:00 EXT_ML       0.213    23.9    3.020    2.380   6in
EML-63   122   2233.14   18.88   6:07 EXT_ML       0.209    25.4    1.647    1.191   6in
EML-64   127   2391.05   26.66   7:30 EXT_ML       0.213    23.9    5.354    2.382   6in
EML-65   127   2395.83   31.44   6:07 EXT_ML       0.209    25.4    9.472    6.748   6in
EML-66   127   2396.45   32.06   7:45 EXT_ML       0.195    30.4    5.220    1.590   6in
EML-67   135   2676.58   23.20   6:45 EXT_ML       0.190    32.1    2.750    2.380   6in
EML-68   135   2689.61   36.23   6:22 EXT_ML       0.199    28.9   14.551    3.573   6in
EML-69   135   2692.41   39.02   6:15 EXT_ML       0.199    28.9    4.120    3.970   6in
P-1      135   2693.30   41.30   6:52 PITTING      0.060    78.6    2.400    1.200   6in   <-- LOWEST REMAINING WALL IN THE RUN (unique); rel_ft is wrong, see note above
EML-70   138   2764.78    0.90   6:37 EXT_ML       0.213    23.9    4.940    3.570   6in
EML-71   138   2790.17   26.29   7:45 EXT_ML       0.176    37.1    2.196    2.382   6in   <-- thinnest external ML, 3-way tie
EML-72   162   3616.11    2.13   6:37 EXT_ML       0.213    23.9    1.647    1.985   6in
EML-73   163   3616.38    2.40   6:37 EXT_ML       0.204    27.1    3.020    1.980   6in
EML-74   163   3640.57   26.59   7:07 EXT_ML       0.213    23.9    1.647    1.985   6in
MD-3     165   3671.07    1.77   9:30 ML_W_DENT    0.157    43.9    3.569    3.970   6in   <-- thinnest metal loss with dent
IML-13   168   3732.81    0.04   6:45 INT_ML       0.204    27.1    1.922    0.794   6in
MD-4     176   3995.06   27.63   8:00 ML_W_DENT    0.162    42.1    4.390    4.760   6in   <-- deepest DENT (0.104 in, per p5); pairs with D-1
D-1      176   3995.25   27.82   7:52 DENT         0.204    27.1    4.667    2.722   6in
EML-75   177   4009.82    4.76  11:37 EXT_ML       0.204    27.1  130.545    0.544   6in
D-2      192   4154.80    1.69   9:15 DENT         0.287    10.9   10.390    5.220   8in
IML-14   203   4303.60   17.87   6:22 INT_ML       0.213    33.9   27.420    4.700   8in
EML-76   213   4473.61    2.12   6:22 EXT_ML       0.227    29.5    2.059    1.567   8in
IML-15   213   4485.65   14.16   6:22 INT_ML       0.236    26.7    6.270    1.570   8in
IML-16   214   4497.35    7.51   6:15 INT_ML       0.241    25.2    2.060    3.130   8in
IML-17   214   4508.31   18.47   6:07 INT_ML       0.241    25.2    5.330    1.570   8in
IML-18   215   4520.32   11.66   6:07 INT_ML       0.241    25.2   11.980    1.570   8in
EML-77   216   4525.50    4.02   6:22 EXT_ML       0.217    32.6    2.250    2.610   8in
IML-19   222   4610.83    0.23   6:45 INT_ML       0.217    32.6    7.955    5.224   8in
IML-20   225   4617.52    1.57   6:07 INT_ML       0.231    28.3   14.507    6.791   8in
IML-21   230   4636.93    3.39   6:15 INT_ML       0.236    26.7    3.211    1.045   8in
EML-78   232   4687.53   16.58   6:45 EXT_ML       0.236    26.7    3.140    3.130   8in
IML-22   249   5146.33    8.94   5:45 INT_ML       0.231    28.3   23.483    3.134   8in
IML-23   250   5162.92   12.19   5:52 INT_ML       0.231    28.3   25.560    2.610   8in
MD-5     271   5400.95    4.76   6:00 ML_W_DENT    0.236    26.7    4.750    4.180   8in
MD-6     271   5404.20    8.02   6:00 ML_W_DENT    0.236    26.7    2.210    2.090   8in
MD-7     271   5406.14    9.95   5:45 ML_W_DENT    0.241    25.2    3.410    3.130   8in
EML-79   272   5415.62    8.16   6:00 EXT_ML       0.241    25.2    1.540    2.090   8in
EML-80   272   5416.13    8.68   6:22 EXT_ML       0.236    26.7    1.200    1.570   8in
MD-8     277   5563.96    1.68   5:45 ML_W_DENT    0.241    25.2    3.210    2.090   8in
MD-9     277   5565.87    3.58   6:30 ML_W_DENT    0.241    25.2    2.010    2.090   8in
```

Type codes: `INT_ML` internal metal loss · `EXT_ML` external metal loss · `ML_W_DENT` metal loss with
dent · `DENT` dent · `PITTING` pitting.

Note the shape of the data, because it is not uniform and the picture should not flatten it.

**The recurring 25.07 in width means the loss wraps the full bore, and this is the single most
important thing to get right in the picture.** 8-inch Sch 40 has an inside diameter of 7.981 in, so
its bore circumference is π × 7.981 = **25.073 in**. Eight records carry a width of exactly 25.07 in.
That is not "wide" — it is 360°, the entire inner surface, which is why eight separate records share
one identical value. The same check confirms it in the other pipe size: 6-inch Sch 40 bore
circumference is 19.054 in, and IML-12 — the one large internal record in the 6-inch section — is
listed at exactly 19.05 in wide. Do not leave an unaffected strip on these; there isn't one.

The **8-inch outbound section** is where that lives. It carries eleven internal metal-loss records,
nine of them running 146 to 276 inches long — that is 12 to 23 ft of continuous thinning per record.
These are long full-bore stretches of general internal wall loss, not spots, and rendering them as
small point defects would contradict the measured extents. Every one of the nine sits in the first
450 ft out of the launcher.

The **6-inch section** is the opposite character: many small external flaws, tightly clustered.
Girth weld 59 is a 38.11 ft joint carrying 16 anomalies inside a 34.65 ft span of it; girth welds
52–56 carry 27 more. Long stretches between clusters carry nothing at all.

**82% of anomalies (94 of 115) fall between 5:00 and 8:00 on the clock** — the bottom of the pipe.
That is where water and debris sit in a line that is not running full, and it is the single most
legible pattern in this dataset.

The 21 that fall outside that band are the exceptions worth being able to find: 17 external metal
loss, 3 metal-loss-with-dent, 1 dent. Two of the three deepest metal-loss-with-dent readings in the
run sit on the *sides* of the pipe rather than the bottom — MD-2 at 3:22 (0.170 in) and MD-3 at 9:30
(0.157 in) — which is a different damage mechanism from the bottom-of-pipe corrosion and reads
differently. And MD-4 (8:00) and D-1 (7:52) sit 0.19 ft apart at girth weld 176, with overlapping
lengths and widths. The report does not say they are the same feature, but two records 2.3 inches
apart whose extents overlap almost certainly describe one physical event seen twice. Treat them as
one, and say that you did.

## Branding

The page is branded for Steady Flux Technologies. Fetch **https://www.steadyflux.com/** and derive
the palette, typeface and visual tone from what is actually there rather than inventing a look. This
is a constraint, not a suggestion — but it fixes the ingredients only. How you compose with them is
entirely yours.
Their identity runs teal/cyan against dark neutrals, minimalist and industrial-technical.

Three fixed points:

- The company name is **Steady Flux Technologies** — two words, unhyphenated. That is the spelling on
  their own report letterhead. Not "Steady-Flux", not "SteadyFlux".
- The tool is the **WiLBR Intelligent Pig**, capitalized that way.
- **Do not reconstruct their wordmark.** Put a clearly-marked `[logo]` placeholder where it belongs,
  sized and positioned correctly, and leave it. Someone will drop the real asset in.

Refer to the asset by a generic physical descriptor — a looped 6-inch and 8-inch marine wharf line,
1.01 miles, carbon steel, Schedule 40. The operator, site and line designation are simply not
supplied to you; don't name them and don't invent substitutes. This is a presentation choice, not a
confidentiality rule: the surveyed route below is real and unmodified, so a map view is available to
you if you want one, and the page will be identifiable to anyone who looks the coordinates up. Build
accordingly and don't claim on the page that the asset is anonymous.

The report's own customer-supplied C-scan color coding is available if you want continuity with how
this customer already reads their data, though you are not obliged to use it:
0.350 in and above dark green · 0.300 in lighter green · 0.200 in yellow · 0.150 in orange ·
0.100 in and below dark red.

## Keeping it true

Short section, because the data has already been reconciled for you. Four things keep the picture
honest, and none of them costs you any visual ambition:

- **Use only the values in the data block.** Don't invent anomalies, readings, clock positions or
  defects. You have plenty of real drama; you don't need manufactured drama.
- **Clock positions are real, so use them.** The convention: **0:00 is the top of the pipe, angle
  increases clockwise looking downstream toward the wharf.** On the return leg "downstream" still
  means toward the wharf. Work out what that implies and be consistent — the bottom-of-pipe pattern
  is only legible if the orientation is right.
- **Between the 115 measured points, anything continuous you draw is your smoothing.** Draw it; a
  continuous surface is almost certainly a better picture than 115 dots. Just don't let the page
  imply it was measured.
- **Say nothing about fitness for service.** No allowable wall was supplied, MAOP was never
  calculated, and grade and SMYS are unknown, so "is this pipe safe" is a question this data cannot
  answer. Show condition; make no verdict.

Four things must appear somewhere on the page. Where and how is entirely your call, and they should
not turn into a wall of disclaimer text:

1. Provenance — inspection company, tool, report number and revision, inspection date.
2. That values between measured points are interpolated.
3. That percentages are against nominal wall. (The `loss_%` column is derived here as
   `1 − wall/nominal`; the report itself gives two conflicting definitions, so this needs stating.)
4. That no serviceability judgement is made.

Two findings worth knowing because they are *absences* that mean something rather than missing data:
ovality was measured and nothing exceeded the 5% reporting threshold — the pipe is round — and no
buckles or wrinkles were found anywhere. Separately, fouling degraded the ultrasonic signal in
places, so unmeasured pipe is not the same as healthy pipe; if your form implies a reading
everywhere, that's worth a word.

## Environment

Four facts about where this runs. They are stated because each fails *silently* — no error, just a
wrong result — and each has already cost someone a day. How you handle them is yours.

1. **A published Claude artifact blocks page-initiated downloads.** The page cannot save a file for a
   viewer: `Blob` + `<a download>` does nothing at all, with no error. A download control gated to
   localhost is fine; shipping a dead one that looks functional is worse than having none.
2. **`canvas.captureStream()` records canvas pixels and nothing else.** Any HTML element layered over
   the canvas — panels, captions, labels — is DOM, and will be absent from a recording. If the page
   records anything, this is the trap.
3. **A backgrounded tab throttles `requestAnimationFrame` to roughly 1 fps.** An animation that
   accumulates its own clock from per-frame deltas falls silently behind real time; in one measured
   case a capped 50 ms delta advanced a timeline 1.22 s across 14 s of wall time. This is a bug in
   ordinary use, not only during capture — switch tabs and come back, and the animation is far
   behind. Drive the timeline from wall-clock time.
4. **`preserveDrawingBuffer: true`** is required on the WebGL renderer if anything ever reads the
   canvas back — `drawImage` of a WebGL canvas without it returns blank.

Delivery constraints:

- **One self-contained HTML file**, no build step, no external requests at runtime. If you use
  three.js, use the **UMD build that defines a `THREE` global** and vendor it into the file — not the
  ESM build, not an import map, not a CDN `<script src>`. The artifact host wraps your file, so write
  the page content directly: no `<!DOCTYPE>`, `<html>`, `<head>` or `<body>` tags of your own, and put
  your `<title>` and `<style>` at the top of the file.
- The page must work in both light and dark viewer themes, or commit to one look and paint its own
  background explicitly. A transparent body borrows the host's theme and will look broken in one of
  them.
- Wrap your app code in a `try/catch` that paints the error and stack into the page. If something
  throws in a sandboxed artifact there is no console you can reach, and a blank dark page tells you
  nothing.

## Look at it, then make it better — at least twice

This is not a final check. It is how the page gets good, and it is the part most likely to be
skipped. **Budget real effort here.** A first render is a draft; nobody's first render is
impressive, including yours.

Run this loop at least twice, and more if it is still improving:

1. Open it in the Browser pane, screenshot it, read the console.
2. **Look at your own screenshot as a critic, not as its author.** Not "does it work" — *is it
   impressive?* Would someone stop on this? Crop in on regions you're unsure about rather than
   judging the whole frame at once; you see far more detail that way.
3. Ask the specific questions: Is the composition strong or is it just centred? Is there a focal
   point, and is it the right one? Does the type have hierarchy or is it all one size? Is the color
   doing work or is it decoration? Is anything overlapping, cramped, or floating unanchored? Is P-1
   — the 0.060 in pit, the most arresting fact in the dataset — findable by someone who doesn't know
   where to look?
4. Fix the weakest thing. Then look again.

Also let it run a full cycle to confirm it doesn't drift, stall, or end somewhere broken, and check
it at a narrow window as well as a wide one.

If after two passes it is working but unremarkable, that is the moment to make a bigger change
rather than to polish. Polishing a timid design produces a well-polished timid design.

## Done means all of these

Visual bar — the part that decides whether this succeeded:

- [ ] You would show this to someone. It is not merely correct.
- [ ] There is a clear focal point and a deliberate composition, not a centred default
- [ ] The 0.060 in pit lands as the event it is
- [ ] You ran the look-and-improve loop at least twice and the page changed because of it
- [ ] The form was chosen deliberately, and you said in a sentence why

Works:

- [ ] One HTML file, opens and runs, no external network requests, no console errors
- [ ] It rewards passive watching, and it covers all 5,600 ft and all 115 anomalies
- [ ] Geometry reconciles with the route and girth-weld tables; odometer-to-route mapping stated
- [ ] Internal versus external damage is distinguishable to a viewer
- [ ] Clock convention correct and consistent across the outbound and return legs
- [ ] Steady Flux Technologies branding from their live site; `[logo]` placeholder, not a rebuilt
      wordmark

True:

- [ ] Every rendered value traces to a row in the data block; nothing invented
- [ ] The four required statements appear somewhere, without becoming a wall of disclaimer text

## Not this

No gamification, no score, no missions, no achievement language. No marketing copy. No invented data,
no invented anomalies, no invented company names. No fabricated wordmark. No serviceability verdict.

And one last time, because it is the thing most likely to go wrong: **do not play it safe.** The
constraints above exist so that ambition stays truthful, not to talk you out of ambition. Make
something worth looking at.
