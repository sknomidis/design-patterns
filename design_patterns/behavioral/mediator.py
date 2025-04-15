"""Centralize communication between components, to reduce coupling."""

from __future__ import annotations

import abc


class Mediator(abc.ABC):
    @abc.abstractmethod
    def register(self, user: User) -> None: ...

    @abc.abstractmethod
    def send_message(self, message: str, user: User) -> None: ...


class ChatRoom(Mediator):
    def __init__(self):
        self._users: list[User] = []

    def register(self, user: User) -> None:
        self._users.append(user)

    def send_message(self, message: str, receiver: User) -> None:
        for user in self._users:
            if user != receiver:
                user.receive(message, receiver)


class User:
    def __init__(self, name: str, mediator: Mediator) -> None:
        self._name = name
        self._mediator = mediator
        self._mediator.register(self)

    def __str__(self) -> str:
        return self._name

    def __eq__(self, other: User) -> bool:
        return str(self) == str(other)

    def send(self, message: str) -> None:
        self._mediator.send_message(message, self)

    def receive(self, message: str, sender: User) -> None:
        print(f"{self} receives from {sender}: {message}")


if __name__ == "__main__":
    chatroom = ChatRoom()

    user_1 = User("user-1", chatroom)
    user_2 = User("user-2", chatroom)
    user_3 = User("user-3", chatroom)

    user_1.send("Hello everyone!")
