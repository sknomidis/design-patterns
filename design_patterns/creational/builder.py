"""Addresses the problem of using an excessive number of constructors

It partitions the process of building an object into 4 roles:
1. Director
2. Abstract builder
3. Concrete builder
4. Product
"""

from __future__ import annotations


class Director:
    """High-level orchestrator."""

    def __init__(self, builder: ConcreteBuilder) -> None:
        self._builder = builder

    def construct_car(self) -> None:
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self) -> Car:
        return self._builder.car


class AbstractBuilder:
    """Create empty object."""

    def __init__(self) -> None:
        self.car: Car | None = None

    def create_new_car(self) -> None:
        self.car = Car()


class ConcreteBuilder(AbstractBuilder):
    """Build object in parts."""

    def add_model(self) -> None:
        self.car.model = "Skylark"

    def add_tires(self) -> None:
        self.car.tires = "Regular tires"

    def add_engine(self) -> None:
        self.car.engine = "Turbo engine"


class Car:
    """Product that is being built."""

    def __init__(self) -> None:
        self.model: str | None = None
        self.tires: str | None = None
        self.engine: str | None = None

    def __str__(self) -> str:
        return f"{self.model} | {self.tires} | {self.engine}"


if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)
    director.construct_car()
    car = director.get_car()
    print(car)
