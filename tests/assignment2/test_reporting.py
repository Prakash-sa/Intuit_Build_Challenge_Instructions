# Copyright (c) 2025 Intuit Build Challenge

from pathlib import Path

from assignment2.analyzer import SalesAnalyzer
from assignment2.data_loader import CSVSalesLoader
from assignment2.reporting import SalesReport, run_report
import pytest


def data_path() -> Path:
    return Path(__file__).resolve().parents[2] / "assignment2" / "data" / "sales_data.csv"


def test_sales_report_matches_expected_headers():
    analyzer = SalesAnalyzer(CSVSalesLoader(data_path()).load())
    report = SalesReport(analyzer).build()
    for header in [
        "Total revenue by region",
        "Average discount by category",
        "Top products by revenue",
        "Monthly sales summary",
        "Best salesperson by region",
    ]:
        assert header in report


def test_run_report_generates_same_content_as_sales_report():
    analyzer = SalesAnalyzer(CSVSalesLoader(data_path()).load())
    expected = SalesReport(analyzer).build()
    assert run_report(data_path()) == expected


def test_run_report_raises_when_file_missing(tmp_path):
    missing = tmp_path / "data.csv"
    with pytest.raises(FileNotFoundError):
        run_report(missing)
