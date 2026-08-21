---
type: idea-seed
status: gated
created: 2026-08-17
revisit-trigger: "A second job report loses hand edits to a re-render, OR Jesse decides re-rendering over a delivered document should be routine rather than avoided -> unpark this and design the marker/splice mechanism — event: checked at the /report render step, when the output path already holds a file"
tags: [idea, fieldpm, job-report, generator, future]
related:
  - "[[2026-08-17-triage-job-report-generator-layout-gaps]]"
  - "[[2026-08-21-idea-research-generator-owns-marked-spans-gated]]"
---

# The generator owns marked spans, not layout

Parked out of the 2026-08-17 triage of [[idea-job-report-generator-layout-gaps]]. Three of the five
ideation frames converged on this independently, which is why it is parked rather than killed.

**Tentative read:** the job-report generator's load-bearing rule — "the generator owns all tables and
layout, the PM edits only prose" — is a larger claim than it can support, and USA26041 is what
happens when reality contradicts it. The smaller true claim is that the generator owns *marked
spans*. Emit a hidden bookmark or zero-width marker run around each generated block; a re-render
opens the existing document, walks the body, and replaces only the runs between a marker pair.
Anything Jesse inserted, moved, or relabelled lives outside a marker and survives by construction.
This is the only mechanism in the set that makes "yes, the generator may write over a delivered
file" a safe answer rather than a risky one — every other candidate makes overwriting *impossible*
rather than *safe*, which is the cheaper fix and the one that shipped first.

**To explore:** does the mechanism degrade acceptably where Jesse's edits are structural rather than
textual — a table he merged from two into one no longer matches the marker pair that produced it, so
what does the splice do there? Is the narrower version better: markers around the prose blocks only,
leaving tables fully generator-owned, which is what the load-bearing rule was probably trying to say
in the first place? Would a prose sidecar file the renderer reads from (narrative bodies keyed by
anchor, edited in any editor, re-render always safe) get the same protection with no marker
machinery at all? And does python-docx write and preserve bookmarks reliably through a Word
round-trip, or does Word rewrite them?

**Gate:** the cheap write-guard landed first (see the triage note). This only earns a design cycle if
that guard proves insufficient — a second edit-loss, or a decision that re-rendering delivered
documents should be routine. Until then the problem it solves is already solved more cheaply.
