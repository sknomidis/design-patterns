"""Allow an object to change its behavior based on its internal state."""

from __future__ import annotations

import abc


# Context
class VendingMachine:
    def __init__(self) -> None:
        self._state: State | None = None

    def set_state(self, state: State) -> None:
        self._state = state

    def insert_coin(self) -> None:
        self._state.insert_coin()

    def dispense(self) -> None:
        self._state.dispense()


# States can manipulate the context and create/set other states.
class State(abc.ABC):
    def __init__(self, machine: VendingMachine) -> None:
        self._machine = machine

    @abc.abstractmethod
    def insert_coin(self) -> None: ...

    @abc.abstractmethod
    def dispense(self) -> None: ...


class WaitingForCoinState(State):
    def insert_coin(self) -> None:
        print("Coin inserted. Ready to dispense.")
        self._machine.set_state(DispensingState(self._machine))

    def dispense(self) -> None:
        print("Insert a coin first.")


class DispensingState(State):
    def insert_coin(self) -> None:
        print("Already received a coin. Dispensing...")

    def dispense(self) -> None:
        print("Dispensing item...")
        self._machine.set_state(WaitingForCoinState(self._machine))


if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.set_state(WaitingForCoinState(vending_machine))

    vending_machine.dispense()
    vending_machine.insert_coin()
    vending_machine.insert_coin()
    vending_machine.dispense()
    vending_machine.dispense()
