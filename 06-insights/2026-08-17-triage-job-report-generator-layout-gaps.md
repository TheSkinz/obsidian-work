---
type: triage-note
created: 2026-08-17
tags: [triage, fieldpm, job-report, generator]
related: [[idea-job-report-generator-layout-gaps]]
---

# Triage — job-report generator layout gaps

Triage of the `/adhd` divergent run on [[idea-job-report-generator-layout-gaps]] (5 frames × 6 ideas
= 30, collapsed to 15 distinct angles by convergence). Every angle below carries exactly one
disposition. Two execute-bound items were red-teamed by fresh-context agents; one red-team's central
empirical claim was checked against the delivered documents and found wrong, which changed a verdict.

---

## Open question — ANSWERED 2026-08-17: `Decoking Analysis:`

**Jesse's call, same day: the default is `Decoking Analysis:`.** Landed — see execute item 2 below.
The evidence that raised the question is kept because it is why the key exists at all.

**What should the per-heater narrative lead-in say by default?** Four delivered reports were opened
and grepped, and they do not agree with each other:

| Report | Per-heater lead-in found |
|---|---|
| USA26041 — ExxonMobil Baytown F-501, Aug 2026 | `Decoking Analysis:` |
| USA26007 — ExxonMobil Baytown PS3, Feb 2026 | `Cleaning Results:` |
| USA26002 H002 — Valero Meraux, Jan 2026 | both `Decoking Analysis:` and `Cleaning Results:` |
| USA26002 H001 — Valero Meraux, Jan 2026 | neither (carries `DECOKING SUMMARY` as a section head) |

The renderer's hard-coded `Result:` appears in **none** of them. That much is settled — the current
literal is a defect, not a preference. What is not settled is whether the variation above is
deliberate (different jobs want different framing) or drift (all four were hand-built or hand-edited
in Word and nobody was holding a standard). Those two readings cannot be distinguished from the
artifacts, and they point at different defaults. This is a Jesse call, not an idea to evaluate.

---

## Execute

### 1. Refuse to overwrite an existing output file — DONE 2026-08-17

**Verdict: execute.** This is the survivor of a red-team that killed the proposal it came from.
**Landed the same day.** `main()` now parses `--force` out of argv and refuses when the output path
exists, checked before the workbook is read so it fails fast. Verified four ways: a new path writes,
an existing path refuses with exit 1 and a **hash-identical** file afterward, `--force` writes, and
a bad argument count prints usage. Then verified against the real thing — the exact invocation that
destroyed the edits on 2026-08-16, pointed at the delivered
`USA26041_Job Report_ExxonMobil Baytown F-501_2026-08.docx`, refused and left the file byte-identical
(`ab8e30e0…`). `scripts/README.md`, `SKILL.md` §`/report` and the USA26041 config docstring now
describe the guard instead of asking people to be careful.

The original idea was a two-layer scheme: a filename convention plus a `PROOF`/`RELEASED` state
stamped in the docx core properties. The red-team took it apart correctly. Trace the sequence — the
renderer writes a PROOF-stamped file, Jesse opens it in Word, Save-As to the delivered name, and the
delivered file inherits the *PROOF* stamp, because nothing in that path sets RELEASED. The guard's
default state is "unprotected," and it green-lights exactly the clobber it exists to prevent.
python-docx also exposes only fixed Dublin Core fields, so the stamp has to squat on `category` or
`keywords` — fields Word surfaces in its own UI and Jesse can blank without knowing what he deleted.
The state machine is dead.

What survives is three lines at `render_job_report.py:544`: if the output path already holds a file,
refuse to write unless `--force` is passed. The red-team's own strongest point argues *for* this
rather than against it — the cause of the 2026-08-16 clobber is unrecorded, so the guard belongs at
the write site where it is cause-agnostic, rather than in a convention that only binds the agent.
On 2026-08-16 the delivered file existed, so this would have refused.

**Execution brief.** *Intent:* make the 2026-08-16 incident structurally impossible regardless of
whether the next re-render comes from `/report`, a shell invocation, or an agent. *Constraint:* no
state machine, no stamps, no new files, no convention that depends on remembering. *Done when:*
`render_job_report.py` exits non-zero with a readable message when `argv[3]` exists and `--force` was
not passed, and re-running the USA26041 render against the delivered path fails instead of writing.
*First step:* wrap `doc.save(out)` at line 544 in an `os.path.exists(out)` check with a `--force`
escape, then verify by pointing it at the delivered USA26041 docx and confirming the file's mtime is
unchanged afterward. *Note:* this supersedes the `⚠ DO NOT RE-RENDER OVER THE DELIVERED DOCX`
docstring comment in `back-test/report_input_usa26041.py`, which is enforced by nothing — delete it
in the same change and say why in the commit.

