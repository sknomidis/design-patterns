"""Achieve singularity by having all instances share the same state.

Singleton is a related pattern, which achieves singularity by enforcing a single
class instance.

Monostate is more flexible than Singleton, allowing for easier subclassing and
testing, but is more implicit.
"""

from __future__ import annotations


class Monostate:
    _shared_data = {}

    def __init__(self) -> None:
        # Attribute dictionary, shared by all instances.
        self.__dict__ = self._shared_data


if __name__ == "__main__":
    object_1 = Monostate()
    object_1.x = 42
    object_2 = Monostate()
    print(object_1.x)
    print(object_2.x)
    print(object_1 is object_2)
