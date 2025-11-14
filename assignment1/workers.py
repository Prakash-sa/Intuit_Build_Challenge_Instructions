# Copyright (c) 2025 Intuit Build Challenge

"""Worker implementations for producer and consumer threads."""

from __future__ import annotations

from dataclasses import dataclass, field
from threading import Thread
from typing import Callable, Optional

from assignment1.buffer import BoundedBuffer
from assignment1.containers import DestinationContainer, SourceContainer

TraceSink = Callable[[str], None]


@dataclass(eq=False)
class Producer(Thread):
    """Worker that pulls from a source container and pushes into the buffer."""

    source: SourceContainer
    buffer: BoundedBuffer
    sentinel: str
    name: str = field(default="Producer")
    trace: Optional[TraceSink] = field(default=None)

    def __post_init__(self) -> None:
        super().__init__(name=self.name)

    def run(
        self,
    ) -> None:  # pragma: no cover - thread start logic covered by system tests
        while True:
            item = self.source.read()
            if item is None:
                self.buffer.put(self.sentinel)
                if self.trace:
                    self.trace(
                        f"{self.name}: sent sentinel (buffer size={self.buffer.size})"
                    )
                break
            self.buffer.put(item)
            if self.trace:
                self.trace(
                    f"{self.name}: produced {item} (buffer size={self.buffer.size})"
                )


@dataclass(eq=False)
class Consumer(Thread):
    """Worker that pulls from the buffer and writes to the destination."""

    destination: DestinationContainer
    buffer: BoundedBuffer
    sentinel: str
    name: str = field(default="Consumer")
    trace: Optional[TraceSink] = field(default=None)

    def __post_init__(self) -> None:
        super().__init__(name=self.name)

    def run(
        self,
    ) -> None:  # pragma: no cover - thread start logic covered by system tests
        while True:
            item = self.buffer.get()
            if item == self.sentinel:
                if self.trace:
                    self.trace(f"{self.name}: received sentinel, shutting down")
                break
            self.destination.write(item)
            if self.trace:
                self.trace(
                    f"{self.name}: consumed {item} (buffer size={self.buffer.size})"
                )
