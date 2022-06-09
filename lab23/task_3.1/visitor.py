from __future__ import annotations
from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_manager(self, manager):
        pass

    @abstractmethod
    def visit_sales_man(self, sales_person):
        pass

    @abstractmethod
    def visit_it_support(self, it_support):
        pass

    @abstractmethod
    def visit_staff_list(self, staff_list):
        pass





