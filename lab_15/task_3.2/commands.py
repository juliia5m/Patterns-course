from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def do(self):
        pass


