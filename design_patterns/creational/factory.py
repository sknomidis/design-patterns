"""Responsible for creating an object without knowing its class until runtime.

Problem:
- Uncertainties in object types.
- Class type decided at runtime.
"""

from __future__ import annotations

import abc
from typing import Literal


class Pet(abc.ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    @abc.abstractmethod
    def speak(self) -> str: ...


class Dog(Pet):
    def speak(self) -> str:
        return "Woof!"


class Cat(Pet):
    def speak(self) -> str:
        return "Meow!"


def get_pet(pet: Literal["dog", "cat"]) -> Pet:
    """Factory method."""
    pets = {
        "dog": Dog("Hope"),
        "cat": Cat("Peace"),
    }
    return pets[pet]


if __name__ == "__main__":
    print(get_pet("dog").speak())
    print(get_pet("cat").speak())
