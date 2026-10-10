#!/usr/bin/env python3
"""grok_sync_check.py — read-only check of Grok Bot state from the OneDrive backup.

WHY THIS EXISTS. Claude's recurring work with Grok Bot is checking the Bots, not
driving them, and on 2026-10-04 every check that mattered could be answered from
the Bots' OneDrive backup without opening the app:

  - the live Duration Model skill had silently lost three 2026-09-17 rulings that
    the vault mirror still held, so Estimator had been running without them
    (mirror drift runs in BOTH directions);
  - skills the Bots wrote from their own threads had baked in one job's values
    (a field map with "text": "Cenovus") that the next job would have inherited;
  - a job's state.md listed 12 "open" items that the vault had mostly settled;
  - the backup routine reports nothing when it succeeds, so a silent failure is
    indistinguishable from a quiet day unless something reads its log.

The routine "Workspace backup" (Architect, Weekdays 18:00 CDT) mirrors setup/,
jobs/, bots/ and skills/ to OneDrive GrokBot-Backup/ and logs each run to
setup/backup-log.md. This script reads that mirror. It never writes to it and
never touches the app. Opening Grok Bot is for sending a Bot a message.

    python tools/grok_sync_check.py            # full report
    python tools/grok_sync_check.py --quiet    # non-PASS lines only

Exit 1 on any FAIL. See 07-llms/grok/bot-setup/SETUP.md, "Driving Grok Bot from
Claude Code".
"""

import argparse
import datetime as dt
import difflib
import re
import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
MIRROR_DIR = VAULT / "07-llms" / "grok" / "bot-setup" / "skills"
DEFAULT_BACKUP = Path(r"C:\Users\Jwuts\OneDrive\GrokBot-Backup")

STALE_BUSINESS_DAYS = 2

# vault mirror name -> live skill folder name, where they differ
NAME_MAP = {
    "safety-lms-training": "isnetworld-online-training",
}

# Same pattern Architect's audit used (/workspace/setup/audit-job-specifics.md).
JOB_PATTERN = re.compile(
    r"Cenovus|Lima|USA2\d{4}|DSP2\d{4}|PR-\d|Alfredo|Wawa|7095|10787|7219|Garza|Ruiz|Mixon",
    re.IGNORECASE,
)
# Method skills that cite closed jobs from the vault as evidence, not as defaults.
# Empty since 2026-10-10: the three that did (Duration Model, Proposal Assembly,
# Work-Up Billing Math) retired with the Bid Desk; that work runs through Claude
# Code on the box with the real skills.
VAULT_CITED: set[str] = set()
EXAMPLE_MARK = re.compile(r"example|worked", re.IGNORECASE)

BOOTSTRAP_LINE = re.compile(r"^\s*Before starting, run `?bash /workspace/setup/bootstrap\.sh`?\.?\s*$")


def business_days_between(start: dt.date, end: dt.date) -> int:
    """Weekdays strictly after `start` up to and including `end`."""
    days, d = 0, start
    while d < end:
        d += dt.timedelta(days=1)
        if d.weekday() < 5:
            days += 1
    return days


def backup_status(backup: Path, today: dt.date | None = None):
    """Return (status, last_ok_date_or_None, detail).

    status is "ok", "FAIL: backup stale", "FAIL: no backup log" or "-" when the
    OneDrive mirror is absent on this machine (nothing judged). Shared with
    vault_health.py so the threshold lives in one place.
    """
    today = today or dt.date.today()
    if not backup.exists():
        return "-", None, f"{backup} not present on this machine"
    log = backup / "setup" / "backup-log.md"
    if not log.exists():
        return "FAIL: no backup log", None, str(log)
    last_ok = None
    for line in log.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"\s*(\d{4}-\d{2}-\d{2})\b.*result=ok", line)
        if m:
            last_ok = dt.date.fromisoformat(m.group(1))
    if last_ok is None:
        return "FAIL: no backup log", None, "no result=ok line"
    gap = business_days_between(last_ok, today)
    if gap > STALE_BUSINESS_DAYS:
        return "FAIL: backup stale", last_ok, f"{gap} business days since last ok run"
    return "ok", last_ok, f"{gap} business day(s) since last ok run"


