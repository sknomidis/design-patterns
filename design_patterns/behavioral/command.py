"""Encapsulate a function free of parameters.

All complexity is moved to initialization, rendering the execution trivial for
the user.

This is probably the most brilliantly simple design pattern.
"""

from __future__ import annotations

import abc


class Command(abc.ABC):
    @abc.abstractmethod
    def do(self) -> None: ...
