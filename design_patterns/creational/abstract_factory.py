"""Produces groups of related items, and builds upon the factory pattern.

Problem:
- User expects to receive a family of related objects.
- They do not know the family type until runtime.
"""

from __future__ import annotations

import abc


# Abstract classes
class PetFactory(abc.ABC):
    """Abstract factory pattern.

    It is responsible for creating both a pet and its suitable food.
    """

    @abc.abstractmethod
    def get_pet(self) -> Pet: ...

    @abc.abstractmethod
    def get_food(self) -> PetFood: ...


class Pet(abc.ABC):
    @abc.abstractmethod
    def speak(self) -> str: ...

    @classmethod
    def __str__(cls) -> str:
        return cls.__name__


class PetFood(abc.ABC):
    @classmethod
    def __str__(cls) -> str:
        return cls.__name__


# Dog related stuff
class DogFactory(PetFactory):
    def get_pet(self) -> Dog:
        return Dog()

    def get_food(self) -> DogFood:
        return DogFood()


class Dog(Pet):
    def speak(self) -> str:
        return "Woof!"


class DogFood(PetFood):
    pass


class PetStore:
    def __init__(self, pet_factory: PetFactory) -> None:
        self._pet_factory = pet_factory

    def show_pet(self) -> None:
        pet = self._pet_factory.get_pet()
        food = self._pet_factory.get_food()
        print(f'Our pet is "{pet}"')
        print(f'Our pet says hello by "{pet.speak()}"')
        print(f'Its food is "{food}"')


if __name__ == "__main__":
    factory = DogFactory()
    store = PetStore(factory)
    store.show_pet()
