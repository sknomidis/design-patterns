"""Define an algorithm's skeleton, and let subclasses override individual steps."""

from __future__ import annotations

import abc


class CaffeinatedBeverage(abc.ABC):
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self) -> None:
        print("Boiling water")

    def pour_in_cup(self) -> None:
        print("Pouring into cup")

    @abc.abstractmethod
    def brew(self) -> None: ...

    @abc.abstractmethod
    def add_condiments(self) -> None: ...


class Tea(CaffeinatedBeverage):
    def brew(self) -> None:
        print("Steeping the tea")

    def add_condiments(self) -> None:
        print("Adding lemon")


class Coffee(CaffeinatedBeverage):
    def brew(self) -> None:
        print("Dripping coffee through filter")

    def add_condiments(self) -> None:
        print("Adding sugar and milk")


if __name__ == "__main__":
    print("Making tea...")
    tea = Tea()
    tea.prepare_recipe()

    print("\nMaking coffee...")
    coffee = Coffee()
    coffee.prepare_recipe()
