"""Mimic multithreading non-blocking behavior on the same run-time stack."""

from __future__ import annotations

import time

from design_patterns.behavioral import command as command_


class ActiveObject:
    def __init__(self) -> None:
        self._commands: list[command_.Command] = []

    def add_command(self, command: command_.Command) -> None:
        self._commands.append(command)

    def run(self) -> None:
        while self._commands:
            command = self._commands.pop(0)
            command.do()


class SleepCommand(command_.Command):
    def __init__(self, sleep_time_in_ms: float, active_object: ActiveObject, wakeup_command: command_.Command) -> None:
        assert sleep_time_in_ms >= 0.0
        self._sleep_time_in_ms = sleep_time_in_ms
        self._active_object = active_object
        self._wakeup_command = wakeup_command
        self._start_time: float | None = None

    def do(self) -> None:
        current_time = time.time()
        if self._is_first_call():
            self._start_time = current_time
            self._active_object.add_command(self)
        elif self._should_keep_sleeping(current_time):
            self._active_object.add_command(self)
        else:
            self._active_object.add_command(self._wakeup_command)

    def _is_first_call(self):
        return self._start_time is None

    def _should_keep_sleeping(self, current_time: float) -> bool:
        return (current_time - self._start_time) < self._sleep_time_in_ms


class PrintCommand(command_.Command):
    _creation_order = 0

    def __init__(self) -> None:
        self._order = self.__class__._creation_order
        self.__class__._creation_order += 1

    def do(self) -> None:
        print(f"[{self._order + 1}/{self.__class__._creation_order}] Some very important text.")


if __name__ == "__main__":
    active_object = ActiveObject()

    active_object.add_command(PrintCommand())
    sleep_command = SleepCommand(0.5, active_object, PrintCommand())
    active_object.add_command(sleep_command)
    active_object.add_command(PrintCommand())

    active_object.run()
