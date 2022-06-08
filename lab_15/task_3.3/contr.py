from abc import ABC, abstractmethod

from device_base import Device
from commands import CommandOn, CommandOff, CommandVolumeUp, CommandVolumeDown, CommandNextChannel, CommandPrevChannel


class Controller(ABC):
    @abstractmethod
    def device_on(self):
        pass

    @abstractmethod
    def device_off(self):
        pass

    @abstractmethod
    def device_vol_up(self):
        pass

    @abstractmethod
    def device_vol_down(self):
        pass

    @abstractmethod
    def device_next_channel(self):
        pass

    @abstractmethod
    def device_prev_channel(self):
        pass


class Controller1(Controller):
    def __init__(self, goal):
        self._on = []
        self._off = []
        self._vol_up = []
        self._vol_down = []
        self._next_ch = []
        self._prev_ch = []
        if isinstance(goal, Device):
            self._on.append(CommandOn(goal))
            self._off.append(CommandOff(goal))
            self._vol_up.append(CommandVolumeUp(goal))
            self._vol_down.append(CommandVolumeDown(goal))
            self._next_ch.append(CommandNextChannel(goal))
            self._prev_ch.append(CommandPrevChannel(goal))
        elif isinstance(goal, list):
            for t in goal:
                self._on.append(CommandOn(t))
                self._off.append(CommandOff(t))
                self._vol_up.append(CommandVolumeUp(t))
                self._vol_down.append(CommandVolumeDown(t))
                self._next_ch.append(CommandNextChannel(t))
                self._prev_ch.append(CommandPrevChannel(t))

    def device_on(self):
        for command in self._on:
            command.do()

    def device_off(self):
        for command in self._off:
            command.do()

    def device_vol_up(self):
        for command in self._vol_up:
            command.do()

    def device_vol_down(self):
        for command in self._vol_down:
            command.do()

    def device_next_channel(self):
        for command in self._next_ch:
            command.do()

    def device_prev_channel(self):
        for command in self._prev_ch:
            command.do()