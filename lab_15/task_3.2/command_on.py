from commands import Command


class CommandOn(Command):
    def __init__(self, aim):
        self._aim = aim

    def do(self):
        self._aim.light_on()
