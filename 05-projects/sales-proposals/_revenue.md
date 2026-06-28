# Revenue Dashboard

## By Client
```dataview
TABLE WITHOUT ID key as "Client", sum(rows.revenue) as "Revenue ($)", sum(rows.cost) as "Cost ($)", sum(rows.margin) as "Margin ($)", length(rows) as "Jobs"
FROM "03-jobs"
WHERE type = "job" AND revenue > 0
GROUP BY client
SORT sum(rows.revenue) DESC
```

## By Facility
```dataview
TABLE WITHOUT ID key as "Facility", sum(rows.revenue) as "Revenue ($)", sum(rows.margin) as "Margin ($)", length(rows) as "Jobs"
FROM "03-jobs"
WHERE type = "job" AND revenue > 0
GROUP BY facility
SORT sum(rows.revenue) DESC
```

## Recent Completed Jobs
```dataview
TABLE job-number as "Job #", client, facility, revenue as "Revenue ($)", margin as "Margin ($)", date-end as "Completed"
FROM "03-jobs"
WHERE type = "job" AND revenue > 0
SORT date-end DESC
LIMIT 20
```
