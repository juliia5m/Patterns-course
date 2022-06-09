from visitor import Visitor


class FineAction(Visitor):
    def __init__(self, fine: int):
        assert 0.5 <= fine, 'fine can not be negative'
        self._fine = fine

    def visit_manager(self, manager):
        salary = manager.get_salary()
        manager.set_salary(max(0.1, salary - self._fine))

    def visit_sales_man(self, sales_person):
        salary = sales_person.get_salary()
        sales_person.set_salary(max(0.1, salary - self._fine))

    def visit_it_support(self, it_support):
        salary = it_support.get_salary()
        it_support.set_salary(max(0.1, salary - self._fine))  # fine can't be greater than salary

    def visit_staff_list(self, staff_list):
        print('all done')