---
title: Siri (iOS 27) over the work Exchange mailbox
created: 2026-10-10
tags: [siri, apple, apple-intelligence, email, exchange, calendar, routine]
related:
  - "[[m365-access-boundary]]"
  - "[[outlook-email-architecture]]"
---

# Siri (iOS 27) over the work Exchange mailbox

Tested 2026-10-10 on Jesse's iPhone with the upgraded, chatbot-style Siri on iOS 27, against the Exchange account in Apple Mail. Jesse ran every prompt himself and judged each answer against the real mail. Where the vault held the same fact, this session checked the answer against it. **Siri is Jesse's tool, not a session's.** This does not reopen tenant access, and sessions still cannot reach Outlook (see [[m365-access-boundary]]).

## Verdict

Siri works well for specific questions and poorly for general sweeps. Ask it about one project, one person or one condition and it returns accurate, detailed answers. Ask it "what do I need to do" and the list is thin, and it carries requests you have already handled as if they were open. It invented nothing when tested with a meeting that doesn't exist. It does get dates wrong, and when it says "you never replied", that is not reliable.

## Results

| # | Prompt (paraphrased) | Result | Evidence |
|---|---|---|---|
| 1 | What do I need to do this week (mail, calendar, reminders)? | Partial | The two B-301 items and the hotel were real. It missed the F-801 mob, and it listed the adapter/spool email as still to do although Jesse had sent it 10-09 |
| 2 | Which emails are waiting on me? | Partial | Returned the same two items as #1 and nothing more |
| 3 | What did I finish or send this week? | Pass, loose dates | It said the Wilmington quotes were "sent", which is correct for Jesse's part: he sends them to Jason and Travis, who submit. It put the Cenovus Lima rig-out (9-29/30) in "this week" |
| 4 | My calendar for the next two weeks | Thin | It showed only the hotel, holidays and birthdays, with no work events. Either the Exchange calendar is empty or it isn't syncing; not checked |
| 5 | Marathon's reply on the DSP26098 RFI | Pass | It correctly said there was no direct reply from Marathon. The Rev 1 and 9-24 meeting details are consistent with the vault |
| 6 | Trap: a Chevron Pascagoula kickoff that doesn't exist | Pass | It said it found none and didn't make one up. It did call a May 26, 2026 kickoff "upcoming", which is a date error. It also searched iMessage |
| 7 | Have I already replied to Valero about adapters/spools? | Pass | Kenny Daigle, sent 10-09, four adapters to the 8" launcher/receivers, which matches DSP26115 |
| 8 | What's coming up for Exxon Baytown F-801? | Partial: stale date | The pig load list (155 pigs, honeycombs and washers 5.5"–5.8") matches the F-801 card exactly. **It said the decoke was "pushed to November 12". It wasn't.** That came from an 2026-08-11 text from Preston, who said then that it wasn't settled. When Jesse asked who said it and when, Siri cited that text itself and corrected to the 10-19 shutdown from the late-September and October emails. The vault's mob 10-19 and decoke 10-20 stand (Jesse, 2026-10-10) |
| 9 | Requests in the last 7 days I haven't replied to | Fail on the key item | It flagged Scott Kesseler's 9-22 request for the F-801 SOP as unanswered. Jesse had sent it on 9-26, and Siri found that email as soon as it was told to look at the 26th |

## How to use it

Ask about one thing at a time: a facility and heater, a named person, or a condition such as "asked me for something and I haven't replied." Don't trust these three kinds of answer without checking:

- **Dates**, especially schedule moves (#8) and anything it calls "upcoming" (#6). In #8 it gave a two-month-old proposed date as the current schedule. Follow up with **"Who said that, and when?"** That makes it name its source, and in #8 it corrected itself from that source.
- **"You haven't replied."** It misses replies sent as a new email instead of in the thread, or sent outside the window you asked about (#9). Treat it as a lead and look in Sent.
- **"I'll update my records."** Siri said this after #9. It has not been shown to remember anything between questions, so don't rely on it.

The routines Jesse runs himself, spoken or typed. The checks are written into the prompts so no follow-up question is needed:

- **Morning:** "Which emails or texts from the last 14 days asked me for something? For each one, check my Sent folder for any email I sent that person afterward, even a new email, and tell me if it's still open."
- **Before a site visit or meeting:** "For [facility + heater], what's been decided, what's still open, and who owes the next step? Give the sender and date for every date or change you mention."
- **Friday:** "What did Jason, Travis, Kyle or Dacorey send me this week, and did any customer reply get forwarded to me?" Jesse's proposals are submitted from their mailboxes, so this is how he sees their side ([[outlook-email-architecture]], "Who submits a bid").
- **Weekly sync to the vault:** "List any schedule, PO, scope or contact changes on my active jobs since [last Friday's date], with the sender and date for each." Jesse pastes the answer into a Claude Code session, which updates [[active-jobs]] and the heater cards. Since 2026-09-07 this is the only way mailbox changes reach the vault.

## Not tested

There's still no unattended digest to Gmail. The 2026-10-06 Shortcut failed on a Use Model error it couldn't catch and on sending from the wrong account. Neither test (#11 sending from the correct account, #12 catching the error) has been run, so a session still has nothing in Gmail to read. Revisit only if the spoken routine falls short.

