# Service: Outlook

## Accounts
- Personal mailbox on the Outlook connector: `jwutsey@outlook.com` (Jesse Utsey). This is Outlook.com, not Gmail and not the company mailbox.
- Company account seen on the shared-browser picker: `jutsey@usadebusk.com`. After password and Authenticator, company sign-in stopped on “Set up your device to get access” (`login.microsoftonline.com` SAS/ProcessAuth). Jesse said stop. Do not click Continue. Do not enroll the shared computer.
- A signed-in shared browser session is visible to every Bot.

## Read mail (connector, this worked)
Namespace `user-Outlook`. Confirm the mailbox with `get_me` before acting.
- Folders: `list_mail_folders`. Junk is the Junk Email folder.
- Messages: `list_mail_messages` on that folder, newest first. Page with `get_next_page`.
- Open `get_mail_message` only when the preview is not enough. Previews almost never include URLs.
- Do not download attachment bytes unless asked.
- On 2026-10-03: Junk had 222 messages (220 unread). A 30-day read covered 185 messages, 2026-09-03 06:08 CT through 2026-10-03 14:01 CT. 37 older messages were not opened.
- On 2026-10-06: Junk had 236 (+14). Fifteen messages after 2026-10-03 14:01 CT; blocked five domains had 0 of those new arrivals.
- One `get_me` call failed with an OAuth refresh race. The retry worked. Do not switch to the browser for a read the connector can do.

## Junk pattern (Jesse's correction)
Malicious mail is bots. Display names and subjects change every message. Do not group by From address.
The main cluster (117 of 185) used 7 addresses on 5 domains, with 115 display names and 117 subjects. Stable envelope domains: thingsgate.com, mastersineducationprograms.org, shopversekitchen.com, grade.thesolutioniseasy.com, startoffcleardebt.com. About 50 fake “Re:” subjects. Sampled link hosts did not match the From domain.
Cluster by subject, phrasing, and link host. Flag possible real mail separately. None of the 185 was USADebusk, bid, or customer mail.

## Block senders (browser, connector cannot)
The connector has no block, junk-rule, or report tool. Do not delete or move existing Junk unless asked.
Worked path, personal account only, after `jwutsey@outlook.com` was signed in on the shared browser:
1. Open `https://outlook.live.com/mail/0/options/mail/junkEmail`.
2. Section label: **Blocked senders and domains**.
3. Add the domain, Save, reload, and read the list back. All five domains above were absent, then present after save and reload.

What failed: that same URL with no Outlook.com session redirected to the Microsoft marketing page “Sign in to Outlook” (`microsoft.com`, deeplink to junkEmail). `outlook.office.com` is the company host, not this personal mailbox.

## Safe / trusted senders (browser, connector cannot)
Same junkEmail settings URL. Path: **Junk email → Senders → tab “Safe senders and domains”**. Helper text: “Don't move email from these senders to my Junk Email folder.”
Add the address, OK, Save (Save disables when done), reload, and read the list back.
Jesse confirmed these as trusted (2026-10-06): `donotreply@rxtx.walgreens.com`, `spectrumadmin@cincsystems.net`, `inspection@bees360.com`, `contactusemails@shellfcu.org`. Only add addresses he names or confirms.

## Sign-in that worked (personal)
Secure form, one visible field per step. Typed values go into the page and are never returned. Do not screenshot a secret field.
1. Account picker showed only `jutsey@usadebusk.com`. Click **Use another account**. Do not click the company account.
2. Email field label: “Enter your email, phone, or Skype.” Fill via the secure form, then click **Next**.
3. Next gate was login.live.com **Get a sign-in request** for `jwutsey@outlook.com`, with **Send request** and **Other ways to sign in**. Click Send request. A number is shown for the phone (98 on this run). Wait for approval.
4. After approval, **We're updating our terms** with **Next** may appear (`account.live.com/tou/accrue`). That is not device enrollment.
5. Then the junkEmail settings URL loads for `jwutsey@outlook.com`.

Password step, if it appears instead: field “Enter the password for [account]”, button **Sign in**. Still one secure-form field, then click Sign in yourself.
