class Gear:
    def __init__(self):
        self._gear = 0

    def gear_var(self, gear):
        if gear < 0 or gear > 5:
            print('error range')

        self._gear = gear
        print(f'----> {gear}')