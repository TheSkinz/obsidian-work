---
type: idea-seed
status: unexplored
created: 2026-07-26
tags: [idea, vault-system, future, estimating, knowledge-system]
---

# Vault-wide stats layer — overall stats across every dimension

Idea seed captured 2026-07-26 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** Jesse's ask is a way to see overall stats across the whole system rather than one card at a time — every job and per facility, covering equipment / TriMax, tube geometry, pigs by size against tube size and footage, filter press, smart-pig vs non-smart-pig jobs, multi-ID vs single-ID heaters, convection vs radiant, and task durations. The motivating context is that **none of this is tracked anywhere in the field**; the vault is the first place it has been consolidated, so there is no external source to fall back on and the return on querying what is already here is unusually high.

**The distinction that came out of the discussion, and the durable part of this seed:** descriptive and validation stats work fine on sparse data; predictive or fitted rates do not. Validation needs one distribution and one outlier, not volume — you do not need a hundred points to know a 5.5" pig in a 5.043" tube is out of family. Claude initially conflated the two and let a caution about *modelling* on thin data gate the entire *descriptive* idea, which was wrong and is recorded here so the next session does not repeat it. The only line worth holding is that a stat should not silently become a quoted number without Jesse ruling on it — that is about how a figure is used downstream, not about what gets counted.

**Why it earns its keep — five real defects caught in one session, all the same shape** (a value out of family with its distribution, each found by manual cross-reading that a stats surface would have made instant):

- DSP25123's $35/hr Filtration Standby against $150/hr everywhere else
- SOP-DCK-F901-001 instructing a 5.5" max pig OD against a 5.043" governing ID — safety-relevant, not bookkeeping
- F-901 radiant footage that does not multiply out: 18 tubes × ~89 ft ≠ the stated 1,200 ft
- Honeycomb tool *lengths* (76" / 84" / 104") sitting in a pig-diameter column on H-19/H-20
- `A335 Gr P9` (×9) and `A-335 P9` (×4) recorded as if they were different alloys

**Coverage baseline, measured 2026-07-26** — what a stats layer would have to work with today:

| Data | Coverage | Queried today |
|---|---|---|
| Tube Geometry (79 section rows: 45 radiant, 32 convection, 2 specialty) | 32/32 cards | nothing reads it |
| — with tube ID / metallurgy / arrangement | 32 / 31 / 30 | — |
| Config Rollup heater totals | 32/32 | partially |
| Connection Info | 32/32 | nothing reads it |
| Job Options (filtration + smart-pig election) | 32/32 | nothing reads it |
| Task Durations | 17/32 (22 rows) | `estimating_rollup.py` |
| Pig Specifications | 23/32 (78 actual rows) | `pig_usage_rollup.py` |

Already computable, never computed: 13 multi-ID vs 19 single-ID heaters · smart pigging 14 Elected / 7 Declined / 11 TBD · filtration 13 / 7 / 11 / 1 Optional · 19 one-rig jobs vs 3 two-rig.

**Not captured in any structured form, so no stat can exist until they are:** filter press hours, which specific TriMax unit ran, flow test results. All prose-only today (18, 3 and 16 files respectively). Widening capture at ingest is a prerequisite for those dimensions, and is a Lane 4 card-schema decision.

**To explore:** What is the right shape — more generated rollups on the proven `estimating_rollup.py` pattern, a spreadsheet, a dashboard, or something queried on demand rather than materialized? How much does a validation-oriented surface differ in design from an analysis-oriented one, given validation is the use case with the strongest evidence behind it? Which dimensions genuinely need new capture at ingest versus already sitting in the cards unread? Does a stats surface change the estimating workflow, or is its real job checking claims and data that do not make sense — Jesse's own framing, and the stronger argument? And how does it stay honest as it grows: keeping quoted separate from actual, sparse separate from dense, and physical relationships separate from negotiated ones like rates, which expire with their contract and have no meaningful aggregate.

**Framing from Jesse, 2026-07-26, that should shape the whole exploration:** automation has been pushed ahead of system and data maturity, and the system should be built up first. Current working mode is discrete tasks — analyze drawings → build a heater card, done; build a job report, done — and that is the right altitude for now. Nothing gets built without Jesse ruling on it.

---

## Triage done with Jesse at end of session, 2026-07-26

He asked for exactly this — explore the ideas, keep the good, toss the bad. Recorded so the fresh session starts from the verdict rather than re-running it.

**Keep.**

- **Validation — using stats to check whether a value makes sense.** Strongest idea raised. Works at current data volume because catching an outlier needs one distribution, not a hundred points. Best value per unit of effort of anything discussed.
- **Tube geometry stats.** 32/32 coverage, nothing reads it, no new capture required. Cheapest real value available.
- **Per-facility and per-job as the aggregation grain.** Matches how Jesse actually bids.
- **Tracking what the field doesn't track — ranked above the tooling question.** If nobody in this niche records pig consumption against tube ID, or ft/hr by coil condition, and Jesse does, that is a durable asset for bidding and for defending a number to a customer. It outlives whatever tool gets built. Under-weighted during the session; it should probably lead the next one.

**Toss.**

- **Filter press / specific TriMax unit / flow test stats.** The data doesn't exist, and capturing it is permanent friction on every future ingest for dimensions never once needed. Revisit only when something concrete asks.
- **A single combined dashboard.** The deciding reason is not evidentiary hygiene — it is that a dashboard must be remembered and opened. Jesse's stated pattern is that he does not track triggers, which is why the health dashboard surfaces at session start rather than waiting. Anything requiring him to go look will go unread.
- **Stats reducing how often Claude must stop and ask.** Mostly wishful. Of the interruptions in this session, only one of four was a data question; the rest were judgment and world-knowledge. Expect maybe a third fewer, not most.

**Genuinely uncertain — needs Jesse, not analysis.** Whether the smart-pig vs non-smart-pig and multi-ID vs single-ID splits would ever actually get used. Both computable today.

## Finding that arrived after this seed was first written

**All five defects were caught by checking a value against a rule, not by reading a distribution.** A pig OD exceeding tube ID + 0.250 · a tube count × length not equalling stated footage · a diameter column holding a length · two spellings of one alloy · a rate not matching its siblings. That is lint, not statistics — which suggests the validation half belongs in `tools/vault_lint.py`, something that already runs unprompted and reports without being asked, rather than in a page someone must open.

**Prerequisite if that route is taken:** the linter currently has noise that would blunt it. Roughly 15 of its 36 warnings come from rule design rather than from anything wrong in the vault. Verified: `vault_lint.py` omits the `sys.stdout.reconfigure(encoding="utf-8")` its three sibling tools all have, so output carries mojibake and bytes that break `grep` and `sort`; `vault_health.py:361` hardcodes the lint-warning row to `flag(True)`, so the count can never signal drift; DEAD-LINK cannot distinguish a wikilink from prose *about* one, producing false positives in `change-log.md`. Design-level: ORPHAN's premise that value equals inbound wikilinks fails for concept files referenced from skills outside the vault (it currently advises archiving `equipment-library.md`) and for terminal artifacts like completed review notes; STATUS-VOCAB rejects five values people naturally reach for, with `closed-unactioned` valid but bare `closed` not. Jesse dropped the fix thread in session — recorded as context, not as a task.

Related: [[idea-pig-actuals-maturation]] (closed — the pig half shipped as `pig_usage_rollup.py`), [[rfq-intake-protocol]] (the deferred cross-quote rate-history rollup, 7 of ~12 quote notes), [[quote-lifecycle]] (why rates get no aggregate stat).
