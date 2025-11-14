# Copyright (c) 2025 Intuit Build Challenge

from pathlib import Path

from assignment2 import run_report
from assignment2.sales_analysis import main as sales_analysis_main


def data_path() -> Path:
    return Path(__file__).resolve().parents[2] / "assignment2" / "data" / "sales_data.csv"


def test_sales_analysis_main_returns_full_report_string():
    report = sales_analysis_main(data_path())
    assert isinstance(report, str)
    assert "Total revenue by region" in report


def test_package_run_report_matches_sales_analysis_main():
    assert run_report(data_path()) == sales_analysis_main(data_path())
