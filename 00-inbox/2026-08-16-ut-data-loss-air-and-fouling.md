<!-- vault-loop: operational — Jesse-supplied field knowledge on UT smart-pig data-loss causes, Lane 4 (domain truth). Not written to any heater card or skill pending his ruling. Capture loop cannot write this content. -->
<!-- vault-prestaged: 2026-08-20-prestaged-ut-data-loss-air-and-fouling.md -->
---
type: note
status: inbox
created: 2026-08-16
tags: [smart-pig, inspection, UT, domain-truth, lane4, ExxonMobil]
---

# Air and fouling are the standing causes of UT data loss on smart-pig runs

Captured 2026-08-16 from Jesse in session. **Lane 4 domain truth — recorded here only, not written
into [[F-501]], the ingest skill, or any other authoritative surface pending his ruling on where it
belongs.**

**The facts as stated.** Air in the coil is a common occurrence on smart-pig runs. Many coils have no
high-point bleeders. USADebusk has a method of bleeding, but it does not always work. Air and fouling
are the two common factors behind data loss in a UT inspection.

**Why it came up.** Steady Flux's B_8_C detail (Appendix C, p. 34 of `26-0663-002 Rev. A`) is the one
segment in F-501 that warrants ExxonMobil's attention — 0.224 in remaining, 56% of nominal, internal,
minimum at 7:00. Unlike A_3_C and A_15_R, which each get a full anomaly table with flaw length and
width, B_8_C gets only a clock position and a distance. The initial read was that the quantification
was omitted. Jesse's correction is that it may simply not have been collectable, which the figure
supports: Figure 17 shows large irregular white voids across the full length of the strip and a zoom
that is a speckle field rather than a coherent surface. There may be no boundary in the data to
bound.

**The consequence that matters, and it is bigger than the missing extent.** Air causes dropout — you
lose data and you can see that you lost it, because the pixels go white. Residual fouling can do
something worse: add an interface the tool may gate on, producing a reading that looks valid and
reads thin. B_8_C's minimum sits at 7:00 in a horizontal tube, which is exactly where deposit settles
*and* exactly where bottom-of-line corrosion lives. Those two are not distinguishable from the C-scan
alone. **If there was residual fouling in that segment, the 0.224 in figure itself is in question,
not just the missing extent.**

**Evidence that argues against air for this specific segment**, offered as evidence and not a verdict:
Figure 3 puts convection tube 1 at the top of the stack with flow running down to 9, so a gas pocket
collects in B_1_C, not B_8_C — and B_1_C images clean at 0.435. That assumes drawn order matches
physical elevation and says nothing about entrained air moving through during the run. Against
uniform deposit: the zoom is heterogeneous, white shot through with orange, green and isolated blue
at 0.5 within inches of each other, which reads more like an irregular surface than a layer over
sound metal. Inferring surface condition from a rendered image is weak evidence and should be held
loosely.

**Open with the vendor.** Jesse put the question to Steady Flux on 2026-08-16: whether the B_8_C
dropout is coupling, residual fouling, or surface condition, and whether the 0.224 reading is
affected. Their raw A-scan waveforms answer it; nothing on the USADebusk side can. **Awaiting
response — this is the live loop from that outreach.**

**Where this should probably land, for Jesse to rule on.** It qualifies the load-bearing inference in
[[idea-smart-pig-report-as-cleaning-verification]], which currently reasons that a clean low-noise
C-scan across a full coil is itself evidence the pigging reached bare metal. That holds, but the
converse does not: a noisy C-scan is **not** evidence of poor cleaning, because trapped air produces
the same signature and is a coil-venting limitation rather than a cleaning failure. Any proposal or
close-out language built on that seed needs the asymmetry stated, or the first unflattering report
will be read against USADebusk for something that was never in scope. Candidates for a permanent home
are a note under `04-knowledge/`, the smart-pig handling in the ingest skill, or both.
