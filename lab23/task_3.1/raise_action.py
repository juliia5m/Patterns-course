from visitor import Visitor


class RaiseAction(Visitor):
    def __init__(self, percent):
        self._percent = percent

    def visit_manager(self, manager):
        salary = manager.get_salary()
        manager.set_salary(salary + int(salary * (self._percent / 100)))

    def visit_sales_man(self, sales_person):
        salary = sales_person.get_salary()
        sales_person.set_salary(salary + int(salary * (self._percent / 100)))

    def visit_it_support(self, it_support):
        salary = it_support.get_salary()
        it_support.set_salary(salary + int(salary * (self._percent / 100)))

    def visit_staff_list(self, staff_list):
        print('done')