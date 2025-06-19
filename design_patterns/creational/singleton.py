"""Achieve singularity by only allowing a single instance of a class.

Monostate is a related pattern, which achieves singularity by enforcing the same
state among different instances.
"""

from __future__ import annotations

from typing import Any, Self


class Singleton:
    _instance = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    object_1 = Singleton()
    object_1.x = 42
    object_2 = Singleton()
    print(object_1.x)
    print(object_2.x)
    print(object_1 is object_2)
