---
type: note
status: inbox
created: 2026-09-03
tags: [inbox, owed, lint, sharepoint, regression, overnight]
---

# Open items left by the 2026-09-03 overnight pass

Four items. None blocks anything. Everything Jesse approved that night was executed except item 1,
which was stopped deliberately.

> [!success] Items 1 and 2 closed 2026-09-03 — see the resolution lines on each.
> Items 3 and 4 remain open. Item 4's SOP half is now also closed.

## 1. ~~The SharePoint retirement was approved on a wrong premise — NOT executed~~ **RESOLVED**

**Resolved 2026-09-03.** Jesse confirmed the eval was finished. The file was deleted and its
`NOT_PROJECTED` entry removed from `sharepoint_export.py`, so the exporter no longer carries a
suppression rule for a file nobody can find; `--check` runs clean. The misreading was corrected in
place on [[2026-09-02-session-open-items]] item 4 rather than deleted, so the *reason* it was nearly
removed for the wrong cause stays on the record. Original write-up below.

### Original entry

Jesse ruled "retire" on `_OUTPUTS/sharepoint/MANUAL-09_Phase-II-Mechanical-Decoking-Rev-A.md`,
on the reading given in [[2026-09-02-session-open-items]] item 4: an orphaned stale duplicate,
holding "CONV port" after the 2026-09-02 correction, unreachable by the exporter's manifest.

**That reading is wrong.** `tools/sharepoint_export.py:149` lists the file in `NOT_PROJECTED`:

> `"MANUAL-09_Phase-II-Mechanical-Decoking-Rev-A.md",  # deliberate-error test file`

It is an **eval instrument**, listed there so the exporter does not claim ownership of it or report
it as unexpected. It is *supposed* to contain a wrong string — that is what makes it a
deliberate-error test artifact. The "unreachable by the manifest" observation is true and was
mistaken for an accident when it is deliberate.

Also worth knowing before deciding again: **`_OUTPUTS/` is untracked**, so deleting it would be
permanent, not recoverable from git as the overnight plan asserted.

**The decision needs re-taking on the corrected facts.** If the eval it belongs to is finished, it
can go; if not, it should stay and the 09-02 note should be corrected rather than the file deleted.
Nothing was changed either way.

## 2. ~~`JOBSHEET-PDF-STALE` is a candidate for `ERROR_CODES`~~ **RULED — stays a warning**

**Ruled 2026-09-03: it stays at warning tier.** Promoting it blocks commits on an edited job-sheet
HTML, which is a workflow change rather than lint tuning. The decision is now recorded in the rule's
own docstring so it is not re-opened on the starts-at-zero argument, which was made and lost.
Original write-up below.

### Original entry

Built and shipped as a warning. **It fires on nothing** — USA26040's PDF is one minute newer than its
HTML, USA26038's pair carry identical mtimes. The plan expected a two-file backlog and there is none.

`vault_lint.py`'s own docstring says a rule that starts at zero belongs at error tier: *"an error that
starts at zero can only ever mean someone typed a new value, which is exactly the event worth stopping
for."* That is the argument TUBE-GEOM-HEADER and VERIFIED-FORMAT were promoted on.

Held at warning because promoting it makes lint exit 1 the moment a job-sheet HTML is edited, blocking
the commit until the PDF is re-rendered. Defensible — a drifted pair should not be committed — but it
is a workflow change rather than lint tuning, and it was not what was approved. One line in
`ERROR_CODES` if wanted.

## 3. Regression debt grew by the merge

Applying F4, F5 and F6 edited `usadebusk-fieldpm` and `usadebusk-vault-ingest`. Under
`~/.claude/regression/README.md` rule 2 that makes their fixtures owed — but they were already owed.
**Total is unchanged at F1, F2, F3, F4, F6**, and it still has its own session per the 2026-09-02
ruling. Recorded so the merge is not read later as having added a new debt it did not.

## 4. Two lint findings nobody has ruled on

Both pre-date this pass and neither was in scope.

- ~~**`usadebusk-sop/SKILL.md:89`** says *"CAD26001, F-901 and F-802 loop at the radiant outlets."*~~
  **CORRECTED 2026-09-03** (config `6b6d4a8`). CAD26001 moved to the convection-inlet list; F-901 and
  F-802 unchanged. The 2026-09-01 drift review could not have caught it — it ran the day before the
  as-built correction, which is the standing gap in a monthly audit.
- **`health.md`'s two inbox-age FAIL rows** (median 14 d against a <14 d target, oldest 35 d against
  <30 d) were already in the committed dashboard and are not caused by this pass. **STILL OPEN, and
  the fix I first proposed was wrong.** Archiving the terminal CAD26001 notes would *not* clear them:
  `inbox_stats()` (`tools/vault_health.py:233`) skips `TERMINAL_STATUS` when computing ages, so those
  notes are already excluded and archiving them lowers only the count. The rows are driven by six
  genuinely pending notes dating to 2026-07-27 — the oldest are
  `2026-07-20-claudeai-skill-library-is-a-second-copy`,
  `2026-07-20-local-toolchain-and-soffice-windows-bug` and
  `2026-07-24-fixtures-work-better-as-rule-audit`. **Clearing this is inbox triage, not a yes/no**,
  and it is the largest remaining piece of decision-free-ish work in the vault.
