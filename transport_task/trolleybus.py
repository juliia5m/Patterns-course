from abc import abstractmethod, ABC
from transport import Transport


class Trolleybus(Transport):

    @abstractmethod
    def move_by_contact_network(self):
        pass


class SkodaTrolleybus(Trolleybus, ABC):
    def __init__(self):
        super().__init__(6800000, 13)

    def move_by_contact_network(self):
        print("go-go-go-go")


class VolvoTrolleybus(Trolleybus, ABC):
    def __init__(self):
        super().__init__(7000000, 13)

    def move_by_contact_network(self):
        print("go-go-go-go")
