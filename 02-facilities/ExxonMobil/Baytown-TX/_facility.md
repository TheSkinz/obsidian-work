---
type: facility
facility-id: ExxonMobil-Baytown-TX
client: ExxonMobil
city: Baytown
state: TX
last-updated: 2026-07-26
tags: [facility, ExxonMobil]
---

# ExxonMobil — Baytown, TX

---

## Site Access

| Field | Value |
|---|---|
| Address | (not recorded) |
| Gate / check-in | (not recorded) |
| Badge / access requirements | (not recorded) |
| Site contact | (not recorded) |
| Site contact phone | (not recorded) |
| Escort requirements | (not recorded) |

⚠ **Equipment clears the asphalt gate on its own schedule — budget for it.** On USA26041 the
filter press could not get through security at the asphalt gate and did not clear until later
that day, costing **3 hours of stand-by on the rig-in shift**. The cause was ExxonMobil's own
gate policy for third-party equipment being unclear, not a USADebusk paperwork miss (Jesse,
2026-08-16). Treat this as a standing Baytown constraint on any scope mobilizing a press, pump
or trailer: get equipment through the gate **ahead of** the crew rather than alongside it, and
confirm the current equipment-entry requirement with the site contact before mob day. Applies to
the pending [[DSP26085]] F-201 and [[DSP26039]] HU9 scopes, both of which mobilize a filter press.

---

## Site Equipment and Constraints

| Resource | Detail |
|---|---|
| Crane | ExxonMobil-controlled overhead crane — coordinate mobilization timing with ExxonMobil |
| Filter press | Known capacity constraint on multi-Trimax jobs; consider larger or dual press on future bids |
| Water supply | (not recorded) |

---

## Site Safety and Procedures

**SOPs are a bid-stage deliverable only.** ExxonMobil Baytown requires the execution SOP as part
of the bid package, where its purpose is to give their engineers enough detail to evaluate the
approach. Once the bid is awarded, **the SOP does not need to be reissued** — scope changes that
land after award do not obligate a REV 2. (Jesse, 2026-07-27, on HU5A F-501: the awarded scope
moved to simultaneous triple-mode cleaning after SOP REV 1 went out describing sequential
execution, and no revision was required.)

