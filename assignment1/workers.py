# Copyright (c) 2025 Intuit Build Challenge

"""Worker implementations for producer and consumer threads."""

from __future__ import annotations

from dataclasses import dataclass, field
from threading import Thread

from assignment1.buffer import BoundedBuffer
from assignment1.containers import DestinationContainer, SourceContainer


@dataclass(eq=False)
class Producer(Thread):
    """Worker that pulls from a source container and pushes into the buffer."""

    source: SourceContainer
    buffer: BoundedBuffer
    sentinel: str
    name: str = field(default="Producer")

    def __post_init__(self) -> None:
        super().__init__(name=self.name)

    def run(
        self,
    ) -> None:  # pragma: no cover - thread start logic covered by system tests
        while True:
            item = self.source.read()
            if item is None:
                # Signal completion to the consumer and exit gracefully.
                self.buffer.put(self.sentinel)
                break
            self.buffer.put(item)


@dataclass(eq=False)
class Consumer(Thread):
    """Worker that pulls from the buffer and writes to the destination."""

    destination: DestinationContainer
    buffer: BoundedBuffer
    sentinel: str
    name: str = field(default="Consumer")

    def __post_init__(self) -> None:
        super().__init__(name=self.name)

    def run(
        self,
    ) -> None:  # pragma: no cover - thread start logic covered by system tests
        while True:
            item = self.buffer.get()
            if item == self.sentinel:
                break
            self.destination.write(item)
