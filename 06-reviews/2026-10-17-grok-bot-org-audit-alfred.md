---
type: review
status: resolved
review_type: audit
source_authority: stated
confidence: medium
created: 2026-10-17
related:
  - "[[SETUP]]"
  - "[[research-2026-10-17-updates]]"
---

<!-- Alfred (marketplace Bot) read-only audit of the Grok Bot org, run 2026-10-17 at Jesse's request. Saved verbatim from OneDrive GrokBot-Backup/handoff/alfred-audit-2026-10-17.reply.md. Claude spot-checked the vault-side claims (bot-profiles line 3, SETUP Duplicate contradiction, fuel-form mirror drift, job values in skill mirrors, /workspace/out in README-FOR-BOTS) and all held. Disposition: Jesse ruled Fuel signs by default (change-log 2026-10-17) and approved the rest of the recommendations the same day; the app-only items (sidebar check, Librarian routines, Forms weekly check, removing Alfred) are his. -->

From: Alfred
Status: done (read-only audit; nothing changed)
Date: 2026-10-17, about 1:30 PM CDT

# Grok Bot organization audit, 2026-10-17

The only things written were this report (OneDrive `GrokBot-Backup/handoff/` and `/workspace/alfred-audit/`). No Bot, profile, skill, routine, connector, memory or file was edited, no Bot was messaged, and nothing was deleted.

**Tags used.** VERIFIED: I read it on the box or in OneDrive today. USER: you told me. INFERRED: my reasoning. UNKNOWN: I couldn't see it.

**What the box can and can't show.** The box keeps each Bot's profile (`/home/box/agent-data/agents/<id>/profile.json`), its settings, a local store and, for some Bots, local copies of the thread and memory. Every one of those files carries a 2026-10-16 15:50–15:51 timestamp. The backup log calls that a "likely box restore", so the local thread copies stop between early September and 2026-10-06 (VERIFIED). The live routine list is on the server. The only routine folders on the box are Librarian's. The transcript-reading tool wasn't available to me. So live routines, live thread length and per-Bot connector bindings are UNKNOWN unless a row says where else I got them.

---

## 1. Roster

**Count: 13 live Bot profiles on the box, against the 16 you expect (VERIFIED).** The 13 are the 12 teammates plus Alfred.

Traces of other Bot ids, none of which has a profile folder (VERIFIED):

- `01d2e587…` is Scribe (Project Report skill, Bid Desk group chat). Its thread is still on the box: 760 KB, last entry 09-07.
- `52a4bc44…` is Intake (RFQ Intake skill). On 2026-10-13 Architect found its folder still on the box. Today only its thread remains.
- `605d1aac…` is Estimator (Duration Model and Work-Up Billing Math skills).
- `96f287dd…` is a competitor-research Bot. It is very likely Scout, which Chief of Staff's memory says was deleted 2026-09-07 (INFERRED).
- `76858980…` appears only in `source-map.json`. Name UNKNOWN; it could be Studio (INFERRED).
- `25bb7d20…` is in `deleted-agents.json`.

**The gap of 3 (INFERRED).** If Intake, Estimator and Scribe are retired but still in your sidebar, 13 + 3 = 16. SETUP.md's "15 Bots" on 2026-10-10 also counted the four retired Bid Desk Bots. Please check the sidebar. The box doesn't record the roster.

| Bot | Lane | Routines | Connectors | Last seen |
|---|---|---|---|---|
| Chief of Staff | Front door, router | Claude inbox; Morning brief | OneDrive, bot inbox | 10-17 12:40 |
| Architect | Grok Bot platform | Workspace backup | GitHub, OneDrive | 10-17 12:05 |
| Librarian | Vault Q&A | Vault refresh; Webhook ping | — | 09-15 |
| Ledger | Receipt extraction | none seen | Drive | 09-07 |
| Forms | Blank receipt fill | Weekly numbering | Drive | 10-12 |
| Clerk | Clean receipt copy | none seen | Drive | unknown |
| Fuel | Fuel forms | none seen | Drive, inbox | ~10-15 |
| Docs | Company MS docs/mail | none seen | Outlook, OneDrive | 10-06 |
| Empower | Safety portals | Weekly training? | Drive | ~10-10 |
| Travel | Trips | none seen | — | 09-10 |
| Purse | Personal money | Monthly review? | Outlook, Gmail, Finance | 10-09 |
| Spam-Call Scrubber | Data-broker opt-outs | pending | bot inbox | 10-17 12:34 |
| Alfred | Org design/audit | 3 templates, paused | — | today |

