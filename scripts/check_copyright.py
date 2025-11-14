#!/usr/bin/env python3
# Copyright (c) 2025 Intuit Build Challenge

"""Validate that every Python file begins with the required copyright header."""

from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_HEADER = "# Copyright (c) 2025 Intuit Build Challenge"


def iter_python_files(root: Path):
    for path in root.rglob("*.py"):
        if any(part.startswith(".") for part in path.parts):
            continue
        yield path


def check_file(path: Path) -> bool:
    content = path.read_text(encoding="utf-8").splitlines()
    for idx, line in enumerate(content):
        stripped = line.strip()
        if not stripped:
            continue
        if idx == 0 and stripped.startswith("#!"):
            # allow shebang before header
            continue
        return stripped == REQUIRED_HEADER
    return False


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures = [path for path in iter_python_files(root) if not check_file(path)]
    if failures:
        print("Missing header in:")
        for path in failures:
            print(f"  - {path.relative_to(root)}")
        print(f"\nExpected header:\n{REQUIRED_HEADER}")
        return 1
    print("All Python files have the required header.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
