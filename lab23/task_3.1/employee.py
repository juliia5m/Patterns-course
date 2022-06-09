from __future__ import annotations
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass


class Staff(Employee):
    def __init__(self):
        self._employees = set()

    def add_employee(self, employee):
        self._employees.add(employee)

    def get_salary(self, summ = 0):
        for employee in self._employees:
            summ += employee.get_salary()

        return summ

    def accept(self, visitor):
        visitor.visit_staff_list(self)
        for employee in self._employees:
            employee.accept(visitor)
