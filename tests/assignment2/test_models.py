# Copyright (c) 2025 Intuit Build Challenge

from datetime import datetime

from assignment2.models import SaleRecord


def test_sale_record_revenue_accounts_for_discount():
    record = SaleRecord(
        order_id="X",
        date=datetime(2025, 1, 1),
        region="Test",
        salesperson="Jordan",
        product="Widget",
        category="Software",
        quantity=4,
        unit_price=50.0,
        discount=0.25,
    )

    assert record.revenue == 150.0
