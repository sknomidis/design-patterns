"""Separate a generic algorithm from its context.

It is very similar to the Template pattern, but uses delegation instead of
inheritance. This, in turn, gives more flexibility at the cost of more code.
"""

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
    def __init__(self, formatter: TextFormatter) -> None:
        self._formatter = formatter

    def publish(self, text: str) -> str:
        return self._formatter.format(text)

    def set_formatter(self, formatter: TextFormatter) -> None:
        self._formatter = formatter


if __name__ == "__main__":
    editor = TextEditor(PlainFormatter())
    print(editor.publish("hello world"))

    editor.set_formatter(UpperCaseFormatter())
    print(editor.publish("hello world"))

    editor.set_formatter(ReverseFormatter())
    print(editor.publish("hello world"))
