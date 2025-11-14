# Copyright (c) 2025 Intuit Build Challenge

"""High-level orchestration of the producer-consumer pipeline."""

from __future__ import annotations

from typing import Callable, Iterable, List, Optional

from assignment1.buffer import BoundedBuffer
from assignment1.containers import DestinationContainer, SourceContainer
from assignment1.workers import Consumer, Producer

ProducerFactory = Callable[[SourceContainer, BoundedBuffer, str], Producer]
ConsumerFactory = Callable[[DestinationContainer, BoundedBuffer, str], Consumer]


class ProducerConsumerSystem:
    """Facade that wires the producer, consumer, and shared buffer."""

    def __init__(
        self,
        payload: Iterable[str],
        queue_capacity: int = 4,
        *,
        sentinel: str = "__END__",
        source: Optional[SourceContainer] = None,
        destination: Optional[DestinationContainer] = None,
        buffer: Optional[BoundedBuffer] = None,
        producer_factory: Optional[ProducerFactory] = None,
        consumer_factory: Optional[ConsumerFactory] = None,
    ) -> None:
        self.source = source or SourceContainer(payload)
        self.destination = destination or DestinationContainer()
        self.buffer = buffer or BoundedBuffer(queue_capacity)
        self._sentinel = sentinel
        self._producer_factory = producer_factory or (lambda s, b, mark: Producer(s, b, mark))
        self._consumer_factory = consumer_factory or (lambda d, b, mark: Consumer(d, b, mark))
        self._producer = self._producer_factory(self.source, self.buffer, self._sentinel)
        self._consumer = self._consumer_factory(self.destination, self.buffer, self._sentinel)

    def transfer_all(self) -> List[str]:
        """Start the workflow and wait until the consumer drains the queue."""
        self._producer.start()
        self._consumer.start()
        self._producer.join()
        self._consumer.join()
        return self.destination.snapshot()
