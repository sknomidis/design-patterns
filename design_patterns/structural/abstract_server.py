"""Provide generic interface for server applications.

It is a simple way to satisfy the dependency inversion principle (DIP).
"""

from __future__ import annotations

import abc


class Switch:
    def __init__(self, switchable: Switchable) -> None:
        # Instead of making it specific to the light switch, we made it
        # easily generalizable to any sort of switchable object.
        self._switchable = switchable

    def turn_on(self) -> None:
        self._switchable.turn_on()

    def turn_off(self) -> None:
        self._switchable.turn_off()


class Switchable(abc.ABC):
    @abc.abstractmethod
    def turn_on(self) -> None: ...

    @abc.abstractmethod
    def turn_off(self) -> None: ...


class Light(Switchable):
    def turn_on(self) -> None:
        print("Light has been turned on.")

    def turn_off(self) -> None:
        print("Light has been turned off.")


if __name__ == "__main__":
    light = Light()
    switch = Switch(light)

    switch.turn_on()
    switch.turn_off()
