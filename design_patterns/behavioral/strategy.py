"""Change the behavior of an object dynamically."""

from __future__ import annotations

import abc


# Strategy
class TextFormatter(abc.ABC):
    @abc.abstractmethod
    def format(self, text: str) -> str: ...


class PlainFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text


class UpperCaseFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.upper()


class ReverseFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text[::-1]


class TextEditor:
    def __init__(self, formatter: TextFormatter | None = None) -> None:
        self._formatter = formatter or PlainFormatter()

    def publish(self, text: str) -> str:
        return self._formatter.format(text)

    def set_formatter(self, formatter: TextFormatter) -> None:
        self._formatter = formatter


if __name__ == "__main__":
    editor = TextEditor()
    print(editor.publish("hello world"))

    editor.set_formatter(UpperCaseFormatter())
    print(editor.publish("hello world"))

    editor.set_formatter(ReverseFormatter())
    print(editor.publish("hello world"))
