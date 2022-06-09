from employee import Staff
from manager import Manager
from salesman import SalesMan
from it_support import ITSupport
from fine_action import FineAction
from raise_action import RaiseAction


def main():
    staff_list = Staff()

    staff_list.add_employee(Manager(10_000))
    staff_list.add_employee(SalesMan(20_000))
    staff_list.add_employee(ITSupport(30_000))

    print(f'Total amount: {staff_list.get_salary()}')

    staff_list.accept(RaiseAction(10))
    print(f'Total amount: {staff_list.get_salary()}')

    staff_list.accept(FineAction(1000))
    print(f'Total amount: {staff_list.get_salary()}')


if __name__ == '__main__':
    main()