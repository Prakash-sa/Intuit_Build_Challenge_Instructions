# Copyright (c) 2025 Intuit Build Challenge

"""Backward-compatible API exposing the sales analysis components."""

from __future__ import annotations

from pathlib import Path

from assignment2.analyzer import SalesAnalyzer
from assignment2.data_loader import CSVSalesLoader
from assignment2.reporting import SalesReport, run_report

__all__ = ["SalesAnalyzer", "CSVSalesLoader", "SalesReport", "run_report"]


def main(data_path: Path) -> str:
    """Utility retained for compatibility with older imports."""
    loader = CSVSalesLoader(data_path)
    analyzer = SalesAnalyzer(loader.load())
    report = SalesReport(analyzer)
    return report.build()
