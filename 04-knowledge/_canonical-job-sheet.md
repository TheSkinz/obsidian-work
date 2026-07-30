---
type: job-sheet
job-number: <USA#####>
client: <Client name>
facility: <Client>-<City>-<ST>
  # ↑ JOIN KEY — must exactly match the facility-id in this site's _facility.md,
  #   same convention as the heater card's facility field.
source: <DSP##### — the specific quoted work-up this sheet was built from>
verified: <YYYY-MM-DD the tables were last checked against that work-up | never>
last-updated: <YYYY-MM-DD>
tags: [job-sheet, <Client>, <USA#####>]
---

<!--
CANONICAL EXEMPLAR — NOT A LIVE JOB SHEET.
This file is the schema authority for all job sheets in the vault. It is never a record of an
actual job; it exists to stay stable while live job sheets mutate. templates/_job-sheet-template.md
derives its structure FROM this file.

STATUS: DRAFT — validated against TWO instances (USA26038, July 2026; USA26040, August 2026).
The second won bid FORCED a change rather than confirming the first shape, which is what this
exemplar was waiting to find out. USA26040 (Jesse, 2026-07-30) established that the job sheet is
an INTERNAL crew document and collapsed the section list from nine blocks to six. USA26038's own
sheet predates the change and was deliberately left unretrofitted — it is a completed job and a
historical record.

Section shape is now better evidenced but still not settled; a third instance may move it again.

THE JOB SHEET IS INTERNAL (core rule, USA26040):
  It goes to the crew, never to the customer. Therefore it carries NO rates, NO markup percentage,
  and NO quoted dollar totals — those live on the quote and, after execution, the ticket breakdown.
  It also carries no customer-proposal boilerplate: verification-of-cleanliness narrative and
  customer-scope readiness checklists were both cut. The crew are experts; the sheet holds what
  they cannot know without being told, and nothing else.

OMISSION RULES (USA26040 — each one earned by a deletion):
  - Don't state what is always true. Every job is a mechanical decoke; saying so is noise.
  - Don't restate what another field already says. The C↔D jumper detail came off because Mode
    already reads "double mode."
  - Don't state mutually exclusive alternatives as if both apply. A given launcher group is at
    grade OR elevated, never both — say it once, inside Launchers. (Different groups on the same
    job may sit at different elevations; see GRADE vs ELEVATION below.)
  - Don't attribute a task to a shift. Both shifts are capable of every task, so which shift
    catches smart pigging is not information.
  - Don't print a computed value that looks like an orderable one. See the Final Pigs rule.

WHAT A JOB SHEET IS (the fact/time wall — core principle):
  A job sheet is STATIC. It is created once, at bid-win, from the quoted work-up, and it holds
  the QUOTE's resource plan — not what actually happened. Actuals, timeline, and real crew belong
  on the job report; accumulated heater facts belong on the heater card. The quote's plan and the
  mobilized reality routinely differ (USA26038 quoted 12 people, sent 10) and that gap is a job
  report finding, never a correction to the job sheet. A job sheet edited to match reality has
  destroyed the only record of what was sold.

  See quote-lifecycle.md for the three-document model (job sheet / heater card / job report) and
  where each is created in the lifecycle.

PROVENANCE (`source` / `verified`): tools/vault_lint.py's OP-FRONTMATTER rule requires both on
every operational note, and for a job sheet they carry real meaning rather than ceremony. `source`
is the specific DSP##### work-up the billing tables were built from — a sheet built from a
superseded quote revision is a live failure mode, and the job number alone does not identify which
revision was used. `verified` is the date the tables were last checked against that work-up. Do not
fill either with a placeholder to silence the lint; an honest warning is worth more than a false
green. (USA26038's own sheet carries neither field, and its DSP# is not recorded anywhere in the
vault as of 2026-07-18 — it stays flagged in the provenance backfill backlog until someone supplies it.)

LOCATION AND NAMING (follows the USA26038 precedent):
  02-facilities/<Client>/<City-ST>/<USA#####>-job-sheet.md — alongside the heater cards for the
  same site, flat, no per-job subfolder. The printable pair (.html source, .pdf render) sits
  beside it under the same basename.
-->

# <USA#####> — <Client> <Facility Name>, <City>, <ST>

> Vault-native copy of the printable crew job sheet. The canonical printable version is
> `<USA#####>-job-sheet.pdf` (rendered from `<USA#####>-job-sheet.html`). A job sheet is static —
> created at bid-win from the quoted work-up. Actuals and timeline live on the job report, never here.

---

## Project Details

<!--
Job-level identity. Everything here is fixed at bid-win.

SCOPE (revised USA26040): heater tag + service, plus the customer elections that change how the
job runs — filtration and smart pigging. Nothing else. Do NOT write "mechanical decoke"; it is
always a mechanical decoke. There is NO separate "Heaters" row — Scope already names them, and
carrying both duplicates the same fact. Filtration and smart pigging are customer elections (Job
Options decisions on the heater card), so state them as elected scope, never as heater specs.

MODE: the field is labeled `Mode`, not `Pigging Mode` — on a pigging job sheet the qualifier is
redundant. Carries the pig path, e.g. "Double mode, 2-pass (A→C→jumper→D→B)".

Runs two field/value pairs per row to use the page width.
-->

| Field | Value | Field | Value |
|---|---|---|---|
| Scope | <TAG + service — w/ Filtration + Smart Pigging> | Job # | <USA#####> |
| Facility | <Facility name — City, ST> | Quote | <DSP#####> |
| Mode | <e.g. Double mode, 2-pass (A→C→jumper→D→B)> | PO # | <PO or TBD> |
| Project Type | <Emergency turnaround project / Planned outage — Month Year> | PM | <name> |
| Lodging | <hotel> | Training | <e.g. Site specific> |

---

## Schedule

<!--
Milestones plus the quoted task split. NO per-phase clock times — assigning a phase to a time
implies assigning it to a shift, which the omission rules forbid.
-->

| Mobilization | Rig-In / Start | Projected Complete |
|---|---|---|
| | | |

| Rig-In | Pig | Smart Pig | Rig-Out | Total |
|---|---|---|---|---|
| | | | | **<N> hrs** |

<N> days / <N> shifts.

---

## Crew & Labor

<!--
MERGED SECTION (USA26040, replacing "Crew Assignment" + the labor half of "Billing Reference").
Those two tables were the same rows described twice — who, then how many hours. One table now
carries both.

THE FOUR NUMERIC COLUMNS — this is where the old format broke, so read carefully:
  - Qty  = the QUOTED resource plan. This is the billing basis. It never changes to match who
           actually showed up.
  - Mob  = ACTUAL headcount mobilizing. This is how the fact/time wall lives inside one table:
           without it, a row reads "Qty 2" beside a single name and contradicts itself on its
           face. Mob is NEVER used in a billing figure — it is there so the sheet can name real
           people without lying about what was sold.
  - Ea. Hrs = per-person shift hours.
  - Man-Hrs = Qty × Ea. Hrs, COMBINED man-hours. Historically the single easiest line to get
           wrong, which is exactly why Ea. is now printed beside it — the math is checkable on
           the page instead of having to be recomputed from the quote.

CREW STRUCTURE (Jesse, 2026-07-30): a 5-man crew at 3 dayshift / 2 nightshift is NORMAL. Division
headcount is fixed; six is preferred when six is quoted, but when a sixth isn't available the
shifts restructure 3/2 and that is standard practice, NOT a variance. Do not flag it as one, and
do not adjust Qty to match — Mob carries it.

PM BILLING (Jesse, 2026-07-30): the person running the project is ALWAYS on dayshift, and bills
as either a billable Project Manager or the Day Supervisor. Which one is decided by the Equipment
and Manpower Allocation block at the bottom of that job's execution-plan page — that block is the
authoritative billable list. No PM row there means no PM is billed, and the person running the
job takes a supervisor slot. Read it per job; it is not a default either way.

PER DIEM bills per DAY and rides the total row. Headcount excludes a billable PM when one exists.
DEF bills per SHIFT — carry it in the note beneath, not as a table row.

Operator names are commonly left BLANK at bid-win for the field to fill in; name the pool in the
note instead. Supervisors are named.
-->

| Shift | Role | Assigned | Qty | Mob | Ea. Hrs | Man-Hrs |
|---|---|---|---|---|---|---|
| Day | Supervisor | <name> | 1 | | <hrs> | |
| Day | Operator | | <n> | | <hrs> | <Qty × Ea.> |
| Night | Supervisor | <name> | 1 | | <hrs> | |
| Night | Operator | | <n> | | <hrs> | <Qty × Ea.> |
| **Per Diem — <n> day × <n> days + <n> night × <n> days = <N> days** | | | **<total>** | **<total>** | | **<total man-hrs>** |

**Qty** = quoted resource plan (billing basis). **Mob** = actual headcount, <n> dayshift / <n> nightshift. Operator pool: <names> — split assigned in the field. PM runs dayshift.

<Note the PM billing resolution for this job and which allocation block it came from.>

---

## Equipment

<!--
MERGED SECTION (USA26040). Previously the same units appeared twice — once as billable line items
and once as a physical mobilization list. One table now carries billable identity, the actual
asset, and its status per row, which also makes the billable/non-billable split visible where two
separate tables hid it.

BILLABLE ROWS ONLY. A non-billable row (e.g. a Glider moving between yards) does not get a table
row; if it carries a live action item, put it in the note beneath.

Hrs = the heater's total pumper hours, × Qty. Filter Unit appears only when filtration was
elected — omit the row entirely on non-filtered jobs rather than carrying it at zero.

Where more vehicles are on site than bill, say so inline: "F150 · Chevrolet 1500 · F350 (2 of 3
bill)". The crew-truck pass allowance is a quote term and is worth knowing.
-->

