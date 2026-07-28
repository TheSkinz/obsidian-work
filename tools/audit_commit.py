"""Word-level audit of a commit: find content lost/added behind reflowing.

Rewrapping prose changes every line, so a line diff cannot distinguish a pure
reflow from a reflow that also dropped a sentence. Comparing word multisets
ignores line structure entirely, so only real content changes survive.

This is the by-sha front door, for auditing history. The comparison itself lives
in vault_lint.py so the staged-diff rule (WORD-DELTA, see `vault_lint.py
--staged`) and this tool cannot drift apart in what they count.

    python tools/audit_commit.py <sha>
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vault_lint import format_delta, word_delta  # noqa: E402

VAULT = str(Path(__file__).resolve().parent.parent)


def run(args):
    return subprocess.run(args, cwd=VAULT, capture_output=True).stdout


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    sha = sys.argv[1]

    files = run(["git", "show", "--stat", "--name-only", "--format=", sha]).decode(
        "utf-8", "replace").split("\n")
    files = [f.strip() for f in files if f.strip().endswith(".md")]

    for f in files:
        before = run(["git", "show", f"{sha}~:{f}"]).decode("utf-8", "replace")
        after = run(["git", "show", f"{sha}:{f}"]).decode("utf-8", "replace")
        if not before and not after:
            continue
        lost, gained = word_delta(before, after)
        if not lost and not gained:
            print(f"  OK (pure reformat)  {f}")
            continue
        print(f"\n>>> {f}")
        if lost:
            print(f"    LOST  : {format_delta(lost)}")
        if gained:
            print(f"    GAINED: {format_delta(gained)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
