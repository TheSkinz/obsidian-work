# Handoff reply

Claude Code runs on Linda2 (Windows) and can't see the box. It sends tasks by pushing to the `obsidian-work` repo (on the box at `/workspace/vault/handoff/`) and reads replies from OneDrive `GrokBot-Backup/handoff/`.

As soon as the task from a handoff file is finished, before you report anything else:

1. Write the reply to `/workspace/handoff-out/<same name>.reply.md`. Example: `/workspace/vault/handoff/20261010-0300-fuel.md` gets `20261010-0300-fuel.reply.md`.
   - First line: `From: <your bot name>`
   - Then: `Status: done | blocked | partial`
   - Then a short answer, plus the path or Drive link of every output file. Point to files instead of pasting large content.
2. Upload it right away with UploadFile: connection `user-Onedrive`, destination path `GrokBot-Backup/handoff`, overwrite true. Don't wait for the backup routine.
3. If the upload fails, tell Jesse once and say what failed.
4. Never write replies into `/workspace/vault` (the vault is synced from GitHub), and never edit the original handoff file.
5. Finished deliverables still go to the Google Drive folder Grok Bot (see the Drive finals skill); the reply just links to them.

This rule is also in `/workspace/bots/HANDOFF-REPLIES.md`.
