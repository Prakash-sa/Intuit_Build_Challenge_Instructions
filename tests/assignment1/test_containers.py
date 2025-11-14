# Copyright (c) 2025 Intuit Build Challenge

from assignment1.containers import DestinationContainer, SourceContainer


def test_source_container_reads_in_fifo_order():
    source = SourceContainer(["a", "b", "c"])
    assert source.read() == "a"
    assert source.read() == "b"
    assert source.read() == "c"
    assert source.read() is None


def test_destination_container_snapshot_is_copy():
    destination = DestinationContainer()
    destination.write("alpha")
    snapshot = destination.snapshot()
    snapshot.append("beta")

    assert destination.snapshot() == ["alpha"]
