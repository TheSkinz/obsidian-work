# Skill — Project Report

**Owner Bot:** Scribe
**Source:** ported from usadebusk-fieldpm, references/report-structure.md. That file is the
authority; this is a working port for a Bot that has no generator script.

## Known deviation, read this first

In the vault, all tables in this document are produced by `scripts/extract_ticket_breakdown.py`
and the standing rule is **do not hand-tally**. Grok Bot has no such script. Anything you produce
here is therefore hand-tallied, which the source skill forbids, so every number you put in a table
must be marked as hand-tallied and shown with its arithmetic. Treat that as a defect to be checked
by Jesse, not as an equivalent output.

## What this is

A branded, customer-facing document delivered at project completion. It goes to the customer
contact and to internal SharePoint. **Output is .docx built with `python-docx`** — there is no
built-in Word Documents skill on this platform and no document plugin in the marketplace; an earlier
version of this line said otherwise and was wrong. The interpreter is the venv at
`/workspace/.venv/bin/python`; if it is missing, rebuild it with `python3 -m venv /workspace/.venv`
then `/workspace/.venv/bin/pip install python-docx`. A bare `pip install` fails under PEP 668.
**Operational only — no financial or change-order data.**

Header on every page: **the USADebusk logo** left, then the right block reading
`JR-DCK-<FAC><JOB> | REV <n>` over `<service> | <N> Heaters | <client>`. Doc id is JR-DCK plus
facility code plus job number, e.g. JR-DCK-HFS26038. REV starts at 0. Footer:
`USADebusk | Deer Park, TX | usadebusk.com` left, page number right. **No cover page.**

**Fonts, colours, table fills and the logo come from the Brand Standards skill. Read it before you
build.** Every "amber" in this file means the gold defined there, and the logo path and sizing are
there too. **The values are not restated here on purpose** — one copy, one place to change.

**Set the table styling explicitly on every table.** python-docx applies a blue default if you do
not, and that blue shipped in the 2026-09-07 build.

**The header belongs in the header, and nowhere else.** Build it as a real `section.header` part.
Do not also describe it in the body — a delivered report that opens with a paragraph narrating its
own running header and doc-id is the structural duplication this skill's verbosity rule exists to
prevent, and it reads as a draft note left in the file.

**Pagination — set these four properties or the document breaks badly.** Two are usually right by
default and two are usually missing; the 2026-09-07 build had `cantSplit` on 40 rows and `keepLines`
on 84 paragraphs, but zero `tblHeader` and zero `keepNext`, which produced a "Project Details"
heading alone at the foot of page 1 and an "Unresolved questions" heading alone at the foot of
page 4.

- **`tblHeader` on every table's first row** — `tr.tblHeaderProperty`, so a table that crosses a page
  repeats its column headings. Without it the continuation is unlabelled columns of data.
- **`keepNext` on every heading and on any paragraph immediately before a table** —
  `paragraph.paragraph_format.keep_with_next = True`. This is what stops a heading stranding itself
  at the bottom of a page with its content overleaf.
- `cantSplit` on rows and `keepLines` on paragraphs, which the build already does.

**No blank gaps, no orphan pages, no heading or section spilling one line onto a new page.** This is
a standing correction, not a preference — check the rendered pagination before calling a build done.

**The document carries report content and nothing else. Build apparatus goes in the chat reply.**
Ruled 2026-09-07 after a build shipped roughly two of five pages of scaffolding. **Never put any of
this in the `.docx`:** the hand-tally notice, "not built in this draft" placeholder sections,
`Pigs Used — not built`, the "Conscious checks" block, `[Awaiting Jesse …]` bracketed callouts, and
the four closing sections (Verified facts, Assumptions, Actions completed, Unresolved questions).

Say all of it in the chat message instead, where it is just as visible to Jesse and costs him
nothing to read. **This does not weaken the four-section reporting rule** — it moves it out of the
deliverable and into the reply, which is where it was always meant to be read.

**A section you could not build is simply absent from the document.** Do not write a heading that
announces its own emptiness — that is the never-document-absent-scope rule applied to your own
output. Tell Jesse in chat what you could not build and why, and leave the file clean.

