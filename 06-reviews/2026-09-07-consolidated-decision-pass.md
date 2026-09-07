---
type: review
status: open
review_type: canonical-update
source_authority: stated
confidence: high
created: 2026-09-07
review_after: 2026-09-21
related:
  - "[[decision-queue]]"
  - "[[2026-09-01-skill-drift-review]]"
  - "[[2026-08-16-prestaged-pointer-dead-severity-tiering]]"
  - "[[2026-08-19-prestaged-treat-gas-loss-nominal-basis]]"
  - "[[2026-08-20-prestaged-ut-data-loss-air-and-fouling]]"
tags: [review, knowledge-system, decision-pass, lane4]
---

# Consolidated decision pass — 2026-09-07

## Trigger

Clearing the two inbox-age FAIL rows meant reading all 39 notes in the ≥14 d inbox tail. Not one was an unfiled capture record. They are rulings addressed to Jesse and owed work sessions — a backlog no filing pass can clear. He asked for the decision-ready ones in a single sitting.

Every candidate below was verified against current file state, not against what its own note claims. **Four notes turned out to be already ruled** and are listed under Closed Without Asking rather than put to him again.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `50-dashboards/decision-queue.md` `## Open` | stated | 6 rows: DQ-016, 017, 019, 024, 025, 029 |
| `06-reviews/` pending-decision notes | stated | 3 notes — all three are the source notes for DQ-019, DQ-024, DQ-025. A strict subset, not additional items |
| `06-reviews/2026-09-01-skill-drift-review.md` | stated | `status: open`, 16 unchecked boxes, **0 `## Decision` headings** — invisible to `count_pending_reviews()` |
| 14 inbox notes posing questions | mixed | 5 decidable, 4 already ruled, 5 not decisions |

**Three counting facts worth stating up front.** The dashboard's "6 open decisions" and "3 review notes awaiting decision" measure overlapping sets, so the real figure was 6, not 9. Two of those six (DQ-016, DQ-017) are settled builds waiting for hands, not questions — DQ-016's own row says "Design is settled by the 2026-08-11 evidence." And the largest ready block, the seven skill-drift rulings, is counted by nothing at all.

---

# Tier 1 — Lane 4, genuinely yours

## 1. DQ-025 — where does the UT data-loss fact live, and does F-501's B_8_C get a caveat?

**What it is.** On 2026-08-16 you said air and fouling are the two standing causes of UT data loss on smart-pig runs, that many coils have no high-point bleeders, and that the USADebusk bleeding method does not always work. That fact currently lives only in an inbox note. Separately, `F-501.md:295-301` presents B_8_C as 0.224" remaining against 0.400" nominal, 43.9% loss, with **no data-quality caveat at all**.

The two failure modes are not symmetrical, and that asymmetry is the commercially important part: air causes dropout, so you lose data and can see that you lost it. Residual fouling can add an interface the tool gates on, producing a reading that looks valid and reads thin.

**Options A1, A2, B and C are mutually exclusive — pick one. D and E are additive and ride with any of them.**

| Option | What it does | What it costs |
|---|---|---|
| **A1** | A short note under `04-knowledge/`, outside the manual | Keeps the edit out of the SharePoint projection until you decide it belongs there |
| **A2** | Amend `manual/14` — extend §14.3 or add §14.8 on data-quality limits | `manual/14` projects to the SharePoint `Knowledge` library (`sharepoint_export.py:100`), so this reaches a shared internal surface on the next export. Internal only — every member of the Furnace Decoking site is trusted with all of its data |
| **B** | Record it on `F-501` only, generalise later | A general rule written now off one segment is a rule written from the weakest available evidence |
| **C** | Leave it in `00-inbox/` as captured | "Giving it a permanent home now spends a Lane 4 ruling on a fact with no current consumer" |
| **D** *(additive)* | Attach the asymmetry to the cleaning-verification claim wherever it is written | **One sentence.** The review calls this "the highest-leverage half of the whole item: it is the piece that protects USADebusk commercially" |
| **E** *(additive)* | Add a validity caveat to F-501's B_8_C entry while the vendor question is open | Counter-argument is that the card is already honest about its limits — but "no threshold supplied" and "the reading may not be valid" are different limitations, and only the first is written down |

