<!-- vault-loop: operational — full-document audit of Steady Flux 26-0663-002 Rev. A, findings beyond the two already on the heater card. Lane 4 where it touches domain values (Treat Gas nominal basis); the rest is vendor-document record. Capture loop cannot write this content. -->
---
type: note
status: inbox
created: 2026-08-16
tags: [smart-pig, inspection, USA26041, ExxonMobil, steady-flux, vendor-qa]
---

# Steady Flux 26-0663-002 Rev. A — full audit, findings beyond the card

Captured at close-out 2026-08-16. [[F-501]] already carries two errors from the 2026-08-15 pass (the
radiant/crossover header ID on pp. 15–20, and Appendix B Table 11's nominal 0.400 on A_15_R). Both
re-verified; neither changes a result. Everything below is new and is **not** on the card. Jesse sent
a findings list to the Steady Flux CEO informally on 2026-08-16 — friend-of-a-friend, not a formal
Rev B demand, and ExxonMobil rather than USADebusk owns the report.

**Airtight — verifiable against the PDF in under a minute each.**

Appendix D contradicts the body on the seven thin short sections. Table 12 (p. 35) lists C_10_R as
"No verifiable thickness reading" while Table 5 (p. 11) and Table 8 (p. 18) both report it at
0.403 in / 13.1% and label it the lowest remaining wall in normal Pass C radiant pipe. Separately,
the "Distance to Upstream Circumferential Weld" column carries the same header but different meaning
in two tables — Table 12 appears to measure to the leading edge of the pup, Table 8 to the minimum
reading inside it. Table 12 gives D_4_R at 36.8 in while Figure 18, on that same page, labels the
same location 39.7 in. Same split on the other three: A_2_R 15.2 vs 19.3, B_4_R 36.2 vs 39.9,
B_11_R 431.6 vs 434.7. Both numbers are probably right; nothing tells the reader which is which.

A_15_R ovality is blank in Table 5 (p. 10) and 1.5% in Table 8 (p. 17) — the only row in Table 5 that
disagrees with its detail row, and it is the segment the card treats as the honest radiant condition
number. A_15_R is also listed at 516.0 in when B_15_R, C_15_R and D_15_R are all 507.0 and Figure 4
draws A_15 and D_15 as mirrored outlet legs; possible transposition, already inherited by the card's
per-pass totals (Pass A 7,482.6 in vs D 7,473.6 in). Immaterial to the 3,588 ft total.

The crossover is measured in Table 7 but appears in no summary — not Table 4, not the executive
summary, not Table 5's per-pass minimums — and has no C-scan of its own. Table 7 computes loss
against 0.464 in, a nominal the report never declares for that section. Nothing in the data is
alarming (worst is A_1B_X at 0.444), but it is the least-documented section and it is where the
Circuit 1 bore restriction lives.

Two executive-summary statements overreach. B_8_C is called "the only bright green/yellow pipe
segment in the C-scan results" (p. 3) — A_3_C and A_7_C band continuously in Figure 6, as do D_5_C
and D_7_C in Figure 9. The same paragraph says that with the exception of B_8_C nearly all readings
exceed the 0.400 nominal, but A_3_C (0.376), A_7_C (0.380), A_1_C (0.398) and D_2_C (0.398) are all
below it, and A_3_C is named in that sentence. Page 4 describes the pups as roughly 6 to 7 inches
long; Table 12 lists three at 7.2, 7.31 and 7.42.

Three unmarked C-scan colour scales: Figures 6–13 run 0.20–0.60 in, Figure 14 (Treat Gas) runs
0.20–0.45, Figure 18 runs 0.15–0.30. Read side by side the Treat Gas section looks healthier than it
is. Typos: "LOCATON" (p. 6); "anomoly" ×3 and "proceeded" for *preceded* (p. 32); "stands out has
having" and "mimimum" (p. 34); Table 12's 36.8 missing its unit; Figures 6 and 7 carry stray digits
in their captions and in the Table of Figures ("Pass A 1 C-Scan", "Pass B 2 C-Scan").

**Solid but needs an argument.** The references (p. 5) give the speed of sound in water as
0.0620 in/µs at 107 °F — about 1,575 m/s. Fresh water at atmospheric pressure peaks near 1,555 m/s
around 165 °F and should read ~0.0602 in/µs at 107 °F, so the stated figure exceeds the physical
maximum at any temperature. Likely a transposition in the reference table. Wall thickness comes off
the steel velocity and is unaffected, **but the water velocity sets the transducer standoff, and
standoff is what produces the internal-radius data** — which is exactly what the card wants requested
to characterise the Circuit 1 A/B crossover restriction. Confirm which value the software used before
requesting that bore profile.

**Questions, not findings — deliberately not asserted.** Table 4 calls the Treat Gas wall "5-inch
schedule 80 (5.563 in x 0.375 MWT)" while the results header calls the same number "Nominal Wall
Thickness." Those are different things: A53/A106 permit −12.5%, so 0.328 in is an acceptable as-new
wall, and 28 of the 31 Treat Gas readings sit above it. If that pipe was bought to schedule rather
than to a minimum wall, much of the reported "9–14.5% loss" may be original mill under-tolerance
rather than corrosion — which would soften the card's Field Notes line describing it as general
thinning. **This is Lane 4 and unresolved; the card has not been changed.** The same terminology slip
runs the other way on the 9Cr sections: if 0.400 and 0.464 are genuinely minimum wall as Table 4
says, real loss there is understated.

**Deliberately excluded from what went to the CEO:** the Appendix E spec-sheet claims — "100%
inspection of the entire heater" against the report's own data-loss caveats, and the 24-hour
final-report spec against a 48-hour delivery (the latter already on the card). Both are real; both
read as commercial complaints rather than a favour, and mixing them changes the nature of the note.

**Not raised, per the card's standing instruction:** the bends and pups computed against the original
0.464 nominal. Both parties already know. The only related suggestion made was that a future revision
carry one context sentence, so a reader of ExxonMobil's file copy in five years does not read
"45.7% loss" as coil condition.

Open item is on [[2026-08-16-ut-data-loss-air-and-fouling]].
