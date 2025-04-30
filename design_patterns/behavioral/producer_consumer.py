"""Coordinate work between producer and consumer threads.

The former produce data which the latter consume.
"""

from __future__ import annotations

import queue
import random
import sys
import threading
import time

# A queue data structure with built-in blocking and waiting mechanism.
buffer = queue.Queue(maxsize=5)


# Generate random integers.
def producer() -> None:
    while True:
        item = random.randint(1, 100)
        # Will block if queue is full, and wait until space is available.
        buffer.put(item)
        print(f"Producer produced {item}")
        time.sleep(random.uniform(0.5, 1.5))


# Consume random integers.
def consumer() -> None:
    while True:
        # Will block if queue is empty, and wait some data become available.
        item = buffer.get()
        print(f"Consumer consumed {item}")
        time.sleep(random.uniform(0.5, 2.0))


if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer, daemon=True)
    consumer_thread = threading.Thread(target=consumer, daemon=True)

    producer_thread.start()
    consumer_thread.start()

    try:
        time.sleep(10)
    except KeyboardInterrupt:
        print("Shutting down...")
        sys.exit(0)
