from abc import abstractmethod, ABC
from transport import Transport

class Tram(Transport):

    @abstractmethod
    def move_by_rails(self):
        pass


class SkodaTram(Tram, ABC):
    def __init__(self):
        super().__init__(9000000, 8)

    def move_by_rails(self):
        print("go-go-go")


class VolvoTram(Tram, ABC):
    def __init__(self):
        super().__init__(10000000, 7)

    def move_by_rails(self):
        print("go-go-go")