Notes on the table:

- **Times** are CDT. A "Last seen" value is the newest dated evidence I could find, not a server timestamp. Sources:
  - Chief of Staff: its reply `20261017-1225-spam-call-scrubber.reply.md` in OneDrive (17:40Z).
  - Architect: `20261017-1202-refresh-claude-config.reply.md` (17:05Z).
  - Librarian: last Vault refresh run in `automations/vault-refresh/automation.json`. Its local thread ends 09-10.
  - Ledger: local thread end.
  - Forms: weekly-check line in `/workspace/bots/Forms/memory.md`.
  - Fuel: the Fuel Form skill cites a "2026-10-15" instruction (INFERRED activity).
  - Docs: newest memory line.
  - Empower: EHS and Plenum skills mirrored 10-10.
  - Travel: local thread and memory.
  - Purse: backup log, "only bots/Purse had newer files" on 10-09.
  - Scrubber: store `createdAt`.
- **Routines.**
  - Claude inbox (webhook): USER, and documented in vault `handoff/README.md`. It works, judging by today's replies.
  - Morning brief: approved 2026-10-11 in `/workspace/setup/routine-requests-20261011.md`. Its last logged run was 2026-10-16 07:19.
  - Workspace backup: weekdays about 18:05. Last run ok 2026-10-16 18:06 (`/workspace/setup/backup-log.md`, VERIFIED).
  - Forms weekly (Mon 8:47) and Purse monthly (first Monday) were approved 10-11. The Empower weekly was too, but no run is logged in its memory, so its status is UNKNOWN. Purse hasn't run yet (no card rules saved).
  - Librarian's two routines are on the box with `enabled: true` (VERIFIED). SETUP.md lists both as retired on 10-10.
  - Alfred's 3 templates (weekly, monthly, quarterly review) were created paused today: you or the parent told me. They aren't on the box.
- **Connectors.** These are the ones each Bot's own instructions or memory name. Account-level connectors on the box are Google Drive, Gmail, OneDrive, Outlook, X, Finance and GitHub (VERIFIED). Per-Bot bindings: UNKNOWN.

**Lane per instructions (VERIFIED from each `profile.json` description):**

- **Chief of Staff:** routes work, holds what's outstanding, runs the morning brief.
- **Architect:** studies Grok Bot itself. Its rules: "You do no domain work", tag findings TESTED/READ/INFERRED, log to `/workspace/platform-notes.md`.
- **Librarian:** answers "what does the vault say" with the path and quoted line. It reads the clone or `git pull`s it, and never writes.
- **Ledger:** turns handwritten receipts into a ticket breakdown and runs invoice readiness. It flags discrepancies and never adjusts. It hands the breakdown to Clerk for sign-off.
- **Forms:** fills a blank service receipt with a new sequential number.
- **Clerk:** whites out scribbles for an admin-readable copy and never extracts.
- **Fuel:** fills the company fuel form from a pump receipt.
- **Docs:** searches and analyzes company SharePoint, OneDrive and Outlook. Read-only by default.
- **Empower:** Empower/ISN work readiness and trainings.
- **Travel:** flights, hotels, cars, check-in and profile hygiene. Payment waits for you.
- **Purse:** personal subscriptions and money. Read-only.
- **Spam-Call Scrubber:** the generic community template text (206 characters). No house rules and no personal-only line.
- **Alfred:** org design and audit, defaults new Bots to zero.

---

## 2. Overlaps and contradictions

The deliberate splits are respected: Ledger extracts, Forms fills, Clerk copies, and writing and sign-off stay in separate Bots. Nothing below proposes a merge.

1. **Fuel signature. Contradiction, high stakes (VERIFIED).**
   - Fuel's description says the employee signature "is Jesse's, never forge it" and "Signature stays blank for Jesse".
   - The live Fuel Form skill (`workflows/fuel-form/SKILL.md` step 5) says "Sign every fuel form by default (Jesse's standing instruction, 2026-10-15)". It draws `/workspace/setup/jesse-utsey-signature.png` and uploads the final to Drive.
   - The vault mirror of the skill still says sign only when asked, and drafts only.
   - So the Bot's instructions and its skill disagree about putting your signature on a company form.
