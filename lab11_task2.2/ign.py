class Ign:
    def __init__(self):
        self._is_on = False

    def turn_on(self):
        self._is_on = True
        print('ignition on')

    def turn_off(self):
        self._is_on = False
        print('ignition off')