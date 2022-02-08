from abc import abstractmethod, ABC
from transport import Transport


class Bus(Transport):

    @abstractmethod
    def move_by_road(self):
        pass


class SkodaBus(Bus, ABC):
    def __init__(self):
        super().__init__(4500000, 25)

    def move_by_road(self):
        print("go-go")


class VolvoBus(Bus, ABC):
    def __init__(self):
        super().__init__(6000000, 20)

    def move_by_road(self):
        print("go-go")
