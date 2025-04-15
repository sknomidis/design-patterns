"""Add new features to existing objects without modifying their structure."""

from __future__ import annotations

import functools
from typing import Any, Callable, TypeVar

_F = TypeVar("_F", bound=Callable[..., str])


def make_blink(function: _F) -> _F:
    """Decorator docstring."""

    @functools.wraps(function)
    def decorator(*args: Any, **kwargs: Any) -> str:
        """Decorator sub-docstring"""
        output = function(*args, **kwargs)
        return "<blink>" + output + "</blink>"

    return decorator


@make_blink
def hello_world() -> str:
    """Simple hello world function."""
    return "Hello, World!"


if __name__ == "__main__":
    print(hello_world())
    print(hello_world.__name__)
    print(hello_world.__doc__)
