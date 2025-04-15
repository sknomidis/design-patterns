"""Convert the interface of a class to what the client expects.

It acts as a translator between two incompatible interfaces.
"""

from __future__ import annotations


class USPlug:
    def get_power(self) -> str:
        return "120V power from US plug"


class EuropeanSocket:
    def provide_electricity(self) -> str:
        return "220V power from European socket"


class EuropeanToUsAdapter(USPlug):
    def __init__(self, european_socket: EuropeanSocket) -> None:
        self._european_socket = european_socket

    def get_power(self) -> str:
        power = self._european_socket.provide_electricity()
        return power


def power_service(us_plug: USPlug) -> None:
    print(us_plug.get_power())


if __name__ == "__main__":
    # Works normally
    us_plug = USPlug()
    power_service(us_plug)

    # To make EU socket work, we wrap it with an adapter
    eu_socket = EuropeanSocket()
    adapter = EuropeanToUsAdapter(eu_socket)
    power_service(adapter)
