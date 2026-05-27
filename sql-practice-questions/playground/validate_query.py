#!/usr/bin/env python3
import argparse
import json
import sqlite3
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SCHEMA_PATH = BASE_DIR / "schema.sql"
SEED_PATH = BASE_DIR / "seed.sql"
QUESTIONS_PATH = BASE_DIR / "questions.json"

BLOCKED_KEYWORDS = {
    "insert",
    "update",
    "delete",
    "drop",
    "create",
    "alter",
    "replace",
    "attach",
    "detach",
    "pragma",
    "vacuum",
}


def load_questions():
    return json.loads(QUESTIONS_PATH.read_text())


def get_question(question_id):
    for question in load_questions():
        if question["id"] == question_id:
            return question
    raise SystemExit(f"Question not found: {question_id}")


def build_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA_PATH.read_text())
    conn.executescript(SEED_PATH.read_text())
    return conn


def normalize_sql(sql):
    stripped = sql.strip().rstrip(";").strip()
    lowered = stripped.lower()
    if not (lowered.startswith("select") or lowered.startswith("with")):
      raise ValueError("Only SELECT queries and CTEs starting with WITH are allowed.")
    for keyword in BLOCKED_KEYWORDS:
        if keyword in lowered.replace("\n", " ").split():
            raise ValueError(f"Blocked keyword found: {keyword}")
    return stripped


def run_query(conn, sql):
    safe_sql = normalize_sql(sql)
    cursor = conn.execute(safe_sql)
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description or []]
    return columns, [tuple(row) for row in rows]


def normalize_value(value):
    if isinstance(value, float):
        return round(value, 6)
    return value


def normalize_rows(rows):
    return [tuple(normalize_value(value) for value in row) for row in rows]


def print_table(columns, rows):
    if not columns:
        print("(no columns)")
        return
    print(" | ".join(columns))
    print("-" * max(10, len(" | ".join(columns))))
    for row in rows:
        print(" | ".join("" if value is None else str(value) for value in row))


def validate(question, answer_sql, show=False):
    conn = build_db()
    expected_columns, expected_rows = run_query(conn, question["expected_sql"])
    actual_columns, actual_rows = run_query(conn, answer_sql)

    expected_rows = normalize_rows(expected_rows)
    actual_rows = normalize_rows(actual_rows)

    if show:
        print("Your query output:")
        print_table(actual_columns, actual_rows)
        print()

    columns_match = actual_columns == expected_columns
    if question.get("order_matters", True):
        rows_match = actual_rows == expected_rows
    else:
        rows_match = sorted(actual_rows) == sorted(expected_rows)

    if columns_match and rows_match:
        print(f"PASS: {question['id']} - {question['title']}")
        return 0

    print(f"FAIL: {question['id']} - {question['title']}")
    if not columns_match:
        print("\nExpected columns:")
        print(expected_columns)
        print("Actual columns:")
        print(actual_columns)
    if not rows_match:
        print("\nExpected rows:")
        print_table(expected_columns, expected_rows)
        print("\nActual rows:")
        print_table(actual_columns, actual_rows)
    return 1


def list_questions():
    for question in load_questions():
        print(
            f"{question['id']} | {question['difficulty']} | "
            f"{question['topic']} | {question['title']}"
        )


def main():
    parser = argparse.ArgumentParser(description="Validate SQL practice answers.")
    parser.add_argument("--list", action="store_true", help="List available questions.")
    parser.add_argument("--question", help="Question id, for example q001.")
    parser.add_argument("--file", help="Path to your SQL answer file.")
    parser.add_argument("--show", action="store_true", help="Print your query output.")
    args = parser.parse_args()

    if args.list:
        list_questions()
        return 0

    if not args.question or not args.file:
        parser.error("--question and --file are required unless using --list")

    question = get_question(args.question)
    answer_path = Path(args.file)
    if not answer_path.exists():
        raise SystemExit(f"Answer file not found: {answer_path}")

    try:
        return validate(question, answer_path.read_text(), show=args.show)
    except sqlite3.Error as exc:
        print(f"SQL error: {exc}")
        return 2
    except ValueError as exc:
        print(f"Validation error: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())