Consequence worth knowing: a Baytown SOP in `Job docs\` can legitimately describe a superseded
scope. Do not read it as the execution authority, and do not treat a stale SOP here as an open
action item. Verify the config against the job sheet and heater card instead.

**PSSR training is required on some Baytown jobs and is held inside the gate** — a site badge
must be issued before crew can attend. Sequence: badge → gate access → PSSR → work. Confirm per
job whether PSSR applies; it is on top of the standard site-specific training.

---

## Rate History — Baytown

<!-- Replaced the single "Contracted Rates — PS8 F-802" block on 2026-07-26. That block was
correctly labeled with its source quote per the rfq-intake-protocol rule, and carried the
same DSP25084 rates reproduced below — it was not wrong, just one column wide. Widening it
to all three Baytown quotes is what exposed DSP25123's bad filtration standby row. The old
"no rate schedule found for DSP26039" line is retired: DSP26039 does carry a full schedule. -->


**These rates are expired, not available.** Two of the three quotes below were short-form
scope contracts: rates were negotiated for one identified scope, billed during execution,
and **the contract ended when the scope completed** (Jesse, 2026-07-26). DSP25084's rates
died with the F-802 turnaround; DSP25123's died with F-901. Only DSP26039 is live, and it
is still pending. So this table is a record of what was charged and when — useful for
seeing the spread, spotting an outlier, and knowing your own history going into a
negotiation. **It is not a rate schedule and nothing here can be quoted from.** The rates
for the next Baytown bid come from that bid's own contract or bid instructions.

**Read a divergence as a flag, not as a Baytown regime.** USADebusk prefers the same rates
at every facility, so the House standard column is the intended figure and most cells
should match it. Where one doesn't, the cause is usually either that the contract froze an
older figure or that the RFQ was contested and rates were cut to win it — not that this
site prices differently by policy.

The one case that would change all of this is a long-term maintenance agreement, where a
multi-year contract sets base rates any scope inside the term inherits. None on this site,
and none on Jesse's accounts as of 2026-07-26. See [[quote-lifecycle]] for the
contract-type model and the `contract-type` / `rate-basis` / `billing-basis` fields.

| Line Item | DSP25084 (F-802, 2025-07-15) — **expired** | DSP25123 (F-901, 2026-04-06) — **expired** | DSP26039 (F-301/F-371A, 2026-04-07) — **pending** | House standard |
|---|---|---|---|---|
| Trimax Triple — Pigging | $800/hr | $800/hr | $800/hr | $800/hr |
| Trimax Double — Pigging | $650/hr | $650/hr | — | $650/hr |
| Trimax Smart Pigging | $600/hr | $600/hr | $600/hr | $600/hr |
| Trimax Rig-In / Out / Over | $500/hr | $500/hr | $500/hr | $500/hr |
| Trimax Standby | $500/hr | $500/hr | $500/hr | $500/hr |
| Filtration | $200/hr | $200/hr | $200/hr | $200/hr |
| Filtration Standby | $150/hr | ~~$35/hr~~ → $150/hr | $150/hr | $150/hr |
| Support Unit | $35/hr | (row absent) | $30/hr | $30/hr |
| Crew Truck | $25/hr | $25/hr | $25/hr | $25/hr |
| 4×3 Pump | $1,016/shift | $1,016/shift | $85/hr | — (basis varies) |
| Project Manager | $94.75/hr | (row absent) | $94.75/hr | $94.75/hr |
| Per Diem | $150/day | $150/day | $150/day | $150/day |
| DEF | $180/shift | $180/shift | $180/shift | $180/shift |

Notes on the three cells that are not clean:

**Filtration Standby $35 on DSP25123 is an error, not a price** — resolved by Jesse
2026-07-26. The F-901 sheet was built from the F-802 template and a deleted Support Unit
row pulled its $35 up into the filtration standby cell, taking the PM row with it.
$150/hr governs. Filtration was declined before execution, so it never reached an
invoice. Detail on [[DSP25123]].

**Support Unit $35 on DSP25084 stands as what that expired contract carried.** $30/hr is
the house standard (`04-knowledge/pricing/_cost-model.md`, `usadebusk-estimating`) and is
what DSP26039 carries. Per Jesse 2026-07-26, $30 will be right for the majority of bids —
but the divergence needs no reconciling, because each figure belonged to a contract that
set its own rates and then ended. Start from the house standard and take the governing
figure from this bid's contract or bid instructions.

**4×3 pump basis changed** between DSP25084/25123 ($1,016/shift) and DSP26039 ($85/hr).
Not reconciled — check which basis the governing contract uses before pricing it.

**DSP26071.2 (HU5A F-501) — awarded 2026-07-27, executed as USA26041, complete 2026-08-14.** The
first live rate set on this site. Not yet added as a column above; that widening is pending. Its
schedule matched the house standard on every line except Filter Stand-by, quoted at **$35/hr** —
genuinely negotiated, not the DSP25123 cell error it happens to match (confirmed by Jesse
2026-07-27). 24 stand-by hours were quoted at it.

⚠ **Superseded before the job started: filtration stand-by was changed to $150/hr by the account
manager, with ExxonMobil rep approval, before mobilization — and Jesse was not told** (Jesse,
2026-08-15). Not a change order raised during execution. He ran USA26041 as PM against a $35 figure
that had already been renegotiated. So on this site the pair reads **$35 quoted → $150 billed**, and
$150/hr governs going forward. Both facts stand: the quote's $35 was real when written, and the
executed contract carries $150. Do not "correct" the DSP26071 quoted schedule to $150 — that table
records what went to the customer — but do not bill or re-quote off the $35 either.

**What is worth carrying is about the number, not the process.** $35/hr has appeared on this site
three ways — a template artifact (DSP25123), a genuinely negotiated rate (DSP26071 as quoted), and
a rate renegotiated away before execution (USA26041 as billed). The number alone diagnoses nothing,
so read the surrounding note rather than pattern-matching the figure.

**The pre-mobilization rate change was a one-off** (Jesse, 2026-08-15), handled directly with the
account manager. It is not a standing risk, not a reason to re-confirm awarded rates at job-start,
and not a step to add to any workflow. See [[DSP26071]] and [[USA26041-job-sheet]].

## Labor Rates — PS8 F-802 (USA26022, quoted vs. actual billed)

| Role               | Quoted ($/hr) | Actual Billed ($/hr) | Notes                                                                                                     |
| ------------------ | ------------- | -------------------- | --------------------------------------------------------------------------------------------------------- |
| Project Manager    | 94.75         | 64.92                | Actual QB billed PM at the Day Supervisor rate — flag before assuming $94.75 is what actually gets billed |
| Supervisor (Day)   | 64.92         | 64.92                | Matches                                                                                                   |
| Supervisor (Night) | 67.79         | 67.79                | Matches                                                                                                   |
| Operator           | 55.39         | 55.39                | Matches                                                                                                   |

Source: DSP# 25084 Rev 2 PS8 F-802 Furnace Decoke 2 TriMax.pdf (quoted);
USA26022 EXXONMOBIL F-802 TriMax Ticket Breakdown.xlsx (actual QB Sheet).

**Quote vs. Actual Overage:** Quoted $211,730.36 vs. actual billed $274,508.25
(change-order Rev 1 revised price) — $62,777.88 over. Actual combined Trimax
pigging hours (110 = Trimax4 55 + Trimax6 55) exceeded quoted 60 project hours;
standby (98 hrs combined) was not planned in the quote at all.

---

## Heaters at This Facility

- [[F-802]]
- [[F-901]]
- [[F-301]]
- [[F-371A]]
- [[F-501]] — HU5A
- [[F-201]] — 27GF1A, Treat Gas
- **Pipestill 3 (PS3)** — decoked January 2026 as job USA26007, four heaters: **F-306, F-305, F-302, F-301**. No heater cards and no HU-prefixed heater IDs recorded for any of the four; the job register, the workup and the signed change order all name them only by these bare PS3 tags. **PS3's "F-301" is not the vault's [[F-301]] card** — that card is `HU9-F301-SplitterReboiler`, a different unit and a different heater that happens to share the number. Do not conflate them if PS3 work ever gets a card of its own. Distinct from the PS8 units (F-802, F-902).

## Completed work not held on a heater card

**Pipestill 3 decoke, January 2026 — DSP#25070 → job USA26007.** Scope: mechanical decoke of PS3's F-306, F-305, F-302 and F-301. PO AM4510698312, contracted **$162,576.42**, mobilized 01/28/2026, executed 01/31/2026. Source: the `2026 Job Numbers.xlsx` register on SharePoint (Jesse, 2026-08-18) for the base facts; the signed change order below (Jesse's Downloads, added to Google Drive 2026-08-18) for the price history — neither is derived from the workup.

**Signed change order, 2/6/2026 — the invoice overage is fully authorized, with room to spare.** Field discovery on F-306: the coil configuration was 6 coils looped to **4 passes**, not the 2 passes the job was priced against, requiring a change-over and extended decoking time. Support doc: "Updated F-306 pigging configuration with correct labeling provided." Company-approved by Jesse Utsey, 2/6/2026; the contractor-approval block is unsigned on the copy retained, which is normal — that side is ExxonMobil's.

| | Amount |
|---|---|
| Original contract price | $162,576.42 |
| Change order (scope change + completion date) | +$44,113.49 |
| **New contract price** | **$206,689.91** |
| Invoiced (invoice 128587, billed through GEP) | $199,756.00 |
| **Invoice vs. authorized price** | **$6,933.91 under** |

This replaces the earlier reading here, which compared the invoice only to the *original* $162,576.42 and called the $37,179.58 gap unexplained. It is explained, by a scope change discovered in the field and authorized in writing before the invoice — and the invoice came in under the authorized ceiling, not over it. General lesson, consistent with [[DSP26071]]'s "governing rate" finding: **the original contract value is not the number to invoice-check against once a change order exists.** Check the invoice against the change-order price, not the quote.

Two workup copies exist and the register settles which governs: `Jobs\USA26007 PS3 2026-02\` totals $162,576.42 on every total it carries and matches the *original* contracted value, so it is authoritative for the base quote; the `_History\Exxon Baytown_PS3 Heaters\` copy at $169,947.76 is a superseded higher revision sitting where superseded revisions belong. Neither workup reflects the change order — it is a separate signed document, not a workup revision. Both copies internally consistent, both read `DSP#: 25070` in both cells — this pair was never a defect. No action needed on the workups.

---

## Notes
