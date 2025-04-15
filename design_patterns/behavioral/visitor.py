"""Add new features to an existing class hierarchy without changing it.

It allows to perform many unrelated operations on objects, without cluttering
the classes themselves.
"""

from __future__ import annotations

import abc
import math


class Shape(abc.ABC):
    @abc.abstractmethod
    def accept(self, visitor: Visitor) -> None:
        """This adds new features with modifying existing classes (OCP)."""


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_rectangle(self)


class Visitor(abc.ABC):
    """All extra logic is implemented here."""

    @abc.abstractmethod
    def visit_circle(self, circle: Circle) -> None: ...

    @abc.abstractmethod
    def visit_rectangle(self, rectangle: Rectangle) -> None: ...


class AreaCalculator(Visitor):
    def visit_circle(self, circle: Circle) -> None:
        area = math.pi * circle.radius**2
        print(f"The area of the circle is: {area:.3g}")

    def visit_rectangle(self, rectangle: Rectangle) -> None:
        area = rectangle.width * rectangle.height
        print(f"The area of the rectangle is: {area}")


if __name__ == "__main__":
    circle = Circle(radius=2.0)
    circle.accept(AreaCalculator())

    rectangle = Rectangle(width=1.0, height=2.0)
    rectangle.accept(AreaCalculator())
