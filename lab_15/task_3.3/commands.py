from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def do(self):
        pass


class CommandOn(Command):
    def __init__(self, goal):
        self._goal = goal

    def do(self):
        self._goal.on()


class CommandOff(Command):
    def __init__(self, goal):
        self._goal = goal

    def do(self):
        self._goal.off()


class CommandVolumeUp(Command):
    def __init__(self, goal):
        self._goal = goal

    def do(self):
        self._goal.vol_up()


class CommandVolumeDown(Command):
    def __init__(self, goal):
        self._goal = goal

    def do(self):
        self._goal.vol_down()


class CommandNextChannel(Command):
    def __init__(self, goal):
        self._goal = goal

    def do(self):
        self._goal.next_channel()


class CommandPrevChannel(Command):
    def __init__(self, goal):
        self._goal = goal

    def do(self):
        self._goal.prev_channel()