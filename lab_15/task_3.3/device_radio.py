from device_base import Device

class Radio(Device):
    def __init__(self):
        self._is_on = False
        self._channel = 12
        self._volume = 5

    def on(self):
        if self._is_on:
            return
        self._is_on = True


    def off(self):
        if not self._is_on:
            return
        self._is_on = False


    def vol_up(self):
        if not self._is_on:
            return
        self._volume += 1
        print(f'Radio new volume = {self._volume}')

    def vol_down(self):
        if not self._is_on:
            return
        self._volume -= 1
        print(f'Radio new volume = {self._volume}')

    def next_channel(self):
        if not self._is_on:
            return
        self._channel += 1
        print(f'Radio new channel = {self._channel}')

    def prev_channel(self):
        if not self._is_on:
            return
        self._channel -= 1
        print(f'Radio new channel = {self._channel}')