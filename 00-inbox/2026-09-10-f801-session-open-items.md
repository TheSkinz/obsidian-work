<!-- vault-loop: Lane 4 content — needs Jesse's ruling, do not self-route -->
---
type: note
status: inbox
created: 2026-09-10
tags: [inbox, owed, lane4, ExxonMobil, Baytown, F-802, quoting, template]
---

# Open items from the F-801 build (2026-09-09/10)

Three items, one resolved. Nothing blocks the F-801 job, which mobs 2026-10-12. Item 1 needs Jesse; item 2 needs a fix
outside the vault.

## 1. [[F-802]]'s card is wrong and has not been corrected — Lane 4, awaiting a ruling

F-802's card is a faithful transcription of `SOP-DCK-F802-001 REV 0`, which assumed **6" Sch 80
pipe**. ExxonMobil's own F-802 inspection report — which Jesse confirmed 2026-09-09 was taken
immediately before the April/May 2026 convection replacement — shows the heater runs **ASTM A213
tube**, sized by OD and wall, not pipe schedule.

**The two sections are different cases and should not be corrected the same way.**

**Radiant — wrong outright.** It was never replaced, so the inspection data describes it as it
stands today:

| Field | Card says | Inspection report |
|---|---|---|
| Tubes/circuit | 30 | **31** |
| Wall | 0.432 | **0.500** |
| ID | 5.761 | **5.625** (computed, 6.625 − 2 × 0.500) |
| Metallurgy | A335 Gr P9 | **ASTM A213 T9** |

**Convection — unverified, not proven wrong.** That section *was* replaced in April/May 2026, so the
inspection report's convection rows describe steel that is no longer in the heater. The card's
5.761" may well be correct for the replacement section. **The replacement section's spec sheet has
been outstanding since June 2026** and the card's asterisked "verify against replacement spec" was
never cleared. Nobody has ever verified what is currently in F-802's convection.

**Not to be acted on:** the card also carries a footage defect (12 tubes × ~39 ft = 468 ft, printed
three lines above "228 ft per pass" in the SOP). Correcting it would move the **52 ft/hr row in
`04-knowledge/estimating-actuals-rollup.md:23`**, one of only five routine rows in the ft/hr
baseline. That correction lost its external corroboration under the 2026-09-09 CEDA exclusion and
now rests solely on an inference from the C-scan's 0–960 in axis. **Leave the rollup alone until a
stated convection tube length turns up.**

**Max pig OD is NOT among the errors.** F-802's 6.00" is correct — Jesse ruled 2026-09-09 that 6" is
the final pig size, and on a looped circuit that sits inside `usadebusk-equipment`'s oversized-final
allowance. An earlier reading in this session that called it over-cap applied the standard rule
without the exception.

**Decision needed:** correct the radiant rows now, or hold the whole card until the replacement spec
sheet lands and do it in one pass. Corrected geometry for the original coil already exists on
[[F-801]] and can be lifted for the radiant half.

## 2. The proposal template ships Citgo's name to ExxonMobil — second occurrence

[[DSP26064]], issued 2026-05-26 and awarded, names **Citgo three times** in its Time and Material
Rate Charges section: waste containers *"provided by Citgo"*, *"Citgo will provide a suitable
area"*, *"Citgo is also responsible for manifesting, transporting, and disposing of all
project-related waste."* It also carries a stray **`F-802`** label at the end of its Technical Data
table on an F-801 proposal.

**This is a recurrence.** The vault recorded exactly this defect on [[DSP25123]] on 2026-07-26 —
*"the issued proposal names Citgo three times in a document sent to ExxonMobil."* The finding was
written down and never reached the source template, so it shipped to the same customer again ten
months later — a finding recorded where it was decided rather than where it would have to act.

**Both documents are already issued and awarded — do not propose reissuing either.** The fix belongs
in the proposal template in the quoting toolchain (OneDrive / the work laptop), which is outside the
vault, and nothing in the vault can enforce it. **This note exists so a third occurrence is not
discovered the same way.** Whoever next edits the template: search it for `Citgo` and for hard-coded
heater tags.

## 3. ~~F-801's PO is not in hand, and 4411488628 should not be assumed~~ **RESOLVED 2026-09-10**

> [!success] **Jesse confirmed 2026-09-10: 4411488628 is scoped and funded for the F-801 decoke.**
> Recorded on his confirmation — no PO document for 4411488628 has been read and no value is
> recorded. Get the PDF into the job folder when it is to hand. **One sub-question stays open:**
> whether ExxonMobil's records show the F-802 decoke billed against 4411442151's F-801-labelled
> line, because a mislabelled line item would misfile F-801 the same way. The reasoning that
> prompted the question is kept below.


PO **4411442151** is superseded on its face by **4411488628**. But comparing its two reprints shows
item 00010 moving **$211,730.37 → $274,508.26** — [[DSP25084]]'s quoted total and USA26022's invoiced
total for [[F-802]], each matching to the cent. **That release was consumed by the F-802 decoke**,
despite a line item reading `26PS8 F801APH REPLACE - DEBUSK HEATER`.

So the assumption that 4411488628 is F-801's PO rests only on the supersession note of a PO that
turned out to be F-802's. **Nothing in hand states 4411488628's scope or value.** The question for
Preston Cheek (+1 346-259-4224) is whether it is scoped and funded for the **F-801 decoke**, or is
simply the next release against the same F-801 APH work order (40004035).

Jesse is making that call. `tools/vault_health.py`'s no-PO alarm arms **2026-09-21**, 21 days before
the 2026-10-12 mob. Worth asking on the same call whether ExxonMobil's records show the F-802 decoke
billed against that F-801-labelled line — if their label is wrong, it will misfile F-801 the same way.
