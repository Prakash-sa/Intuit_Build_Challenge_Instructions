# Copyright (c) 2025 Intuit Build Challenge

import threading
import time

import pytest

from assignment1.buffer import BoundedBuffer


def test_bounded_buffer_requires_positive_capacity():
    with pytest.raises(ValueError):
        BoundedBuffer(0)


def test_put_blocks_until_space_available():
    buffer = BoundedBuffer(1)
    buffer.put("first")

    def delayed_pop():
        time.sleep(0.2)
        buffer.get()

    worker = threading.Thread(target=delayed_pop)
    worker.start()

    start = time.time()
    buffer.put("second")
    elapsed = time.time() - start

    worker.join()
    assert elapsed >= 0.2


def test_get_blocks_until_item_available():
    buffer = BoundedBuffer(1)

    def delayed_put():
        time.sleep(0.2)
        buffer.put("available")

    worker = threading.Thread(target=delayed_put)
    worker.start()

    start = time.time()
    item = buffer.get()
    elapsed = time.time() - start

    worker.join()
    assert item == "available"
    assert elapsed >= 0.2
