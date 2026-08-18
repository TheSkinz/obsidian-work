---
type: review
status: resolved
decided: 2026-08-18
decision: "Option A — Jobs copy ($46,657.08) authoritative; Bids copy ($40,477.08) disposed of. DSP25138/DSP25070 deferred; Option D not taken up."
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-18
related:
  - "[[DSP26085]]"
  - "[[2026-08-16-duplicate-workups-disagree-on-price]]"
  - "[[2026-07-24-dsp26085-submitted-wrong-quote-number]]"
  - "[[idea-quotation-workup-reconciliation-check]]"
tags: [review, estimating, quotes, data-quality, exxon-baytown, pre-staged]
---

# Review — Which workup copy is authoritative on the three bids that hold two, and does the stray get deleted or labelled?

## Trigger

Pre-staging loop run 2026-08-18, processing `00-inbox/2026-08-16-duplicate-workups-disagree-on-price.md` — the oldest unprocessed candidate carrying the `vault-loop:` marker without a `vault-prestaged:` marker (git first-commit 2026-08-16T01:26, ahead of the five other same-date candidates at 15:34 and later). No items were skipped this run; this was the first candidate examined.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-08-16-duplicate-workups-disagree-on-price.md` (read this run) | Observed | The finding itself, filed while building the pre-send gate (DQ-015). Six DSP#-era workup filenames exist twice under the canonical store; three pairs disagree on total — DSP26085 by **$6,180.00**, DSP25138 Valero McKee by **$96,343.64**, DSP25070 Exxon PS3 by **$7,371.34** — and three agree (DSP26061, DSP26075) or are unreadable by the older template (DSP24144). Note states explicitly that nothing was changed in any file and that the per-bid authoritative-copy ruling is Jesse's. Its own framing of the question is the sharp one: not "why do these differ" but "is the copy someone would open the authoritative one." |
| Canonical store, `find` over `ExxonMobil/**/*26085*Workup*.xlsx` (run read-only this run, 2026-08-18) | Observed | **Both DSP26085 copies are still present and unchanged since the finding.** `Bids/Exxon Baytown_F-201/` — 2026-07-07 09:27, 1,151,341 bytes. `Jobs/` — 2026-07-25 15:26, 1,307,343 bytes. Same filename, 156 KB apart. Confirms this is live and undisposed, not something already handled off-vault. |
| `02-facilities/ExxonMobil/Baytown-TX/DSP26085.md` (read this run) | Observed | Records `value: 40477.08`, `status: pending`, `valid-through: 2026-09-29`, `date-execution: 2027-01`, `verified: 2026-07-27`. Its **Source Files** block names the `Bids\Exxon Baytown_F-201\` path only — the $40,477.08 copy. The Pricing table's Mechanical Decoke line reads **$23,580.00**, matching the Bids copy; the Jobs copy's $29,760.00 has no counterpart anywhere in the vault. So the vault's recorded truth is unambiguous even though the store is not. |
| `archive/2026-07-24-dsp26085-submitted-wrong-quote-number.md` (read this run) | Observed | The precedent and the date collision. The 2026-07-25 quote-number fix was a ten-byte patch inside `word/media/image6.emf` that deliberately avoided re-pasting from Excel, and the note records the total holding at $40,477.08 — so it does not explain the Jobs copy's $6,180, but it is the same day. Also the disposal precedent: `DSP#26071.1_...Rev001.docx` carried Rev002's entire pricing block (a $37,846.84 error under a Rev001 filename); Jesse's call was **delete**, keeping the native PDF as the authoritative record. That note also states the estate scan covered **quotations only** — workups were never scanned, which is why these sat a year. |
| `~/.claude/skills/usadebusk-estimating/scripts/backtest_workup.py:41-61, 95` (read this run) | Observed | Partial coverage, already shipped. `resolve()` raises rather than first-matching when a filename is ambiguous, and DSP26085's case carries `"prefer": r"\Bids"`. Its docstring names this exact pair and both totals. This makes the **regression suite** deterministic; it does not rule which copy is authoritative and does not look at any bid not in `CASES`. |
| `~/.claude/skills/usadebusk-estimating/scripts/presend_gate.py:372-386` (read this run) | Observed | Second half of the existing coverage. `find_pair()` returns every match and its docstring states it "Reports ambiguity rather than choosing," citing DSP26085 by name and the $6,180 gap. So a divergent pair **is** caught — but only at the moment someone runs the gate on that specific quote number, which happens per-bid before a send. Nothing sweeps the estate for new pairs. |
| `50-dashboards/health.md:37, 43` (read this run) | Observed | The `Bid folder` column is explicitly "a soft signal, not a gate" doing existence-and-recency only, and its own text defers value reconciliation to the pre-send gate. The DSP26085 row currently reads `ok` under both **Signal** and **Bid folder** — the dashboard shows a clean live bid while two copies of its workup differ by $6,180. Not a defect in the column (it is doing what it says), but it means the dashboard will never surface this class. |
| `50-dashboards/decision-queue.md` (read this run) | Observed | Six open rows, DQ-016 through DQ-021 — none concern duplicate workups, authoritative-copy rulings, or the canonical store's file hygiene. DQ-015 (closed 2026-08-15) built the pre-send gate and its outcome text records the DSP26085 `Jobs` copy blocking on the $6,180 matched-scope gap, but closing it settled the *tool*, not the *files*. Not already queued. |
| `git log --since=2026-08-10` on the vault and on `~/.claude` (checked this run) | Observed | No commit since the 2026-08-16 filing touches the duplicate-workup question. The estimating-script commits in the window (`c7d31c2` pre-send gate, `19ed522`/`a8cc6fd` F1 crew-truck) are the tooling half already accounted for above. Confirms genuinely undecided rather than merely unfound in prose. |

