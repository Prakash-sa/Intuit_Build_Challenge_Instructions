# Copyright (c) 2025 Intuit Build Challenge

"""Reporting helpers for rendering analyzer output."""

from __future__ import annotations

from pathlib import Path

from assignment2.analyzer import SalesAnalyzer
from assignment2.data_loader import CSVSalesLoader


class SalesReport:
    """Generates a textual report for all analysis metrics."""

    def __init__(self, analyzer: SalesAnalyzer) -> None:
        self._analyzer = analyzer

    def build(self) -> str:
        lines = []

        lines.append("Total revenue by region:")
        for region, revenue in sorted(self._analyzer.total_revenue_by_region().items()):
            lines.append(f"  {region}: ${revenue:,.2f}")

        lines.append("\nAverage discount by category:")
        for category, discount in sorted(self._analyzer.average_discount_by_category().items()):
            lines.append(f"  {category}: {discount:.2%}")

        lines.append("\nTop products by revenue:")
        for product, revenue in self._analyzer.top_products_by_revenue():
            lines.append(f"  {product}: ${revenue:,.2f}")

        lines.append("\nMonthly sales summary:")
        for month, stats in sorted(self._analyzer.monthly_sales_summary().items()):
            lines.append(
                f"  {month}: orders={stats['orders']}, units={stats['units']}, revenue=${stats['revenue']:,.2f}"
            )

        lines.append("\nBest salesperson by region:")
        for region, (salesperson, revenue) in sorted(
            self._analyzer.best_salesperson_by_region().items()
        ):
            lines.append(f"  {region}: {salesperson} (${revenue:,.2f})")

        return "\n".join(lines)


def run_report(data_path: Path) -> str:
    loader = CSVSalesLoader(data_path)
    analyzer = SalesAnalyzer(loader.load())
    report = SalesReport(analyzer)
    return report.build()
