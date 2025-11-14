# Copyright (c) 2025 Intuit Build Challenge

from pathlib import Path

from assignment2 import run_report
from assignment2.sales_analysis import main as legacy_main


def fixture_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "sales_data.csv"


def test_legacy_main_returns_report_string():
    result = legacy_main(fixture_path())
    assert isinstance(result, str)
    assert "Total revenue by region" in result


def test_run_report_matches_legacy_main_output():
    assert run_report(fixture_path()) == legacy_main(fixture_path())