CLAUDE_CONFIG = Path.home() / ".claude"


def claude_config_status(backup: Path):
    """Return (status, copied_label_or_None, detail) for the Bot box's claude-config copy.

    The Bot box cannot pull the private claude-config repo (its network carries
    HTTPS only, and SSH is refused on every port -- 2026-10-10), so Architect
    copies skills/ and CLAUDE.md through the GitHub connector when Claude Code
    asks, and records the git object ids it copied in setup/claude-config-sha.txt
    on OneDrive. Comparing tree/blob ids -- not the repo HEAD -- means a memory or
    settings commit never reads as drift; only a change to what the box runs does.
    Compared against origin/main because the box copies what is pushed.
    """
    if not backup.exists():
        return "-", None, f"{backup} not present on this machine"
    marker = backup / "setup" / "claude-config-sha.txt"
    if not marker.exists():
        return "FAIL: no copy marker", None, str(marker)
    fields = dict(
        line.split("=", 1) for line in marker.read_text(encoding="utf-8", errors="replace").splitlines()
        if "=" in line
    )
    fields = {k.strip(): v.strip() for k, v in fields.items()}
    copied = fields.get("copied")
    want = {}
    for key, ref in (("skills_tree", "origin/main:skills"), ("claude_md_blob", "origin/main:CLAUDE.md")):
        try:
            want[key] = subprocess.run(
                ["git", "-C", str(CLAUDE_CONFIG), "rev-parse", ref],
                capture_output=True, text=True, check=True,
            ).stdout.strip()
        except (OSError, subprocess.CalledProcessError):
            return "-", copied, f"cannot read {ref} in {CLAUDE_CONFIG}"
    behind = [k for k, sha in want.items() if fields.get(k) != sha]
    if behind:
        return "FAIL: box copy behind", copied, f"{', '.join(behind)} differ from origin/main -- send Architect a refresh handoff"
    return "ok", copied, "skills/ and CLAUDE.md match origin/main"


