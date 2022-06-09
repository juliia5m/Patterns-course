from employee import Employee


class SalesMan(Employee):
    def __init__(self, salary):
        self._salary = salary

    def set_salary(self, updated_salary):
        self._salary = updated_salary

    def get_salary(self):
        return self._salary

    def accept(self, visitor):
        visitor.visit_sales_man(self)