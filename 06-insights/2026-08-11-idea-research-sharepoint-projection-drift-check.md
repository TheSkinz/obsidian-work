---
type: review
status: complete
review_type: idea-research
source_authority: primary
confidence: high
created: 2026-08-11
review_after: 2026-09-11
related:
  - "[[idea-sharepoint-projection-drift-check]]"
  - "[[2026-08-10-markdown-ranking-retest-owed]]"
  - "[[overview]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, idea-research, gated, copilot, sharepoint]
---

# Idea Research — SharePoint Projection Drift Check on the Health Dashboard (Gate Check)

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Only one `idea-seed` was `unexplored` in `00-inbox/`: [[idea-sharepoint-projection-drift-check]] (`created: 2026-08-10`). Per [[vault-idea-loop-spec]] step 3, the seed's own gate is checked from files before any web research starts.

## Evidence

The seed's `**Gate:**` line: "Phase 6 has not run — the library holds five pilot files, and there is no corpus to drift yet. Build after the full load, not before." Its `revisit-trigger:` frontmatter states the same condition as an event: "Phase 6 of the SharePoint knowledge base lands (22 more files in the Knowledge library) ... event: check when the full load completes."

Checked the build plan (`~/.claude/plans/create-a-new-session-effervescent-papert.md`, Phase 6) and the same-day session record in [[overview]] and `change-log.md`. Phase 6 has since split into two tranches, and only the first has landed:

- **Tranche A — landed 2026-08-10.** The 19 manual chapters, loaded with columns and Owner set via REST and audited to zero drift ([[overview]], "Two column mechanics found loading tranche A"; `change-log.md` 2026-08-10 entry: "Tranche A loaded the same session: 19 manual chapters...").
- **Tranche B — staged, not loaded.** 8 files (concept and context notes) sit ready in `_OUTPUTS/sharepoint/` but were deliberately held back so tranche A's homogeneous corpus would give a clean ranking signal. [[2026-08-10-markdown-ranking-retest-owed]] states this directly: "This is why tranche B was held back — adding eight unrelated concept and context notes first would dilute the test," and gives the load condition explicitly: "**Pass** → load tranche B... **Fail** → convert tranche A to `.docx` before loading anything else."

The retest that gates tranche B is itself unresolved as of this run: its `revisit-trigger:` says to run it "2026-08-11 or later," which is today, but nothing in the vault records the retest as having been run or scored — [[overview]] carries the Phase 5 eval and the tranche-A load notes but no ranking-retest result section, and `50-dashboards/health.md`'s dormant-trigger registry (as of the `fe46def` commit) still lists it as an open, unchecked trigger.

So the corpus this idea needs — a full, settled `Knowledge` library with nothing further staged to load — does not exist yet. A drift check built now would only ever see 19 of the library's eventual files, and could not distinguish "vault edited, SharePoint copy stale" from "tranche B simply hasn't been uploaded," which is exactly the kind of false signal the seed exists to avoid.

## Interpretation

**Gate verifiably unmet.** The trigger condition is a completed full load, and the vault's own records show the load is mid-flight: one tranche landed, one tranche staged and explicitly blocked on an eval that has not yet been scored. Per spec, no web research was performed this run.

Worth flagging for whoever reopens this: the seed's "22 more files" figure doesn't cleanly reconcile against the plan's own Phase 6 file list (19 manual chapters + 5 concepts + 1 equipment + 3 context = 28, separate from the one newly-authored Outlook-routing doc) or against tranche A + tranche B (19 + 8 = 27). Not a gate-relevant discrepancy — the qualitative fact (tranche B unloaded) settles the gate regardless of the exact count — but the revisit-trigger below points at the concrete tranche-B/retest event rather than the "22 files" figure, since that's what will actually be checkable when this is revisited.

## Recommended Action

**Stay gated — no research yet.** Re-check when tranche B is uploaded to the `Knowledge` library (evidence: [[2026-08-10-markdown-ranking-retest-owed]] scored and closed with a Pass, and the library's item count moving past the tranche-A total). At that point this seed should research where the drift check hooks (`vault_lint.py` rule, separate `vault_health.py` call, or the capture loop) and whether staged-vs-vault or live-vs-vault is the right comparison, per its own "To explore" section.

## Decision

- [ ] Confirm continued gated status
- [ ] Re-open now (gate judged satisfied)
- [ ] Drop entirely

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| | | | |
