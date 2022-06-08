from commands import Command


class CommandOff(Command):
    def __init__(self, aim):
        self._aim = aim

    def do(self):
        self._aim.light_off()