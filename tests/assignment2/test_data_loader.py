# Copyright (c) 2025 Intuit Build Challenge

from pathlib import Path

from assignment2.data_loader import CSVSalesLoader
import pytest


def test_csv_loader_reads_all_rows_and_parses_types():
    data_path = Path(__file__).resolve().parents[2] / "assignment2" / "data" / "sales_data.csv"
    loader = CSVSalesLoader(data_path)
    records = loader.load()

    assert len(records) == 10
    first = records[0]
    assert first.order_id == "1001"
    assert first.quantity == 5
    assert first.unit_price == 1200.0


def test_csv_loader_raises_for_missing_file(tmp_path):
    missing_file = tmp_path / "missing.csv"
    loader = CSVSalesLoader(missing_file)
    with pytest.raises(FileNotFoundError):
        loader.load()
