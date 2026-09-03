---
type: note
status: inbox
created: 2026-09-03
tags: [inbox, owed, lint, sharepoint, regression, overnight]
---

# Open items left by the 2026-09-03 overnight pass

Four items. None blocks anything. Everything Jesse approved that night was executed except item 1,
which was stopped deliberately.

## 1. The SharePoint retirement was approved on a wrong premise — NOT executed

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

## 2. `JOBSHEET-PDF-STALE` is a candidate for `ERROR_CODES`

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

- **`usadebusk-sop/SKILL.md:89`** says *"CAD26001, F-901 and F-802 loop at the radiant outlets."*
  [[7-1-F-1]] records the opposite as of 2026-09-02 — CAD26001's 180s went in at the **convection
  inlets**. The 2026-09-01 drift review could not have caught this; it ran the day before the
  correction. **Lane 4, so not touched.**
- **`health.md`'s two inbox-age FAIL rows** (median 14 d against a <14 d target, oldest 35 d against
  <30 d) were already in the committed dashboard and are not caused by this pass. Archiving the
  terminal CAD26001 notes — the capture sheet at `complete`, the job-report handoff at `resolved` —
  would clear both. Proposed in the 2026-09-03 recon, never approved, so not done.
