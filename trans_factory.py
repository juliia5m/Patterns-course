from abc import abstractmethod
from abc import ABC

from bus import SkodaBus, VolvoBus
from tram import SkodaTram, VolvoTram
from trolleybus import SkodaTrolleybus, VolvoTrolleybus


class TransFactory(ABC):

    @abstractmethod
    def create_bus(self):
        pass

    @abstractmethod
    def create_tram(self):
        pass

    @abstractmethod
    def create_trolleybus(self):
        pass


class SkodaFactory(TransFactory):
    def create_bus(self):
        return SkodaBus()

    def create_tram(self):
        return SkodaTram()

    def create_trolleybus(self):
        return SkodaTrolleybus()


class VolvoFactory(TransFactory):
    def create_bus(self):
        return VolvoBus()

    def create_tram(self):
        return VolvoTram()

    def create_trolleybus(self):
        return VolvoTrolleybus()
