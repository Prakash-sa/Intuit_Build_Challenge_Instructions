# Copyright (c) 2025 Intuit Build Challenge

"""Container abstractions for the producer-consumer workflow."""

from __future__ import annotations

from collections import deque
from threading import Lock
from typing import Deque, Iterable, List, Optional


class SourceContainer:
    """Thread-safe container that serves as a finite data source."""

    def __init__(self, items: Iterable[str]) -> None:
        self._items: Deque[str] = deque(items)
        self._lock = Lock()

    def read(self) -> Optional[str]:
        """Return the next item or None when depleted."""
        with self._lock:
            if self._items:
                return self._items.popleft()
            return None


class DestinationContainer:
    """Thread-safe sink that records consumed items."""

    def __init__(self) -> None:
        self._items: List[str] = []
        self._lock = Lock()

    def write(self, item: str) -> None:
        """Persist an item consumed from the queue."""
        with self._lock:
            self._items.append(item)

    def snapshot(self) -> List[str]:
        """Return a copy of all stored items."""
        with self._lock:
            return list(self._items)