| Qty | Billable As | Asset | Hrs | Status |
|---|---|---|---|---|
| 1 | Trimax Pumper | <Trimax #> | <total> | <Staged / mobilizing from …> |
| 1 | Support Unit | <Support #> | <total> | |
| 1 | Filter Unit | <Press #> | <total> | |
| <n> | Crew Truck | <vehicles> | <total> | |

DEF <n> shifts. <Gate passes, non-billable movements, and other pre-mob action items.>

---

## <TAG> — Coil Data & Connections

<!--
COMPACT reference only — the crew needs enough to work from, not the full card. The heater card
(02-facilities/.../<TAG>.md) remains the single source of truth for tube geometry; this is a
convenience copy of what matters at the launcher, and it should be copied FROM the card, never
authored here and back-filled later.

Metallurgy is a COLUMN in the table (per-section, matching the heater card) — not prose.

CONNECTIONS (USA26040) fold into this block rather than standing alone, and are formatted as a
BORDERED BLOCK beneath the table — NOT a second table, which read badly when tried. Two tiers,
because hard specs and prose caveats fight each other when run together inline:
  1. A spec strip: the four values a crew reaches for, set large and bold.
  2. Labeled note lines beneath for the caveats.

TERMINOLOGY (Jesse, 2026-07-30): they are INLETS and OUTLETS. Never "nozzles" — not the term used
here. (A source drawing literally named a "nozzle sheet" is transcribed as-is; that is a document
title, not our word for the connection.)

