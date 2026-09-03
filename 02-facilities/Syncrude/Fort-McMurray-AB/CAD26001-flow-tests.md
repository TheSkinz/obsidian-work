---
type: flow-test-record
job-number: CAD26001
client: Syncrude
facility: Syncrude-Fort-McMurray-AB
heaters: [7-1-F-1]
source: 4 scanned field sheets — `OneDrive/USADeBusk/Facilities/Syncrude/Syncrude Fort McMurray AB/Jobs/CAD26001 Syncrude Fort McMurray/CAD26001 7-1F-1 Flow Test Sheets.pdf` (Jesse-supplied 2026-09-01; moved out of `Downloads/` and renamed 2026-09-02 — see Source Files on [[CAD26001-job-sheet]])
verified: 2026-09-02
passes-3-4-status: placeholder-not-measured
passes-3-4-note: >
  The scanned passes 3+4 sheet is a mistaken copy that the crew scrapped (Jesse, 2026-09-02);
  its readings are unusable. The figures carried in the body are the mean of the other three
  circuits, standing in until the official copy is located. NOT a measurement — do not render
  them into a customer deliverable, and do not feed them to the job-report generator's
  Verification of Pass Cleanliness section, as measured results. As-scanned values preserved
  under Provenance.
tags: [flow-test, Syncrude, Fort-McMurray, CAD26001]
---

# CAD26001 — Flow Tests

Transcribed 2026-09-02 from the four field sheets of the August 2026 decoke of [[7-1-F-1]]. Companion to
[[CAD26001-job-sheet]]. This note is the structured source — read it instead of re-reading the scans. The
rest of the job data (durations, pig usage, receipts) had not arrived when this was written; nothing here
has been carried onto the heater card yet.

**The sheets cover all eight coils as four looped circuits — passes 1+2, 3+4, 5+6, 7+8.** That is the
looping plan executing as designed, and it is the first field evidence of it. Trimax 5 ran passes 1+2 off
its LEFT discharge and passes 7+8 off RIGHT — two looped circuits from one rig at once, which is the
double-mode arrangement the CAD26001 build-up assumed and which CAD25004 never tested (there, the one
looped pair had a Trimax to itself).

Each sheet records a four-step GPM ladder with RPM and PSI before and after the decoke. **GPM is the
controlled constant** (`sop-formatting-standard.md` §7) — the ladder is read down the same 800/700/600/500
steps on both sides, and **the drop in PSI at a matched GPM step is the measurement.** RPM is only the
pump speed needed to hold that step — it is recorded because the sheet has a column for it, and it is not
the result (Jesse, 2026-09-02). Read the Δ PSI column; the RPM columns are transcribed for completeness
and carry no weight. Δ PSI is computed (before − after), **never fabricated**.

The sheet carries two PSI columns, PIG FORCE and DIGITAL. **They are the same reading** and should agree
on every project; techs sometimes enter a value under the wrong one (Jesse, 2026-09-02). Which column a
given sheet used is not meaningful and is not tracked here. The passes 7+8 sheet is the one place both
were filled, and they agree within 5 PSI on readings of 135–255 — which is the point. Why the template
carries both columns is not recorded.

Footage was left blank on all four sheets. Pipe ID is recorded on the sheets as 6" (passes 1+2, 5+6) and
6.026" (passes 7+8); the heater's ID of record is **6.065"** and that is what the [[pig-tracker]] circuits
use — the 6.026" entry is a field-sheet slip, not a correction. Note also that the flow-test ladder runs
500–800 GPM, above the 448–559 GPM pigging band the tracker targets. That is expected: flow tests are
water-only with no pig in the circuit, and 800 GPM must never be read back as a pigging rate.

Smart pigging: Quest, per the sheets. Filtration: none.

## 7-1 F-1 — Passes 1 + 2 (looped)

2026-08-28 · Trimax 5, LEFT discharge · pipe ID 6" · scan page 2 · test operator pre Peter Campbell, post James McDaniel

| GPM | Before RPM | Before PSI | After RPM | After PSI | Δ PSI |
|---|---|---|---|---|---|
| 800 | 1600 | 280 | 1500 | 245 | 35 |
| 700 | 1400 | 230 | 1330 | 195 | 35 |
| 600 | 1200 | 170 | 1150 | 145 | 25 |
| 500 | 1025 | 125 | 950 | 100 | 25 |