**If nothing is done.** "The first unflattering report will be read against USADebusk for something that was never in scope." A noisy C-scan is not evidence of poor cleaning — trapped air produces the same signature and is a coil-venting limitation, not a cleaning failure.

**What is blocked.** **E only.** You put the B_8_C question to Steady Flux on 2026-08-16 and it is still unanswered at 22 days; their raw A-scan waveforms settle whether the dropout is coupling, residual fouling or surface condition, and nothing on the USADebusk side can. **D is not blocked** — the asymmetry is a physics fact about what a noisy scan can and cannot prove, true whichever way B_8_C resolves. Do not let the home question hold D hostage.

---

## 2. DQ-024 — F-501 Treat Gas loss: is 0.375" the nominal or the minimum wall?

**What it is.** Steady Flux report 26-0663-002 Rev. A calls the same number two things. Table 4 says `5-inch schedule 80 (5.563 in x 0.375 MWT)` — minimum wall. The results header calls it **Nominal Wall Thickness**. A53/A106 permit −12.5%, so if it is nominal, **0.328" is an acceptable as-new wall** and 28 of the 31 Treat Gas readings sit above it.

The magnitude: the worst point, A_7_TG at 0.321", is **14.4% below 0.375" but only 2.1% below 0.328"**. The two readings of one measurement differ by roughly a factor of seven. `F-501.md:304` currently states, unqualified: "Treat Gas a uniform 9–14.5%, min 0.321" at A_7_TG. The Treat Gas pattern is general thinning."

It cuts both ways — if 0.400 and 0.464 on the 9Cr sections are genuinely minimum wall as Table 4 says, real loss **there** is understated.

**Options A, B and C are mutually exclusive. D is additive.**

| Option | What it does | What it costs |
|---|---|---|
| **A** | Qualify the card now; change no number | "The caveat costs nothing and the exposure is asymmetric." Weakness: the −12.5% argument is not established for this pipe — the card records metallurgy only as "carbon steel, no grade." If it was procured to a minimum wall, a caveat written now is a **wrong** caveat, not a cautious one |
| **B** | Ask Steady Flux first, write after | Near-zero — the channel is warm, you sent the audit findings to their CEO on 2026-08-16 and already have an open B_8_C question riding it |
| **C** | Leave the card as written | "Adding a hedge to a section nothing depends on is ceremony." But it leaves an unqualified characterisation of a customer's asset on a card that feeds proposals |
| **D** *(additive)* | Settle the nominal-vs-minimum convention once, for every section and every future report | Short to write. Risk is scope creep from n=1 — "n=1 conventions written into a skill are how the vault has previously acquired rules it later had to unpick." Weakest-evidenced of the four |

**If nothing is done.** "If the question is not asked in the same conversation as the audit findings, it likely never gets asked, and the card sits unqualified anyway — **which is Option C by default rather than by decision.**" Vendor goodwill and technician recall are freshest now; F-501's next scope is years out. No pending bid and no money at risk.

**One caveat on my own evidence.** The "28 of 31 readings above 0.328" figure comes from the inbox note and was **not** re-checked against the PDF. That is recoverable locally if it matters to your answer.

---

## 3. Honeycomb — a registry row, and three cells recording a length as a diameter

**What it is.** Two answers, both from your own knowledge, neither needing research.

**(a) The registry gap.** HC is real and shipped — the delivered USA26038 report legend reads "Swab — dewatering swab. HC — honeycomb gauge," and that job ran **35 of them**. The canonical pig-type registry at `~/.claude/skills/usadebusk-equipment/SKILL.md` §Pig Types lists exactly four rows: Foam, TC, HR, Swab. Honeycomb is in neither that table nor the field-shorthand list (BLT, Wire Brush, Bald, Gauge). The extraction reference defers to that registry on any definition conflict, so on honeycomb it defers to nothing. **Needed: body description and use case, for a row alongside the other four.**