### 2. Make the narrative lead-in config-driven — DONE 2026-08-17

**Verdict: execute**, reshaped by evidence from the red-team pass. **Landed the same day**
(config repo `db84e4b`+): `DEFAULT_LEAD_IN = "Decoking Analysis:  "` added beside `PIG_BUCKETS`,
call site at line 385 now reads `bold_lead=ht.get("lead_in", DEFAULT_LEAD_IN)`, and
`references/report-structure.md` plus the build-spec format table name the key instead of asserting
a fixed `Result:`. Verified by re-rendering USA26041 to a scratch path and grepping the output:
one `Decoking Analysis:`, zero `Result:`. The stale ⚠ comment in `report_input_usa26041.py` saying
this needed a renderer change is retired.

The red-team argued for a second hard-code — swap `Result:` for `Decoking Analysis:` and add no knob,
because there was "no observed variation to configure." It supported that with a claim that three
delivered reports across two customers all read `Decoking Analysis:`. That claim did not survive
checking. The real corpus is in the open-question table above: two labels, one report using both, one
using neither. Variation is observed, so a knob is the right shape and the seed's original instinct
was correct.

The renderer already supports this. `body(doc, text, *, bold_lead=None)` at line 179 takes an
arbitrary lead-in as a parameter; the literal is hard-coded at the *call site*, line 385. The change
is `bold_lead=ht.get("lead_in", DEFAULT)`. The red-team's residual objection — that the config field
is named `"result"` while the output would read something else — dissolves on inspection, because
`result` holds the prose and `lead_in` would hold the label. They are different fields; no rename.

**Execution brief.** *Intent:* let the report say what the document should say without a Word pass,
and stop the renderer contradicting the skill that feeds it — `usadebusk-fieldpm/SKILL.md` §`/report`
already collects this as the "Decoking Summary / Analysis narrative." *Constraint:* one optional key,
not a layout DSL; the default is Jesse's call per the open question above and is the only blocker.
*Done when:* `ht["lead_in"]` overrides the default, the three job configs render unchanged when the
key is absent, and `references/report-structure.md` §Heater Data names the key instead of asserting a
fixed `Result:` paragraph. *First step:* get the default from Jesse, then change line 385 and the one
sentence in `report-structure.md`.

---

## Test

### 3. Derive the pig-table and image shapes from the data

**Verdict: test.** The shape is clear and the assumption underneath it is not, which is the
definition of a test rather than an execute.

The idea: branch `build_pigs()` on `len(sizes)` — below a threshold emit one 6-column table with
`pigs_note` beneath it, above it keep the current 2-up carrier — and let `PIG_BUCKETS`' last label
travel with the shape (`SWAB` single, `SWAB/HC` split). Same logic for images, branching on heater
count, calling the already-standalone `_image_row()` from inside `build_heaters()` and
`build_flow_tests()` instead of from a terminal section. This answers two of the seed's three "always
or only sometimes" questions with data instead of a decision.

The unproven assumption is the threshold. Nothing establishes where a single pig table stops fitting,
and USA25025's 26 sizes were never rendered unsplit. Adopting "always one table" without that check
is the trap killed below.

**The experiment.** Render USA25025 with the split forced off, convert, `pdftoppm` page by page, and
look at it. *Pass:* the 26-row table fits and reads on one page, in which case the threshold is above
26 and the split can be deleted outright rather than made conditional. *Fail:* it overflows or reads
badly, in which case the threshold sits between 4 and 26 and a second render bisects it. *Deadline:*
before the next Baytown report, per the source seed's own gate. *Cost:* one render plus a rasterize,
both mechanisms that already exist.

---

## Park

### 4. The generator owns marked spans, not layout

**Verdict: park**, seed written to
[[idea-generator-owns-marked-spans-not-layout]] (`status: unexplored`, gated with a
`revisit-trigger:`).

Three of the five frames converged on this independently — emit markers around each generated block,
splice only what is between a marker pair on re-render, and everything Jesse touched survives by
construction. It is the only mechanism in the whole set that makes overwriting a delivered file
*safe* rather than *impossible*, and it is the correct reframing of the load-bearing rule: the
generator owns marked spans, not all layout.

It is parked and not executed because execute item 1 makes the same incident impossible for three
lines instead of a build, and because the mechanism degrades exactly where Jesse's edits are
structural — a table he merged from two into one no longer matches the marker pair that produced it.
The gate is a second edit-loss, or a decision that re-rendering delivered documents should be routine.

---

## Merged as duplicate

### 5. Raster the artifact, not just the arithmetic

