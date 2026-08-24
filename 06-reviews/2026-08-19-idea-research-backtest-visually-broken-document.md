---
type: review
status: resolved
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-08-19
review_after: 2026-09-19
related:
  - "[[2026-08-16-backtest-passed-on-a-visually-broken-document]]"
  - "[[2026-08-17-triage-job-report-generator-layout-gaps]]"
  - "[[job-report-generator-build-spec]]"
  - "[[2026-07-23-idea-research-workup-to-proposal-generator]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, idea-research, back-test, generator, validation, cross-cutting]
---

# Idea Research — A Back-Test That Only Checks Numbers Passes on a Visually Broken Document

## Trigger

Scheduled nightly run of the Vault Idea Research Loop, 2026-08-19. The oldest unexplored seed
(`idea-smart-pig-report-as-cleaning-verification`, 2026-08-15) was gate-checked first and its gate is
verifiably shut — see [[2026-08-19-idea-research-smart-pig-report-verification-gated]]. This seed is
next-oldest (2026-08-16, first commit 15:34:40, ahead of `idea-isometric-rig-diagram-from-debusk-renders`
at 20:39:16) and its `**Gate:**` line reads "None — researchable now," so it was researched.

## Evidence

**1. The general principle is settled prior art, and the seed's diagnosis matches it exactly.** The
failure mode has a name and a large literature: a green suite that answers "does it work?" and never
"does it still look right?", producing the retrospective pattern of a visual bug found by a user
after every assertion passed. The class of defect it catches is listed almost verbatim against this
incident — missing or incorrectly rendered components, styling inconsistencies in fonts, colors and
margins.
[Visual Regression Testing: Catch Bugs Tests Miss](https://bugbug.io/blog/software-testing/visual-regression-testing/) ·
[Visual Regression Testing Catches What Other Tests Miss](https://blog.vibecoder.me/visual-regression-testing-catching-ui-breaks)

**2. The seed's proposed mechanism is the standard one, and it is a well-trodden path for documents
specifically — not just web UI.** Render, rasterize each page to PNG at fixed resolution, diff
against an approved baseline, pin the renderer so baseline and run use the same engine. Working
implementations exist at every scale: `pdf-visual-diff` (pdf.js → PNG, jimp diff, emits `.new.png`
and `.diff.png` for inspection), Antenna House's regression system for pixel-by-pixel PDF and
directory comparison, and the ApprovalTests / Verify family for the approval-testing framing.
[pdf-visual-diff](https://github.com/moshensky/pdf-visual-diff) ·
[AH Regression Testing System](https://www.antennahouse.com/ahrts) ·
[Verify](https://github.com/verifytests/verify) ·
[Implementing Approval Tests For PDF Document Generation](https://principal-it.eu/2021/12/implementing-approval-tests_for_pdf_document_generation/)

**3. But the two defects that actually shipped are structural, not visual, and the cheapest assertion
that catches them is not a raster at all.** Both are now explicit OOXML elements in the renderer:
`_table_borders()` writes `w:tblBorders` (`render_job_report.py:65`, applied by `_grid()` at `:91`),
and `build_kpi_band()` writes the gold rules as `_line(GOLD_HEX, 12)` top and bottom (`:244`, `:254`).
Their absence was an *absence of XML*, which `python-docx`/lxml can assert directly against the
written `.docx` — no rendering, no LibreOffice, no image, no threshold. The raster is what *found*
them, because nobody knew what to look for; it is not what has to *guard* them now that we do. Two
lines of "every content table has a `w:tblBorders` child" and "the KPI table carries top and bottom
borders at `FCC30A`" close the exact hole the seed opened.

**4. The seed's own hardest question — how much drift is acceptable given LibreOffice and Word
rasterize differently — is a real, recurring cost that prior art has had to pay, and it is the reason
not to put pixels in tier one.** R's `doconv`, which exists specifically to snapshot-test Word
documents, exposes a `tolerance` parameter for the ratio of differing pixels allowed before failure,
and states plainly that when Word is unavailable LibreOffice is used and "the rendering may sometimes
differ from the original documents." `pdf-visual-diff` carries the same warning one level down —
there may be differences between images generated from the *same* PDF on different operating
systems, so baselines are not portable. A pixel tier therefore ships a tuning knob, a per-machine
baseline, and a flake budget. A structural tier ships none of those.
[doconv on CRAN](https://archive.linux.duke.edu/cran/web/packages/doconv/index.html)

**5. Where the raster genuinely earns its place is pagination and fit — and this vault has already
proved that, once, in a run that falsified its own premise.** The 2026-08-17 triage rendered USA25025
with the pig-table split forced off, rasterized page by page, and found that the 2-up split "does not
deliver a one-page fit either" — the split's entire stated justification was false at the one job it
was built for, fit is governed by where the section lands rather than row count, and a *second*
defect fell out of the same raster (the `SWAB` header would have mislabelled USA26038's 35 honeycomb
gauges on a customer document). No XML assertion could have seen any of that. The triage also
recorded this seed as a **hard dependency** of that test rather than a parallel idea
(`2026-08-17-triage-job-report-generator-layout-gaps.md`, "Merged as duplicate").

**6. Nothing in the deployed skills does either check today — this is not already covered.** A grep
for `pdftoppm`, `rasteriz`, `pixel`, `visual regression` and `screenshot` across all of
`~/.claude/skills/` returns nothing. What the README calls a "back-test" is three input fixtures
(`report_input_usa26038.py`, `usa25025`, `usa26041`) plus a manual comparison of extracted numbers.
The README already carries the confession in its own Validated section — "'Exactly' was only ever
true of the *numbers*" — but the fix landed in the renderer and no assertion was added, so the same
class of defect can ship again tomorrow.

**7. The seed's second half — does this apply to the other document generators — has no live target
yet.** The workup-to-proposal generator is not built; that idea is `status: resolved` and the build
spec is explicit that "each transfer step must be proven against its own back-test before merging
render cores." So there is nothing to retrofit. What is actionable is that the back-test *standard*
set here becomes the one that transfer step has to meet, rather than a second generator shipping with
a numbers-only back-test and rediscovering this.

## Interpretation

**Sound — the diagnosis is right and confirmed by external prior art, but the proposed mechanism is
the right tool aimed at the wrong tier.** The seed asks "what is the cheapest visual assertion that
would have caught this," and the honest answer from the evidence is: for *these* two defects, no
visual assertion at all. Both were missing OOXML elements, and a structural check on the emitted
`.docx` catches them deterministically, on every render, at zero tolerance-tuning cost — which is
strictly better than a pixel diff that needs a threshold, a pinned renderer, and a per-machine
baseline to say the same thing less reliably.

That does not retire the raster. It relocates it. Rasterizing is the only thing that can see
pagination, fit and where a section lands, and this vault has one clean instance of it paying for
itself by killing a false premise and catching a customer-facing mislabel in the same pass. The
correct shape is two tiers with different costs and different jobs: **assert the XML automatically,
look at the pixels deliberately.** The seed's instinct that "the gap is what counts as the match
surface" is exactly right — the match surface just turns out to have two layers, not one.

Worth naming as the load-bearing risk: adopting the pixel tier as an automated pass/fail is how this
becomes machinery nobody maintains. `doconv`'s tolerance parameter and `pdf-visual-diff`'s cross-OS
caveat are both scar tissue from that, and an unbounded auto-checker fails the standing
bounded-propose-only preference. Keeping tier two as "render, rasterize, look at it" — a step a human
performs when layout changed, not a gate that fires on every run — keeps the value and drops the
maintenance.

## Recommended Action

**Bounded build for tier one; keep tier two a habit, not a harness.**

Tier one — add a structural assertion pass to the job-report back-test, run against the rendered
`.docx` of all three existing fixtures. Minimum content: every content table carries `w:tblBorders`;
the KPI band carries top and bottom rules at `FCC30A`; each table's column count and header row match
the build spec's section table. Deterministic, no external renderer, and it fails loudly on exactly
the class of defect that shipped silently. Estimated cost is comparable to the border fix itself —
one file, no new dependency beyond what `render_job_report.py` already imports.

Tier two — write the raster step into the generator's documented process as a *layout-change*
checkpoint, not a per-run gate: when a change touches table shape, page breaks or the KPI band,
render a fixture, convert, `pdftoppm`, and look at page 1 and the pages the change should affect. No
tolerance threshold, no stored baseline images, no CI.

Do **not** build an automated pixel-diff harness with a tolerance knob. The prior art says that is
where the maintenance cost lives, and the two defects that motivated this seed do not need it.

Carry the standard forward: when the workup-to-proposal transfer step is built, its back-test has to
clear tier one before it is called validated. That is a one-line addition to the build spec's merge
condition, not work today.

**Scope note.** This is a skills-side change (`~/.claude/skills/usadebusk-fieldpm/`), which this loop
is barred from making. Nothing here was implemented.

## Decision

- [x] Approved — build tier one (structural assertions) and document tier two as a layout-change checkpoint — **ruled and built 2026-08-21**, config repo `0f64003`. See Apply Log.
- [ ] Approved, tier one only — skip documenting the raster step
- [ ] Approved with edits
- [ ] Rejected — the numbers-only back-test plus the landed border fix is enough
- [ ] Needs more source material

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-21 | **Tier one built and verified.** `skills/usadebusk-fieldpm/back-test/assert_structure.py`, config repo `0f64003`. | Claude | Two checks — BORDERS and KPI-RULE — reading the written OOXML directly. Clean on all three fixtures rendered from their real workbooks; stripping `w:tblBorders` to recreate the pre-2026-08-16 document fires 15 findings, so it catches the incident that motivated the seed. `--self-test` proves each check fires on its own defect. |
| 2026-08-21 | Three false-positive classes found by running it, each now exempt. | Claude | Callout boxes carry a gold left bar as cell-level `w:tcBorders`, not `w:tblBorders`. Figure tables hold an image and caption — a border around a photograph is wrong; these surfaced only because all three fixtures were run, since 26038 and 25025 carry no images. And a **width check was written and removed after measuring** — it fired on 17 of 18 tables in a report that shipped and was accepted; rendering to PDF showed content ends 0.03" past the text edge on every page, so the layout engine normalises the declared widths and the check was asserting a defect the renderer does not produce. |
| 2026-08-21 | Tier two recorded as a habit, not a gate. | Claude | Rasterize-and-look documented in the scripts README as a layout-change checkpoint. No pixel-diff harness, no tolerance knob, no baseline images — the note's own prior-art finding. |
|  |  |  |  |
