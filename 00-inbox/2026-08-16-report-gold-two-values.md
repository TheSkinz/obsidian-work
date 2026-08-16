---
type: note
status: open
created: 2026-08-16
tags: [loose-end, brand, job-report, decision-needed]
related: [[USA26041-job-report]]
---

# Two golds are in circulation on shipped documents — pick one

Open decision carried out of the USA26041 close-out, 2026-08-16. Needs Jesse.

Sampled from the artifacts themselves, not from documentation:

| Source | Gold | How it got there |
|---|---|---|
| `usadebusk-core` Brand Standards | `#FCC30A` | The documented house value |
| Job-report generator (`render_job_report.py`) | `#FCC30A` | Follows the brand doc |
| **Shipped USA26038 job report (PDF)** | **`#F2A900`** | Hand-built in Word before the generator existed |
| **USA25025 job-report HTML mock** | **`#F2A900`** | Hand-authored, matches the shipped report |

So every report USADebusk has actually *sent a customer* carries `#F2A900`, and every report the
generator produces from here carries `#FCC30A`. Both are defensible in isolation; side by side in
a customer's folder they read as two different brands. The difference is visible — `#F2A900` is a
deeper amber, `#FCC30A` a brighter yellow-gold.

**The call:** either the brand doc is right and the older documents were off-spec (change nothing,
accept that pre-2026-08 reports differ), or the shipped documents are the de facto standard and
`GOLD` in the generator plus the brand doc should both move to `#F2A900`. Changing `GOLD` restyles
every rule, section header, KPI band and callout in every future report, so this is not a cleanup
to make in passing.

Recorded on the generator's `scripts/README.md` so nobody "fixes" it silently in either direction.
