"""Clone object based on a prototypical instance.

Useful when creating many identical objects is expensive.
"""

from __future__ import annotations

import copy
from typing import Any, TypeVar

ObjectType = TypeVar("ObjectType")


class Prototype:
    def __init__(self) -> None:
        self._objects: dict[str, ObjectType] = {}

    def register_object(self, name: str, obj: ObjectType) -> None:
        self._objects[name] = obj

    def unregister_object(self, name: str) -> None:
        del self._objects[name]

    def clone(self, name: str, **kwargs: Any) -> ObjectType:
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(kwargs)
        return obj


class Car:
    def __init__(self) -> None:
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self) -> str:
        return f"{self.name} | {self.color} | {self.options}"


if __name__ == "__main__":
    car = Car()
    prototype = Prototype()
    prototype.register_object("skylark", car)

    car_cloned = prototype.clone("skylark", options="winter tires")
    print(car_cloned)
