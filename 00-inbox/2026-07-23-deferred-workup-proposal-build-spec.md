---
type: note
status: inbox
created: 2026-07-23
tags: [inbox, estimating, automation, deferred, build-spec]
---

# Deferred — workup-to-proposal generator build-spec session

The [[2026-07-23-idea-research-workup-to-proposal-generator]] review was
**approved** on 2026-07-23: feasibility fork resolved (workups are structurally
stable, internally unorganized) and back-tested to exact match on one real pair.
Jesse greenlit a dedicated build-spec session but is picking it up **in a later,
separate session**. Capturing it here so it keeps a trigger — the review note is
now `resolved` and won't surface as pending.

What the build-spec session owes, mirroring [[job-report-generator-build-spec]]:

- **Write the full cell-region → proposal-line mapping spec** for `workup xlsx →
  proposal docx`. Starting reference for cell locations: the region map already
  reverse-engineered in `Workup-Template-v1-design.md` (local OneDrive Facilities
  tree, dated 2026-07-19 — not yet in the vault; consider ingesting it).
- **Back-test the two additional matched pairs** to confirm the mapping
  generalizes past one instance: `DSP26085` (Baytown F-201) and `DSP26068.1`
  (Formosa VR-401G). Both have workup + submitted Quotation docx/pdf in the same
  `Submit` folder. (First pair already proven: DSP#26071.2 reproduces its
  submitted quotation total $60,287.42 and every line item 1:1.)
- **Decide the source question:** build the mapping against the proven-but-messy
  current old-style workup (4 live instances, multi-heater) vs. the cleaner but
  unfinished single-heater `Workup-Template-v1.xlsx`. Leaning: build against the
  current workup now, treat v1 as a parallel input-cleanup track Jesse finishes on
  his own timeline — don't block the generator on a template rewrite.
- **Architecture:** shared `structured-source → branded-docx` render core (reuse
  the `docx` skill / python-docx approach proven on the job-report generator),
  separate mapping front-end. Build lands in `usadebusk-estimating` (parallel to
  the job-report generator living in `usadebusk-fieldpm`).

Not urgent. Revisit when Jesse opens the build-spec session.
