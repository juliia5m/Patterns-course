from employee import Employee


class ITSupport(Employee):
    def __init__(self, salary):
        self._salary = salary

    def set_salary(self, updated_salary):
        self._salary = updated_salary

    def get_salary(self):
        return self._salary

    def accept(self, visitor):
        visitor.visit_it_support(self)