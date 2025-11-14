# Copyright (c) 2025 Intuit Build Challenge

"""Domain models shared across sales analysis components."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SaleRecord:
    """Immutable representation of a sales transaction."""

    order_id: str
    date: datetime
    region: str
    salesperson: str
    product: str
    category: str
    quantity: int
    unit_price: float
    discount: float

    @property
    def revenue(self) -> float:
        return self.quantity * self.unit_price * (1 - self.discount)
