class Lamp:
    def __init__(self, name="dyson lamp"):
        self.name = name
        self.is_on = False

    def light_on(self):
        if not self.is_on:
            print(f"{self.name} is on")
            self.is_on = True

    def light_off(self):
        if self.is_on:
            print(f"{self.name} is off")
            self.is_lamp_on = False