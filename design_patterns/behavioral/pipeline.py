"""Organize computation into a sequence of sequential stages.

The output of each stage is the input of the next one down the line.
"""

from __future__ import annotations

import queue
import threading


# Stage 1
def producer(sentence: str, out_queue: queue.Queue) -> None:
    print("Initial sentence is:", sentence)
    for word in sentence.split():
        out_queue.put(word)


# Stage 2
def uppercaser(in_queue: queue.Queue, out_queue: queue.Queue) -> None:
    while not in_queue.empty():
        word: str = in_queue.get()
        out_queue.put(word.upper())


# Stage 3
def reverser(in_queue: queue.Queue, out_queue: queue.Queue) -> None:
    while not in_queue.empty():
        word: str = in_queue.get()
        out_queue.put(word[::-1])


# Stage 4
def consumer(in_queue: queue.Queue) -> None:
    words = []
    while not in_queue.empty():
        word = in_queue.get()
        words.append(word)
    sentence = " ".join(words)
    print("Final sentence is:", sentence)


if __name__ == "__main__":
    sentence = "The sun sets behind the mountains, painting the sky in shades of orange."
    queue_1 = queue.Queue()
    queue_2 = queue.Queue()
    queue_3 = queue.Queue()

    threads = [
        threading.Thread(target=producer, args=(sentence, queue_1)),
        threading.Thread(target=uppercaser, args=(queue_1, queue_2)),
        threading.Thread(target=reverser, args=(queue_2, queue_3)),
        threading.Thread(target=consumer, args=(queue_3,)),
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
