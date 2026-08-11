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

Content is projected verbatim otherwise. Every member of the Furnace Decoking
site is trusted with all of its data (Jesse, 2026-08-10), so nothing is
withheld or rewritten on the way out.

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

# Vault source -> SharePoint filename.
#
# Deliberately absent, do not "fix" by adding:
#   04-knowledge/concepts/estimating-pricing.md   commercial content
#   04-knowledge/concepts/rfq-intake-protocol.md  mostly vault-internal mechanics
#                                                 (INDEX lookups, dormant triggers,
#                                                 quote frontmatter) plus customer-
#                                                 linked rate detail — low value here
#   01-context/active-jobs.md                     volatile, no refresh mechanism
#   01-context/output-preferences.md              Claude-harness specific
#   01-context/system-workflow-reference.md       Claude-harness specific
MANIFEST: list[tuple[str, str]] = [
    # --- Phase 3 pilot -----------------------------------------------------
    ("04-knowledge/manual/09-phase-ii-mechanical-decoking.md",
     "MANUAL-09_Phase-II-Mechanical-Decoking.md"),
    ("04-knowledge/manual/10-verification-and-completion.md",
     "MANUAL-10_Verification-and-Completion.md"),
    ("01-context/company-context.md",
     "CONTEXT_Company.md"),
    ("04-knowledge/concepts/quote-lifecycle.md",
     "CONCEPT_Quote-Lifecycle.md"),

    # --- Phase 6 tranche A: the remaining manual chapters ------------------
    # Loaded and ranking-tested alone. Seventeen documents about one process,
    # competing directly with each other — the sharpest available test of
    # whether markdown ranks at volume in this tenant.
    ("04-knowledge/manual/00-manual-index.md",
     "MANUAL-00_Manual-Index.md"),
    ("04-knowledge/manual/01-scope-and-use.md",
     "MANUAL-01_Scope-and-Use.md"),
    ("04-knowledge/manual/02-what-mechanical-pigging-is.md",
     "MANUAL-02_What-Mechanical-Pigging-Is.md"),
    ("04-knowledge/manual/03-heater-and-coil-fundamentals.md",
     "MANUAL-03_Heater-and-Coil-Fundamentals.md"),
    ("04-knowledge/manual/04-project-inputs-and-engineering.md",
     "MANUAL-04_Project-Inputs-and-Engineering.md"),
    ("04-knowledge/manual/05-system-and-equipment.md",
     "MANUAL-05_System-and-Equipment.md"),
    ("04-knowledge/manual/06-safety-and-permit-interface.md",
     "MANUAL-06_Safety-and-Permit-Interface.md"),
    ("04-knowledge/manual/07-roles-and-responsibilities.md",
     "MANUAL-07_Roles-and-Responsibilities.md"),
    ("04-knowledge/manual/08-phase-i-rig-in.md",
     "MANUAL-08_Phase-I-Rig-In.md"),
    ("04-knowledge/manual/11-phase-iii-rig-out-and-restoration.md",
     "MANUAL-11_Phase-III-Rig-Out-and-Restoration.md"),
    ("04-knowledge/manual/12-ancillary-filtration-and-waste.md",
     "MANUAL-12_Ancillary-Filtration-and-Waste.md"),
    ("04-knowledge/manual/13-ancillary-initial-flush-and-pitch-removal.md",
     "MANUAL-13_Ancillary-Initial-Flush-and-Pitch-Removal.md"),
    ("04-knowledge/manual/14-ancillary-smart-pig-support.md",
     "MANUAL-14_Ancillary-Smart-Pig-Support.md"),
    ("04-knowledge/manual/15-ancillary-passivation-stainless.md",
     "MANUAL-15_Ancillary-Passivation-Stainless.md"),
    ("04-knowledge/manual/16-documentation-and-deliverables.md",
     "MANUAL-16_Documentation-and-Deliverables.md"),
    ("04-knowledge/manual/17-glossary.md",
     "MANUAL-17_Glossary.md"),
    ("04-knowledge/manual/18-reference-tables.md",
     "MANUAL-18_Reference-Tables.md"),

    # --- Phase 6 tranche B: gated on the tranche A ranking retest ----------
    ("04-knowledge/concepts/industry-foundation.md",
     "CONCEPT_Industry-Foundation.md"),
    ("04-knowledge/concepts/process-flow.md",
     "CONCEPT_Process-Flow.md"),
    ("04-knowledge/concepts/decoking-method-comparison.md",
     "CONCEPT_Decoking-Method-Comparison.md"),
    ("04-knowledge/concepts/field-operations.md",
     "CONCEPT_Field-Operations.md"),
    ("04-knowledge/equipment/equipment-library.md",
     "EQUIP_Equipment-Library.md"),
    ("01-context/equipment-fleet.md",
     "CONTEXT_Equipment-Fleet.md"),
    ("01-context/estimating-approach.md",
     "CONTEXT_Estimating-Approach.md"),
    ("01-context/workflow-map.md",
     "CONTEXT_Workflow-Map.md"),

    # Authored 2026-08-11 for this load, not projected from pre-existing vault
    # content. The three-tier model was buried inside 07-llms/copilot/overview.md;
    # Copilot reads these nine folders daily without knowing what any of them mean.
    #
    # Its consumer is tenant-wide M365 Copilot, NOT the Decoking Knowledge agent —
    # SharePoint agents cannot reach Outlook mail. It sits on this site because that
    # is what puts it in the tenant index, and any eval of it must be run untagged.
    ("08-systems/outlook-email-architecture.md",
     "CONTEXT_Outlook-Routing.md"),
]

# No redaction or restricted-content scan lives here, deliberately.
#
# A redaction mechanism and a cost/margin scanner were built on 2026-08-10 and
# removed the same day: Jesse ruled that every member of the Furnace Decoking
# site is trusted with all of its data, so nothing needs redacting and the
# machinery had no constraint left to serve. Both are recoverable from commit
# 613d872 if site membership ever stops being fully trusted — restore rather
# than rebuild.

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
