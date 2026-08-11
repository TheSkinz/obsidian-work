"""Export selected vault notes to the SharePoint staging folder.

The vault is canonical; the SharePoint `Knowledge` library is a one-way
projection of it. This script is that projection. Re-run it after editing any
sourced note so the SharePoint copy does not silently drift.

No format conversion happens here. Markdown was verified on 2026-08-10 to
index, retrieve, and cite correctly in this tenant at both the M365 Copilot app
and a library-scoped SharePoint agent, so the `.docx` converter the original
build plan called for was dropped. See `07-llms/copilot/overview.md`.

What the transform does:
  - strips YAML frontmatter (the SharePoint columns are the only copy of
    `status` and `review_after`; two copies would silently disagree)
  - stamps a provenance line under the H1 naming the vault source and date
  - writes out under the leading-token filename convention the index ranks on

Usage:
    python tools/sharepoint_export.py            # write staging copies
    python tools/sharepoint_export.py --check    # report drift, write nothing

`--check` exits 1 if any staged file is missing or differs from what the vault
would produce now, so it can gate a pre-upload step.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
STAGING = VAULT / "_OUTPUTS" / "sharepoint"

# Vault source -> SharePoint filename. Phase 6 additions go here.
MANIFEST: list[tuple[str, str]] = [
    ("04-knowledge/manual/09-phase-ii-mechanical-decoking.md",
     "MANUAL-09_Phase-II-Mechanical-Decoking.md"),
    ("04-knowledge/manual/10-verification-and-completion.md",
     "MANUAL-10_Verification-and-Completion.md"),
    ("01-context/company-context.md",
     "CONTEXT_Company.md"),
    ("04-knowledge/concepts/quote-lifecycle.md",
     "CONCEPT_Quote-Lifecycle.md"),
]

# Eval instruments and other hand-built staging files this script must not
# claim ownership of or report as unexpected.
NOT_PROJECTED = {
    "MANUAL-09_Phase-II-Mechanical-Decoking-Rev-A.md",  # deliberate-error test file
    "_COLUMN-VALUES.md",
}

FRONTMATTER = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)
PROVENANCE = re.compile(r"^\*Source: `[^`]+` — exported \d{4}-\d{2}-\d{2}\*$")


def project(text: str, source_rel: str, exported: str) -> str:
    """Vault note -> the exact bytes that belong in the staging folder."""
    text = FRONTMATTER.sub("", text).lstrip("\n")
    line = f"*Source: `{source_rel}` — exported {exported}*"

    lines = text.split("\n")
    if lines and lines[0].startswith("# "):
        out = [lines[0], "", line] + lines[1:]
    else:
        out = [line, ""] + lines
    return "\n".join(out).rstrip() + "\n"


def existing_export_date(path: Path) -> str | None:
    """Reuse the prior export date when content is otherwise unchanged, so a
    no-op run does not churn every file's provenance line."""
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8").split("\n")[:5]:
        if PROVENANCE.match(line.strip()):
            return line.strip().rsplit(" ", 1)[1].rstrip("*")
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="report drift and write nothing; exit 1 if any file is stale")
    args = ap.parse_args()

    today = date.today().isoformat()
    STAGING.mkdir(parents=True, exist_ok=True)

    stale: list[str] = []
    for src_rel, out_name in MANIFEST:
        src = VAULT / src_rel
        if not src.exists():
            print(f"MISSING SOURCE  {src_rel}")
            stale.append(out_name)
            continue

        dest = STAGING / out_name
        prior = existing_export_date(dest)

        # Compare against the prior date first: if only the date would differ,
        # the content is unchanged and there is nothing to re-export.
        unchanged = (
            prior is not None
            and dest.read_text(encoding="utf-8")
            == project(src.read_text(encoding="utf-8"), src_rel, prior)
        )

        if unchanged:
            print(f"ok       {out_name}")
            continue

        stale.append(out_name)
        if args.check:
            print(f"STALE    {out_name}  <- {src_rel}")
        else:
            dest.write_text(project(src.read_text(encoding="utf-8"), src_rel, today),
                            encoding="utf-8")
            print(f"written  {out_name}  <- {src_rel}")

    projected = {name for _, name in MANIFEST}
    for path in sorted(STAGING.glob("*.md")):
        if path.name not in projected and path.name not in NOT_PROJECTED:
            print(f"UNTRACKED  {path.name}  (in staging, not in MANIFEST)")

    if args.check and stale:
        print(f"\n{len(stale)} file(s) stale — re-run without --check before uploading.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
