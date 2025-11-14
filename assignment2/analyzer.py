# Copyright (c) 2025 Intuit Build Challenge

"""Sales data analyzer implemented with an OO approach."""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Sequence, Tuple

from assignment2.models import SaleRecord


class SalesAnalyzer:
    """Performs aggregate computations using a functional style."""

    def __init__(self, records: Sequence[SaleRecord]) -> None:
        self._records = list(records)

    def total_revenue_by_region(self) -> Dict[str, float]:
        totals: Dict[str, float] = defaultdict(float)
        for record in self._records:
            totals[record.region] += record.revenue
        return dict(totals)

    def average_discount_by_category(self) -> Dict[str, float]:
        accumulators: Dict[str, Tuple[float, int]] = defaultdict(lambda: (0.0, 0))
        for record in self._records:
            total_discount, count = accumulators[record.category]
            accumulators[record.category] = (total_discount + record.discount, count + 1)
        return {
            category: total_discount / count
            for category, (total_discount, count) in accumulators.items()
            if count
        }

    def top_products_by_revenue(self, limit: int = 3) -> List[Tuple[str, float]]:
        revenue_map: Dict[str, float] = defaultdict(float)
        for record in self._records:
            revenue_map[record.product] += record.revenue
        return sorted(
            revenue_map.items(), key=lambda item: item[1], reverse=True
        )[:limit]

    def monthly_sales_summary(self) -> Dict[str, Dict[str, float]]:
        summary: Dict[str, Dict[str, float]] = defaultdict(
            lambda: {"orders": 0, "units": 0, "revenue": 0.0}
        )
        for record in self._records:
            key = record.date.strftime("%Y-%m")
            summary[key]["orders"] += 1
            summary[key]["units"] += record.quantity
            summary[key]["revenue"] += record.revenue
        return dict(summary)

    def best_salesperson_by_region(self) -> Dict[str, Tuple[str, float]]:
        region_sales: Dict[str, Dict[str, float]] = defaultdict(lambda: defaultdict(float))
        for record in self._records:
            region_sales[record.region][record.salesperson] += record.revenue

        best: Dict[str, Tuple[str, float]] = {}
        for region, sales in region_sales.items():
            best_salesperson = max(sales.items(), key=lambda item: item[1])
            best[region] = best_salesperson
        return best
