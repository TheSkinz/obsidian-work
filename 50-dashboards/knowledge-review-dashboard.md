---
type: dashboard
status: active
created: 2026-06-26
tags: [dashboard, knowledge-system]
---

# Knowledge Review Dashboard

## Inbox

```dataview
TABLE type, status, file.mtime as "Updated"
FROM "00-inbox"
SORT file.mtime DESC
```

## Open Reviews

```dataview
TABLE review_type, status, confidence, review_after, file.mtime as "Updated"
FROM "00-inbox" OR "06-insights" OR "04-knowledge"
WHERE type = "review" AND status != "complete"
SORT file.mtime DESC
```

## Unresolved Contradictions

```dataview
TABLE status, confidence, review_after, file.mtime as "Updated"
FROM "00-inbox" OR "04-knowledge" OR "06-insights"
WHERE type = "contradiction" AND status != "resolved"
SORT file.mtime DESC
```

## Open Questions

```dataview
TABLE question_type, status, confidence, review_after, file.mtime as "Updated"
FROM "00-inbox" OR "04-knowledge" OR "06-insights"
WHERE type = "question" AND status != "complete"
SORT file.mtime DESC
```

## Stale Or Due For Review

```dataview
TABLE type, status, last_reviewed, review_after, file.mtime as "Updated"
FROM "01-context" OR "02-facilities" OR "04-knowledge" OR "06-insights"
WHERE status = "stale" OR (review_after AND review_after <= date(today))
SORT review_after ASC
```

## Blank Tags

```dataview
TABLE type, status, file.folder as "Folder", file.mtime as "Updated"
FROM "00-inbox"
WHERE tags = []
SORT file.mtime DESC
```

## Governance

- [[knowledge-system-governance]]
- [[review-note-template]]
- [[contradiction-template]]
- [[source-note-template]]
- [[question-template]]
- [[canonical-knowledge-template]]