**This still means one file, not two.** The deliverable is the only artifact. Nothing gets a
companion build-notes document — the wrong file gets uploaded and looks correct.

## Section sequence

### 1. Title block and Project Information (page 1)

Amber eyebrow driven by condition and scope, e.g. EMERGENCY MECHANICAL DECOKE. Title is
`[Facility] — [Heater Tags] [Scope]`. Subtitle is `Project Report | USADebusk | [Facility] —
[City, ST]`.

Two four-column project tables: **PROJECT NO.** / FACILITY / EXECUTION / PROJECT MANAGER, then
PO NO. / SCOPE / HEATERS / DURATION. **The column header is PROJECT NO., not JOB NO.** — it is
customer-facing and it is the last place "Job" survived in a printed heading after the rest of the
document moved to "Project". A case-sensitive check for "Job" will not find it.

KPI band, four stats, large number over caption: heaters cleaned, operating hours, pigs run,
smart-pig inspections. **Operating hours = rig + pig + smart-pig. Stand-by is excluded** — it
appears only in the Stand-By Summary.

Then a Project Information header and three tables. Customer Details: facility, address, project and
PO number, contact — **the row label is `Project & PO #`, not `Job & PO #`**. It is the one place
"Job" survived as a customer-facing label after the rest of the document was moved to "Project". Project Details: scope, execution date range with day count, heater tags,
equipment list. Crew Details: project manager, shift lead split day and night, dayshift names,
nightshift names.

The section is called Project Information, not Job Summary. "Project" reads more appropriate than
"Job" (Jesse, 2026-09-02) and that applies throughout the document.

### 2. Project Duration, Stand-By, Pigs (page 2)

**PROJECT DURATION** — per-heater rows carry PIG and SMART PIG; rigging is pooled to a single
project line; then a TOTAL row. Columns: SCOPE, UNIT, PIG, SMART PIG, SUBTOTAL.

Rig hours are pooled at project level — rig-in plus rig-out plus rig-over across all units —
because rigging is fungible, same rate and same task, so a per-heater rig split is an allocation
convention rather than a measured fact. PIG and SMART are allocated per heater from the
pumper-to-heater assignment. Superscript footnotes below the table carry delays, delayed release,
or as-built reconfiguration, all PM-supplied.

**STAND-BY SUMMARY** — columns CAUSE, DATES, HOURS, plus a TOTAL row. Open with one sentence
saying stand-by is on-site time the units were not actively pigging, cause taken from the daily
service receipts. Close with a combined line: operating hours plus stand-by hours equals total
pumping-unit hours.

**PIGS USED** — one full-width table across every size, aggregated over all shifts and all
heaters, with the legend note beneath it. Columns: SIZE, TC, HR, FOAM, SWAB or SWAB/HC, TOTAL.
Legend: TC = pin, HR = Hell Razor, Foam = pin and gauge foam, Swab = dewatering swab, HC =
honeycomb gauge. The last column header follows the data — SWAB where the job ran no honeycomb
gauges, SWAB/HC where it did. Keep the table together so it moves whole to the next page rather
than breaking mid-table; one table fits 26 sizes with a third of a page to spare, and the 2-up
split that used to be here was measured and found to break anyway.

### 3. Heater Data and Results (page 3)

Per heater: amber sub-header `[H-tag] — [Heater Name]`, a data table, a bold-lead narrative
paragraph, then an amber callout box for the critical note.

Table fields: number of passes as-built; total footage with looped pig path if applicable;
convection tube ID with OD, wall and schedule; radiant tube ID with OD and wall plus outlet
section if any; metallurgy per section and never a single card-level value; return bends;
inlet and outlet flange count, size, rating and location; smart pigging yes with vendor or no.

The narrative is PM-written: deposit severity and location, pass buy-off, key field events. The
bold lead-in defaults to **Decoking Analysis:**. The amber callout is the PM's critical note —
dewatering difficulty, restrictions and the like. Where as-built pass configuration differed from
the quoted plan, the PM confirms it here.

### 4. Flow Tests (page 4)

