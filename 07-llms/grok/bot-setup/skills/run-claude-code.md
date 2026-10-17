# Run Claude Code

Claude Code (`~/.local/bin/claude`) is already signed in on the box. Never sign in or out, and never touch `~/.claude/.credentials.json`.

1. Run `bash /workspace/setup/bootstrap.sh` first. It pulls the vault and checks the claude CLI and the `~/.claude` skill links.
2. `mkdir -p /workspace/scratch/<task>`, where `<task>` is a short slug.
3. From /workspace/vault, run:
   ```
   timeout 900 ~/.local/bin/claude -p "<task prompt>" \
     --permission-mode acceptEdits \
     --allowedTools "Read" "Write" "Edit" "Glob" "Grep" "Skill" "Bash(/workspace/.venv/bin/python:*)" "Bash(mkdir:*)" "Bash(ls:*)" "Bash(soffice:*)" \
     --add-dir /workspace/scratch/<task> --add-dir /home/box/.claude/skills \
     --output-format json > /workspace/scratch/<task>/run.json
   ```
   Tell it in the prompt to save outputs under /workspace/scratch/<task>/. Never use `--dangerously-skip-permissions`. If a run is denied a tool, add only that one tool and rerun once.
4. Read run.json for the result, `duration_ms`, `total_cost_usd` and any `permission_denials`.
5. Deliver finished files the same day, as a chat attachment to Jesse or to OneDrive. Finals also go to the Drive folder Grok Bot (see the Drive finals skill). Pass Claude Code's result back as it is; don't rewrite it. Report the run time, the cost and anything it said it couldn't do.
6. Nothing goes to a customer or anyone else without Jesse's approval.
