# Copyright (c) 2025 Intuit Build Challenge

"""Backward-compatible entry point for the producer-consumer package."""

from __future__ import annotations

from assignment1.buffer import BoundedBuffer
from assignment1.system import ProducerConsumerSystem

__all__ = ["BoundedBuffer", "ProducerConsumerSystem", "demo_run"]


def demo_run() -> None:
    """Execute a sample transfer to showcase thread coordination."""
    payload = [f"event-{idx}" for idx in range(1, 11)]
    system = ProducerConsumerSystem(payload, queue_capacity=3)
    results = system.transfer_all()
    print("Producer/Consumer transfer complete:")
    for item in results:
        print(f"  -> {item}")


if __name__ == "__main__":
    demo_run()
