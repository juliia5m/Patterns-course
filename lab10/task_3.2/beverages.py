from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def cost(self):
        pass



