"""Establish one-to-many relationship between a subject and multiple observers.

This pattern comes in two versions:
1. Pull Model: The entire subject is passed upon notification. This is more
   suitable for simple enough problems, when it is trivial what has been
   modified.
2. Push Model: Only what has been updated is passed upon notification. This is
   more suitable for complex problems, when only a small part of the subject
   might have changed.
"""

from __future__ import annotations

import abc
from typing import Generic, TypeVar


class Observer(abc.ABC):
    pass


class ObserverPull(Observer, abc.ABC):
    @abc.abstractmethod
    def update(self, value: SubjectPull) -> None: ...


class ObserverPush(Observer, abc.ABC):
    @abc.abstractmethod
    def update(self, value: Hint) -> None: ...


ObserverType = TypeVar("ObserverType", bound=Observer)


class Subject(Generic[ObserverType], abc.ABC):
    def __init__(self) -> None:
        self._observers: list[ObserverType] = []

    def register(self, observer: ObserverType) -> None:
        self._observers.append(observer)

    @abc.abstractmethod
    def notify(self) -> None: ...


class SubjectPull(Subject[ObserverPull], abc.ABC):
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


class SubjectPush(Subject[ObserverPush], abc.ABC):
    def __init__(self) -> None:
        self._hint = Hint()

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._hint)


class Hint:
    """This can be any kind of Subject information."""