**(b) Three bad cells.** `H19.md:100` records `104"`, `H20.md:104` records `76"`, `H20.md:105` records `84"` — all Honeycomb, all job USA25051, all in a pig **diameter** column, all on a **3.068" bore** coil. The card itself already flags it in prose: "size appears to be a length, not an OD (104" OD impossible on this coil); confirm unit." **Needed: the honeycomb's actual OD on those coils.**

**If nothing is done.** `pig-usage-rollup.md` already flags and excludes them, so the rollup is not wrong today — but the cards are, and any future consumer that does not know to exclude them will read a 104-inch pig. No commercial exposure, no bid, no money.

---

## 4. B-151 max pig OD — cheaper than its own note says

**What it is.** `Suncor/Montreal-QC/B-151.md:63` carries `Governed by ID ~4.03" → max pig OD ≈ 4.28" (consistent with the 4" pig family used across this package)`. Its sibling B-101 carries `confirmed ID 4.026" → max pig OD ≈ 4.276"`, confirmed from the BOM on 2026-07-07. Two sibling heaters, same field, different confidence tiers, no recorded reason.

**The note's own cost estimate is wrong, and its pre-staging header says so.** The note says "cost is presumably one BOM read, the same as B-101's." But B-151's Tube Geometry row (`:39`) **already records OD 4.5" and wall 0.237"** — the same as B-101 — so ID = 4.5 − 0.474 = **4.026"** falls straight out of data already on the card. No BOM read is needed; it is arithmetic.

| Option | What it costs |
|---|---|
| Upgrade the wording to confirmed on the existing arithmetic | One card edit, no source read |
| Do the BOM read anyway for a true independent confirmation | One BOM read |
| Leave `~4.03"` and record why the siblings differ | One sentence; the discrepancy stops looking like an error |

**If nothing is done.** Nothing operational. Per the equipment skill's own rounding rule both values give the same answer — 4.026" ID → 4.276" → a **4.250" pig**. Verified 2026-07-28 that the approximate value is B-151's genuine committed state, not a silent revert; the 2026-07-19 stale-buffer incident touched B-101 only.

---

## 5. Skill-drift F1 — two frozen baselines encode rules you struck eight days later

**What it is.** The 2026-08-23 rulings struck the **25–40% parallel-friction allowance** and the **whole-shift landing**. Both are welded into f1 and f6.

`f6-duration-mobdemob-output.md:25` makes the allowance diff key 4, the thing a replay is judged on. `f1-proposal-output.md:18` puts it inside what that file calls "the single most load-bearing arithmetic in this fixture" — coil round-up, then the allowance on the rounded figure, then round the set elapsed up. f1 also carries the struck landing rule as its own line item at `:123`/`:146`.

**The detector is inverted.** A replay that correctly applies the current skill — no allowance, no landing adjustment — *fails* f1 diff keys 4 and 8 and f6 diff key 4. The only way to pass is to reproduce a rule the skill flags as dead. The health dashboard's `behind` rows understate this: it is not "unverified," it is **verified wrong**. F1 is the worse of the two because the error propagates into every downstream dollar figure rather than sitting on one line.

**Options** (from the review):

- Re-cut F6 and F1 from judged replays against current skills
- Re-cut F6 only for now; leave F1
- Leave both; the README caveat (item 12) is enough of a warning
- Something else

**Cost.** Re-cutting requires a judged clean replay first, per the suite's own "When to re-cut frozen/" — hand-patching the figures is forbidden, because re-authoring a baseline makes the arithmetic the reviewer's and destroys the record of raw model behaviour. Recommended sequence if you take it: **F6 first** (smaller, one struck rule, one line moves), judge, re-cut; then F1 (two struck rules, the rounding sequence changes, most numerics move).

**Interacts with item 8** — both concern the frozen files. Decide them together.

**Also noted, not a decision:** `f6:16` cites a "shift-landing section" of `usadebusk-estimating` that no longer exists, quoting a sentence absent from the skill.

---

## 6. Skill-drift F4 — `usadebusk-fieldpm` still teaches "crash means a dirtier coil"

**What it is.** `usadebusk-fieldpm/SKILL.md:206` asserts as fact: "**A crashed/upset furnace runs significantly dirtier**, and its hours must never be used to estimate a routine clean."

The canonical home corrected this on 2026-08-20 under DQ-026. `_canonical-heater-card.md:241-244`: "`crash` = UNSCHEDULED MOBILIZATION… **It is a callout label, NOT a fouling grade** (Jesse, 2026-08-20) — the coil is usually dirty, but not by definition, and this column does not record how dirty." And `:272-275`: the prohibition on mixing crash and routine rows "**stands on its own; it does not rest on a claim that crash coils are dirtier**, which is not something this table measures."

Second defect in the same two lines: fieldpm offers Condition as a **two-value** choice, while the canonical column is **four** — `routine | crash | first | unknown`. A `/report` run following fieldpm has no way to record a first-ever clean, and the exemplar is explicit that `unknown` must be written rather than `routine` inferred.

**This matters more than ordinary pointer drift** because `/report` is the *upstream* of the `Condition` value, not a downstream reader of it.

**Decision: Accept / Reject.** The rewrite is already drafted on the branch — accepting is the execution.

**If nothing is done.** Every `/report` run keeps writing a two-value vocabulary into a four-value column and keeps restating a retired mechanism as fact.

---

# Tier 2 — vault and tooling, carrying my recommendation

These come with a recommendation rather than an open question. Override where you disagree.

## 7. DQ-019 — POINTER-DEAD severity tiering

POINTER-DEAD sits at `warning` and folds into one undifferentiated "Lint warnings" count that `health.md` describes as backlog. Two of three 2026-08-01 findings sat dead **nine days** unnoticed, caught only by reading raw lint output during unrelated work. One of them was DSP26071's pointer, dead with the job mobilizing in ten days. A dead pointer to a customer's quote folder is not backlog — it is a broken bid trail that decayed silently.

| Option | Cost |
|---|---|
| **A** promote to lint `error` | Any future finding blocks every commit touching that note, including unrelated ones — "a much larger blast radius than the two facility notes actually affected" |
| **B** its own dashboard row, target 0, FAIL if nonzero | "A soft-signal row that never reads FAIL can be scanned past exactly like the aggregate count it replaces" |
| **C** a procedural reminder at the folder-reorg (Bids→Jobs) event that causes it | Cheapest. Risk: "a procedural reminder that lives nowhere concrete is not meaningfully different from the current status quo that already failed" |
| **D** leave as-is | Defensible on the numbers: 3 findings in ~4 weeks, all caught by the rule, all fixed same-day once surfaced. **The gap is attention, not detection** |

**Recommendation: B.** The trigger is event-shaped, not decay-shaped — pointers go stale when the OneDrive tree is reorganised on award and at cleanup — so findings arrive in clusters and a row that reads 0 almost always is exactly the shape that gets noticed when it stops reading 0. A is disproportionate; C is the status quo with a note attached.

## 8. Frozen-fixture frontmatter that does not parse — **new evidence since the note was written**

The note said five of six frozen fixtures fail a YAML parse, f5 being the only clean one, all from an unquoted value containing `": "`.

**That census is now stale, and the change kills option B.** `config_frontmatter_lint.py` today reports **6 findings — all six fail**, including f4 and f5, which were clean when the note was written. They went dirty on the 2026-09-03→06 re-promotions; f5 now carries an unquoted `promoted: … PRE-REGISTERED AND COMMITTED BEFORE THE RUN WAS DISPATCHED -- see runs/…`. **The condition regenerates on every re-promote**, so a one-time quoting sweep does not hold.

| Option | Cost |
|---|---|
| **A** leave them | "The trap stays for the next tool author, who has to already know" |
| **B** quote the offending values | Edits frozen files, which the regression discipline treats as near-immutable — **and now has to be redone after every re-promote** |
| **C** leave them, document the constraint in `regression/README.md` | One paragraph. "Converts a trap into a documented rule — but it is a comment, and comments are not enforcement" |

**Recommendation: C.** Nothing is broken today and nothing decays — the replay guard reads staged file paths, not frontmatter. The real risk is the trap: `baseline_staleness.py` was specified to read `baseline_commits:` out of these files, and `yaml.safe_load` would have returned nothing for five of six and reported them all clean. A staleness checker that silently sees no baselines is worse than no checker. `config_frontmatter_lint.py` already detects the condition; C makes the rule findable. **Verified not already done:** no mention of a line parser or `safe_load` exists in `regression/README.md`.

**Adjacent, and also yours:** the note asks whether to adopt agnix. No ruling exists in either repo. Not folded into this recommendation.

## 9. DQ-029 — which terminal statuses mean *finished and filed* vs *finished and still load-bearing*

The sweep allowlist and `vault_lint.py`'s status vocabulary have drifted in both directions. `executed` and `spec-complete` sit on the sweep allowlist while being outside `ALLOWED_STATUS` entirely — latent only because they appear solely in `archive/`, which `SKIP_SCAN` excludes. Meanwhile seven `TERMINAL_STATUS` values are absent from the allowlist.

**The obvious fix is wrong, and the row says so:** deriving the allowlist from `TERMINAL_STATUS` would sweep `awarded` and `lost`, which are quote outcomes rather than closed commitments, and `decided-blocked`/`approved-blocked`, which mean decided-but-blocked and must stay visible. So this is a vocabulary question, not a list-sync chore.

**Recommendation: state the rule, then derive the allowlist from it.** Sweepable means *the commitment is closed and the record is filed elsewhere* — `complete`, `resolved`, `superseded`, `deprecated`, `closed-unactioned`, `executed`, `spec-complete`. Not sweepable means *terminal but still load-bearing*: `awarded` and `lost` are live commercial outcomes people search for, and `decided-blocked`/`approved-blocked` describe work waiting on something. Then add `executed` and `spec-complete` to `ALLOWED_STATUS` so the two lists stop disagreeing about what words exist.

**If nothing is done.** Bounded today. The realised cost of the same class is on the record from DQ-018: a correctly-retired commitment "stays in `00-inbox/` forever — four already do," which reached seven before being cleared by hand.

## 10. Statusless notes — the class fix, relocated

A note with no `status:` field can never be swept, however finished it is, because the sweep correctly skips what it cannot parse. Two notes sat stuck five weeks for exactly this reason.

**The instance half is done** — I checked every note in `00-inbox/`, and **zero** now lack a status. **The class fix as written is unexecutable.** It was specified as "have the capture loop normalize any note missing `status:` to `status: inbox` under its Lane 1 frontmatter authority" — and the capture loop has not run since 2026-08-21. DQ-018 already caught this exact trap: "A alone is inert. The sweep runs at the end of inbox ingestion and the capture loop was disabled 2026-08-21, so nothing would have executed the new rule."

**Recommendation: rebuild it as a `vault_lint.py` rule.** `STATUS-VOCAB` fires on a *wrong* status, not an *absent* one, so nothing covers it today. A warning-tier rule gets the same "no note is invisible" guarantee via machinery that still runs. Needs a fixture under `tools/fixtures/` — the linter's own rule is no fixture, no rule. Half a session.

## 11. The change order form has no canonical home

A fillable REV001 Word form was built 2026-08-17 for a coworker, with the real logo extracted from the source PDF and all ten checkboxes as verified content controls. It lives on the Desktop. **The vault has no change order template at all** — only narrative mentions inside job notes. No pointer note exists anywhere: grep for `REV001` or `Revamped Docs` across the vault returns only the inbox note itself.

**The note undercounts the problem.** It describes two files side by side. There are now **four** generations across two folders: the REV001 editable `.docx`, a REV001 fillable `.pdf`, the superseded `OLD_USADebusk Blank Change-order.docx` still adjacent, and a fourth at `OneDrive\Desktop\Tools\Templates\USA26022_Change_Order_v2.docx`.

**Recommendation: SharePoint, with a pointer note in the vault** — matching how job docs and workups are already indexed by path. A `.docx` does not belong in `templates/`, which is markdown note scaffolding. And retire the `OLD_` copy: "anyone browsing that directory can grab the pre-REV001 layout by mistake."

**Second, smaller call:** delete the `OLD_` copy or move it to an `_History\` subfolder.

## 12. Skill-drift F2, F3, F1-side, F5, F6 — five Accept/Reject calls, all already drafted

| # | Finding | Proposed | Recommend |
|---|---|---|---|
| **F2** | `regression/README.md:52` names F6 @ `ebb1217` — the commit that *wrote* the frozen file, not the skill state it was cut against. The frontmatter says `60e86c7`, and the README's own rule at `:56` says the frontmatter is authoritative. Third instance of this defect in one table | `F6 @ 60e86c7` | **Accept** |
| **F3** | `regression/README.md:1` reads `# USADeBusk Skill Regression Suite` — a dead string per `usadebusk-core:9`. Replay *inputs* carrying the same string are deliberately untouched, since editing them would silently alter the spelling delta the README rules an expected pass | `# USADebusk Skill Regression Suite` | **Accept** |
| **F1-side** | A README caveat naming f1 and f6 as encoding the struck rules, with the affected diff keys. Touches nothing under `frozen/` and takes no position on re-cutting | add the caveat | **Accept** — it is true regardless of how item 5 goes, and it is the warning that makes "leave both" survivable |
| **F5** | `/report` never captures per-coilset hours, while `usadebusk-vault-ingest:389` is told to harvest them from the job report and warned the step is unrecoverable, and `usadebusk-estimating:34` sends the outlier check there to read them. `grep -i coilset` over fieldpm returns nothing | add per-coilset hours as a third mandatory capture item alongside the abnormality narrative | **Accept** — the Syncrude 48/35/36 spread that rule was written from had to be recovered by hand |
| **F6** | `usadebusk-vault-ingest` hardcodes `USA#####` at four places where the vault uses any job number. Live cards already disagree — `7-1-F-1.md` carries `### CAD24002` and `### CAD25004`. The skill knows about CAD# elsewhere, so this is internal inconsistency | generalise the four occurrences | **Accept** — becomes live now: CAD26001 mobilized 2026-08-25 and its actuals land on that same card |

---

# Tier 3 — not rulings, but you should know

- **The 17 untracked `archive/` snapshots are gone.** `CLAUDE.md` records "Checked 2026-09-03: 47 files tracked, 17 untracked." Today `git ls-files archive/` returns 47 and `ls archive/` returns 47, with **zero** untracked or ignored files. Because they were untracked, no commit records the removal and nothing can say who did it or when. **Confirm the deletion was intended** — this is the exact irrecoverability trap `CLAUDE.md` warns about, arriving from the other direction.
- **DSP26080 — HF Sinclair Artesia, 2027-02 execution — has been silent since 2026-06-26.** Ten weeks. Its `date-submitted` and `valid-through` are still blank. A sales follow-up, not a vault fix.
- **The 4×3 pump basis is unreconciled and sitting on live money.** `ExxonMobil/Baytown-TX/_facility.md:106,129` records `$1,016/shift` on DSP25084/25123 against `$85/hr` on DSP26039, marked "Not reconciled." `DSP26085.md:132` publishes **$85.00/hr** in the Section 8 rates that govern stand-by and overrun on T&M — on the **pending $46,657.08 Baytown 27GF1A F-201 Treat Gas quote**, valid through 2026-09-29, executing Jan 2027. At a 12-hr shift the two are near-identical ($1,020 vs $1,016), so the exposure is a basis mismatch on a partial shift, not a pricing gap. One sentence if you happen to know the governing contract's basis; not worth a research task.
- **Pig appendage hardness (AlphaMet File 23890)** — lowest stakes on the list, included only for completeness. The customer question it came from was answered 2026-07-20 and the disclosure line was settled with you then. The note names **no consequence** for leaving it in the inbox. The one genuine gap — stud projection — is not in File 23890 and needs a vendor, not you.

---

# Closed without asking

Verified already ruled. These get a terminal status and a pointer, not a question.

| Note | Closed by | Evidence |
|---|---|---|
| `2026-08-16-duplicate-workups-disagree-on-price` | DQ-022 + DQ-023, both 2026-08-18 | All three bids resolved. DSP26085's authoritative workup is the $46,657.08 copy (Jesse, 2026-08-18); DSP25138 was an abandoned draft, not a duplicate; DSP25070 needed no action |
| `2026-08-15-usa26041-estimating-feedback` | DQ-020, 2026-08-21 | All three findings ruled — per diem unchanged, pig unit filed as actuals, rig-out re-classified as not n=1 |
| `2026-08-21-two-small-calls-owed-to-jesse` | both halves dead | Pig-load-list status ruled 2026-09-03 in `208da24` (`complete` → `unexplored`); the archive question has no subject left (see Tier 3) |
| `2026-08-11-quote-notes-missing-date-submitted` | `e1e3f0e` + 2026-09-05 | DSP26085 backfilled from Jason, not from Copilot's figure, as the note demanded. Its stated rationale — the quote-expiry FAIL — was itself retired 2026-09-05 |

Also not asked, with reasons: `2026-08-01-pointer-dead-is-mis-tiered` explicitly says "Not proposing a fix" and its decidable twin is item 7; `2026-07-26-baytown-quote-loose-ends` needs bid instructions and the governing contract read, and the note forbids answering from knowledge; `2026-08-16-steady-flux-f501-report-audit-findings` is item 2 plus a transcription task (its airtight tier — Appendix D contradictions, the two-meanings header, A_15_R's ovality outlier, the undocumented crossover, the colour scales — is already sent to Steady Flux and belongs on the card's "send back for Rev B" section, which still carries only the two errors from the 2026-08-15 pass).

---

## Risks / Open Questions

- **Items 5 and 8 interact** — both concern the frozen fixtures. Deciding 5 as "re-cut" and 8 as "leave the frontmatter" is coherent; deciding 8 as "quote the values" while re-cutting means quoting twice.
- **Items 1 and 2 both wait on the same Steady Flux thread**, unanswered 22 days. If item 2 goes to B, item 1's option E should ride the same message.
- **One unverified figure**, flagged in item 2: "28 of 31 readings above 0.328" comes from the inbox note, not from the PDF.
- **A counting defect this note is itself the test for.** `count_pending_reviews()` (`tools/vault_health.py:224`) requires a `## Decision` heading *and* an unchecked box. `unqueued_decisions()` requires the same, so `Open decisions not in the queue` reads a false green for the identical reason — the completeness check shares the hole of the thing it checks. Seven pending rulings, one of them Lane 4, have been uncounted since 2026-09-01. Separately, the decision queue's `age (d)` column reads `0` on all six open rows against real ages of 17–23 days.
- **DQ-029's `source` link is broken** — it cites `2026-08-18-idea-research-researched-status-outlives-build`, which is resolved and about a different question. The actual question originated in DQ-018's outcome and is stated only in the queue row itself.
- **DQ-016 and DQ-017 are not decisions** and should leave the queue for whatever tracks owed work, so the cap means something.

## Decision

- [ ] Tier 1 ruled (items 1-6)
- [ ] Tier 2 ruled or recommendations accepted (items 7-12)
- [ ] Tier 3 acknowledged
- [ ] Counting defects fixed and queue reconciled

## Apply Log

(Pending — Jesse to rule.)
