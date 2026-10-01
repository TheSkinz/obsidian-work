---
type: review
status: resolved
review_type: skill-drift
source_authority: primary
confidence: high
created: 2026-10-01
review_after: 2026-11-01
related:
  - "[[vault-skill-drift-loop-spec]]"
  - "[[2026-09-01-skill-drift-review]]"
  - "[[_canonical-heater-card]]"
tags: [review, skill-drift, skills, knowledge-system]
---

# Skill-Drift Review — 2026-10-01

## Trigger

Scheduled fire of `vault-skill-drift-loop`. Window: everything since the last `skill-drift:` heartbeat `4343c61` (2026-09-01 03:17) — 82 config-repo commits and 243 vault commits. Read: all 10 skills under `~/.claude/skills/` with every reference file and script README, the vault knowledge layers changed in the window (`01-context/`, `04-knowledge/`, `06-reviews/`, `07-llms/`, `08-systems/`, `change-log.md`, both CLAUDE.md files), `04-knowledge/estimating-actuals-rollup.md`, the regression suite (`README.md`, `fixtures/`, `frozen/` frontmatter and domain references), and the agent memory directory. Three parallel readers did the sweep; **every quote below was re-read from the file by the main session before it was written here.**

Config repo was clean on `main` after `git fetch`. The prior note [[2026-09-01-skill-drift-review]] is `status: resolved`, so per the spec's Branch States table it is not a backlog. Branch `drift/2026-10` was free and was created from `main`. **It carries 9 commits, one per skill touched plus one for the regression suite — verified with `git log main..drift/2026-10` before this note was written** (last month's branch had zero, see that note's Apply Log). Nothing under `frozen/` is on it.

**25 findings: 21 proposed on the branch, 1 renderer finding reported only, 5 frozen-baseline findings reported only (R1–R5), 7 vault-side findings reported only (V1–V7), 9 memory flags (M1–M9), 12 open questions.**

