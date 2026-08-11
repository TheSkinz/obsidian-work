---
type: review
status: open
review_type: cleanup
source_authority: session
confidence: high
created: 2026-08-10
review_after: 2026-08-24
revisit-trigger: "Phase 5 eval of the SharePoint Knowledge agent completes -> delete the deliberate-error test file MANUAL-09_Phase-II-Mechanical-Decoking-Rev-A from the Knowledge library, and delete or repoint the PROBE - Markdown Format Test agent — event: check when the six eval questions have been run twice"
related:
  - "[[overview]]"
tags: [copilot, sharepoint, cleanup, safety]
---

# SharePoint pilot — cleanup owed after Phase 5

Three items created on 2026-08-10 during the Furnace Decoking SharePoint build are deliberately temporary. Two of them must not outlive the eval that needs them.

## 1. Delete `MANUAL-09_Phase-II-Mechanical-Decoking-Rev-A` — do not defer this

It is a **deliberately falsified engineering document**, sitting in the `Knowledge` library at `usadebusk.sharepoint.com/sites/FurnaceDecoking`. It is a self-consistent copy of manual chapter 9 with the pig-OD ceiling changed from *governing tube ID + 0.250 in* to **+ 0.500 in**, and the worked example's ceiling changed from 6.315 in to 6.565 in to match. Nothing in the body marks it as wrong — that is what makes it a valid test of whether the `Status` column fires, and exactly what makes it a hazard if it is forgotten.

Its guards are metadata only: `Status = deprecated`, `Source Rank = 6 AI/unreviewed`, `Confidence = low`, a past `Review After`, and a Description reading "SYNTHETIC TEST FILE." Those guards protect a careful reader. They do not protect someone who asks an agent a question and gets an answer.

It exists to answer eval Q1: does the agent prefer the `active` file over the `deprecated` one, or flag the deprecation, when both answer the same question and contradict on one number. Once that question has been run twice, the file has done its job.

**Q1 passed on run 1, 2026-08-10** (detail in [[overview]]). The agent returned 0.250 citing the active file and naming its Status, then on follow-up identified Rev-A by name, cited its `deprecated`/`low` values, and ruled it non-authoritative. Run 2 is still owed, along with eval Q2–Q6. **The file may be deleted as soon as run 2 completes — it has already produced the result it was built for.**

## 2. Delete or repoint `PROBE - Markdown Format Test.agent`

Lives in the `Documents` library. Built to test whether a library-scoped agent could retrieve and cite `.md` — it can. Either delete it, or repoint its source from `Documents` to `Knowledge` and reuse it for the Phase 6 volume retest, which is still owed: markdown was proven reachable and citable at n=2 with identical content, never proven to *rank* against a corpus of differing files.

## 3. `Review Overdue` view — checked, no fix needed

Recorded because it was investigated and the first read was wrong. The filter is `ReviewAfter < [Today]` with no is-not-empty clause, and `Decoking Knowledge.agent` briefly appeared in the view with no date set — which looked like empty dates matching the filter, a bug that would make the view useless at Phase 6 volume.

It is not a bug. Re-checked minutes later with the `.agent` file still in the library and still carrying no Review After value: the view returns exactly one row, the deprecated test file. Empty dates do not match. The earlier appearance was the list rendering a just-created item before the filter re-queried.

**Do not "fix" this filter.** An attempt to add the clause through the classic `ViewEdit.aspx` page failed with "View does not exist" and committed nothing — verified against the REST API, all four views intact with their original GUIDs and CAML unchanged. Worth knowing generally: **classic view-edit postbacks do not reliably save against a modern library on this site.** Use the Copilot panel or the modern view UI instead.

## Also noted, lower priority

`Decoking Knowledge.agent` saved into the `Knowledge` library itself, so the agent's own config sits inside its knowledge source. Probably harmless — it is JSON, not prose — but the library's whole value is being curated. Move it to `Site Assets` when convenient.
