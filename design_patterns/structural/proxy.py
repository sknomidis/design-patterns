"""Postpone object creation unless absolutely necessary.

It is a middleman between the user and the object, and it can be used for:
- access control
- lazy initialization
- remote proxies
"""

from __future__ import annotations

import abc
import time


class Image(abc.ABC):
    @abc.abstractmethod
    def __init__(self, path: str) -> None: ...

    @abc.abstractmethod
    def display(self) -> None: ...


class RealImage(Image):
    def __init__(self, path: str) -> None:
        self._load_image(path)

    def display(self) -> None:
        print("Here is the image: ...")

    @staticmethod
    def _load_image(path: str) -> None:
        # Some slow process
        print("Loading image from disk...")
        time.sleep(2)


class ProxyImage(Image):
    def __init__(self, path: str) -> None:
        self._path = path
        self._image: RealImage | None = None

    def display(self) -> None:
        if self._image is None:
            self._image = RealImage(self._path)
        self._image.display()


if __name__ == "__main__":
    image = ProxyImage("image.png")
    print("Initialized image")

    image.display()
