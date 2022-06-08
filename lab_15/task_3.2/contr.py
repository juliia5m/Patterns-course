
from lamp import Lamp
from command_off import CommandOff
from command_on import CommandOn


class Contr:
    def __init__(self, goal):
        self._commands_on = []
        self._commands_off = []
        if isinstance(goal, Lamp):
            self._commands_on.append(CommandOn(goal))
            self._commands_off.append(CommandOff(goal))
        elif isinstance(goal, list):
            for t in goal:
                self._commands_on.append(CommandOn(t))
                self._commands_off.append(CommandOff(t))

    def on(self):
        for command in self._commands_on:
            command.do()

    def off(self):
        for command in self._commands_off:
            command.do()