from beverages import Beverage
from abc import ABC


class BaseAdding(Beverage, ABC):
    def __init__(self, beverage):
        self._beverage = beverage


class Milk(BaseAdding):
    def __init__(self, beverage):
        super(Milk, self).__init__(beverage)

    def name(self):
        return self._beverage.name() + ' + milk'

    def cost(self):
        return self._beverage.cost() + 5


class Sugar(BaseAdding):
    def __init__(self, beverage):
        super(Sugar, self).__init__(beverage)

    def name(self):
        return self._beverage.name() + ' + sugar'

    def cost(self):
        return self._beverage.cost() + 5


class SourCream(BaseAdding):
    def __init__(self, beverage):
        super(SourCream, self).__init__(beverage)

    def name(self):
        return self._beverage.name() + ' + sour cream'

    def cost(self):
        return self._beverage.cost() + 5


class Cream(BaseAdding):
    def __init__(self, beverage):
        super(Cream, self).__init__(beverage)

    def name(self):
        return self._beverage.name() + ' + cream'

    def cost(self):
        return self._beverage.cost() + 5