# Copyright (c) 2025 Intuit Build Challenge

"""Utilities for loading sales data from CSV files."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from assignment2.models import SaleRecord


class CSVSalesLoader:
    """Parses CSV rows into SaleRecord instances."""

    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path

    def load(self) -> List[SaleRecord]:
        with self._file_path.open("r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return [self._parse_row(row) for row in reader]

    def _parse_row(self, row: Dict[str, str]) -> SaleRecord:
        return SaleRecord(
            order_id=row["order_id"],
            date=datetime.strptime(row["date"], self.DATE_FORMAT),
            region=row["region"],
            salesperson=row["salesperson"],
            product=row["product"],
            category=row["category"],
            quantity=int(row["quantity"]),
            unit_price=float(row["unit_price"]),
            discount=float(row["discount"]),
        )
