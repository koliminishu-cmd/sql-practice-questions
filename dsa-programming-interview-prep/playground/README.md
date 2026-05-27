# DSA and Programming Playground

Solve coding interview problems locally and validate your Python solution.

No external packages are required.

## Quick Start

List problems:

```bash
python3 dsa-programming-interview-prep/playground/validate_solution.py --list
```

Validate the example solution:

```bash
python3 dsa-programming-interview-prep/playground/validate_solution.py --problem p001 --file dsa-programming-interview-prep/playground/solutions/p001_example.py
```

Create your own solution:

```bash
cp dsa-programming-interview-prep/playground/solutions/p001_template.py dsa-programming-interview-prep/playground/solutions/p001.py
```

Then edit `p001.py` and run:

```bash
python3 dsa-programming-interview-prep/playground/validate_solution.py --problem p001 --file dsa-programming-interview-prep/playground/solutions/p001.py
```

## Rules

- Use Python.
- Do not read from stdin.
- Do not print from your solution.
- Implement the function name shown in the problem.
- Return the answer instead of printing it.

