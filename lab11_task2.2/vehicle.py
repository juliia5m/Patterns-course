from ign import Ign
from gear import Gear
from accelerator import Accelerator
from h_br import H_br
from cl import Cl


class Vehicle:

    def __init__(self):
        self._ignition = Ign()
        self._clutch = Cl()
        self._accelerator = Accelerator()
        self._gear_stick = Gear()
        self._handbrake = H_br()

    def drive(self):
        self._ignition.turn_on()
        self._clutch.press()
        self._accelerator.press()
        self._clutch.lift()
        self._gear_stick.gear_var(3)
        self._handbrake.push_down()
        self._accelerator.press()
        self._clutch.press()