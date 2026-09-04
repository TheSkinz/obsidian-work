---
type: note
status: complete
created: 2026-09-03
tags: [inbox, regression, skills, session-record]
---

# Regression battery, 2026-09-03 — what ran and what it found

Index note for the session that cleared the replay debt owed since 2026-09-02. Full plan and judging record at `~/.claude/plans/plan-mode-plan-the-flickering-lightning.md`; runs at `~/.claude/regression/runs/claude-opus-5/f{1,2,4,6}-replay-2026-09-03.md`.

## Result

Four fixtures replayed blind, all four passing their surviving diff keys. Three re-cut.

| Fixture | Keys | Verdict | Effect |
|---|---|---|---|
| F6 | 11 of 11 surviving | pass | duration 48 → 40 hrs; **re-cut** |
| F1 | 9 of 9 surviving | pass | duration 48 → 37 hrs, total $61,595.60 → $50,492.60; **re-cut** |
| F4 | 7 of 7 + new key 8 | pass | struck port-naming and role-boundary content corrected; **re-cut** |
| F2 | 9 of 10 | **missed key 10** | not re-cut — awaiting a core patch, then a re-run |

F3 and F5 were **judged not to need a replay**, with evidence: `references/extraction-format.md` (what F3 executes) is untouched since its baseline and 21 of its 25 `behind` commits are the job-report generator it never invokes; F5's only equipment commit is the port-naming and looped-end correction, and F5's frozen output already stated the corrected position independently.

## Why three baselines were wrong

Two rules struck on 2026-08-23 — the 25–40% parallel-friction allowance and the whole-shift landing rule — were still encoded as *requirements* in F1's and F6's frozen outputs, so a run following the current skill correctly would have failed. **F4 turned out to be a third and nobody had flagged it**: it carried `Trimax rear CONV port` / `RAD port` in four places against `fc7f8f6`, and wrote the launcher install as USADebusk's own work against `9cddfaf`. It went unseen because all seven of F4's diff keys were structural — none looked at content — which is why a new content key 8 was added at re-cut.

**Standing lesson: when a rule is struck, grep `frozen/` for it the same day.** A frozen output encoding a retired rule does not fail loudly; it silently redefines a regression as the standard.

## Confidence in the re-cuts

The lines that should not have moved did not move, to the cent. F1 reproduced mob $3,648.00 / demob $3,648.00, per diem $1,800.00, crew truck Qty 1, max pig OD 4.250", and the four-term piece-count swing at **$552.00**. F6 reproduced its whole mob/demob build-up line for line. Only rate-driven lines moved, which is what distinguishes a rule change from model drift.

## Rulings made this session

- **Derate gate: only records open it** (Jesse, 2026-09-03). A customer's stated expected condition — *"cleaned 3 years ago, nominal buildup expected"* — is a claim, not a known fouling history. The gate needs prior actuals on that heater, a recorded fouling history, or hard service Jesse has personally seen. This is what puts F1 on the round 100 ft/hr. Recorded in `change-log.md` and in F1's frontmatter as `derate_gate_RULING`, deliberately: the allowance this battery once manufactured carried Jesse's name with no ruling behind it, and this figure does not.
- **F2 key 10: sharpen core's pointer** rather than demote the key — see the linked note for the proposed wording, which is awaiting approval before any edit.

## Open, one note each

- [[2026-09-03-core-154-looped-max-od-pointer]] — the F2 patch, blocking F2's re-run
- [[2026-09-03-fitter-adder-absorbed-at-rig-in-cap]] — ~4 hrs of stated exposure vanishing at the 12-hr cap
- [[2026-09-03-stated-values-only-vs-config-rollup-derived]] — two schema texts contradicting
- [[2026-09-03-nearest-even-rounding-gaps]] — undefined ties, and an unbounded discretionary hatch
- [[2026-09-03-regression-coverage-gaps]] — F2's uncompelled schema fields, no `/report` fixture, and the tool's inability to say "judged, not owed"
- [[2026-09-03-sop-voice-pipefitter-role]] — whether an SOP body is customer-facing, and `9cddfaf` disagreeing with its own worked example

## Protocol change

Blinding now fences the vault's `06-reviews/` as well as `~/.claude/regression/`. The F6 run found `06-reviews/2026-08-08-prestaged-f6-rig-tier-decision.md` — a note naming that fixture and carrying its expected figures — outside the fence as it stood. It handled the contamination correctly and the leak is disclosed in F6's frontmatter rather than hidden, but fixture answers live in the vault and the protocol had not accounted for that.

**Second leak, same day, new directory — the fence is not converging.** The verification replay below ran F6 under both fences and it leaked anyway, this time from `archive/2026-07-25-f6-divergences-awaiting-adjudication.md`, which records a re-promoted replay of that exact job data at *"raw 41 → 45, quoted unchanged at 48."* The run again handled it correctly and disclosed it unprompted — it refused to reverse-engineer the gap toward the leaked figure, argued the 45/48 was stale because it predates both the 2026-08-23 landing-rule removal and the derate gate, and landed on 40 from the rules, which is the frozen figure. Also noted: F1 and F6 both read `50-dashboards/health.md` as a session-startup requirement, and that dashboard publishes the **fixture roster by name** with each one's behind-count. No values leak there, but the existence and staleness of every fixture does.

