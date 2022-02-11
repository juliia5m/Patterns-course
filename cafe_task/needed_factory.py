from abc import abstractmethod
from abc import ABC

from classes_ import Americano, Cappuccino, Expresso, Late, Tea


class BeverageFactory(ABC):

    @abstractmethod
    def create_beverage(self):
        pass


class AmericanoFactory(BeverageFactory):
    def create_beverage(self):
        return Americano()


class CappuccinoFactory(BeverageFactory):
    def create_beverage(self):
        return Cappuccino()


class ExpressoFactory(BeverageFactory):
    def create_beverage(self):
        return Expresso()


class LateFactory(BeverageFactory):
    def create_beverage(self):
        return Late()


class TeaFactory(BeverageFactory):
    def create_beverage(self):
        return Tea()

