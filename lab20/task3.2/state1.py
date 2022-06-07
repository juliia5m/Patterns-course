from __future__ import annotations
from abc import ABC, abstractmethod


class State1(ABC):
    @abstractmethod
    def turn_up(self, fan):
        pass

    @abstractmethod
    def turn_down(self, fan):
        pass


class OffState(State1):
    def turn_up(self, fan):
        fan.set_state(LowState())
        print('Low')

    def turn_down(self, fan):
        pass


class LowState(State1):
    def turn_up(self, fan):
        fan.set_state(MediumState())
        print('Increasing Medium')

    def turn_down(self, fan):
        fan.set_state(OffState())
        print('fan off')


class MediumState(State1):
    def turn_up(self, fan):
        fan.set_state(HighState())
        print('Increasing: High')

    def turn_down(self, fan):
        fan.set_state(LowState())
        print('Decreasing: Low')


class HighState(State1):
    def turn_up(self, fan):
        pass

    def turn_down(self, fan):
        fan.set_state(MediumState())
        print('Decreasing fan: Medium')