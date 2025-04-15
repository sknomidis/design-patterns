"""Untangle a complicated class hierarchy.

It decouples an abstraction from its implementation, so that the two can vary
independently.
"""

from __future__ import annotations

import abc


class DrawingAPI(abc.ABC):
    """Responsible for drawing the circle."""

    @abc.abstractmethod
    def draw_circle(self, x: float, y: float, radius: float) -> None: ...


class DrawingAPIOne(DrawingAPI):
    """Method 1 for drawing a circle."""

    def draw_circle(self, x: float, y: float, radius: float) -> None:
        print(f"API 1 drawing a circle with radius {radius} at ({x}, {y})!")


class DrawingAPITwo(DrawingAPI):
    """Method 2 for drawing a circle."""

    def draw_circle(self, x: float, y: float, radius: float) -> None:
        print(f"API 2 drawing a circle at ({x}, {y}) with radius {radius}!")


class Circle:
    """Responsible only for representing a circle, but not for drawing it."""

    def __init__(self, x: float, y: float, radius: float, drawing_api: DrawingAPI) -> None:
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self) -> None:
        # Implementation specific logic taken care of by another class
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent: float) -> None:
        self._radius *= percent


if __name__ == "__main__":
    circle_1 = Circle(1.0, 2.0, 3.0, DrawingAPIOne())
    circle_1.draw()

    circle_2 = Circle(2.0, 3.0, 4.0, DrawingAPITwo())
    circle_2.draw()
