"""Parallelize a problem in a divide-and-conquer manner.

Consists of the following steps, often applied recursively:
1. Fork task into smaller ones.
2. Solve them in parallel.
3. Join the results.
"""

from __future__ import annotations

import threading
from typing import Sequence, TypeVar

ValueType = TypeVar("ValueType")


def merge_sort(array: Sequence[ValueType]) -> list[ValueType]:
    array = list(array)
    target = array.copy()
    _merge_sort(array, target, index_left=0, index_right=len(target))
    return target


def _merge_sort(source: list[ValueType], target: list[ValueType], index_left: int, index_right: int) -> None:
    if index_right - index_left <= 1:
        return

    # Fork (sort left and right sub-arrays).
    index_middle = (index_left + index_right) // 2
    thread_left = threading.Thread(target=_merge_sort, args=(target, source, index_left, index_middle))
    thread_right = threading.Thread(target=_merge_sort, args=(target, source, index_middle, index_right))
    thread_left.start()
    thread_right.start()

    # Join (merge sub-arrays).
    thread_left.join()
    thread_right.join()
    _sort_and_merge(source, target, index_left, index_middle, index_right)


def _sort_and_merge(
    source: list[ValueType], target: list[ValueType], index_left: int, index_middle: int, index_right: int
) -> None:
    # The details of how merge sort works are out of scope.
    index_sub_left = index_left
    index_sub_right = index_middle
    for index_target in range(index_left, index_right):
        is_left_empty = index_sub_left == index_middle
        is_right_empty = index_sub_right == index_right
        should_merge_from_left = is_right_empty or (
            not is_left_empty and source[index_sub_left] <= source[index_sub_right]
        )

        if should_merge_from_left:
            target[index_target] = source[index_sub_left]
            index_sub_left += 1
        else:
            target[index_target] = source[index_sub_right]
            index_sub_right += 1


if __name__ == "__main__":
    array = [42, 87, 13, 76, 5, 59, 93, 34, 28, 67, 19, 22, 80, 49, 71, 7, 64, 90, 55, 38]
    array_sorted = merge_sort(array)
    assert array_sorted == sorted(array)
    print(array_sorted)