One table per pass-pair, amber sub-header `[H-tag] — [Pass label] (Before | After)`. GPM held
constant in the left column, before and after side by side, delta PSI last. Columns: GPM, BEFORE
RPM, BEFORE PSI, AFTER RPM, AFTER PSI, delta PSI.

Flow data comes from the field Decoking Data Sheet, which is separate from the service receipts
and arrives as a PDF or image to transcribe. **Never fabricate a missing AFTER column.** Render
what exists, mark the gaps, and do not curve-fit to a realistic-looking result.

### 5. Images (page 5)

Pig-progression photos and any pass-visualization diagram. The PM attaches these at report time.

### 6. Project Summary and Close (page 6)

Project Summary is PM prose. Project Close is PM prose: heaters returned, decon and demob date,
customer thanks. Then the closing block — PM name, USADebusk, Project Manager, cell, email.

## Prose rules

These govern every PM-written string: the per-heater narrative, the amber callout, the Project
Summary and the Project Close. The tables are mechanical; the words are not.

**What does not belong in the prose.** Do not restate what the customer owns — pass count,
footage, tube IDs and metallurgy are already in the data table and in the reader's own drawings,
so name a dimension only where it carries a finding. Do not narrate the SOP; report what happened,
not how the work is done. Do not describe the report inside the report. Equipment-level
granularity only where it carries a finding: "2-inch pigs returned badly damaged against a
3.068-inch radiant ID" earns its place because the damage is the evidence, "TC pigs were run" does
not. No invented phrasing — if a phrase is not in the glossary and is not plain English, it is a
coinage, so cut it.

**Never document the absence of something that was never in scope.** If filtration was never sold
or mobilized, the report is silent about filtration. And the corollary, which is where this
actually gets broken: an observation nobody made is absent from the report, not reported as
absent. If no localized hard spot was recorded, say nothing about hard spots — do not say none was
found. Never fill a heading because the template has one.

**The Project Summary is two moves, and the second is optional.** Move one, always: scope
executed — what was performed, for whom, when, and the equipment arrangement that made it
possible. Move two, only where it exists: what the job found that the customer did not already
know, as **one sentence, a pointer not a paragraph**, because the finding itself already lives in
the per-heater narrative. No deviation means no second paragraph. A job that ran to plan has a
one-paragraph summary and that is a complete summary, not a thin one.

That rule exists because the verbosity was structural duplication, not word choice. On one
delivered report roughly 155 of 258 summary words already lived elsewhere in the same document,
and its stand-by paragraph named two causes where its own table carried four. Back-tested across
three reports, this shape cuts 27 to 54 percent.

**The cleanliness result and its basis go in the per-heater narrative, not the summary.** State
the three completion criteria together, plus the final pig size reached against that section's
Clean ID, plus smart-pig confirmation where the job carried one. Each criterion alone can be
satisfied by a coil that is not clean, so naming why they are jointly sufficient is a stronger
position than leaving the question for the customer to raise.

**Terminology.** The glossary at 04-knowledge/manual/17-glossary.md is the single authority. Two
rules carry most of the weight. First, finding language only — expectation language is what we
predicted going in (standard coke, hard coke, pitch), finding language is what we observed coming
out (final pig size, localized restriction, residual fouling, return duration, recovered fragments,
pig condition). A report states findings; it may note what was expected and how the job differed,
never present an expectation as an observation. Second, never assert what a pig run cannot
evidence — our evidence is hydraulic and mechanical, so deposit composition, morphology, formation
mechanism and metallurgical condition are outside it. Those come from the customer's inspection
data or a lab result, cited as theirs, or they are not stated. Fouling and deposit are the default
nouns; coke only where composition was actually established.

Difficulty is written as effort, never as a material property: progression steps, sizes that
stalled, hours per pass. A percentage needs a measurement behind it — "90% clean" is not a
finding, a final pig size is, and Clean ID is not that number.

The reader is a reliability engineer, process engineer or metallurgist who owns the asset. Write
for someone who knows the plant better than we do and was not standing at the launcher.

## Safety boundaries

Mark every hand-tallied figure as hand-tallied and show its arithmetic. Never invent a flow-test
value. Draft prose is a placeholder for the PM to replace, and say so. The finished file goes to
/workspace/out and nowhere else — you do not send it.