**A denylist extended once per leak cannot converge** — it is always one directory behind the next note someone writes. The shape that would converge is an **allowlist**: name what a replay *may* read (the loaded skills, `01-context/`, `02-facilities/`, `04-knowledge/`, the specific vault files a fixture declares) and fence everything else by default. Not designed, and it is a harness-contract change rather than something to apply in passing — recorded here as the proposal, for Jesse.

---

## Verification replay, 2026-09-03 — after the four terminology commits

The four fouling-terminology commits (`3ea505a`, `fa4af93`, `f646dcb`, `b173e05`) landed **immediately after** the battery above re-cut F1/F4/F6 at `6b6d4a8`, putting all three 4 behind on skills they actually load. Replayed blind to ask one question: did the terminology change move the output. Runs at `runs/claude-opus-5/f{1,4,6}-*-2026-09-03-postterm.md`; config commit `dd177fc`.

**It moved all three, and not one of the moves is visible to any of the 28 surviving diff keys.** "Passes its keys" and "did not move" turned out to be different answers, which is worth carrying forward as a judging distinction.

| Fixture | Keys | Numerics | What moved |
|---|---|---|---|
| F1 | pass 9/9 | exact | dropped 3 of 4 negative-scope statements; added expectation-language tagging |
| F6 | pass 13/13 | exact | dropped its scaffolding bullet outright — zero occurrences of the string |
| F4 | **fail key 6** | exact | added the joint-basis completion block |

F1 and F6 both dropped negative-scope prose, which is `usadebusk-estimating:463` working. Frozen F1 carried four such statements including *"Jumper spools are not required for this scope … Scaffolding is not required"*; the replay carries one, and it is the intake-checklist echo of the customer's own RFQ item rather than a proposal-body claim. F4 added a block stating all three completion criteria together plus the final pig size against the section's Clean ID, where frozen stated two criteria in three places and no final pig size anywhere — `usadebusk-sop:102` working, and precisely the class `diff_key_8_WHY` was added to catch.

**F4 fails diff key 6, and it has nothing to do with the terminology change.** Roughly ten em dashes as sentence punctuation in the SOP body against frozen's two, plus ranges rendered `150–300 PSI` where frozen deliberately writes `150 to 300`. `sop-formatting-standard.md:24` bans them and the baseline's own `em_dash_note` says to fail exactly this. No terminology commit touches punctuation — independent drift, judge it on its own.

**A near-miss worth recording.** F1's quotation read $50,681.40 against frozen's $50,492.60 and looked like an automatic numeric fail. The entire $188.80 is the pig-count line, and the baseline's own `pig_quantity_note` pre-declares that field as expected variance — *"Judge the METHOD, not the count"* — with 48 already on its list of previously observed values. A judge who applied the README's "any numeric drift = fail" rule without reading the per-fixture frontmatter would have reported a false failure.

**Nothing was re-cut.** `frozen/` is untouched and all three still read `behind`, which is correct — these runs were cut to answer a question, not to promote. F1 and F6 are clean re-cut candidates whenever the promotion is worth spending; F4 is not, until the em-dash drift is patched or accepted.

### The standing lesson above was broken the day it was written

This note says: *"when a rule is struck, grep `frozen/` for it the same day. A frozen output encoding a retired rule does not fail loudly; it silently redefines a regression as the standard."*

Hours after that was written, the same session struck the **Clean ID** definition — and did not grep `frozen/`. `frozen/f3-extract-output.md` still encodes *"Clean ID is defined as maximum pig size run"* at its lines 13, 15 and 98, and asserts *"A two-pass ticket cannot carry one honest Clean ID,"* which is false now that Clean ID is a property of the tube rather than of the shift. Its diff key 3 accepts the wrong reading as a pass and `REPLAY-CHECKLIST.md:95` grades on it, so **a correctly-behaving extractor now fails this baseline**.

F3 was excluded from that session's scope on staleness-count grounds — *"already 9, 25 and 3 behind"* — not from having read its content, so the exclusion never reached this. It also carries the identical arithmetic signature that exposed the error in the first place: a "Clean ID" of 4.125" against a 4.026" bore, the same shape as the specimen's 6.25" against a 6.065" bore that made Jesse look twice.

**F3 owes a replay-and-re-cut in its own session**, ranked ahead of routine baseline debt because it is the last live copy of a definition ruled dead. Budget a full session: `usadebusk-fieldpm` carries `disable-model-invocation: true` so the agent must read `SKILL.md` and `references/` from disk, and the fixture input is deliberately ambiguous, so the judging call is genuinely hard. Reported, not touched, per Jesse 2026-09-03. See also [[2026-08-15-idea-frozen-baselines-may-carry-unexercised-convention-defects]], whose thesis this is a concrete instance of.