## The Question

Per bid, which copy is authoritative, and what happens to the stray — deleted on the DSP26071.1 precedent, or kept as a labelled superseded revision? **DSP26085 is the one with a clock on it:** it is the only pending bid of the three, valid through 2026-09-29 with 2027-01 execution, and a $6,180 ambiguity sits on a live number. DSP25138 and DSP25070 are historical (executed July 2026; became USA26007) and have no vault quote note, so they are data integrity rather than commercial exposure.

**Not proposed here — this is Lane 4.** Which copy is the real one is a pricing/customer-facing fact this loop cannot rule on, and deleting a file in the canonical store is irreversible. What follows frames the disposition pattern; the ruling itself is Jesse's.

## Proposed Change

*A, B and C are mutually exclusive dispositions — pick one. D is additive and can be approved alongside whichever of A/B/C is chosen, or on its own.*

**A. Rule DSP26085 now, defer the two historical bids.** Decide the live one (the vault, the submitted quotation, the frozen regression expectation and the `Bids` copy all agree at $40,477.08 — the Jobs copy is the outlier with no quotation beside it), and leave DSP25138 and DSP25070 as an untimed cleanup item. Smallest action, matches the source note's own "DSP26085 first" recommendation, and keeps an irreversible deletion decision scoped to one file whose evidence is strongest.

- [ ] Approved
- [x] Approved with edits — *2026-08-18: taken, but the ruling inverted to the `Jobs` copy at $46,657.08*
- [ ] Rejected
- [ ] Needs more research

