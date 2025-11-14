# Copyright (c) 2025 Intuit Build Challenge

"""Command-line entry point for Assignment 2."""

from pathlib import Path

from assignment2.reporting import run_report


def main() -> None:
    data_path = Path(__file__).resolve().parent / "data" / "sales_data.csv"
    print(run_report(data_path))


if __name__ == "__main__":
    main()
