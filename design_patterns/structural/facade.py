"""Provide a simplified interface to a large, complex system."""

from __future__ import annotations


class DVDPlayer:
    def on(self) -> None:
        print("DVD Player: ON")

    def play(self, movie: str) -> None:
        print(f"DVD Player: Playing '{movie}'")

    def off(self) -> None:
        print("DVD Player: OFF")


class Projector:
    def on(self) -> None:
        print("Projector: ON")

    def set_input(self, source: str) -> None:
        print(f"Projector: Input set to '{source}'")

    def off(self) -> None:
        print("Projector: OFF")


class Lights:
    def dim(self) -> None:
        print("Lights: Dimming...")

    def on(self) -> None:
        print("Lights: ON")


class HomeTheaterFacade:
    def __init__(self) -> None:
        self._dvd_player = DVDPlayer()
        self._projector = Projector()
        self._lights = Lights()

    def watch_movie(self, movie: str) -> None:
        print("Get ready to watch a movie...")
        self._lights.dim()
        self._projector.on()
        self._projector.set_input("DVD")
        self._dvd_player.on()
        self._dvd_player.play(movie)

    def end_movie(self) -> None:
        print("Shutting movie theater down...")
        self._dvd_player.off()
        self._projector.off()
        self._lights.on()


if __name__ == "__main__":
    home_theater = HomeTheaterFacade()
    home_theater.watch_movie("Black Mirror")
    home_theater.end_movie()
