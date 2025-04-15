"""Save and restore internal state of an object, without exposing it."""

from __future__ import annotations


# Originator
class TextEditor:
    def __init__(self) -> None:
        self._text = ""

    def write(self, new_text: str) -> None:
        self._text += new_text

    def get_text(self) -> str:
        return self._text

    def save(self) -> TextMemento:
        return TextMemento(self._text)

    def restore(self, memento: TextMemento) -> str:
        self._text = memento.get_saved_text()


# Memento
class TextMemento:
    def __init__(self, text: str) -> None:
        self._text = text

    def get_saved_text(self) -> str:
        return self._text


# Caretaker
class History:
    def __init__(self) -> None:
        self._undo_stack: list[TextMemento] = []

    def save(self, memento: TextMemento) -> None:
        self._undo_stack.append(memento)

    def undo(self) -> TextMemento:
        return self._undo_stack.pop()


if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    history.save(editor.save())
    editor.write("Hello")
    history.save(editor.save())

    editor.write(" world!")

    print("Current:", editor.get_text())
    editor.restore(history.undo())
    print("Undo 1:", editor.get_text())
    editor.restore(history.undo())
    print("Undo 2:", editor.get_text())
