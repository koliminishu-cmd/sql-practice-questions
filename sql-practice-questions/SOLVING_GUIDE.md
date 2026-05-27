# SQL Solving Guide for Data Engineering Interviews

Use this guide while solving each question. The goal is not only to get the final query, but to explain your thinking clearly.

## Problem-Solving Template

For every question, write:

```text
Question number:
Topic:
Difficulty:
Tables used:
Expected grain:
Approach:
Edge cases:
Final SQL:
Explanation:
```

## Interview-Friendly Approach

1. Identify the output grain.
   - Example: one row per customer, per month, per product, or per session.

2. Identify filters.
   - Date range
   - Status values
   - Active versus inactive records
   - Current versus historical records

3. Choose the core SQL pattern.
   - Aggregation
   - Join
   - Window function
   - CTE pipeline
   - Recursive CTE
   - Temporal join
   - Anti-join
   - Deduplication

4. Handle edge cases.
   - Duplicate rows
   - Null values
   - Tied rankings
   - Missing dates
   - Late-arriving events
   - Overlapping time ranges
   - Multiple matching dimension rows

5. Explain the query.
   - Start with the input tables.
   - Explain each CTE.
   - Explain why the final grouping or window function is correct.
   - Mention performance improvements if the table is large.

## Common SQL Patterns

### Deduplication

Use `ROW_NUMBER()` over the natural key and keep the preferred row.

```sql
ROW_NUMBER() OVER (
  PARTITION BY business_key
  ORDER BY updated_at DESC
) AS rn
```

### Latest Record Per Entity

Use a window function instead of a correlated subquery when possible.

```sql
ROW_NUMBER() OVER (
  PARTITION BY user_id
  ORDER BY event_time DESC
) AS rn
```

### Running Total

```sql
SUM(amount) OVER (
  PARTITION BY customer_id
  ORDER BY order_date
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS running_total
```

### Rolling Window

Use rolling windows for retention, active users, quality checks, and monitoring.

```sql
COUNT(*) OVER (
  PARTITION BY table_name
  ORDER BY snapshot_date
  ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
) AS rolling_7_count
```

### Temporal Join

Use effective dates for SCD and price history problems.

```sql
fact.event_time >= dim.effective_start
AND fact.event_time < COALESCE(dim.effective_end, TIMESTAMP '9999-12-31')
```

### Anti-Join

Use this for "did not happen" questions.

```sql
LEFT JOIN target t
  ON s.id = t.id
WHERE t.id IS NULL
```

## What Interviewers Look For

- Clear understanding of grain
- Correct handling of duplicates and nulls
- Good use of window functions
- Ability to break complex logic into CTEs
- Awareness of data quality issues
- Knowledge of incremental loads and late-arriving data
- Explanation of performance tradeoffs

## Self-Review Checklist

- [ ] Did I define the output grain?
- [ ] Did I avoid accidental many-to-many joins?
- [ ] Did I handle ties?
- [ ] Did I handle nulls?
- [ ] Did I check date boundaries?
- [ ] Did I consider duplicate source rows?
- [ ] Can I explain every CTE?
- [ ] Can this query run on large data?

