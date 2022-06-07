from employee import Employee
from staff_people import Staff



def main():
    anya = Employee('Anya', 'profesor', 59)
    yuliia = Employee('Yuliia', 'researcher', 19)
    sashko = Employee('Sashko', 'programmer', 35)
    andrew = Employee('Andrew', 'hr', 27)

    staff_ = Staff([anya, yuliia, sashko, andrew])
    for employee in staff_:
        print(employee.get_name(), employee.get_position(), employee.get_age())

    print('---- end of the list -----')


if __name__ == '__main__':
    main()
