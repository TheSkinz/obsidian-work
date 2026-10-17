---
type: research
date: 2026-10-17
status: draft
tags: [grok, grok-bot, research]
---

# Grok Bot updates, use cases and Spam-Call Scrubber (2026-10-17)

Read-only web research, public sources only. `x.ai/changelog/bot` returned HTTP 403 to the fetcher, so the version lines below come from search-result summaries of it, not the page itself. Companion to [[research-2026-10-power-user]].

## Updates since the power-user research

| Date | Change | Source |
|---|---|---|
| 2026-10-07 | v0.68.1: Secure Forms fill into the page the Bot has open; reconnect prompt when X or Vercel sign-in expires | changelog summary |
| 2026-10-09 | Each Bot can claim its own `@mail.grokbot.com` inbox; on team plans an admin must enable it | [9to5Mac](https://9to5mac.com/2026/10/09/grok-bot-just-got-its-own-email-address-heres-how-to-claim-yours/) |
| 2026-10-11 | v0.70.2: Bot email addresses, X search, in-chat apps; voice calls use the correct local date | changelog summary |
| ~2026-10-14 | Plus aliases: send and receive on a tagged alias, and routines that fire only for mail to that alias | [TeslaNorth](https://teslanorth.com/2026/10/14/grok-bot-plus-aliases-email/) |
| 2026-10-17 | X Chat connector; Robinhood, Coinbase, Trello, PostHog, beehiiv, eToro connectors coming; better cross-conversation memory; notifications only to the active device; faster voice calls; card UI refresh | [iPhone in Canada](https://www.iphoneincanada.ca/2026/10/17/grok-bot-major-update/) |

A Basenor blog post claims Grok 4.7 has shipped ([Basenor](https://www.basenor.com/blogs/news/grok-4-7-is-here-what-changed-and-what-to-know)). Not verified against xAI. It matters because the Bot's model auto-switches with no announcement and nothing is pinned.

## Use cases that fit

Ranked for Jesse's setup, all inferred from the features above, none tested yet.

1. **Plus-alias routines.** A `receipts+` alias he emails field receipt photos to from the parking lot, triggering the receipt-extraction skill; a `travel+` alias for hotel and rental confirmations that lands in job state. The strongest new fit, because it makes the Bot reachable from the phone's mail app with no chat open. The `mail.grokbot.com` sender must never reach a customer.
2. **Secure Forms** for ISNetworld and other portal sign-ins, consistent with the 2026-10-04 rule that sign-ins go through the secure forms only.
3. **Personal inbox cleanup** on personal Gmail, the most-cited community use (one reported run sorted about 90,000 emails across two accounts; [cellcog](https://cellcog.ai/blog/grok-bot-email/)).
4. **House-memory Bot** that holds appliance stickers, filter sizes, breaker panel and warranties from one round of photos ([grokbot.dev](https://grokbot.dev/use-cases/give-your-grok-bot-a-phone-number/) index).

Not worth it: the Bland phone-number / "dial bot" pattern (voice cloning, outbound calls under his name; at most hotel-hold calls), X Chat, the finance connectors. A community index of 313 use cases exists at [botusecases](https://botusecases.netlify.app/) and is mostly operations, coding and email.

## Spam-Call Scrubber

**What it is.** A free community skill by @MinimalDuck (Arash), not an official xAI skill, promoted by Elon Musk around 2026-10-15 ([skill page](https://x.ai/bot/fUj6TYhiW_cjtzWvbsFgz), [Arash on X](https://x.com/MinimalDuck/status/2110712459405464057), [Teslarati](https://www.teslarati.com/grok-bot-spam-call-text-scrubber-elon-musk/)). It finds the phone number on people-search sites and data brokers, files the opt-outs, completes the confirmation emails, and rechecks on a schedule the user picks. The page names no sites and says only that it asks for "the minimum details it needs."

**Assessment.** Worth running, but it is data-broker opt-out, the service DeleteMe sells, not call blocking. It reduces calls driven by the number being listed or sold; it does nothing about random-dial robocallers, and Teslarati notes listings reappear, which is why the recheck matters. Grok's own account says carrier-level blocking is outside bot scope for now. [inferred] Broker opt-out forms usually want full name, city and state, sometimes age and an email, so point confirmations at the Bot's own inbox rather than personal Gmail. Pair it with iPhone Silence Unknown Callers / call screening and the carrier's free spam filter, which cover what it cannot.
