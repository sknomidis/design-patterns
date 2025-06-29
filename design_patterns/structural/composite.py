"""Achieve a one-to-many behavior without implementing one-to-many relationship.

Since one-to-one relationships are much easier to understand, this tends to
simplify usage logic.
"""

from __future__ import annotations

import abc


class FileSystemItem(abc.ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    @abc.abstractmethod
    def display(self, *, indent: int = 0) -> None: ...


class File(FileSystemItem):
    def display(self, *, indent: int = 0) -> None:
        print(" " * indent + f"- File: {self._name}")


class Folder(FileSystemItem):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children: list[File] = []

    def display(self, *, indent: int = 0) -> None:
        print(" " * indent + f"- Folder: {self._name}")
        for child in self._children:
            child.display(indent=indent + 1)

    def add(self, file: File) -> None:
        self._children.append(file)


if __name__ == "__main__":
    root = Folder("root")

    docs = Folder("Documents")
    docs.add(File("resume.pdf"))
    docs.add(File("cover_letter.docx"))

    pics = Folder("Pictures")
    pics.add(File("vacation.jpg"))

    root.add(docs)
    root.add(pics)
    root.display()