2. **Who signs off Ledger's breakdown (VERIFIED).**
   - Ledger's description and README rule 2 both say to hand the breakdown to Clerk for sign-off ("Ledger → Clerk").
   - Clerk's description defines no review step. It says "Ledger's extraction (or Jesse) still owns numbers" and gives Clerk only clean copies.
   - So the sign-off half of the split has no stated job. This is a gap in wording, not a reason to merge.
3. **Who runs bid, proposal and report work (VERIFIED + USER).**
   - You call Run Claude Code Architect's skill. Chief of Staff's roster also tells Chief of Staff to "use the Run Claude Code skill and pass the result back".
   - Architect's description says "You do no domain work. You do not touch a bid, a receipt, a proposal".
   - No Bot's instructions name one owner for running bid jobs.
4. **Personal Outlook has two Bots (VERIFIED).**
   - Docs' description limits it to the company Microsoft lane. Its memory, though, is mostly personal Outlook (`jwutsey@outlook.com`) junk rules, blocked senders and safe senders. SETUP.md also says "plus personal Outlook hygiene".
   - Purse reads the same mailbox for subscriptions.
   - Their jobs differ, but Docs' instructions don't say it owns personal mail.
5. **Chief of Staff can create Bots on its own (VERIFIED).** Its description says "If nothing fits and the work will recur, make a new Bot for it." That conflicts with README rule 3 ("Any new scheduled routine or new Bot needs Jesse's typed yes") and with Alfred's default of zero new Bots.
6. **Chief of Staff's always-loaded memory contradicts its description (VERIFIED, `agents/82fbaa6d…/memory/profile.md`, marked "Kept in mind every turn").** Three lines are stale:
   - "must never do specialist work itself". Its description now allows quick one-offs, and its own `/workspace` memory marks this line obsolete.
   - "competitor questions are routed to Scout". Scout was deleted 09-07.
   - "no SharePoint or Outlook connected because it stays credential-free". This was lifted 09-19.
7. **Vault pulls (VERIFIED).**
   - Librarian: "You are the only Bot that touches the clone."
   - SETUP.md: every Bot pulls through `bootstrap.sh`, and the Claude inbox routine "pulls the vault".
8. **Librarian writes handoffs (VERIFIED).**
   - Librarian: "hand them to Claude via a handoff file."
   - Vault `handoff/README.md`: "Bots read handoffs and do not write them; replies go to OneDrive only."
9. **The ISNetworld skill exists twice (VERIFIED).** "Service: ISNetworld" and "Safety LMS online training" (`isnetworld-online-training`) both cover finishing assigned ISNetworld courses. That's two methods for one task.
10. **Forms inputs (VERIFIED).**
    - Forms' description accepts "Jesse's dictation of fields".
    - The Receipt Typesetting skill reads "values only from the current job folder".
    - Chief of Staff describes Forms as "typesets them" (receipts).
11. **Spam-Call Scrubber's first round was done by Chief of Staff (VERIFIED, today's handoff reply).**
    - Chief of Staff filed FastPeopleSearch from the shared bot inbox `jskinz@mail.grokbot.com` before the Scrubber Bot took over. Ownership is handed over now, but both Bots use the one inbox.
    - Claude's handoff says "Do not store the number or name anywhere outside this task". A monthly recheck has to keep them somewhere. That conflict isn't settled.

---

## 3. Stale items

**Retired Bots in live instructions (VERIFIED):**

- Clerk's description says "Scribe owns customer .docx. Studio owns branded PowerPoint and non-Scribe collateral." Both were retired 2026-10-10.
- Chief of Staff's always-loaded memory mentions Scout (item 6 above).
- `bot-profiles.md` line 3 still says "Seven Bots were built; Scout was deleted… leaving six." This is the vault, so it's for Claude to fix.
- The `run-claude-code` skill mentions the retired Bid Desk only to say it replaces them. That's fine.
- Librarian's platform log (`memory/log/2026-09.md`) still describes the Bid Desk order: Intake → Estimator → Scribe. It's a log, so low risk.

