from abc import ABC, abstractmethod


class Cafe(ABC):

    @abstractmethod
    def create_beverage(self):
        pass