- Note — day supervisor D. Slater, night supervisor Sam Mixon; day operator Peter Campbell, night James McDaniel
- Note — manual by-pass confirmed closed on both sides

## 7-1 F-1 — Passes 3 + 4 (looped)

2026-08-29 · pumper not recorded · pipe ID not recorded · scan page 3 · test operator Travis Trenholm

| GPM | Before RPM | Before PSI | After RPM | After PSI | Δ PSI |
|---|---|---|---|---|---|
| 800 | 1620 | 285 | 1560 | 260 | 25 |
| 700 | 1430 | 230 | 1370 | 205 | 25 |
| 600 | 1225 | 170 | 1175 | 140 | 30 |
| 500 | 1045 | 125 | 970 | 100 | 25 |

- Note — figures pending the official sheet; see frontmatter `passes-3-4-status`.
- Note — this circuit came in on the **Pass Cleanliness sign-off form**, not a Decoking Data Sheet. Its table is headed simply RPM / PSI / GPM, with no PIG FORCE vs DIGITAL distinction.
- Note — sign-off section: effluent return and visual condition of cleaning pigs both initialed by DeBusk and by the client (KN). **Final white gauge foam is N/A on the DeBusk side** but carries a client initial. Customer signature present.
- Note — coil condition on this circuit was no better or worse than the rest (Jesse, 2026-09-02); all eight coils came out nominal.

## 7-1 F-1 — Passes 5 + 6 (looped)

2026-08-28 · Trimax 6, LEFT discharge · pipe ID 6" · scan page 1 · test operator pre Jason Harman, post "DRam" (illegible)

| GPM | Before RPM | Before PSI | After RPM | After PSI | Δ PSI |
|---|---|---|---|---|---|
| 800 | 1645 | 285 | 1620 | 270 | 15 |
| 700 | 1440 | 215 | 1395 | 200 | 15 |
| 600 | 1225 | 150 | 1180 | 140 | 10 |
| 500 | 1065 | 115 | 1010 | 102 | 13 |

- Note — **this circuit shows the smallest pressure drop of the measured circuits** — Δ of 15/15/10/13 PSI against 35/35/25/25 on passes 1+2 and –/35/50/35 on passes 7+8. Coil condition does not explain it: all eight coils came out nominal (see Coil condition below), so the spread is not a fouling difference. Per the standing base rate, a weak or erratic reading is a failed measurement rather than a finding about the coil — see [[business-normal-facts]].
- Note — project manager D. Slater, day supervisor Marshall Douglas, night supervisor Sam Mixon; day operators T. Trenholm and J. Harman
- Note — post test operator name is a scrawl reading "DRam"; the signature is initials only. Left as written rather than guessed at.

## 7-1 F-1 — Passes 7 + 8 (looped)

2026-08-28 · Trimax 5, RIGHT discharge · pipe ID 6.026" as written (see preamble) · scan page 4 · test operator pre M. Douglas, post James McDaniel

| GPM | Before RPM | Before PSI | After RPM | After PSI | Δ PSI |
|---|---|---|---|---|---|
| 800 | N/A | N/A | N/A | N/A | – |
| 700 | 1450 | 250 | 1385 | 215 | 35 |
| 600 | 1250 | 185 | 1190 | 135 | 50 |
| 500 | 1050 | 135 | 950 | 100 | 35 |

- Note — the pre side is the one sheet where both PSI columns were filled: 250 / 185 / 135 against 255 / 190 / 140 at 700 / 600 / 500 GPM. The table uses the first of the two throughout.
- Note — the 800 GPM step is written N/A on both sides. The ladder on this circuit ran 700/600/500 only, so there is no top-step Δ.
- Note — sheet is marked `PAGE # N/A — COVER SHEET`, and the JOB # field was left blank.
- Note — **direction of travel: `B → R`, Blue to Red**, hand-written beneath the pre-decoke flow test box. That is the default direction (Jesse, 2026-09-02; see [[equipment-library]]), so the annotation confirms the standard arrangement rather than flagging an exception. Blue is the feed port at the pumper rear, Red the return. This is the only one of the four sheets where direction was marked; the other three left the printed arrow blank, which given the default is a recording omission and not evidence they ran the other way.
- Note — day supervisor D. Slater, night supervisor S. Mixon; day operators P. Campbell and M. Douglas, night J. Utsey

## Coil condition — post-decoke

