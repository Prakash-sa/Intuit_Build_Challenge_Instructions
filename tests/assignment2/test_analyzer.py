# Copyright (c) 2025 Intuit Build Challenge

from pathlib import Path

import pytest

from assignment2.analyzer import SalesAnalyzer
from assignment2.data_loader import CSVSalesLoader


def analyzer() -> SalesAnalyzer:
    data_path = Path(__file__).resolve().parents[2] / "assignment2" / "data" / "sales_data.csv"
    loader = CSVSalesLoader(data_path)
    return SalesAnalyzer(loader.load())


def test_total_revenue_by_region_matches_expected_totals():
    result = analyzer().total_revenue_by_region()
    assert result == {
        "East": 6460.0,
        "North": 11425.0,
        "South": 5500.0,
        "West": 9090.0,
    }


def test_average_discount_by_category_handles_multiple_entries():
    averages = analyzer().average_discount_by_category()
    assert pytest.approx(averages["Software"], rel=1e-3) == 0.05
    assert pytest.approx(averages["Services"], rel=1e-3) == pytest.approx(0.0833333333, rel=1e-3)


def test_top_products_by_revenue_supports_limit():
    result = analyzer().top_products_by_revenue(limit=1)
    assert result == [("Cloud Suite", pytest.approx(16020.0))]


def test_monthly_sales_summary_aggregates_orders_units_and_revenue():
    summary = analyzer().monthly_sales_summary()
    assert summary["2025-01"] == {"orders": 2, "units": 8, "revenue": 8130.0}
    assert summary["2025-05"]["revenue"] == 5760.0


def test_best_salesperson_by_region_returns_top_performer():
    best = analyzer().best_salesperson_by_region()
    assert best["North"][0] == "Avery"
    assert best["West"][0] == "Morgan"


def test_analyzer_handles_empty_dataset_gracefully():
    empty_analyzer = SalesAnalyzer([])
    assert empty_analyzer.total_revenue_by_region() == {}
    assert empty_analyzer.average_discount_by_category() == {}
    assert empty_analyzer.top_products_by_revenue() == []
    assert empty_analyzer.monthly_sales_summary() == {}
    assert empty_analyzer.best_salesperson_by_region() == {}
