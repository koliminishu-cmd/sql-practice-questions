#!/usr/bin/env python3
import argparse
import copy
import importlib.util
import json
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PROBLEMS_PATH = BASE_DIR / "problems.json"


def load_problems():
    return json.loads(PROBLEMS_PATH.read_text())


def get_problem(problem_id):
    for problem in load_problems():
        if problem["id"] == problem_id:
            return problem
    raise SystemExit(f"Problem not found: {problem_id}")


def load_solution(path):
    solution_path = Path(path).resolve()
    spec = importlib.util.spec_from_file_location("candidate_solution", solution_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def normalize_grouped(value):
    return sorted(sorted(group) for group in value)


def normalize(value, problem):
    if problem.get("unordered_groups"):
        return normalize_grouped(value)
    if problem.get("unordered"):
        return sorted(value)
    return value


def validate(problem, file_path):
    module = load_solution(file_path)
    function_name = problem["function"]
    if not hasattr(module, function_name):
        print(f"FAIL: function `{function_name}` not found in {file_path}")
        return 1

    func = getattr(module, function_name)
    failures = 0

    for index, test in enumerate(problem["tests"], start=1):
        args = copy.deepcopy(test["args"])
        expected = test["expected"]
        try:
            actual = func(*args)
        except Exception as exc:
            failures += 1
            print(f"Test {index}: ERROR {type(exc).__name__}: {exc}")
            continue

        if normalize(actual, problem) != normalize(expected, problem):
            failures += 1
            print(f"Test {index}: FAIL")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")
        else:
            print(f"Test {index}: PASS")

    if failures:
        print(f"\nFAIL: {problem['id']} - {problem['title']} ({failures} failing test(s))")
        return 1

    print(f"\nPASS: {problem['id']} - {problem['title']}")
    return 0


def list_problems():
    for problem in load_problems():
        print(f"{problem['id']} | {problem['difficulty']} | {problem['topic']} | {problem['title']} | function: {problem['function']}")


def main():
    parser = argparse.ArgumentParser(description="Validate DSA/programming solutions.")
    parser.add_argument("--list", action="store_true", help="List available problems.")
    parser.add_argument("--problem", help="Problem id, for example p001.")
    parser.add_argument("--file", help="Path to Python solution file.")
    args = parser.parse_args()

    if args.list:
        list_problems()
        return 0

    if not args.problem or not args.file:
        parser.error("--problem and --file are required unless using --list")

    problem = get_problem(args.problem)
    return validate(problem, args.file)


if __name__ == "__main__":
    sys.exit(main())

