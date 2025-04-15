"""Establish one-to-many relationship between a subject and multiple observers."""

from __future__ import annotations

import abc


class Subject(abc.ABC):
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, modifier: Observer | None = None) -> None:
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):
    def __init__(self, name: str = "") -> None:
        super().__init__()
        self._name = name
        self._temperature = 0.0

    @property
    def name(self) -> str:
        return self._name

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: float) -> None:
        self._temperature = temperature
        self.notify()


class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, subject: Subject) -> None: ...


class TemperatureViewer(Observer):
    def update(self, subject: Core) -> None:
        print(f"Temperature viewer: {subject.name} has temperature {subject.temperature}")


if __name__ == "__main__":
    core_1 = Core("core-1")
    core_2 = Core("core-2")

    viewer_1 = TemperatureViewer()
    viewer_2 = TemperatureViewer()

    core_1.attach(viewer_1)
    core_1.attach(viewer_2)

    core_1.temperature = 80.0
    core_1.temperature = 90.0
