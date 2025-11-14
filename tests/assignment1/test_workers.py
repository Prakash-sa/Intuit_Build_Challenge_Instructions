# Copyright (c) 2025 Intuit Build Challenge

from assignment1.buffer import BoundedBuffer
from assignment1.containers import DestinationContainer, SourceContainer
from assignment1.workers import Consumer, Producer


def test_producer_emits_all_items_and_sentinel():
    buffer = BoundedBuffer(5)
    source = SourceContainer(["x", "y"])
    sentinel = "__END__"
    producer = Producer(source, buffer, sentinel, name="producer-test")

    producer.start()
    received = [buffer.get(), buffer.get(), buffer.get()]
    producer.join()

    assert received.count("x") == 1
    assert received.count("y") == 1
    assert sentinel in received


def test_consumer_stops_on_sentinel_and_writes_items():
    buffer = BoundedBuffer(5)
    destination = DestinationContainer()
    sentinel = "__END__"

    for payload in ["alpha", "beta", sentinel]:
        buffer.put(payload)

    consumer = Consumer(destination, buffer, sentinel, name="consumer-test")
    consumer.start()
    consumer.join(timeout=1)

    assert destination.snapshot() == ["alpha", "beta"]


def test_producer_and_consumer_coordinate_via_sentinel():
    buffer = BoundedBuffer(2)
    destination = DestinationContainer()
    sentinel = "__END__"

    source = SourceContainer(["one", "two", "three"])
    producer = Producer(source, buffer, sentinel)
    consumer = Consumer(destination, buffer, sentinel)

    threads = [producer, consumer]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join(timeout=2)

    assert destination.snapshot() == ["one", "two", "three"]


def test_consumer_handles_sentinel_first_without_writes():
    buffer = BoundedBuffer(2)
    destination = DestinationContainer()
    sentinel = "__STOP__"
    buffer.put(sentinel)

    consumer = Consumer(destination, buffer, sentinel)
    consumer.start()
    consumer.join(timeout=1)

    assert destination.snapshot() == []


def test_trace_sink_receives_producer_and_consumer_events():
    events = []
    buffer = BoundedBuffer(2)
    source = SourceContainer(["alpha"])
    destination = DestinationContainer()
    sentinel = "__STOP__"

    producer = Producer(source, buffer, sentinel, trace=events.append)
    consumer = Consumer(destination, buffer, sentinel, trace=events.append)

    producer.start()
    consumer.start()
    producer.join(timeout=1)
    consumer.join(timeout=1)

    assert any("produced alpha" in event for event in events)
    assert any("consumed alpha" in event for event in events)
    assert any("sentinel" in event for event in events)
