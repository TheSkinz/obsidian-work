---
type: idea-seed
status: gated
created: 2026-08-10
revisit-trigger: "FIRED 2026-08-11 — tranche B landed (8 files; CONTEXT_Outlook-Routing.md added, CONTEXT_Workflow-Map.md dropped) and the Knowledge-library load completed at 29 markdown files, so the gate is satisfied -> build the projection drift check so health.md surfaces stale SharePoint copies. A real drift instance was caught by hand the same day (see the Evidence section below) — design against it."
related:
  - "[[2026-08-11-idea-research-sharepoint-projection-drift-check]]"
tags: [idea, vault-system, future, copilot, sharepoint]
---

# SharePoint projection drift check on the health dashboard

Idea seed captured 2026-08-10 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** The vault→SharePoint `Knowledge` library is a one-way projection with no staleness signal. `tools/sharepoint_export.py --check` already computes exactly the right answer — it exits 1 when a staged file has drifted from its vault source — but nothing runs it, so the failure mode is silent: edit a manual chapter in the vault, and Copilot keeps serving the old text indefinitely with nothing anywhere indicating a problem. A row on `50-dashboards/health.md` reading "SharePoint copies stale: N" would close that, using the mechanism that already carries pending work to Jesse.

**To explore:** Where the check hooks — a rule inside `vault_lint.py`, a separate call from `vault_health.py`, or the capture loop. Whether staged-vs-vault is the right comparison at all, or whether it should compare the vault against what is actually *live in SharePoint* (the staging folder can itself be stale relative to the uploaded copy, so a green staging check could still mean a stale library — this is the real question and it may need a REST read rather than a local diff). Whether the row is informational or a FAIL. What happens to the `Rev-A` style non-projected files that must not be reported as drift.

**Gate — satisfied 2026-08-11.** The full load has run: 29 markdown files in the library. Build is unblocked.

## Evidence from the tranche B load — design against this case

A real drift instance was caught by hand during the load, and it settles the open question above about *what* to compare.

`CONTEXT_Outlook-Routing.md` was uploaded manually and the library held the **vault source** rather than the projection — YAML frontmatter intact, no provenance line, dead `[[wikilinks]]`. Everything a cheap check would look at was correct: the filename matched, all twelve columns were set, Owner was right, the content read plausibly. Only `File/Length` against the staged copy on disk gave it away, 5489 against 5461, and SHA-256 confirmed it.

Three consequences for the design:

**Presence-only would have passed it.** So would a columns-complete check. The comparison has to be on content.

**Staged-vs-vault is not sufficient** — `--check` was green throughout, because the staging folder was correct; it was the *library* that was wrong. This confirms the tentative read in the "To explore" section: the check needs a REST read of what is actually live, not a local diff. `File/Length` is the cheap first pass and a `$value` fetch plus hash is the exact one.

**The failure mode is a plausible-looking wrong file, not a missing one.** Any path that does not run `sharepoint_export.py` — a hand upload, a drag-and-drop, a file pulled from the wrong folder — produces something that looks right everywhere the library can see.

---

## Related: an M365/SharePoint operating skill

Not a separate seed, because the trigger is the same class of event. Jesse expects to build workflows, agents, and Power Automate flows on this tenant eventually, with no immediate plans (stated 2026-08-10). If M365 admin work recurs past Phase 6, the Chrome-driving operating notes now recorded in [[overview]] are the content of a skill, already written — REST-verify instead of trusting the UI, prefer the Copilot panel to clicking, native dialogs block the extension, classic `ViewEdit.aspx` does not save, `find` beats `read_page` on SharePoint's dropdowns.

Promote them to a skill at the **third** M365 admin session, not before. One build plus one load is not a pattern.
