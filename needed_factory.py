from abc import abstractmethod
from abc import ABC

from classes_ import Americano, Cappuccino, Expresso, Late, Tea


class CafeFactory(ABC):

    @abstractmethod
    def create_beverage(self):
        pass


class AmericanoFactory(CafeFactory):
    def create_beverage(self):
        return Americano()


class CappuccinoFactory(CafeFactory):
    def create_beverage(self):
        return Cappuccino()


class ExpressoFactory(CafeFactory):
    def create_beverage(self):
        return Expresso()


class LateFactory(CafeFactory):
    def create_beverage(self):
        return Late()


class TeaFactory(CafeFactory):
    def create_beverage(self):
        return Tea()

