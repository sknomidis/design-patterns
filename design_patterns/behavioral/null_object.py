"""Avoid returning `None` when something failed or was not found.

Instead, return a no-op object that implements the same methods as its normal
counterparts, but without any functionality.
"""

from __future__ import annotations

import abc


class Database:
    def get_employee(self, employee_id: int) -> Employee:
        if employee_id == 42:
            return FullTimeEmployee()
        else:
            return NullEmployee()


class Employee(abc.ABC):
    @abc.abstractmethod
    def pay_salary(self) -> None: ...


class FullTimeEmployee(Employee):
    def pay_salary(self) -> None:
        print("Deposited salary to employee's account.")


class NullEmployee(Employee):
    def pay_salary(self) -> None:
        print("Employ was not found, so no salary is deposited.")


if __name__ == "__main__":
    database = Database()
    employee_1 = database.get_employee(42)
    employee_1.pay_salary()
    employee_2 = database.get_employee(404)
    employee_2.pay_salary()