FINAL PIGS — label it "Final Pigs", not "Pig Sizes", and never write "final foam". Print only
ORDERABLE sizes, e.g. 6.0" / 6.125". NEVER print the heater card's "Max pig OD" figure: that is a
computed sizing-rule cap (governing ID + 0.250) and resolves to values like 6.011" that no pig is
made in. The card is correct to record it as a rule cap; it must not propagate to a crew sheet
where it reads as a size to grab.

GRADE vs ELEVATION: elevation belongs INSIDE the Launchers spec value ("4 × 6" · at grade") and
never gets a line of its own. Corrected 2026-07-30 — the rule was first written as "at grade OR on
scaffolding, never both," which is wrong at the job level. A single launcher GROUP is at one
elevation, but one job can carry groups at different ones: USA26038 ran "convection (4) 4"
launchers, 10' from grade; radiant (2) 4" launchers at grade." When groups differ, say both, each
with its own elevation.

SCAFFOLD IS NOT AN ELEVATION. Customer-scope scaffold for bolting up inlet/outlet spools at
elevated nozzles says nothing about where OUR launcher sits, and the two get confused constantly.
H-2421 is the worked example: the heater card records "scaffold req'd at A, B, C, D" (HF Sinclair's
spool work, up at the nozzles) while the launchers themselves sit at grade, fed by risers — the
drawing markup reads "PIG LAUNCHER PIPING — CONNECT TO A,B (RUN DOWN TO GRADE)". Both are true.
Launchers reports OUR position; customer scaffold scope does not belong on the job sheet at all.
-->

| Section | Coils | Pipe OD | Wall | Pipe ID | Tube Lgth | Tubes/Coil | Ft/Section | Metallurgy |
|---|---|---|---|---|---|---|---|---|
| Convection | | | | | | | | |
| Radiant | | | | | | | | |

> **Inlets <A / B>** <size + rating + face> · **Outlets <C / D>** <size + rating + face> · **Launchers** <n × size> · <at grade> · **Final Pigs** <orderable sizes>
>
> **Adapters** — <required or not; what the launcher piping terminates at vs. the connection rating; who fabricates; bolt-up and wrench sizes>
> **Water** — <source>
> **Coil** — <heater total effective footage; crossover ID and whether a reducer exists>

<!-- In the HTML printable this is `.connbox`: 1px border, 4px #FCC30A left rule, a `.spec-strip`
     of four `.spec` blocks (small uppercase label over a 9.2pt bold value), then `.cline` rows
     with a right-aligned 52px label gutter. -->

<!-- After the last heater's block: -->
Full tube geometry, config rollup, and pig spec history: [[<TAG>]], [[<TAG>]].

---

## Carry-Forward Notes — Prior Decoke (<USA#####>, <Month Year>)

<!--
CONDITIONAL SECTION — include only when the heater(s) have prior job history to carry forward.
On a first-time heater there is nothing to carry and the section is omitted entirely rather than
left as an empty shell (same rule as the heater card's stainless warning block).

Source is the prior job's Field Notes on the heater card. Every row is actionable: what to watch
for, and what to do about it. "Confirm still in effect" is a legitimate Action — conditions change
between turnarounds and the crew should verify rather than assume.
-->

| Heater | Watch For | Action |
|---|---|---|
| <TAG> | <what went wrong or slowed the prior job> | <what to do on arrival> |
| Both | <cross-heater or customer-procedure item> | <action> |

---

## Notes

Printable deliverable: `<USA#####>-job-sheet.pdf` (source `<USA#####>-job-sheet.html`), alongside
this file. Billing tables reflect the quoted work-up (<N>-person resource plan). Actual mobilized
crew and timeline are recorded on the job report, not here.

<!--
RENDER PIPELINE (still not tooled, but the command is known). Produced from the HTML via headless
Chrome; this exact invocation produced USA26040 on 2026-07-30, one page, Letter:

  "/c/Program Files/Google/Chrome/Application/chrome.exe" --headless --disable-gpu \
    --no-pdf-header-footer --print-to-pdf="<abs path>.pdf" "file:///<abs path>.html"

Verify with `pdfinfo <pdf> | grep Pages` — ONE PAGE is the design target, and the section merges
in this exemplar exist largely to hold that line.

A tools/render_job_sheet.py wrapper was scoped and explicitly deferred on 2026-07-18. Two manual
runs in, it is still not friction — leave it deferred.
See 06-insights/2026-07-18-idea-research-job-sheet-type-formalization.md.

PAGE BUDGET: Letter portrait, 0.55in × 0.6in margins ≈ 9.4in usable height. Six blocks fit with
room to spare; nine did not. If a future section is proposed, something else comes off.

BRAND: gold is #FCC30A. RESOLVED 2026-07-30 against the live usadebusk.com stylesheet, which
carries #FCC30A throughout (nav hover, header links, hero gradient) and #F2A900 not once. The
earlier #F2A900 in the printables was never a brand color; usadebusk-core was right all along.
USA26040's printable was corrected. USA26038's was deliberately NOT — completed job, historical
record — so the two printables differ in gold on purpose. That is not drift; do not "fix" it.
-->

<!--
SECTIONS REMOVED 2026-07-30 (USA26040) — do not reintroduce without a reason that survives the
omission rules at the top of this file:
  - Quoted Value / dollar totals — internal document, no money.
  - Verification of Pass Cleanliness — customer-proposal boilerplate; the crew knows the process.
  - Site Readiness / customer-scope checklist — the part that mattered (connection sizes and
    locations) moved into Coil Data & Connections, where it belongs as a connection fact.
  - Project Details "Heaters" row — duplicated Scope.
  - Standalone Crew Assignment and Equipment Mobilized — merged, see above.
-->