Jesse, 2026-09-02. This is the field account, not a flow-sheet reading; it is here because it is what the
Δ PSI figures have to be read against. Carry it to [[7-1-F-1]] Field Notes with the rest of the CAD26001
actuals.

All eight tube coils exhibited **nominal coking, consistent with historical run times.** The thickest
deposits — about **1/8" thick** — were located in the **last few radiant tubes of each pass**, and they
came off easily once the first oversized pig (**6.25"**) was run through each coil. *(Location sharpened
2026-09-02: first recorded as "in the radiant tubes" generally, corrected by Jesse to the last few tubes
of each pass. Not a detail — it puts the heaviest deposits in the same place as the residual below.)* Coils were inspected after the decoke: the last three
radiant tubes (**tubes 29, 30, 31**) showed a few spots of light fouling, within those same three tubes, in
select coils. **Quest Integrity holds the data identifying the exact passes and locations** — and that is
where it stays. Quest does not share reports and should not be expected to; they are a competitor with
their own decoking division, and verbal communication on the job is the ceiling for what reaches us
(Jesse, 2026-09-02; see [[business-normal-facts]]). The account above is the record — it is not a
placeholder for a document we are going to obtain.

Two things follow. First, the residual at tubes 29–31 is **this heater's recurring signature, not a CAD26001
finding** — the CAD24002 report recorded the heaviest and hardest deposits in exactly those three tubes at
the outlet, with the smart pig finding minimal fouling there and calling it typical of previous decokes
(see [[7-1-F-1]] Field Notes). Two decokes apart, same three tubes. Second, since all eight coils were
nominal, **the spread in Δ PSI across circuits is not a coil-condition effect.** With the scrapped passes
3+4 sheet set aside, the measured circuits run 15 to 35 PSI at the top step. Per the standing base rate,
that spread is the expected behaviour of the instrument, not a signal about the coils, and it is not to be
chased (see [[business-normal-facts]]).

## Summary — Δ PSI at matched GPM

| Circuit | 800 GPM | 700 GPM | 600 GPM | 500 GPM |
|---|---|---|---|---|
| Passes 1 + 2 | 35 | 35 | 25 | 25 |
| Passes 3 + 4 | 25 | 25 | 30 | 25 |
| Passes 5 + 6 | 15 | 15 | 10 | 13 |
| Passes 7 + 8 | – | 35 | 50 | 35 |

Every value in this table is computed from the before/after PSI above, not copied from a sheet. All eight
coils came out nominal, so the spread between circuits is not a coil-condition difference and is not to be
read as one. The passes 3+4 row is a placeholder, not a measurement; see frontmatter `passes-3-4-status`.

## Provenance

Values read from the scan pages. Identity fields were normalized to the job of record per Jesse's ruling
2026-09-02 — the field sheets carry several header errors (a wrong customer name, a wrong year, and
abbreviated heater names) which are not reproduced here. **The job number was not one of them:** one
sheet wrote `CAD26001` and was correct; it was normalised to `CND26001` that morning on the strength of
a ruling reversed later the same day, and that normalisation was the error, not the sheet. **Numeric cells were not
normalized**: every RPM, PSI and GPM above is as written, with the ambiguous ones re-read on zoomed 300–600
dpi crops and noted inline. The one exception is passes 3+4 — see below.

### Passes 3 + 4 — the scrapped sheet, as scanned

Jesse, 2026-09-02: the passes 3+4 sheet in the scan is a mistaken copy the crew scrapped and replaced; the
official copy has not been located. Its readings are preserved here and are not to be used.

| GPM | Before RPM | Before PSI | After RPM | After PSI | Δ PSI |
|---|---|---|---|---|---|
| 800 | 1600 | 400 | 1500 | 280 | 120 |
| 700 | 1450 | 300 | 1400 | 240 | 60 |
| 600 | 1200 | 200 | 1200 | 190 | 10 |
| 500 | 1050 | 180 | 1000 | 140 | 40 |

The 500 GPM before PSI is written over a struck-through earlier figure; read as 180 on a 300 dpi crop.

Both the before and the after readings sit outside the pattern of the other three circuits, so the sheet
cannot be salvaged by correcting one column. That is as far as this goes: a failed measurement is not a
puzzle to solve with arithmetic, and reconstructing what it "should" have read would be fabricating a
measurement. Recovery path is the official sheet or the correct numbers from the crew.