**B. Rule all three now, bid by bid.** Same ruling for DSP26085, plus explicit calls on DSP25138 (the odd copy sits loose at the facility root, in neither `Bids` nor `Jobs`) and DSP25070 (the second copy is under `_History\`, which is plausibly a deliberate archive of a superseded revision — the source note flags this as the case where a differing total may be correct behaviour). Clears the class in one pass while the evidence is assembled, at the cost of two rulings on bids where nothing is at stake this year.

- [ ] Approved
- [ ] Approved with edits
- [x] Rejected — *2026-08-18: superseded by A; DSP25138 and DSP25070 stay deferred*
- [ ] Needs more research

**C. Adopt a standing folder-of-record rule instead of per-bid rulings.** Rather than three judgments, write one convention — e.g. the copy in the folder matching the bid's current lifecycle state is authoritative, `_History\` is a legitimate archive and its divergence is expected, and a copy loose at a facility root is presumed stray — then apply it mechanically to all three and to future pairs. Converts a recurring judgment into a rule, but the source note's DSP25070 caveat is exactly the case where a blanket rule could delete a deliberate archive.

- [ ] Approved
- [ ] Approved with edits
- [x] Rejected — *2026-08-18: superseded by A. Worth noting the DSP26085 case would have broken a folder-of-record rule too: the authoritative copy was the one in `Jobs\` on a bid that was never awarded*
- [ ] Needs more research

**D (additive). Close the detection gap at the `Bids/ → Jobs/` move.** The source note's own follow-on: the award move is what creates most of these pairs, and nothing checks the two copies match at the moment of the move. Existing coverage is per-bid and on-demand only — `backtest_workup.py` disambiguates its five hard-coded cases via `prefer`, `presend_gate.py --find` reports ambiguity when someone runs it on a quote number, and `health.md`'s Bid folder column is presence-and-recency by design. Nothing sweeps. This could be a one-off estate sweep (the missing half of the 2026-07-25 quotation scan) or a standing check; deciding which is part of the option.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

The strongest counter-argument to acting fast on DSP26085 is that the Jobs copy's provenance is unexplained, and deleting an unexplained file destroys the evidence for why it exists. The $6,180 sits entirely on the Mechanical Decoke line with task hours identical on both copies (6/18/6/6), which means someone re-priced equipment without changing scope — that is a deliberate edit, not a corruption, and it may be a considered revision that simply never became a quotation. The 2026-07-25 timestamp collides with the quote-number fix session, and the source note is right that a shared cause is worth checking rather than assuming; if the two events do share a cause, the Jobs copy is evidence about a process defect and should not be disposed of before that is understood. Against that: the `Jobs\` folder normally means awarded, and DSP26085 is still `pending` with 2027-01 execution — a higher-priced copy sitting in the awarded folder for a bid that was never awarded is the shape most likely to be opened by mistake by someone who does not know the history, which is precisely the risk the ruling exists to close.

Option C's risk is the one the source note names directly — a blanket folder-precedence rule would classify DSP25070's `_History\` copy as stray when an archive of a superseded revision is what `_History\` is for, and the rule would then be wrong on one of the three cases it was written to settle. Option D's risk is the vault's recurring one: a check whose fire rate is unmeasured. The known base rate here is three divergent pairs out of six duplicated filenames over roughly a year, but that count comes from a single scan of one file class and nobody has measured how often a benign duplicate is created — DSP26061 and DSP26075 both duplicated without diverging, so a sweep that flags every duplicate rather than every divergence would carry known-benign noise from day one. A one-off sweep sidesteps this entirely and is the cheaper first move; a standing check should probably wait until a sweep says how many pairs exist.

Finally, none of these options addresses whether the pre-send gate's exit-2 "could not judge" is loud enough. It reports ambiguity correctly, but it reports it to whoever ran it, at send time — which on a bid submitted in July would have been the last moment before the customer saw a number, not a moment with room to investigate.

## Decision

**2026-08-18 — Option A, with the ruling inverted from what the evidence in this note pointed at.**
Jesse: *"The 46,657.08 total is the correct one."* The `Jobs` copy is authoritative; the `Bids`
copy at $40,477.08 was the stale one and was disposed of. DSP25138 and DSP25070 remain
undecided and untimed. **Option D was not addressed and stays open** — the detection gap at the
`Bids/ → Jobs/` move is still unclosed, and nothing sweeps for new divergent pairs.

Recorded as *Approved with edits* rather than *Approved*: the disposition pattern in A was taken
as written, but A's own reasoning named the `Bids` copy as the one to keep, and that direction
was inverted.

This note argued for the `Bids` copy on the strength of four artifacts agreeing at $40,477.08
(the vault note, the quotation, the frozen regression expectation, and the file the Source Files
block named). All four were downstream of the same stale workup, so their agreement was
circular rather than corroborating — the count of agreeing artifacts was never evidence. What
the note did not do was open the two sheets and compare the pricing mechanics, which settles it
in one pass: task hours are identical at 6/18/6/6 and the whole $6,180.00 sits on equipment
**rates** — pumper flat $450 → tiered $500/$650/$600/$500, support unit $30 → $35, filtration
$150 → $200. A flat pumper rate across rig, pig and smart-pig is the anomaly; the tiered card
matches the Baytown pattern, and `DSP26085.md` had *already flagged* the flat $450 as unusual
against [[DSP26071]]'s tiered $500/$800/$600/$500. The correction was sitting in the note the
whole time, one section above the pricing table it contradicted.

The "unexplained provenance" risk in Risks and Counter-Arguments also dissolves: a clean rate-card
swap with untouched hours is a deliberate re-price, and the 2026-07-25 15:26 save landing 52
minutes before the 16:18 quote-number patch reads as one working session where the sheet was
corrected and the quotation was never re-pasted from it. No shared defect to chase.

Because this bid was **never sent** ([[2026-07-24-dsp26085-submitted-wrong-quote-number]]), the
correction carries no external exposure. The live consequence is internal: the quotation `.docx`
still renders $40,477.08 from a frozen metafile paste and must be regenerated before submission.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-18 | Verified both copies on disk and extracted both via `extract_workup.py` — `Bids` $40,477.08 / `Jobs` $46,657.08 confirmed, and the delta localised to eight equipment rate cells | Claude |
| 2026-08-18 | Backed up the `Bids` workup to session scratchpad, then sent it to the Recycle Bin (recoverable) per the DSP26071.1 precedent; re-ran `find` to confirm one copy remains | Claude |
| 2026-08-18 | Rebuilt `DSP26085.md` from the `Jobs` copy — `value`, Pricing table, pricing-summary box, composite rate ($1,296.03/hr), Equipment revenue detail, Hourly Rates, Internal Financials (Equipment 70%, Total 53%), Source Files, and the flat-$450 commentary | Claude |
| 2026-08-18 | `backtest_workup.py`: dropped `prefer: "\Bids"` so a future duplicate raises instead of resolving silently; expectations → $29,760.00 / $46,657.08 / Equipment $33,318.72. Suite passes 3/3, exit 0 | Claude |
| 2026-08-18 | `presend_gate.py`: `find_pair()` docstring updated — pair is history, and the no-sweep limitation is now stated explicitly | Claude |
| 2026-08-18 | Jesse replaced the quotation's pricing block with current prices and moved the workup from `Jobs\` back to `Bids\Exxon Baytown_F-201\` | Jesse |
| 2026-08-18 | Re-verified after his edits: workup still $46,657.08 (the file grew 7 KB on re-save, numbers unchanged), and the quotation rendered docx→PDF reconciles line-for-line — Mechanical Decoke $29,760.00, Total $46,657.08, box $33,318.72 / $11,268.36 / $2,070.00, quote number `DSP#:26085`. Source Files and script comments updated to the new layout | Claude |
| 2026-08-18 | **Found and raised:** the quotation's Section 8 rate card was not updated and still publishes the flat $450 / $30 / $150, which reproduces the old $23,580.00 against the quoted hours. Recorded as an open item on [[DSP26085]]; the client document was not modified | Claude |
