"""Decouple the sender of a request from the receiver by introducing handlers.

Each handler can decide to either handle the request or pass it over to the next
handler in the chain.
"""

from __future__ import annotations

import abc
from typing import Sequence


class Handler(abc.ABC):
    def __init__(self, successor: "Handler" | None = None) -> None:
        self._successor = successor

    def handle(self, request: int) -> bool:
        has_been_handled = self._handle(request)
        if not has_been_handled:
            self._successor.handle(request)

    @abc.abstractmethod
    def _handle(self, request: int) -> bool: ...


class ConcreteHandler(Handler):
    def _handle(self, request: int) -> bool:
        if 0 < request <= 10:
            print(f"Request {request} has been handled by handler 1")
            return True
        return False


class DefaultHandler(Handler):
    def _handle(self, request: int) -> bool:
        print(f"End of chain, no handler for request {request}")
        return True


class Client:
    def __init__(self) -> None:
        default_handler = DefaultHandler()
        self._handler = ConcreteHandler(default_handler)

    def delegate(self, requests: Sequence[int]) -> None:
        for request in requests:
            self._handler.handle(request)


if __name__ == "__main__":
    client = Client()
    requests = [2, 5, 30]
    client.delegate(requests)
