# Copyright (c) 2025 Intuit Build Challenge

import assignment1


def test_assignment1_package_exposes_public_symbols():
    assert hasattr(assignment1, "BoundedBuffer")
    assert hasattr(assignment1, "ProducerConsumerSystem")
    assert hasattr(assignment1, "Producer")
    assert hasattr(assignment1, "Consumer")
