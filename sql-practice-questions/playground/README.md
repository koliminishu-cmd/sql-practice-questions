# SQL Playground

Practice SQL questions locally and validate your answers using SQLite.

No external packages are required. The validator uses Python's built-in `sqlite3` module.

## Quick Start

From the repository root:

```bash
python3 sql-practice-questions/playground/validate_query.py --list
```

Pick a question and create an answer file:

```bash
cp sql-practice-questions/playground/answers/q001.example.sql sql-practice-questions/playground/answers/q001.sql
```

Run validation:

```bash
python3 sql-practice-questions/playground/validate_query.py --question q001 --file sql-practice-questions/playground/answers/q001.sql
```

Run your query and print the output without validation:

```bash
python3 sql-practice-questions/playground/validate_query.py --question q001 --file sql-practice-questions/playground/answers/q001.sql --show
```

## Folder Structure

| File | Purpose |
| --- | --- |
| `schema.sql` | SQLite table definitions |
| `seed.sql` | Sample interview-style data |
| `questions.json` | Practice questions and expected SQL |
| `validate_query.py` | Runs and validates your SQL |
| `answers/` | Your SQL answer files |

## Answer Rules

- Write one `SELECT` query per answer file.
- CTEs are allowed.
- Do not use `INSERT`, `UPDATE`, `DELETE`, `DROP`, `CREATE`, or `ALTER`.
- Match the requested output columns.
- If a question says the result should be ordered, include `ORDER BY`.

## Add More Questions

To add a new validated question:

1. Add sample data to `seed.sql` if needed.
2. Add the question and expected query to `questions.json`.
3. Create your answer in `answers/qXXX.sql`.
4. Run the validator.

