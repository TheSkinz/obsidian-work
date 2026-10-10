---
type: idea-seed
status: unexplored
created: 2026-10-09
tags: [idea, proposals, future]
---

# Redesign the company quote template

Idea seed captured 2026-10-09 at Jesse's request, as the task for a future session. The read below is tentative; confirm intent with Jesse before designing.

**Tentative read:** Jesse's view is that the current USADebusk proposal template (Jason's DSP26100-format `.docx`, used for DSP26112–26115) looks amateur. Someone else designed it. He wants a redesigned company quote template that looks professional while keeping the 12–16 page section structure the `usadebusk-estimating` skill defines.

**To explore:**
- What exactly reads as amateur: cover, header band, fonts, the Execution and Quotation pages pasted in as workup screenshots, inconsistent spacing.
- Whether the redesign should keep the workup-picture approach or render the Execution and Quotation pages as native tables. Native tables would also let `presend_gate.py` read the quote, which it can't today; DSP26115 returned CANNOT JUDGE.
- Whose approval it needs. A branded redesign was built for DSP26112–26114 on 2026-10-08 and Jesse reverted it to Jason's format the same night (commit `22f326e`). Find out why before redesigning again. Was the problem the design itself, or the switch away from a format Jason and Travis already know?
- Brand standards in `usadebusk-core`, and the existing generator `usadebusk-estimating/scripts/render_proposal.py`.
- Show Jesse a one-page specimen before building the full template.
