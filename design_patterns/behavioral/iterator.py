"""Sequential access to elements of an object without exposing its structure."""

from __future__ import annotations

from typing import Iterator


def count_to(count: int) -> Iterator[str]:
    assert count < 6
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]
    iterator = zip(range(count), numbers_in_german)
    for _, number in iterator:
        yield number


if __name__ == "__main__":
    for number in count_to(5):
        print(number)
