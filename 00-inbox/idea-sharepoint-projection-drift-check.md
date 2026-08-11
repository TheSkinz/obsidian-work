---
type: idea-seed
status: gated
created: 2026-08-10
revisit-trigger: "Tranche B lands (8 files, staged in _OUTPUTS/sharepoint/ — no longer blocked, the markdown ranking retest passed 2026-08-11 per [[2026-08-10-markdown-ranking-retest-owed]], so the load is free to run) and the full Knowledge-library load completes -> build the projection drift check so health.md surfaces stale SharePoint copies — event: check when tranche B is uploaded (verified still staged, not loaded, 2026-08-11)"
related:
  - "[[2026-08-11-idea-research-sharepoint-projection-drift-check]]"
tags: [idea, vault-system, future, copilot, sharepoint]
---

# SharePoint projection drift check on the health dashboard

Idea seed captured 2026-08-10 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** The vault→SharePoint `Knowledge` library is a one-way projection with no staleness signal. `tools/sharepoint_export.py --check` already computes exactly the right answer — it exits 1 when a staged file has drifted from its vault source — but nothing runs it, so the failure mode is silent: edit a manual chapter in the vault, and Copilot keeps serving the old text indefinitely with nothing anywhere indicating a problem. A row on `50-dashboards/health.md` reading "SharePoint copies stale: N" would close that, using the mechanism that already carries pending work to Jesse.

**To explore:** Where the check hooks — a rule inside `vault_lint.py`, a separate call from `vault_health.py`, or the capture loop. Whether staged-vs-vault is the right comparison at all, or whether it should compare the vault against what is actually *live in SharePoint* (the staging folder can itself be stale relative to the uploaded copy, so a green staging check could still mean a stale library — this is the real question and it may need a REST read rather than a local diff). Whether the row is informational or a FAIL. What happens to the `Rev-A` style non-projected files that must not be reported as drift.

**Gate:** Phase 6 has not run — the library holds five pilot files, and there is no corpus to drift yet. Build after the full load, not before.

---

## Related: an M365/SharePoint operating skill

Not a separate seed, because the trigger is the same class of event. Jesse expects to build workflows, agents, and Power Automate flows on this tenant eventually, with no immediate plans (stated 2026-08-10). If M365 admin work recurs past Phase 6, the Chrome-driving operating notes now recorded in [[overview]] are the content of a skill, already written — REST-verify instead of trusting the UI, prefer the Copilot panel to clicking, native dialogs block the extension, classic `ViewEdit.aspx` does not save, `find` beats `read_page` on SharePoint's dropdowns.

Promote them to a skill at the **third** M365 admin session, not before. One build plus one load is not a pattern.
