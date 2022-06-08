class Lamp:
    def __init__(self, room):
        self._room = room
        self._is_light_on = False
        self._is_light_off = False

    def light_on(self):
        if self._is_light_on:
            return
        self._is_light_on = True
        print(f'Light"s on in {self._room}')

    def light_off(self):
        if self._is_light_off:
            return
        self._is_light_off = True
        print(f'Light"s off in {self._room}')
