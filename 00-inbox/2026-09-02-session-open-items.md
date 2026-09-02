---
type: note
status: inbox
created: 2026-09-02
tags: [inbox, owed, regression, data-quality, file-estate]
---

# Open items left by the 2026-09-02 flow-test / CAD-rename session

Six loose ends from a session that landed three Lane 4 rulings. None blocks the CAD26001 job report — that has its own handoff at [[2026-09-02-cad26001-job-report-handoff]].

## 1. Regression replay owed — six skills edited, none replayed

`~/.claude/regression/README.md` rule 2 (Jesse's call, 2026-07-25): after a substantive edit to any skill, replay the one or two fixtures that load it **before the edit is trusted.** A substantive edit is one that changes what a number comes out as, adds or removes a rule, or resolves an ambiguity — all three describe today's changes.

Edited in commit `fc7f8f6`: `usadebusk-core`, `usadebusk-equipment` (+ `references/equipment-circuit-diagrams.md`), `usadebusk-estimating`, `usadebusk-sop` (+ `references/sop-pigging-diagrams.md`), `usadebusk-vault-ingest` (+ `references/document-routing.md`).

Fixtures owed: **F1, F2, F4, F6.**

This is a known rot path, not a hypothetical — the README records a 2026-07-28 staleness sweep that found five fixtures each sitting behind at least one un-replayed skill commit. Jesse ruled 2026-09-02 that this gets its own session rather than riding along with the job report.

## 2. CLAUDE.md says `archive/` is gitignored. It is not.

The vault CLAUDE.md states archive is gitignored and warns that *"a file in `archive/` may exist only on disk. Never treat deletion from `archive/` as recoverable without checking `git ls-files` first."*

`git ls-files archive/` returns tracked files. The caution is built on a false premise. Checked 2026-09-02 before renaming three files there, which is how it surfaced.

Either the ignore rule was added after those files were already tracked (git keeps tracking what it already tracks), or the claim was never true. Worth establishing which before correcting the line, because the *advice* — verify before deleting — is still right even though its stated reason is wrong.

## 3. Remaining `CND` filenames on the file estate

Jesse renamed the folders he could find on 2026-09-02; some filenames remain. The vault is now fully `CAD` and the disk is catching up, so the mismatch is deliberate and temporary.

**Do not sweep `CND25002 NWR Final Tickets.pdf` with the Syncrude rename.** It belongs to **North West Redwater**, a different customer and a different job. It appears in the vault only at `archive/2026-06-26-cad25004-routing-review.md`, in a table that was recording filenames *as observed on disk* in OneDrive on 2026-06-26. That note's three path cells were rewritten by the 2026-09-02 sweep along with everything else; Jesse ruled no revert, on the basis that the disk is being renamed to match.

Nothing lints this. `POINTER-DEAD` only resolves absolute paths under `02-facilities/`, and these are relative `OneDrive/…` paths in `archive/` — they fail both gates and will never surface as broken.

## 4. Stale SharePoint projection with no generator

`_OUTPUTS/sharepoint/MANUAL-09_Phase-II-Mechanical-Decoking-Rev-A.md` still contains "CONV port" after the 2026-09-02 correction. **`tools/sharepoint_export.py`'s manifest does not know about it**, so no amount of re-running the exporter will fix it — it is an orphaned duplicate beside the real projection, which did regenerate correctly.

Retire it or regenerate it by hand. As it stands it is a wrong document sitting in the upload staging directory.

## 5. The six-port Trimax figure is inferred, not verified

`04-knowledge/equipment/equipment-library.md` previously read *"Two Fig. 200 (3") ports at rear of trailer."* Jesse, 2026-09-02: *"For all 3 sides / pumps of the Trimax units, each side (left, center, right) has a Blue and Red port."* Six follows from that on a triple.

The card now says six and **marks it as not eyeballed on a unit.** One glance at a trailer settles it. Until then it is an inference from a statement, not a count.

## 6. Syncrude has no `## Source Files` section

Per `rfq-intake-protocol.md:26`, *"The vault is the index, OneDrive is the store… the full path **must** be recorded in the quote note's `## Source Files` section… An unrecorded path is how a bid trail goes cold."* Eight notes carry such a section. **None of them is Syncrude** — it is the one recently-active job with an entirely unrecorded file estate.

Two specifics worth fixing while someone is in there:

- [[CAD26001-flow-tests]] frontmatter sources the scan as `Downloads/Doc 09-01-2026 18-05-51.pdf` — a bare relative path in the most sweepable directory on the machine. Move it into the OneDrive job folder and re-point.
- [[7-1-F-1]] names five source documents (`syncrude drawings.pdf`, `F-1 DRAWINGS.pdf`, `7-1F-1.tif`, `Job_24002_Syncrude_Fort_McMurray_71_F1_Heater_Job_Report.pdf`, and a rejected 37-1 binder) but **never names the folder any of them live in.** None carries a job-number prefix, so the CAD rename does not touch them — the problem is that they have no recorded home at all.
