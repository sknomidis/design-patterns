"""Adapt an incompatible interface to what the client expects."""

from __future__ import annotations

import abc


class ClientInterface(abc.ABC):
    @abc.abstractmethod
    def run(self) -> None: ...


class ActualInterface(abc.ABC):
    @abc.abstractmethod
    def execute(self) -> None: ...


# The client can now use the `ActualInterface`, even though it has an
# incompatible interface.
class Adapter(ClientInterface):
    def __init__(self, actual_interface: ActualInterface) -> None:
        self._actual_interface = actual_interface

    def run(self) -> None:
        self._actual_interface.execute()
