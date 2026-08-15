---
type: review
status: resolved
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-08-12
review_after: 2026-09-12
related:
  - [[idea-job-sheet-third-instance-no-migration]]
  - [[2026-07-18-idea-research-job-sheet-type-formalization]]
  - [[_canonical-job-sheet]]
tags: [review, knowledge-system, idea-research, job-sheet, schema]
---

# Idea Research — Job-Sheet Third Instance, No Migration

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. `idea-job-sheet-third-instance-no-migration` was the only `unexplored` idea-seed in `00-inbox/` (the sole other `type: idea` file at `status: unexplored`, `2026-07-27-over-wide-tables-remainder.md`, is not an `idea-seed` and carries its own `vault-loop: operational` defer marker to the Agent-Review loop, so it was excluded from this loop's queue on two independent grounds). The seed records that USA26041 (ExxonMobil Baytown, HU5A F-501) became the third job-sheet instance the canonical's STATUS block anticipated — its sheet predated the 2026-07-30 six-block shape and already carried Baytown-specific sections (Direct Contact, Turnaround Coordination, Circuit Assignments, Prerequisites), and rather than migrate, mobilization detail was added as one ad-hoc "Equipment Mobilized" section on top of the existing shape.

## Evidence

**Internal — the canonical already anticipates this exact situation but never resolves it.** `04-knowledge/_canonical-job-sheet.md`'s STATUS block (lines 33–40) reads: "validated against TWO instances (USA26038, USA26040)... Section shape is now better evidenced but still not settled; a third instance may move it again." That sentence is the seed's whole premise — USA26041 is that third instance, and per the seed it did *not* move the shape; it coexisted with it. There is no line anywhere in the canonical, `templates/_job-sheet-template.md`, or the `usadebusk-vault-ingest` skill's routing doc stating whether the six blocks are a floor or a ceiling — checked `document-routing.md`'s Job Sheet section (Priority 0.5) and it only covers *where* a job sheet routes, not what it must or may contain. The sibling research note from 2026-07-18 (`2026-07-18-idea-research-job-sheet-type-formalization.md`), which originated the canonical, doesn't address extensibility either — it was written when only one instance (USA26038) existed. So this is a genuine gap, not a re-ask of settled ground.

**External — "core required + optional extension" is the standard, load-bearing convention in both document-template and machine-schema design, which directly answers the seed's first question.** Structured-document guidance treats a template as "modular... flexible... scalable," built around mandatory sections plus an explicit slot for site- or project-specific additions rather than a rigid fixed set ([Docsie, Document Templates: Definition, Examples & Best Practices](https://www.docsie.io/blog/glossary/document-templates/); [CompuScholar, Project Documentation Templates](https://www.compuscholar.com/schools/blog/project-documentation-templates)). The machine-schema analogue is sharper and more directly on point: JSON Schema objects are **open by default** — `additionalProperties` defaults to allowing extra fields, and a base schema must be deliberately closed (`additionalProperties: false`) to forbid them, which is also the *only* setting that breaks the standard extension pattern (`allOf` + `$ref` to layer added fields onto a base) ([JSON Schema — object](https://json-schema.org/understanding-json-schema/reference/object); [A Tour of JSON Schema — Additional Properties](https://tour.json-schema.org/content/03-Objects/02-Additional-Properties); [endjin, Json Schema Patterns in .NET — Extending a base type](https://endjin.com/blog/json-schema-patterns-dotnet-extending-base-type)). Translated to this vault's schema: the canonical's six blocks read exactly like an "open" base schema already — nothing in it says `additionalProperties: false` — but that is implicit, not stated, which is precisely the ambiguity the seed flags.

## Interpretation

**Sound, and the easy two-thirds of it is already answered by convention — the third question is the one that needs Jesse, not research.** The seed's first question ("is six blocks a floor or a ceiling") has a clear, externally-validated answer: open-by-default with an explicit opt-in to close is the standard pattern in both document and schema design, and it costs one sentence in the canonical's STATUS block or rule preamble to make explicit what is already the de facto reading. The second question (log USA26041 as a third data point that didn't force a move) is bookkeeping — the STATUS block already tracks instance count and this is the same maintenance the 2026-07-30 update performed for USA26040. Neither is a domain rule under the canonical's own LAYOUT/DOMAIN split (`_canonical-job-sheet.md` lines 20–28) — both are layout/documentation housekeeping, safe to change on judgment, no `(Jesse, YYYY-MM-DD)` attribution required by the canonical's own stated rule. The third question — retroactively migrating the live Baytown sheet's Crew Assignment / Billing Reference tables to the merged Crew & Labor / Equipment shape while USA26041 is still executing — is different in kind: the canonical's own "fact/time wall" principle (lines 64–70) treats a job sheet as static from bid-win, created once from the quoted work-up, precisely so it stays a stable record. Restructuring a live job's sheet mid-execution is a real, if smaller, version of the same risk the fact/time wall exists to prevent, and the seed itself already leans toward deferring it until the job report closes the job out. This is exactly the kind of narrow, single-open-question decision the Idea Research Loop exists to hand back rather than resolve.

## Recommended Action

Bounded one-shot edit, not urgent (USA26041's sheet works as-is), and entirely within `04-knowledge/` canonical content — out of this loop's write scope regardless of Jesse's call. If approved: (1) add one sentence to the canonical's STATUS block or the section-shape rule stating the six blocks are a minimum, additional site-specific sections are expected and do not constitute schema drift; (2) update the STATUS block's instance log to record USA26041 as a third data point that coexisted with the shape rather than forcing a move; (3) explicitly leave the Baytown sheet's own tables unmigrated until USA26041's job report closes it out, and say so in the canonical rather than leaving it silent — turns an implicit deferral into a stated one.

## Decision

- [x] Approved — make all three edits now
- [ ] Approved with edits
- [ ] Park — revisit at job report closeout
- [ ] Drop

**Resolved 2026-08-15 (Jesse, in session).** All three applied. The deciding point is the one the research note makes about rule class: under the canonical's own LAYOUT/DOMAIN split, none of these three is a domain rule. Whether the six blocks are a floor, what the instance count is, and whether a live sheet gets restructured mid-job are all layout and documentation decisions — verifiable by looking at the document, safe to change on judgment, no `(Jesse, YYYY-MM-DD)` attribution required by the canonical's own stated convention. Nothing here asserts how USADebusk operates.

Edit (1) is the substantive one and it only writes down what was already true. Nothing in the canonical, the template, or `document-routing.md` ever said the six blocks were closed; the reading was implicit, and USA26041 is what made the ambiguity cost something. Edit (3) is worth more than it looks: an unstated deferral is indistinguishable from an oversight, and the risk being managed is that a future session "tidies" a live job's sheet in good faith. Saying it in the canonical is what stops that.

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-15 | All three edits applied to `04-knowledge/_canonical-job-sheet.md`. STATUS block moved from TWO to THREE validated instances and records that USA26041 coexisted with the shape rather than moving it, replacing the "a third instance may move it again" open question that this note closed. Added a `THE SIX BLOCKS ARE A FLOOR, NOT A CEILING` layout rule and a `USA26041'S OWN SHEET STAYS UNMIGRATED UNTIL ITS JOB REPORT CLOSES IT OUT` block, the latter tied to the existing fact/time wall rather than asserted independently. No domain rule added, no attribution tag required per the canonical's own LAYOUT/DOMAIN convention. `templates/_job-sheet-template.md` deliberately untouched — it derives structure from the canonical and the floor/ceiling rule changes no structure. USA26041's live sheet not modified. | Claude (review queue) |