def skill_body(path: Path) -> list[str]:
    """Strip YAML frontmatter and the bootstrap line; drop blank lines; trim whitespace."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                lines = lines[i + 1:]
                break
    out = []
    for ln in lines:
        if BOOTSTRAP_LINE.match(ln):
            continue
        norm = " ".join(ln.split())
        if norm:
            out.append(norm)
    return out


def check_drift(backup: Path):
    rows = []
    live_root = backup / "skills"
    if not live_root.exists():
        return [("FAIL", "skills/ missing from backup")]
    mirrored_live = set()
    for mirror in sorted(MIRROR_DIR.glob("*.md")):
        live_name = NAME_MAP.get(mirror.stem, mirror.stem)
        mirrored_live.add(live_name)
        live = live_root / live_name / "SKILL.md"
        if not live.exists():
            rows.append(("WARN", f"{mirror.stem}: no live skill '{live_name}' in backup"))
            continue
        a, b = skill_body(mirror), skill_body(live)
        vault_only = live_only = 0
        for op in difflib.ndiff(a, b):
            if op.startswith("- "):
                vault_only += 1
            elif op.startswith("+ "):
                live_only += 1
        if not vault_only and not live_only:
            rows.append(("PASS", f"{mirror.stem}: in sync"))
            continue
        hints = []
        if vault_only:
            hints.append(f"{vault_only} vault-only (live may be stale)")
        if live_only:
            hints.append(f"{live_only} live-only (mirror may be stale)")
        rows.append(("WARN", f"{mirror.stem}: " + ", ".join(hints)))
    for folder in sorted(p for p in live_root.iterdir() if p.is_dir()):
        if folder.name not in mirrored_live:
            rows.append(("WARN", f"{folder.name}: live skill has no vault mirror"))
    return rows


def check_job_specifics(backup: Path):
    rows, flagged, ok = [], 0, 0
    targets = list((backup / "skills").glob("*/SKILL.md"))
    setup = backup / "setup"
    if setup.exists():
        for p in setup.rglob("*"):
            if not p.is_file() or p.name == "audit-job-specifics.md":
                continue
            if "reference" in p.parts or p.suffix.lower() not in {".md", ".json", ".txt", ".sh"}:
                continue
            targets.append(p)
    for p in sorted(targets):
        skill = p.parent.name if p.name == "SKILL.md" else None
        in_example = False  # inside a heading or paragraph block labeled as an example
        for n, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            s = line.strip()
            if s.startswith("#"):
                in_example = bool(EXAMPLE_MARK.search(s))
            elif re.match(r"^\**(worked )?example\b", s, re.IGNORECASE):
                in_example = True
            if not JOB_PATTERN.search(line):
                continue
            if skill in VAULT_CITED or in_example or EXAMPLE_MARK.search(line):
                ok += 1
                continue
            flagged += 1
            rel = p.relative_to(backup)
            rows.append(("WARN", f"{rel}:{n}: {line.strip()[:110]}"))
    rows.insert(0, ("PASS" if not flagged else "WARN",
                    f"{ok} labeled/vault-cited hit(s), {flagged} unlabeled"))
    return rows


def open_items(backup: Path):
    rows = []
    for state in sorted((backup / "jobs").glob("*/state.md")):
        job = state.parent.name
        if job.startswith("USA999"):
            continue
        items, in_open = [], False
        for line in state.read_text(encoding="utf-8", errors="replace").splitlines():
            s = line.strip()
            if re.match(r"^(#+\s*)?Open\b", s):
                in_open = True
                continue
            if in_open:
                if s.startswith("- "):
                    items.append(s[2:])
                elif s:
                    in_open = False
        rows.append(("PASS" if not items else "INFO", f"{job}: {len(items)} open"))
        rows += [("INFO", f"  {i[:120]}") for i in items]
    cos = backup / "bots" / "Chief of Staff" / "outstanding.md"
    if cos.exists():
        items = [l.strip()[2:] for l in cos.read_text(encoding="utf-8", errors="replace").splitlines()
                 if l.strip().startswith("- ")]
        rows.append(("PASS" if not items else "INFO", f"Chief of Staff outstanding: {len(items)}"))
        rows += [("INFO", f"  {i[:120]}") for i in items]
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--backup", type=Path, default=DEFAULT_BACKUP,
                    help="GrokBot-Backup root (default: local OneDrive mirror)")
    ap.add_argument("--quiet", action="store_true", help="print only non-PASS lines")
    args = ap.parse_args()

    status, last_ok, detail = backup_status(args.backup)
    sections = [("Backup age", [("PASS" if status == "ok" else
                                  "SKIP" if status == "-" else "FAIL",
                                  f"last ok run {last_ok or '-'}; {detail}")])]
    cc_status, cc_copied, cc_detail = claude_config_status(args.backup)
    sections.append(("claude-config copy on the Bot box", [(
        "PASS" if cc_status == "ok" else "SKIP" if cc_status == "-" else "FAIL",
        f"copied {cc_copied or '-'}; {cc_detail}")]))
    if status != "-":
        sections += [
            ("Mirror drift (vault skills vs live)", check_drift(args.backup)),
            ("Job specifics in skills/setup", check_job_specifics(args.backup)),
            ("Open items", open_items(args.backup)),
        ]

    failed = False
    for title, rows in sections:
        shown = [r for r in rows if not (args.quiet and r[0] == "PASS")]
        if not shown:
            continue
        print(f"\n== {title}")
        for level, text in shown:
            print(f"[{level}] {text}")
            failed = failed or level == "FAIL"
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
