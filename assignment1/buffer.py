# Copyright (c) 2025 Intuit Build Challenge

"""Bounded buffer implementation shared by producer and consumer workers."""

from __future__ import annotations

from collections import deque
from threading import Condition
from typing import Deque


class BoundedBuffer:
    """Blocking queue implementation backed by a deque and Condition."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._capacity = capacity
        self._buffer: Deque[str] = deque()
        self._condition = Condition()

    def put(self, item: str) -> None:
        """Insert an item, blocking while the buffer is full."""
        with self._condition:
            while len(self._buffer) >= self._capacity:
                self._condition.wait()
            self._buffer.append(item)
            self._condition.notify_all()

    def get(self) -> str:
        """Remove and return an item, blocking while the buffer is empty."""
        with self._condition:
            while not self._buffer:
                self._condition.wait()
            item = self._buffer.popleft()
            self._condition.notify_all()
            return item

    @property
    def size(self) -> int:
        """Current number of items in the buffer."""
        with self._condition:
            return len(self._buffer)

    @property
    def capacity(self) -> int:
        return self._capacity
