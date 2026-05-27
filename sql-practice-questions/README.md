# SQL Practice Questions for Data Engineering Interviews

This repository is a SQL practice pack for data engineering interviews. It includes medium, hard, extremely hard, and company-style questions with a simple workflow for solving, tracking, and reviewing.

## Start Here

| File | Use it for |
| --- | --- |
| `SOLVING_GUIDE.md` | How to approach each SQL problem in an interview-friendly way |
| `progress-tracker.md` | Track solved, revised, and weak questions |
| `sql-practice-questions.md` | 150 medium and hard SQL questions |
| `extremely-hard-sql-questions.md` | 100 senior-level data engineering SQL challenges |
| `company-wise-sql-interview-questions.md` | Company-style SQL questions inspired by common interview patterns |
| `playground/` | Local SQLite playground to run and validate SQL answers |
| `GITHUB_UPLOAD_STEPS.md` | Notes for pushing this folder to GitHub |

## SQL Playground

Run validated practice questions locally:

```bash
python3 sql-practice-questions/playground/validate_query.py --list
python3 sql-practice-questions/playground/validate_query.py --question q001 --file sql-practice-questions/playground/answers/q001.example.sql --show
```

## Practice Paths

### 30-Day Interview Prep

1. Days 1-10: Solve medium questions from `sql-practice-questions.md`.
2. Days 11-20: Solve hard questions from `sql-practice-questions.md`.
3. Days 21-25: Solve company-style questions.
4. Days 26-30: Solve extremely hard questions and revise weak areas.

### Topic Order

1. Aggregations and joins
2. Window functions
3. CTEs and subqueries
4. Deduplication and data quality
5. Sessionization and funnels
6. Cohort and retention analysis
7. SCD Type 2 and temporal joins
8. Recursive SQL and lineage
9. Pipeline monitoring and warehouse observability

## Suggested Practice Method

1. Pick 5-10 questions per day.
2. Write the query before looking up patterns.
3. Test edge cases such as nulls, duplicates, late-arriving data, and tied ranks.
4. Rewrite the same answer using CTEs, window functions, and subqueries where possible.
5. Explain the query as if you were speaking in an interview.

## How to Mark Progress

Use this status style in `progress-tracker.md`:

- `Not Started`
- `Attempted`
- `Solved`
- `Needs Revision`
- `Mastered`
