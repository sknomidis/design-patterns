"""Interpret a simple domain-specific language."""

from __future__ import annotations

import abc


class Expression(abc.ABC):
    @abc.abstractmethod
    def interpret(self) -> bool: ...


# Terminal expression (leaves in the syntax tree)
class BooleanLiteral(Expression):
    def __init__(self, value: bool) -> None:
        self._value = value

    def interpret(self) -> bool:
        return self._value


# Non-terminal expressions (nodes in the syntax tree)
class AndExpression(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self._left = left
        self._right = right

    def interpret(self) -> bool:
        return self._left.interpret() and self._right.interpret()


class OrExpression(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self._left = left
        self._right = right

    def interpret(self) -> bool:
        return self._left.interpret() or self._right.interpret()


if __name__ == "__main__":
    expression = OrExpression(
        AndExpression(
            BooleanLiteral(True),
            BooleanLiteral(False),
        ),
        BooleanLiteral(True),
    )

    print(expression.interpret())
