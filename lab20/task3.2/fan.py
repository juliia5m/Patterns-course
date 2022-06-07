from __future__ import annotations
from state1 import OffState


class Fan:
    def __init__(self):
        self._state = OffState()

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def turn_up(self):
        self._state.turn_up(self)

    def turn_down(self):
        self._state.turn_down(self)
