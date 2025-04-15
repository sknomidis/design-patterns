"""Global variable in an object-oriented way.

Scenario: An information cache shared by multiple objects.
"""

from __future__ import annotations

from typing import Any


class Borg:
    """A Python-specific design pattern."""

    _shared_data = {}

    def __init__(self) -> None:
        # Attribute dictionary, shared by all instances.
        self.__dict__ = self._shared_data


class Singleton(Borg):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__()
        self._shared_data.update(kwargs)

    def __str__(self) -> str:
        return str(self._shared_data)


if __name__ == "__main__":
    x = Singleton(HTTP="Hyper Text Transfer Protocol")
    print(x)
    y = Singleton(SNMP="Simple Network Management Protocol")
    print(y)