**Verdict: duplicate — merged, not re-decided.** Already covered by
[[2026-08-16-backtest-passed-on-a-visually-broken-document]] (`status: unexplored`), which proposes
exactly this mechanism (`pdftoppm` page 1, scan full-width horizontal features, compare count/colour/
position against the shipped reference) and already asks whether it should become a standing part of
the generator's back-test.

Worth recording that it is a **hard dependency of the test above**, not a parallel idea — the
USA25025 forced-single-table experiment *is* that seed's mechanism applied to a new question. Triage
them together when that seed comes up, rather than either alone.

---

## Kill

**Collapse the three duplicated layout contracts.** Killed. The premise does not hold. Both
`references/report-structure.md` and `04-knowledge/job-report-generator-build-spec.md` were checked
and they currently agree — the build spec (lines 106–110) records that report-structure.md was stale
and *was reconciled to it* as part of that work, and report-structure.md now carries the same refined
layout. Nothing has desynced. The build spec is additionally a dated decision record with `[!done]`
validation callouts, so deleting layout prose from it loses information to buy a maintenance saving
that has never been paid. Revisit only if a real layout edit is shown to have desynced the copies,
and then the collapse points *at* the build spec rather than deleting from it.

**Move layout ownership into Word — .dotx content controls, or a template plus a numbered checklist.**
Killed. It trades a generator Jesse does not hand-edit for a template he would have to maintain in
Word, and the checklist variant is a manual pass repeated every report forever, which is the failure
mode the generator was built to remove. It also puts the layout contract somewhere the back-test
cannot see it.

**Absorb the delivered .docx back into the config.** Killed. Reading a hand-edited document and
inferring config deltas has to be right about an artifact nobody independently validated, and a
silently-wrong absorb writes a false record that then reads as checked — the same shape as the
back-test that passed on a borderless document.

**Provenance sidecar with config/workbook hashes and a verify mode.** Killed. Unbounded machinery for
a failure that has not occurred (a customer disputing a number), while doing nothing about the one
that did. Fails the bounded-propose-only preference.

**Scaffold the config from the workbook.** Killed. It reduces the cost of *creating* a config, which
is not the observed defect. The defect is the config diverging from the delivered document *after*
hand-edits — `report_input_usa26041.py` still lists `launchers.png`, which the delivered report
dropped. Scaffolding does not touch that.

**Delete the per-job config once a report ships.** Killed. The config is the only structured record of
the job's static skeleton and narrative, and the next bid on that heater wants it. Throwing away the
asset to kill the drift symptom is the wrong trade.

**Re-render as tracked changes (`w:ins`/`w:del`).** Killed. python-docx has no supported API for
revision markup; it is raw OXML against Word's rsid and author model, for an event that happens a few
times a year. It also cannot express a structural change — a 2-up table merged into one is not an
insertion over the old structure.

**Word's Review > Compare > Combine as the merge tool.** Killed. Compare assumes a shared ancestor
with similar structure; a regenerated 2-up pig table against a hand-merged single table diffs as
noise. It also produces a third document sitting beside two others, and the live risk is that the
comparison file is the one that gets sent.

**Always emit one pig table.** Killed as stated, superseded by the test above. It is the smallest fix
and it matches what Jesse actually did, which is what makes it tempting — but it is validated only on
USA26041's 4 sizes and gambles the 26-size turnaround case, which is the more valuable one. The 2-up
split exists because of that job.

**Delete the lead-in label entirely.** Killed. It was carried as the run's provocation and it does
reframe the set usefully — two of the three gaps are the generator *adding* something the document
does not need. But it is not supported by the corpus: three of the four delivered reports carry a
per-heater lead-in of some kind. Removing it would move the generator further from shipped practice,
not closer.

---

## Tally

**2 execute · 1 test · 1 park · 1 merged as duplicate · 10 kill**

**Status as of 2026-08-17 close: both execute items are done and verified.** What remains is the
test — one USA25025 render with the pig split forced off, rasterized, to find where a single table
stops fitting — and it should happen before the next Baytown report. The park
([[idea-generator-owns-marked-spans-not-layout]]) is gated behind a second edit-loss, which the
write guard now makes considerably less likely.

Adjacent, and closed the same day: [[2026-08-16-report-gold-two-values]] asked whether the
generator's `#FCC30A` or the shipped documents' `#F2A900` was the house gold. **Jesse ruled
2026-08-17 — `#FCC30A`, nothing changes.** Older documents carrying a slightly different amber are
expected drift, not a defect to chase. `GOLD` in `render_job_report.py` stays as it is, and the
generator's `scripts/README.md` now records the ruling instead of an unresolved discrepancy.
