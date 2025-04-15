"""Turn a request into a standalone object.

This decouples the sender from the receiver.
"""

from __future__ import annotations

import abc


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self) -> None: ...


class Copy(Command):
    def execute(self) -> None:
        print("Copying...")


class Paste(Command):
    def execute(self) -> None:
        print("Pasting...")


class Save(Command):
    def execute(self) -> None:
        print("Saving...")


class Macro:
    """This class does not care about the details of the commands."""

    def __init__(self) -> None:
        self._commands: list[Command] = []

    def add(self, command: Command) -> None:
        self._commands.append(command)

    def run(self) -> None:
        for command in self._commands:
            command.execute()


if __name__ == "__main__":
    macro = Macro()
    macro.add(Copy())
    macro.add(Paste())
    macro.add(Save())
    macro.run()
