# Copyright (c) 2025 Intuit Build Challenge

from assignment1.system import ProducerConsumerSystem
import pytest


def test_system_transfer_all_returns_payload():
    payload = [f"item-{i}" for i in range(5)]
    system = ProducerConsumerSystem(payload, queue_capacity=2)
    assert system.transfer_all() == payload


def test_system_with_empty_payload_returns_empty_list():
    system = ProducerConsumerSystem([], queue_capacity=1)
    assert system.transfer_all() == []


def test_system_raises_when_queue_capacity_invalid():
    with pytest.raises(ValueError):
        ProducerConsumerSystem([], queue_capacity=0)