**Dead or broken routines (VERIFIED from Librarian's `automations/` on the box):**

- **Vault refresh** is `enabled: true`. It listens to a webhook and to GitHub `pr-opened` on `TheSkinz/obsidian-work`. It last ran 2026-09-15, and the local run log holds 20 runs. SETUP.md says it was retired 10-10 and that "Jesse deletes Vault refresh and the test leftover Webhook ping in the app". The pre-push hook is gone, but the **PR-opened trigger is still armed**. Opening a PR on that repo would wake Librarian to run `git pull` (INFERRED from the trigger config).
- **Webhook ping** is `enabled: true`. It was a test, and it ran once (2026-09-06).
- These folders come from the restored snapshot, so whether they still exist in the app is UNKNOWN.

**Stale paths and facts in descriptions (VERIFIED):**

- `/workspace/out` doesn't exist. Forms' memory also notes "/workspace/out missing" on 10-12. These still point at it:
  - Forms' description: "Prefer deliverables under /workspace/out".
  - Forms' weekly check, which compares against `/workspace/out`.
  - Clerk's description.
  - Fuel's description, which puts the template at `/workspace/out/fuel-form/fuel-form-template.pdf`. The real template is at `/workspace/setup/fuel-form-template.pdf`, which the skill uses.
  - README-FOR-BOTS ("Nothing is done until it leaves here").
- Empower's description says to "work in the browser on https://app.joinempower.com". Empower's own memory says that URL "= Firebase Invalid Dynamic Link. Stop retrying that URL" and that Empower is phone-only.
- Architect's description has no "Bar and habits" section, unlike the 10 Bots updated on 10-11. It doesn't mention the Workspace backup routine, Run Claude Code or Refresh claude-config either.
- SETUP.md contradicts itself. Line 245 says "the app has no Duplicate option". Line 281 gives a thread-reset method that uses "right-click > Duplicate".

**Skills nothing references (VERIFIED by searching every description, memory file, the house files and the other skills).** Skills are shared, so "not named" doesn't prove "unused":

- `new-bot-starter`: no Bot names it. It's useful for Alfred, so keep it.
- `isnetworld-online-training` ("Safety LMS online training"): no references. It duplicates Service: ISNetworld (item 9 above).
- `receipt-clean-copy`: Clerk's description doesn't name it. SETUP says it's Clerk's.
- `receipt-typesetting`: Forms' description doesn't name it. SETUP says it's Forms'.
- `service-gmail`: no Bot names it.
- `refresh-claude-config`: no description names it, but Architect used it today, so it's live.

**Job values inside skills.** These cut against "skills hold method only" (VERIFIED):

- **`service-isnetworld`** has a full Cenovus Lima example: the Drive folder id `1m_QZ5py4o8scRC7bye3wyOfGk2S4xmfz`, course names, a 90% score and expirations of 2027-09-19. These are job and person values.
- **`fuel-form`** has a USA26046 example: the odometer, $4.059/gal, "Card ending 7255" and the station address. It's marked "do not reuse", but it's still job data.
- **`receipt-clean-copy`** has the USA26046 file names. Marked "do not reuse". Low risk.
- **`receipt-typesetting`** only points at `/workspace/jobs/USA26046/receipt-values.json`. That's fine.
- `drive-finals` holds the Grok Bot Drive folder id. That's account config, not a job value. Fine.

**Skill mirror drift (VERIFIED).** Vault `bot-setup/skills/` doesn't have `handoff-reply`, `run-claude-code`, `refresh-claude-config` or `new-bot-starter`. The vault has `safety-lms-training`, which is the live `isnetworld-online-training`. Its `fuel-form` is the older "sign only when asked" version.

---

## 4. Usage cost

**Descriptions aren't the problem (VERIFIED).** Size of each description, at about 4 characters per token:

| Bot | Chars | Tokens |
|---|---|---|
| Chief of Staff | 2884 | ~720 |
| Forms | 2583 | ~650 |
| Librarian | 2480 | ~620 |
| Ledger | 2346 | ~590 |
| Clerk | 2216 | ~550 |
| Architect | 2070 | ~520 |
| Empower | 2018 | ~500 |
| Fuel | 1900 | ~475 |
| Docs | 1787 | ~450 |
| Travel | 1741 | ~435 |
| Purse | 961 | ~240 |
| Alfred | 270 | ~70 |
| Scrubber | 206 | ~50 |

The always-loaded platform memory (`memory/profile.md`) is small: Travel 1710, Librarian 1151, Chief of Staff 855, Ledger 710, Architect 302 characters. The `/workspace/bots/<Bot>/memory.md` files are 80 to 3347 characters, all far under the 150-line cap.

**What actually rides on every turn:**

- **Teammate directory.** It runs about 6,000 to 7,100 characters (~1,500 to 1,800 tokens) per turn in the September prompt snapshots in each store's `promptSectionSnapshots` (VERIFIED). It lists every other Bot, so it grows with every Bot you add, and every Bot pays for it each turn (INFERRED). That's a real reason to keep new Bots at zero.
- **README-FOR-BOTS.md.** It's 10,429 characters (~2,600 tokens) (VERIFIED). Five descriptions say to read it "before anything else": Ledger, Forms, Clerk, Fuel and Librarian. The other 10-11 Bots point at its House habits. So it gets read at the start of most tasks (INFERRED).

**Long threads.** Sizes are from the local copies, which end where noted, so the live threads are at least this long. The app summarizes as threads grow, so raw size isn't the per-turn cost (vault SETUP.md, READ). SETUP.md also says "the whole transcript is resent every turn", and README says "Above 200K tokens… every call costs double".

| Bot | Local | User msgs | Ends |
|---|---|---|---|
| Architect | 3.53 MB | 9 | 10-06 |
| Librarian | 829 KB | 29 | 09-10 |
| Travel | 487 KB | 81 | 09-09 |
| Ledger | 241 KB | 8 | 09-07 |
| Chief of Staff | 98 KB | 17 | 09-08 |

- **Architect** has one shell output of **2.1 MB** (VERIFIED, the largest line in its transcript). Two more are 209 KB and 102 KB. A raw dump that size cuts against "Open files, never folders" and is the single biggest weight I found.
- **Travel** has the most turns: 77 recorded requests, 21 of them background revivals. It also has 978 conversation blobs (screenshots from browser sign-ins).
- **Ledger's** `conversation-blobs.db` is 54.9 MB of receipt images and PDFs.
- **Librarian's** store holds 68 routine-completion entries, from the Vault refresh webhooks that fired on every push.
- Docs, Forms, Clerk, Fuel, Empower and Purse have no thread on the box, so their length is UNKNOWN.

**Routine cost:**

- The **Workspace backup** re-uploaded **104 files** on 10-13, 10-15 and 10-16 because box restores reset mtimes, against 4 files on a normal day (VERIFIED, `backup-log.md`). That's churn, not data change.
- **Forms' weekly check** runs while last-issued is "unknown (never seeded)" (VERIFIED, memory, since 10-12). README says a routine shouldn't be scheduled if a run with nothing to do just spends tokens finding that out.
- **Chief of Staff's morning brief** lists the whole OneDrive handoff folder every weekday. The folder now holds 25 files, and the vault handoff README says to delete handoffs once their reply is read (VERIFIED).

---

## 5. Ranked recommendations

None of these adds a Bot. Each one waits for your yes. Several are app-only actions you'd do yourself.

1. **Decide whether Fuel signs, then make Fuel's description and the Fuel Form skill say the same thing.**
   - Saves: a company form carrying your signature when you didn't intend it, or an unsigned form bouncing back.
   - Risks: if the 10-15 "sign by default" instruction is real, rewriting the skill to "blank" undoes it. Either way the vault mirror needs a matching update from Claude.
2. **Clean Chief of Staff:** remove its 3 stale always-loaded memory lines, delete "make a new Bot for it", and add Spam-Call Scrubber (personal) and Alfred to its roster paragraph.
   - Saves: misroutes to a Bot that doesn't exist, an unapproved new Bot, and wrong refusals ("credential-free").
   - Risks: almost none. All three lines are already superseded in its own files.
3. **Pause (don't delete yet) Librarian's Vault refresh and Webhook ping. Delete them once you've confirmed in the app that they're idle.**
   - Saves: a surprise Librarian run whenever a PR opens on obsidian-work, or if the old webhook URL is hit.
   - Risks: deleting is permanent and drops the 20-run history. Pausing is reversible.
4. **Check the sidebar against this count of 13.** If Intake, Estimator or Scribe (or Scout or Studio) still show, delete them there.
   - Saves: their teammate-directory lines on every other Bot's turns, and the chance of routing to a retired Bot.
   - Risks: their threads are lost. Their profiles are already in vault git history (bot-profiles.md).
5. **Fix the stale paths and lines in one pass:**
   - `/workspace/out` in Forms, Clerk and Fuel, and in README-FOR-BOTS (Claude).
   - Fuel's template path.
   - Empower's `app.joinempower.com` line.
   - Clerk's Scribe/Studio sentence.
   - Librarian's "only Bot that touches the clone" and "handoff file to Claude".
   - Saves: wasted lookups and retries on paths that don't exist, and Bots following rules that were dropped.
   - Risks: low. These are wording edits.
6. **Give the Ledger → Clerk sign-off a stated job without merging anything.** Add one line to Clerk saying what it checks on Ledger's breakdown and how it reports, or name yourself as the sign-off.
   - Saves: a sign-off step that exists only on Ledger's side.
   - Risks: Clerk's lane grows slightly. Keep it to "check and flag, never change".
7. **Name one owner for running bid, proposal and report jobs through Run Claude Code.**
   - If it's Architect, narrow "You do no domain work" to "runs Claude Code, never edits its output".
   - If it's Chief of Staff, say so in the skill.
   - Saves: two Bots both thinking they run, or neither does.
   - Risks: Architect's no-domain rule was deliberate, so a careless rewrite weakens it.
8. **Cut thread weight:**
   - Add one line to Architect: "write large outputs to a file and read only what you need".
   - Consider a handoff-summary reset for Architect and Travel.
   - Saves: the 2.1 MB dump and the long Travel thread on later turns.
   - Risks: in-thread context outside memory files is lost on reset. Also, SETUP.md disagrees with itself about whether Duplicate exists, so test the reset method first.
9. **Seed Forms' last-issued number, or pause the weekly numbering check until you do.**
   - Saves: one run a week that can only report "unknown".
   - Risks: none while no receipts are being filled.
10. **Tidy skills.**
    - Fold `isnetworld-online-training` into Service: ISNetworld.
    - Move the Cenovus folder id, scores and the fuel card example out of the skills and into `/workspace/jobs/USA26046/`.
    - Name each skill in its owner's description: Clerk → Receipt Clean Copy, Forms → Receipt Typesetting.
    - Saves: two methods for one task, and job values leaking into the next job.
    - Risks: the worked example that made the skill clear is gone. Keep a short generic example.
11. **Give Spam-Call Scrubber the house basics:**
    - The README pointer and Bar and habits.
    - "Personal only, never USADebusk".
    - Use `jskinz@mail.grokbot.com` for confirmations.
    - Get your yes before creating its monthly recheck.
    - Settle where the phone number may be stored for rechecks.
    - Saves: drift from the rules every other Bot follows.
    - Risks: none to its lane.
12. **Settle personal Outlook.** Either add "personal Outlook hygiene" to Docs' description (matching SETUP.md and its memory) or move that work to Purse.
    - Saves: confusion over which Bot touches `jwutsey@outlook.com` rules.
    - Risks: Docs' lane widens. Keep Purse read-only either way.

**Smaller, for Claude (vault):**

- Update `bot-profiles.md` line 3.
- Fix the SETUP.md Duplicate contradiction.
- Mirror the 4 live-only skills into `bot-setup/skills/`.
- Change the backup script to compare file hashes instead of mtimes. That stops the 104-file re-uploads after each restore.

---

## Unknowns

- The live routine list for every Bot except Librarian. This includes whether Empower's weekly check and Purse's monthly review were ever created, and Alfred's 3 paused templates (stated by you or the parent, not seen on the box).
- Current thread length and last activity for Docs, Forms, Clerk, Fuel, Empower and Purse. Their threads aren't on the box, and the transcript tool wasn't available to me.
- Per-Bot connector bindings.
- Whether retired Bots still show in the sidebar, and why you count 16.
