from dark_coffee import DarkCoffee
from decaf import Decaf
from espresso import Espresso
from addings import Milk, Cream, SourCream, Sugar


def main():
    b1 = Sugar(Sugar(Espresso()))
    print(f'{b1.name() = }, {b1.cost() = }\n')

    b2 = Sugar(Sugar(SourCream(DarkCoffee())))
    print(f'{b2.name() = }, {b2.cost() = }\n')

    b3 = Sugar(Cream(Espresso()))
    print(f'{b3.name() = }, {b3.cost() = }\n')

    b4 = Sugar(Sugar(Milk(Decaf())))
    print(f'{b4.name() = }, {b4.cost() = }\n')


if __name__ == '__main__':
    main()
