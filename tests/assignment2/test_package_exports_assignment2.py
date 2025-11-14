# Copyright (c) 2025 Intuit Build Challenge

import assignment2


def test_assignment2_package_public_api():
    assert hasattr(assignment2, "SalesAnalyzer")
    assert hasattr(assignment2, "CSVSalesLoader")
    assert hasattr(assignment2, "run_report")
