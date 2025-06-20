"""Decouple layered class hierarchies having different degrees of freedom."""

from __future__ import annotations

import abc

"""Layered class hierarchy.

Notice how a new variant must be written twice (once for each interface),
while a new interface will introduce two variants.
"""

# Top layer


class Base(abc.ABC):
    @abc.abstractmethod
    def method(self) -> None: ...


# Intermediate layer (1st degree of freedom)


class Interface1(Base, abc.ABC):
    @abc.abstractmethod
    def method(self) -> None: ...


class Interface2(Base, abc.ABC):
    @abc.abstractmethod
    def method(self) -> None: ...


# Bottom layer (2nd degree of freedom)


class Interface1Variant1(Interface1):
    def method(self) -> None:
        pass


class Interface1Variant2(Interface1):
    def method(self) -> None:
        pass


class Interface2Variant1(Interface2):
    def method(self) -> None:
        pass


class Interface2Variant2(Interface2):
    def method(self) -> None:
        pass


"""Bridge pattern to the rescue!

Each variant is now injected to the interface, thus decoupling the two. The
interface is closed against a new variant, and vice versa.
"""

# 1st degree of freedom


class Base(abc.ABC):
    def __init__(self, variant: Variant) -> None:
        self._variant = variant

    @abc.abstractmethod
    def method(self) -> None: ...


class Interface1(Base, abc.ABC):
    @abc.abstractmethod
    def method(self) -> None: ...


class Interface2(Base, abc.ABC):
    @abc.abstractmethod
    def method(self) -> None: ...


# 2nd degree of freedom


class Variant(abc.ABC):
    @abc.abstractmethod
    def method(self) -> None: ...


class Variant1(Variant):
    def method(self) -> None:
        pass


class Variant2(Variant):
    def method(self) -> None:
        pass
