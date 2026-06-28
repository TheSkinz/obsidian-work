# Sales Pipeline

## Open Quotes
```dataview
TABLE quote-number as "DSP #", client, facility, value as "Value ($)", date-submitted as "Submitted", date-execution as "Execution"
FROM "05-projects/sales-proposals"
WHERE type = "quote" AND status = "pending"
SORT date-submitted ASC
```

## Recently Awarded
```dataview
TABLE quote-number as "DSP #", client, facility, value as "Value ($)", awarded-as as "Job #", date-decided as "Awarded", date-execution as "Execution"
FROM "05-projects/sales-proposals"
WHERE type = "quote" AND status = "awarded"
SORT date-decided DESC
LIMIT 10
```

## Lost Quotes
```dataview
TABLE quote-number as "DSP #", client, facility, value as "Value ($)", lost-reason as "Reason", date-decided as "Date"
FROM "05-projects/sales-proposals"
WHERE type = "quote" AND status = "lost"
SORT date-decided DESC
```
