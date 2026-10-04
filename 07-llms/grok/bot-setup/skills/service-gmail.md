# Service: Gmail

Read this before using Gmail on the shared computer. This is not Linda2.

## Account
- Website Gmail: `jskinz2083@gmail.com` (Jesse Utsey).
- This is not the Grok account. Grok is `jwutsey@outlook.com`.
- A signed-in website session on this Chrome is visible to every Bot.
- Credentials go through the secure form. Never put the password in chat or a file. Do not screenshot a password field.

## What worked (2026-10-04)
- Opening `https://mail.google.com/mail/u/0/#inbox` loaded the inbox for `jskinz2083@gmail.com`.
- A website session is enough to read Gmail in the browser. It does not require Chrome itself to be signed in.

## What failed
- The Google password does not stick as a Chrome sign-in. Jesse reported that on 2026-10-04.
- The verified block the same day: Chrome browser sign-in is locked off. `/etc/opt/chrome/policies/managed/sand.json` sets `BrowserSignin` to 0. Settings shows **Allow Chrome sign-in** disabled, with “This setting is managed by your administrator.”
- Because of that lock, the profile stays **Person 1** (also seen labeled **You**). Bookmarks and settings do not sync. Do not edit that policy file unless Jesse explicitly asks.

## Chrome sync
- Sync will not work on this computer. Website Gmail can still be signed in while the browser profile is not.
- He was right that the top of Chrome did not show `jskinz2083@gmail.com`. The site session and the browser profile are different.

## Gotchas
- Do not treat a loaded inbox as proof that Chrome is signed in.
- Do not search local files for a saved Google password. There is not one you should read.
- Prefer the Gmail connector (`user-Gmail`) when the job is reading mail. Use this browser session only when the connector cannot do it.
- Linda2 is his own computer. A login here does not sign in Chrome on Linda2.
