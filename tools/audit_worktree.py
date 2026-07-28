"""Word-multiset audit of the working tree against HEAD (same method as tools/audit_commit.py)."""
import collections
import re
import subprocess
import sys

REPO = sys.argv[1]
WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9._#/'-]*")


def run(a):
    return subprocess.run(a, cwd=REPO, capture_output=True).stdout


files = [f for f in run(["git", "diff", "--name-only"]).decode(
    "utf-8", "replace").split("\n") if f.strip().endswith(".md")]

tot_lost = collections.Counter()
tot_gain = collections.Counter()
clean = 0
for f in files:
    before = run(["git", "show", "HEAD:" + f]).decode("utf-8", "replace")
    after = open(REPO + "/" + f, encoding="utf-8", errors="replace").read()
    b = collections.Counter(WORD.findall(before))
    a = collections.Counter(WORD.findall(after))
    lost, gain = b - a, a - b
    if not lost and not gain:
        clean += 1
        continue
    tot_lost.update(lost)
    tot_gain.update(gain)
    print("  %-58s lost=%-3d gained=%d" % (f[-58:], sum(lost.values()), sum(gain.values())))

print("\n%d files, %d word-identical" % (len(files), clean))
print("\nAGGREGATE LOST  : %s" % (dict(tot_lost) or "(nothing)"))
print("AGGREGATE GAINED: %s" % (dict(tot_gain) or "(nothing)"))