**The pattern behind most of it:** two rulings landed in their canonical homes and stopped. The **2026-09-28/29 max-pig rulings** (one figure per tube size; ID + 0.250" a default planning size, not a cap; config `652e40e`, `40788c6`, `79992c1`) reached equipment, estimating and fieldpm, but not core, ops, sop, vault-ingest, the glossary, the canonical card or the template — and `79992c1` dissolved the "looped-circuit exception" that three skills still point at. The **2026-09-02 flow-test demotion** (vault `a89ec7a`, Lane 4) never reached the SOP skill, whose authority clause lets it override the vault. That second one is the most consequential item here.

**Replay owed before merge.** The branch edits core, estimating, sop, equipment, fieldpm and vault-ingest; the fixture-replay guard warned on every one. Several are substantive under the README's trigger #2 (F1 changes a duration, F3 changes a completion rule, F16 removes a caveat a frozen key requires). Replays are a merge-time step, not something this loop does.

---

## Part 1 — Skill drift (proposed on `drift/2026-10`)

### F1 · Proposal Gantt row still quotes the struck flat 4-hr Smart Pig — HIGH · Lane 4 (propagation of a ruled value)

`~/.claude/skills/usadebusk-estimating/SKILL.md:428`:
> - Standard task rows: … | Smart Pig (if applicable, 4 hrs) | Rig-out equipment (matches rig-in)

Evidence, same file `:125`:
> **Smart Pig: 2 hrs per pass when elected.** (Jesse, 2026-09-06 — replaces the former flat 4 hrs, which was one event covering the pass set.)

`change-log.md` records that ruling as "Propagated to all four statements in one pass" — this fifth one was missed.

Proposed: `| Smart Pig (if elected — 2 hrs per pass, per the Duration Model) |` — commit `b5d6835`.

- [x] Accept
- [ ] Reject — reason: ______

### F2 · Three skills point at a "looped-circuit exception" that no longer exists — HIGH · Lane 4 (propagation)

`usadebusk-estimating/SKILL.md:301`:
> Full rule, the per-size rule, the reducer-and-reverse run method and the looped-circuit exception live in `usadebusk-equipment`

`usadebusk-ops/SKILL.md:18`:
> Max pig size = Clean ID + 0.250" (sizing rule and looped-circuit exception canonical in usadebusk-equipment).

`usadebusk-core/SKILL.md:175`:
> The sizing rule, the per-size rule and the looped-circuit oversized-final exception are canonical in usadebusk-equipment

Evidence, `usadebusk-equipment/SKILL.md:103-104`:
> **6.500" has been run on heavy fouling or looped circuits** — a recorded larger-than-default case, not an exception to a limit

and the `79992c1` message: *"the 6.500" line is now a recorded larger-than-default case rather than an exception breaching a limit."* `grep -i exception` on equipment returns only that line and an unrelated firewater line.

Proposed: drop the pointer and state default-not-cap — estimating `b5d6835`, ops `fedaeb4`, core `cb386a3` (core's behavioural paragraph is F16).

- [x] Accept
- [ ] Reject — reason: ______

### F3 · SOP skill still requires all three completion criteria; the flow test was demoted 2026-09-02 — HIGH · Lane 4 (propagation of a ruled value)

`usadebusk-sop/SKILL.md:118-120`:
> - Before/after flow tests show measurable pressure drop improvement at equivalent GPM
>
> **All three, together — and say so when the result is stated.**

`usadebusk-fieldpm/references/report-structure.md:362`:
> three completion criteria together, plus the final pig size reached against the section's Clean ID

Evidence, `04-knowledge/manual/10-verification-and-completion.md:36` and `:44`:
> Two criteria carry the completion determination, and a third corroborates it.
> A circuit meeting criteria 1 and 2, whose flow test is invalid or unavailable, is complete

Vault commit `a89ec7a` (2026-09-02): *"[Lane 4] Flow tests: demote delta PSI to corroborating."* **Aggravating:** `usadebusk-sop/SKILL.md:8` says *"On any conflict over procedural/SOP content between this skill and a project prompt, vault note, or other layer, this skill governs"* — so the stale skill currently overrides the ruling for any SOP session.

Proposed: mark criterion 3 corroborating and replace "All three, together" with the two-decide/one-corroborates statement taken from manual 10 §10.2; report-structure aligned to match, and its stale `usadebusk-sop:102` line pointer replaced with the section name — sop `0e30820`, fieldpm `1b7d655`.

- [x] Accept
- [ ] Reject — reason: ______

### F4 · ID + 0.250" still stated as a cap and as one heater figure — MEDIUM · Lane 4 (propagation)

`usadebusk-sop/SKILL.md:147`:
> | Maximum Pig OD | Tube ID + 0.250" max (canonical: usadebusk-equipment) |

`usadebusk-sop/references/sop-pigging-diagrams.md:66`:
> OVER[Oversized final pig<br/>tube ID + up to 0.250 in]

`usadebusk-vault-ingest/SKILL.md:595`:
> USADebusk's own sizing rule (governing ID + 0.250", rounded to the nearest 1/8" pig size not exceeding it; full rule in `usadebusk-equipment`)

Evidence, `usadebusk-equipment/SKILL.md:107-108` and `:134-135`:
> **Max pig OD — the DEFAULT PLANNING SIZE, not a limit on what may be run.** (Jesse, 2026-07-25; reclassified from a ceiling 2026-09-29.)
> **One max pig size PER TUBE SIZE, not one per heater.** (Jesse, 2026-09-28 — this **reverses** the earlier "smallest ID across all sections and segments" wording

Proposed: "Default planning size per tube size: that section's ID + 0.250", rounded down to a 1/8" size — not a cap" in each — sop `0e30820`, ops `fedaeb4`, vault-ingest `1ced2de`.

- [x] Accept
- [ ] Reject — reason: ______

### F5 · Extraction output block still prints `MISSING` for signatures — MEDIUM · Lane 3

`usadebusk-fieldpm/references/extraction-format.md:123-125`:
> SIGN-OFF
>   Customer:      [signed / MISSING]
>   Supervisor:    [signed / MISSING]

Evidence, same file `:62` and `:38`:
> | Customer signature | Record if legibly present. **Never report its absence**
> | *(signature block)* | **Never flag anything in it** — not a missing signature, …

Proposed: `[signed — omit this line if not legibly present]` — `1b7d655`.

- [x] Accept
- [ ] Reject — reason: ______

### F6 · Report reference lags the job-report build spec — MEDIUM · Lane 3 (client deliverable)

`usadebusk-fieldpm/references/report-structure.md:45`, `:107`, `:173-174`:
> | JOB NO. | FACILITY | EXECUTION | PROJECT MANAGER |
> | CAUSE | DATES | HOURS |
> render what exists and mark gaps

Evidence, `04-knowledge/job-report-generator-build-spec.md:118`, `:121`, `:240`:
> **Two-row project table** (4 cols): PROJECT NO / FACILITY / EXECUTION / PROJECT MANAGER
> table **DATES / HOURS / CAUSE** (reordered from CAUSE / DATES / HOURS — Jesse, 2026-09-07)
> The rule is **omit, never annotate.** A pass whose source record flags it suspect is left out of the Flow Tests section — no row, no footnote, no explanation of the gap.

`report-structure.md` itself says to keep the reference and the spec in sync. Proposed: PROJECT NO., DATES | HOURS | CAUSE, omit-never-annotate — `1b7d655`. The renderer is F22, reported only.

- [x] Accept
- [ ] Reject — reason: ______

### F7 · "Coils looped to N passes" contradicts Coil = Pass — MEDIUM · Lane 3 (vocabulary already ruled)

`usadebusk-core/SKILL.md:165`:
> | Heater total | | | | | State loop arrangement, e.g. "10 coils looped to 5 passes" |

`usadebusk-fieldpm/references/report-structure.md:142`, `:159` (customer-facing template):
> | Number of Passes | [as-built config — e.g. "2 coils looped to 1 pass (Pass 1 & 2)"] |
> (e.g. USA26038 H-20 re-looped to 4 coils / 2 passes in the field).

Evidence, `usadebusk-core/SKILL.md:47-48`:
> | Coil = Pass | **The same thing — one continuous tube run through the heater** … Jesse, 2026-09-17: *"Coils = passes."*
> | Circuit | **What one pig actually travels.** … CAD26001 ran *8 coils looped into 4 circuits*

Proposed: "looped to N circuits" — core `cb386a3`, fieldpm `1b7d655` (that commit message labels this "F12(part)"; it is F7).

- [x] Accept
- [ ] Reject — reason: ______

### F8 · "Only records open the derate gate" never reached the skill — MEDIUM · Lane 4 (propagation)

`usadebusk-estimating/SKILL.md:36`:
> Reason to believe means **prior actuals on that heater, a known fouling history, or hard service Jesse has personally seen on that unit**.

Evidence, `change-log.md` 2026-09-03 row:
> **Jesse's ruling: only records open the derate gate** — prior actuals on that heater, a recorded fouling history, or hard service h[e has personally seen] …

`grep "only records\|is a claim"` returns nothing in the skill or in `01-context/estimating-approach.md` (V6).

Proposed append: *"Only records open the gate — 'known' means recorded. A customer's stated expected condition is a claim, not a fouling history, and does not open it (Jesse, 2026-09-03)."* — `b5d6835`.

- [x] Accept
- [ ] Reject — reason: ______

### F9 · Rig-over defined as including moves between heaters — MEDIUM · Lane 4 (estimating method; internal contradiction)

`usadebusk-core/SKILL.md:57` and `usadebusk-estimating/SKILL.md:312`:
> | Rig-over | Moving equipment between passes or heaters mid-job |
> *Rig-Over occurs between passes or heaters mid-job, not before pigging begins.*

Evidence, `usadebusk-estimating/SKILL.md:149`:
> A same-mobilization move between nearby heaters is priced as a **reduced rig-in plus a mirrored rig-out on the destination heater**, not as a rig-over line. Rig-over remains the right line for moving between pass sets *within* one heater.

Proposed: rig-over = between pass sets within one heater; nearby-heater move = reduced rig-in — core `cb386a3`, estimating `b5d6835`. Distant-heater moves are open question Q3.

- [x] Accept
- [ ] Reject — reason: ______

### F10 · Core's fouling MIRROR lists Clean ID as a finding; the glossary authority does not — LOW · Lane 3

`usadebusk-core/SKILL.md:82`:
> `Clean ID` · `localized restriction` · `residual fouling` · … are observations and belong in reports

Evidence: core's own `:78` names `17-glossary.md` § Fouling as the authority for this block. Glossary `:25` defines Clean ID as *"A sizing input, not a cleaning result"*, and core's own `:69` says the same. The glossary's finding list has Final pig size.

Proposed: `final pig size` in place of `Clean ID` — `cb386a3`.

- [x] Accept
- [ ] Reject — reason: ______

### F11 · Per-diem role split missing from the skill — LOW-MED · Lane 4 (rates)

`usadebusk-estimating/SKILL.md:205`:
> | Per Diem | Daily per person | 1 PD per 12-hr shift |

Evidence, `04-knowledge/concepts/estimating-pricing.md:57-60`:
> The generic base is **$150 per crew member per shift regardless of position or title** (Jesse, 2026-09-05). A facility can require it built to their own rules, and then it splits by role — Valero Port Arthur's DSP#26035 contract carries `Per Diem — Supervision $150/day` and `Per Diem — Operator $130/day`.

Proposed: append the generic base and the contract-split caveat — `b5d6835`.

- [x] Accept
- [ ] Reject — reason: ______

### F12 · "Pass/circuit count" conflates two terms — LOW · Lane 3

`usadebusk-core/SKILL.md:130`, `usadebusk-estimating/SKILL.md:11` and `:326`, `usadebusk-sop/SKILL.md:219`:
> Pass/circuit count · Tube ID …
> 1. **Pass / circuit count** → …
> 4. Pass/circuit count and coil pairing
> 3. Pass/circuit count and coil pairing

Evidence: core `:48`, *"Coils ≠ circuits whenever looping is elected."* Proposed: "Coil (pass) count and circuit count" — core, estimating and sop commits.

- [x] Accept
- [ ] Reject — reason: ______

### F13 · Ports still named after heater sections — MEDIUM · Lane 3

`usadebusk-equipment/references/equipment-circuit-diagrams.md:30-31` and `usadebusk-sop/SKILL.md:258`:
> BLUE([BLUE port / CONV]):::blue
> RED([RED port / RAD]):::red
> - Fig. 200 (3") at Trimax rear — CONV and RAD ports, valve manifold

Evidence, `usadebusk-equipment/SKILL.md:28`:
> **CONV and RAD are heater sections, not port names.** … Corrected 2026-09-02

The diagram's own scope note at `:18` says colour is bonded *"not to a coil section"*. Proposed: `BLUE port` / `RED port`; "Blue (feed) and Red (return) port per pump assembly" — equipment `5316e4b`, sop `0e30820`.

- [x] Accept
- [ ] Reject — reason: ______

### F14 · "Pass" used for a pig run — LOW · Lane 3

`usadebusk-equipment/SKILL.md:99` and `usadebusk-sop/SKILL.md:148`:
> - Increment: 1/8" per successful pass
> | Pig Sizing Increment | 1/8" per successful pass |

Evidence, `04-knowledge/manual/17-glossary.md:70`: *"Counted in **pig runs** — never "passes", which is a tube path through the heater."* Proposed: "per successful pig run".

- [x] Accept
- [ ] Reject — reason: ______

### F15 · Superseded DSP26085 total restated without its caveat — LOW · Lane 3

`usadebusk-estimating/SKILL.md:531` and `scripts/README.md:130`:
> … DSP26085 $40,477.08, …
> - **DSP26085** — T&M, 6-line → $40,477.08

Evidence, `01-context/active-jobs.md:49`: *"[[DSP26085]] | ExxonMobil Baytown, TX | … | $46,657.08"*. Proposed: append "(regression record of the 2026-07-24 `Bids\` workbook; the ruled quote total is $46,657.08)" — `b5d6835`. The back-test figure itself is left alone.

- [x] Accept
- [ ] Reject — reason: ______

### F16 · Core's looped-card caveat instructs a check against a dissolved exception — HIGH · Lane 4 · **frozen F2 key 10 depends on the old text**

`usadebusk-core/SKILL.md:177`:
> **When the card's configuration is looped and `usadebusk-equipment` is NOT loaded, say so on the Max pig OD figure: record that the looped-circuit oversized-final exception was neither applied nor ruled out, and do not present the computed figure as settled.**

Evidence: same as F2 — the exception no longer exists. Proposed replacement (`cb386a3`): *"The Max pig OD field carries the default planning figure; an actual run size is recorded as run and never reconciled to it. There is no looped-circuit exception any more … Do not derive a larger figure for a looped card."* The "do not derive a larger figure" guard is kept. **This invalidates frozen F2 diff key 10 (R5)** — accept F16 and R5 together, or neither.

- [x] Accept (with F2 replay and re-cut)
- [ ] Reject — reason: ______

### F17 · fieldpm `/log` and inputs carry superseded assumptions — LOW · Lane 3

`usadebusk-fieldpm/SKILL.md:118` and `:87`:
> - PDT: start time, cause (customer-side), estimated duration
> **Inputs:** One or two scanned receipt PDFs (day shift + night shift).

Evidence, same file `:139`: *"**Never write "customer-caused," "customer-side" or any variant** next to plant down time or stand-by."* and the never-merge-shifts / count-pages rules (`d43189d`). Proposed: "cause as stated on the receipt or by the crew"; "One or more scanned receipt PDFs — count pages first" — `1b7d655`. The `payroll email` wording in the fieldpm and ops `description:` fields is left alone, because a description change moves triggering.

- [x] Accept
- [ ] Reject — reason: ______

### F18 · Dead path in the SOP skill — LOW · Lane 2

`usadebusk-sop/SKILL.md:73`:
> Filed at `00-inbox/2026-09-03-sop-voice-pipefitter-role.md`.

Evidence: `test -e` fails; the file is at `archive/2026-09-03-sop-voice-pipefitter-role.md`. Proposed: repoint — `0e30820`.

- [x] Accept
- [ ] Reject — reason: ______

### F19 · Ingest client list names a folder that doesn't exist — MEDIUM · Lane 2

`usadebusk-vault-ingest/SKILL.md:71`:
> … Syncrude, Targa, Valero, Westlake

Evidence: `ls 02-facilities` shows `Westlake-Chemical`, and `02-facilities/_directory.md:21` names that company tier. The skill's auto-create-site-folder rule would make a parallel `Westlake/`. Proposed: "Westlake-Chemical (folder name; "Westlake" / "Westlake South" in a source routes here, `client:` stays as signed)" — `1ced2de`.

- [x] Accept
- [ ] Reject — reason: ______

### F20 · Ingest Configuration example implies outlets are the default loop end — LOW · Lane 3

`usadebusk-vault-ingest/SKILL.md:131`:
> - Configuration (Looped-at-outlets / Individual-Passes / etc.)

Evidence, the same skill at `:203`: the looped end is a per-job election with no default, never assume radiant outlets. Proposed: "(Looped-at-Radiant-outlet-flanges / Looped-at-Convection-inlet-flanges / Individual-Passes — the end the source states; no default)" — `1ced2de`.

- [x] Accept
- [ ] Reject — reason: ______

### F21 · adversarial-review role table contradicts its own cross-model default — LOW · Lane 2

`adversarial-review/SKILL.md:406` against `:410`:
> | **Adversary** | `model: "opus"` | Needs strong reasoning to challenge the Finder's claims |
> **Cross-model Adversary — the default whenever you run the chain at all.** Spawn the Adversary on a different model from the Finder

Proposed: "different family from the Finder (e.g. `"fable"` vs an `"opus"` Finder)" — `3ec0613`.

- [x] Accept
- [ ] Reject — reason: ______

### F22 · Job-report renderer and input template lag the build spec — MEDIUM · Lane 3 · **reported only, no code changed**

`usadebusk-fieldpm/scripts/render_job_report.py:368` and `scripts/report_input_template.py:30`:
> header_row(t.add_row().cells, ["CAUSE", "DATES", "HOURS"])
> [("JOB NO.", ""), ("FACILITY", ""), ("EXECUTION", ""), ("PROJECT MANAGER", "")],

Evidence: build spec `:118` and `:121` (quoted in F6). The spec's 2026-09-07 changes also set column widths (`1.40 / 0.70 / 4.80`), and spec commits `7ffb4a6` and `8247ad9` may carry more renderer changes; those were not verified line by line. That is why the code was not edited from a drift loop. Recommended: one build session to implement the spec delta, then re-run `back-test/assert_structure.py`.

- [ ] Schedule the renderer build
- [x] Leave until the next report is due

### F23–F25 · Regression README and fixture prose — MEDIUM/LOW · Lane 2 · commit `1d8345f`

**F23**, `~/.claude/regression/README.md:70-72`. The per-fixture commit line reads *"F1 @ `6b6d4a8`, F4 @ `6b6d4a8`, F6 @ `6b6d4a8` …, F2 @ `f20db13`, F3 @ `4ec2d76`, F5 @ `28827d3`"*. **All six** disagree with the frontmatter `baseline_commits:` (`f1:6` 328189f, `f2:6` ccc5086, `f3:6` 574273b, `f4:6` 35e53c6, `f5:6` 79992c1, `f6:6` b449e63). Replaced with the frontmatter values, and the "wrong before" tally bumped to five.

**F24**, `README.md:96`: *"Battery status as of 2026-09-04: 6 of 6 read `behind`…"*. This predates both F5 re-cuts (`9127f21`, `c975d6e`). A 2026-10-01 status block was added above it, naming R1–R5. Also in F24:
- `:295-296` lists *"(missing signature, illegible field, …)"* as required flags, against fieldpm `extraction-format.md:62`; the signature is dropped.
- `:306` says *"Ruled so far: F1's hard pig quantity"*, against `f6:11` `rig_in_RULED_UNKEYED_AND_VARIABLE`; F6 rig-in is added.
- `:479-482` says *"Key 5 is independent again"*, against `f6:14` *"KEY 5 IS NOW UNKEYED"*; a superseded marker is added.

**F25**, three smaller README fixes:
- `:405-406`: *"64 occurrences across all five frozen outputs"*. A grep now counts 9 across six files (F2 4, F6 3, F4 2), and the line is updated.
- `:489-490`: *"(repo @ 3489e1b)"* is a superseded F3 predecessor; it now points at each file's own frontmatter.
- `:18` points at `00-inbox/2026-07-24-fixtures-work-better-as-rule-audit.md`; `test -e` fails and the file is in `archive/`.

F25 also covers `fixtures/f6-duration-mobdemob-input.md:33-35`, *"so the rig tier is derivable from the rule that now governs it (connection elevation, run distance from the pumper, pipefitter wait)"*, which describes the tier machinery struck by `b449e63`. A dated note was appended; the original text is kept.

- [x] Accept F23–F25
- [ ] Reject — reason: ______

---

## Part 2 — Frozen baselines (report only — never edited by this loop)

Re-cutting is your call after a judged clean replay. **R1 and R2 are inverted: a correct replay against the current skill fails them.**

**R1 · F3 key 4 requires the missing-signature flag — HIGH.** `frozen/f3-extract-output.md:21`: *"(4) the missing customer signature flagged as a dispute and invoice-readiness risk"*; `:117`: *"5. Customer signature blank. Unsigned receipt is dispute risk at invoicing."* Against fieldpm `SKILL.md:94`, *"**Never flag a missing signature**"*. Baseline `574273b` predates `bf5314c` and `e4d3c47`.

**R2 · F6 key 6 requires the flat 4-hr Smart Pig — HIGH.** `frozen/f6-duration-mobdemob-output.md:14`: *"(6) smart pig 4 hrs as ONE event covering the set, not per pass"*; `:277`: *"Smart Pig = 4 hrs"*. Against estimating `:125`, 2 hrs per pass (`8e68d13`, after baseline `b449e63`). Six passes take smart pig from 4 to 12 hrs and move the total (computed, not replayed).

**R3 · F1 key 2 rewards the struck rig-in tier reasoning — MEDIUM.** `frozen/f1-proposal-output.md:15`: *"(2) rig-in/rig-out tiered from the LAUNCHER/RECEIVER CONNECTION POINTS, Moderate 6 hrs"*; `:167`: *"Three drivers, which multiply rather than offset"*. Against estimating `:89`, *"**Rig-in is 6 hours.**"* (`b449e63`). The figure is unchanged; the reasoning the key scores is now wrong.

**R4 · F1, F2 and F4 call ID + 0.250" a ceiling — LOW.** `f1:252`: *"The 0.250" is a ceiling, not a target"*; `f4:140`: *"gives a ceiling of 4.276""*. Against equipment `:107-108` (`79992c1`). The 4.250" figures are unaffected. Separately, F1 and F6 never split the Pig line into its travel component and pigging task (`grep -c` returns 0), which estimating `:44-46` now requires (`c473a6b`).

**R5 · F2 key 10 requires the dissolved looped-circuit exception — HIGH if F16 is accepted.** `frozen/f2-ingest-dryrun-output.md:26`: *"(10) the looped-configuration caveat on max pig OD - H-77 is looped at the radiant outlet flanges, which triggers the oversized-final-pig exception living in usadebusk-equipment"*. F2's provenance wording *"6 circuits looped to 3 passes"* (fixture `:56`, key 1) is also the old Coil = Pass vocabulary; the numbers are unchanged.

Side note: `f4:5` says *"claude-config @ ccc5086"* while `f4:6` says `35e53c6`. The file disagrees with itself; fix it at the next re-cut.

- [x] Replay and re-cut F3 and F6 (the inverted keys) first, then F2 with F16, then F1
- [ ] Re-cut only F3 and F6 for now
- [ ] Leave all; the README status block is warning enough

---

## Part 3 — Vault-side drift (report only — this loop never edits vault content)

**V1 · Canonical card and template still compute one Max pig OD from the smallest ID — HIGH · Lane 4 / schema.** `04-knowledge/_canonical-heater-card.md:187`: *"<governing tube ID + 0.250" — compute from the SMALLEST ID across all sections/segments, typically radiant>"*. `templates/_heater-template.md:86`: *"<governing tube ID + 0.250" — smallest ID across all sections>"*. Against equipment `:134-135` and `change-log.md` 2026-09-30. The card is the schema authority (core `:136`), so every new ingest inherits the reversed rule. The exemplar's `:145`, `:157` and `:170` also carry *"10 coils looped to 5 passes"*. The field is single-valued, so the multi-bore format needs your call (Q-list).

**V2 · Glossary defines Max pig OD as a per-circuit cap and binds launcher/receiver to inlet/outlet — MEDIUM · Lane 4.** `17-glossary.md:96`: *"The largest pig permitted in a circuit: governing tube ID plus 0.250 inches."* `:26`: *"Sets the maximum pig OD for that entire circuit."* `:97`: *"The vessel mounted on the coil inlet flange from which pigs are launched."* Against equipment `:107-112`, *"**It is not a cap on the field.**"*, and `:64-65`, *"**Same form factor and the same unit**"* on whichever flanges (2026-09-02).

**V3 · Manual 10 contradicts itself after the flow-test demotion — MEDIUM · Lane 4.** §10.2 (`:36`) has two criteria deciding, but §10.3 is still headed *"Why all three"* (`:48`), and `:50` cites *"a final pass at full permitted pig OD"*. `04-knowledge/sops/sop-formatting-standard.md:86` still has *"reduction confirms cleaning effectiveness"*.

**V4 · Equipment library lacks the Honeycomb pig — LOW · Lane 4.** `04-knowledge/equipment/equipment-library.md` § Pig Types lists Foam / TC / HR / Swab only, against equipment `SKILL.md:84` (HC row) and `:88` (*"Honeycomb sizes are stated in MILLIMETRES"*, Jesse 2026-09-07).

**V5 · Seed template and governance still describe the stopped research loop — LOW · Lane 2.** `templates/_idea-seed-template.md:16`: *"the research loop enforces it"*. `knowledge-system-governance.md:199`: status *"flips to `researched`"*. Against idea-triage `SKILL.md:33` (loop stopped 2026-08-21) and `change-log.md`, *"`status: researched` is no longer a resting place"*.

**V6 · `01-context/estimating-approach.md:24` lacks the "only records" derate-gate ruling — MEDIUM · Lane 4.** This is the same gap as F8, on the vault side.

**V7 · This loop's own spec cites the retired git-guard hook — LOW · Lane 2.** `vault-skill-drift-loop-spec.md:32`: *"The `usadebusk-git-guard.mjs` PreToolUse hook only matches paths containing `USADEBUSK[\\/]`"*. Against global CLAUDE.md, *"The former `usadebusk-git-guard` was retired 2026-09-04"*. `ls ~/.claude/hooks` shows no git-guard.

- [x] Fix V1–V7 in a session (V1, V2, V3, V4, V6 need your Lane 4 ask)
- [ ] Fix only V1 and V3 now
- [ ] Leave

---

## Part 4 — Agent memory (flag only — recommend one `/consolidate-memory` pass)

- **M1** `reference-command-only-skills-not-subagent-loadable.md:13-14`: *"As of 2026-07-28 this covers `usadebusk-vault-ingest`, `usadebusk-fieldpm` and `idea-triage`"*. `grep disable-model-invocation` now finds only adhd and idea-triage (fieldpm `:8` mentions it in prose: removed 2026-09-04).
- **M2** `project-usadebusk-claude-arch.md:13`: *"-fieldpm (dormant between mobilizations)"*. The dormancy lifecycle was dropped 2026-09-04 (`30f829f`).
- **M3** `project-vault-five-loop-system.md:32`: *"the git-guard hook matches only `USADEBUSK[\\/]` path[s]"*. That hook was retired 2026-09-04. Its tools list also omits `rate_history_rollup.py`, `notify_grok_bot.py` and `fill_service_receipt.py`.
- **M4** `feedback-low-effort-automation.md:13`: *"monthly skill-drift, monthly consolidation, and now the daily pre-staging loop"*. Pre-staging was disabled 2026-08-21.
- **M5** `project-knowledge-loop-os.md:4`: *"bare `python` is not on PATH"*. Contradicted by `reference-vault-python-interpreter.md:11`, *"Resolved 2026-07-18"*.
- **M6** `reference-fable5-when-to-use.md:16`: *"**Current rule: Opus 5 for essentially everything"*. `07-llms/claude/opus-5-5.md:19` records the switch to Opus 5.5 on 2026-09-30. The routing rule probably survives with the version bumped.
- **M7** `feedback-max-pig-od-field-purpose.md:21`: *"the governing restriction (smallest ID, bend ID where bends govern)"*; `feedback-pipeline-pigging-scope.md:28`: *"sizing to the governing (smallest) ID plus 0.250""*. Reversed 2026-09-28.
- **M8** `project-outlook-architecture.md:31`: *"read them from the mailbox, which takes about three calls through the Chrome integration"*. Contradicted by its own `:11` and by `reference-m365-access-boundary.md`.
- **M9** dead pointers: `feedback-diff-w-before-committing-vault-edits.md:19` names `tools/audit_commit.py`, which `ls` shows absent (deleted `4b0e869`), and its `:15` inbox note is gone. `feedback-count-the-complaints-before-designing.md:15` points at `00-inbox/idea-job-report-summary-quality.md`, now in `archive/`. Four `~/.claude/plans/*.md` files cited by the leverage, setup-scout, shift-delta and copilot memories are absent.

The index maps 1:1 to topic files (89/89).

- [x] Run `/consolidate-memory` against M1–M9 — done by hand 2026-10-01 (M1–M8 corrected; M9's two inbox pointers repointed and the `audit_commit.py` line marked deleted; the four absent `~/.claude/plans/*.md` citations left, since they are historical provenance on project memories)

---

## Open questions (domain truth the loop cannot settle from files)

1. **HR pig spelling.** "Hell Raiser" appears in equipment `:82` and extraction-format `:143`. "Hell Razor" appears in report-structure `:116` (customer legend), `report_input_template.py:68`, `extract_ticket_breakdown.py:63` and `USA25025-job-record.md:64`. Which is right?
2. **Derate trigger lists differ.** `estimating-approach.md:13-14` has "Hard fouling history" and "Tight tube ID (under ~3")". Estimating `:37` has neither, but lists plug-header / mule-ear bends, which the vault omits. Which list is canonical?
3. **Rig-over for a distant heater on one mobilization.** F9 covers nearby heaters only. Is a distant move still a rig-over?
4. **Coil-condition grade vs never-flag.** `_canonical-heater-card.md:341, 359` grades "final pig size short of max pig OD" as `heavy`. Equipment `:123-126` says never flag a size for sitting below the default. Is a grade a flag?
5. **Multi-bore Max pig OD format** on the single-valued card field (V1). One cell listing each bore, or one row per bore?
6. **4" GPM figure.** SOP `:128` says *"at 1.5 ft/s ≈ 54 GPM"*. My computation gives ≈58.7 GPM for 4.000" ID; 54 matches 3.826" (Sch 80). Computed, not measured. Lane 4.
7. **"Missing Clean ID" as a billing variance** (ops `:99`). Clean ID has been a sizing input since 2026-09-03, so does its absence still matter for invoicing?
8. **Loop arrangement: permanent or per job?** Core `:160` and ingest `:259` say *"a permanent physical fact, not a per-job choice"*. The 2026-09-02 rulings call the looped end a per-job election, and F-501 uses temporary 180° spools.
9. **Config Rollup "Per circuit" row on looped heaters.** It is defined as one coil, while core `:48` now defines circuit as what one pig travels.
10. **Job-report companions vs ingest.** Ingest `:417` says job reports are *"NOT stored as standalone job files"*, yet `USA26041-job-report.md`, `USA26038-job-report.md` and `CAD26001-flow-tests.md` exist at site level (`active-jobs.md:21` links one). Are these intended `/report` products outside ingest's scope?
11. **Receipt-extraction layout lives only in memory.** `feedback-receipt-extraction-format.md` ("TOTAL TASK HOURS … M/D Total … Project Total", settled 2026-09-26/27) is not in fieldpm, which ends with *"TO DATE — [n] shifts"*. Promote it to the skill?
12. **Confidentiality footer.** report-structure `:383` requires a *"Confidentiality/footer line on every page"*, but its own footer spec (`:29`) and the build spec (`:113`) carry no confidentiality text.

Considered and **not** findings: fieldpm `:222`, *"never as a claim about what the deposit was"*, sits beside item 4's `hard | brittle | powdery` fragment capture, so it reads as the round-2 rule rather than the struck round-1 one. Ops `:126` and report-structure `:6` name SharePoint as Jesse's filing location, not as something a session reads. Rig-in, Smart Pig 2 hrs/pass, tie-round-down, the Pig-line split, the baseline rate table (30 rows), the rollup figures, the brand table and the Waterous / Honeycomb registry all agree across skills and vault.

---

## Apply Log

**2026-10-01 (Jesse, same day).**

- **Part 1 — F1–F21 and F23–F25 accepted and merged.** `drift/2026-10` merged into config `main` as `40377e5` (no-ff, branch kept). Diff read line by line before merge and matched this note; test-merge against `dc43f11` (DQ-033 README edit) was clean.
- **F22 — renderer left until the next job report is due.** USA26046 may be the next one; do the build first if so.
- **Part 2 — re-cut F3, F6, F2, then F1**, in a dedicated session. Queued as an owed build in [[decision-queue]] (DQ-036). Until done, F3/F6 replays fail on inverted keys and F2 key 10 is stale (F16 merged).
- **Part 3 — V1–V7 fixed in the vault the same day.** V1's multi-bore format ruled **cell + table** ("Per tube size — see table below", then Section / ID / Max pig OD), matching PR-170002 and PR-170029; applied to `_canonical-heater-card.md` and `_heater-template.md`, which also take "looped to N circuits". V2 glossary (Governing tube ID, Maximum pig OD, Launcher, Receiver), V3 manual 10 §10.3 and `sop-formatting-standard.md`, V4 Honeycomb row in `equipment-library.md`, V5 seed template and governance, V6 `estimating-approach.md` only-records line, V7 drift-loop spec git-guard sentence.
- **Part 4 — memory corrected by hand** (see the checkbox above).
- **Open questions 1–12 — all answered the same day** (Q5 in Part 3's pass, the other eleven in three rounds). Rulings and what each changed are in DQ-037's Closed row in [[decision-queue]]. One answer added a rule nobody asked about: **customer documents list pig sizes only, never pig types** — the report reference is updated, and the renderer's TC/HR/FOAM/SWAB columns join the F22 build, which should now run before the next customer job report.
