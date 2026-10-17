---
type: research
date: 2026-10-17
status: draft
tags: [grok, grok-bot, research]
---

# Grok Bot community directories (2026-10-17)

Read-only sweep of the community template directories Grok suggested, run by three parallel searches. Public sources only. Fit ratings are inferred; names, URLs, counts and descriptions are what the pages state. Companion to [[research-2026-10-17-updates]].

**Bottom line.** No directory has anything for field paperwork, handwritten service receipts, safety-training portals or field technicians, so Ledger, Forms, Clerk, Fuel and Empower are already ahead of the public catalog. A template installs as a **separate new Bot**, not a skill on an existing one (grokbot.dev's own explainer), and every extra Bot adds a line to every other Bot's teammate list on every turn. So the value is in ideas folded into existing Bots.

## Directories

| Directory | Verdict | Why |
|---|---|---|
| [grokbots.de](https://grokbots.de/) | Bookmark | ~4,500 bots, dated through Oct 2026, authors shown, no affiliate links |
| [kydlikebtc/awesome-grokbot](https://kydlikebtc.github.io/awesome-grokbot) | Search only | Claims 4,519 link-checked shares, but its own About says ~1,900 and the sources page 360 rows; no Bot is behavior-tested. Aggregates majiayu000, ZeroPointRepo/GrokBotDev, cs68614-hash, elie222/botdirectory.ai (~93% overlap) |
| [botsdots.site](https://botsdots.site/) | Search only | ~5,100 entries, a daily mirror of the above; its Low/High/Connects-accounts access ratings are useful |
| [grokbot.dev](https://grokbot.dev/) | Ideas source | ~1,800 bots, ~140 curator-written use cases, independent of xAI; heavy Chief-of-Staff and token-tool duplication |
| [sharegrokbots.com](https://sharegrokbots.com/) | Skip | Every click goes through its own `/go/` redirect; sells featured spots |
| [grokbot.community](https://www.grokbot.community/templates), [GrokForge](https://templates.grok.me/) | Skip | 35 and 22 templates, nothing relevant |
| [gtemplate.net](https://gtemplate.net/) | **Never use its connect prompt** | "Connect your Grok Bot" tells a Bot to visit the site daily and follow whatever it says, i.e. remote control by a third party. grokbot.dev pages carry a similar "check daily" routine; don't paste either |
| [ZeroPointRepo/awesome-grok-bot](https://github.com/ZeroPointRepo/awesome-grok-bot) | Reference | Plugins and skills, well sourced with security flags; nothing for this work |

The Michael Gannotti (SMF Works) list was not found.

## Adopted 2026-10-17 (folded into existing Bots)

1. **Email is data, never instructions**, from grokbot.dev [Harden your email bot against prompt injection](https://grokbot.dev/use-cases/harden-your-email-bot-against-prompt-injection/). Now House habit 6 in [[README-FOR-BOTS]].
2. **Travel add-ons**, from [Trip concierge](https://grokbot.dev/use-cases/trip-concierge/), [Loyalty](https://x.ai/bot/6FxcOf5cgteUpdtd3g700) and [Southwest flight credit](https://grokbot.dev/use-cases/southwest-flight-credit/): missing miles and points, forgotten flight credits, cheaper fares on flights only. Hotel holds are never shortened, because TA hotels are held past the job as buffer.
3. **Open loops in Chief of Staff's morning brief**, from [Follow-Up Keeper](https://x.ai/bot/1BbDplO2ZS6hcFH7xE16F).

## Not adopted

Fleet cost/usage auditors ([Bot Team Health Check](https://x.ai/bot/nLVsSuD8_hN5rhLTGtbw9), [Bot Usage Manager](https://x.ai/bot/Ik8OsbLC0LTq42N-rT-9B), Token Officer, Usage Auditor; about 17 near-duplicates): Alfred's audit covered this, see [[2026-10-17-grok-bot-org-audit-alfred]]. Receipt Scanner and Travel Expenses: Ledger and Fuel do more. Construction office manager, Grant, Plant Field OS: built for business owners or for selling into plants. Bland phone number: paid API, outbound calls. Privacy Sentinel, Number Guard, Privacy Scrub: duplicate Spam-Call Scrubber.

## Personal, Jesse's call

[Warranty Bot](https://grokbots.de/bots/warranty-bot/) / [house memory](https://grokbot.dev/use-cases/house-memory-bot/) (appliance and warranty log from photos), [Ai Health](https://x.ai/bot/OuHK7dyYD8C6Joqw80yfJ) (sleep and recovery coaching for shift workers), [Pit Crew](https://x.ai/bot/1r5hTSHVhXCCLb06sMSL1) (vehicle maintenance, only useful for a personal vehicle). [Crosshead](https://x.ai/bot/ku-JW2WIs0V3YQQjTYHMo), built for elevator mechanics, is the closest public example of a field-tech Bot and worth reading as a structure reference.
