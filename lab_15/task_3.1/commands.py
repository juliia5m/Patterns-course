from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, dev):
        self.dev = dev

    @abstractmethod
    def do(self):
        pass


class CommandOn(Command):
    def do(self):
        self.dev.light_on()


class CommandOff(Command):
    def do(self):
        self.dev.light_off()
