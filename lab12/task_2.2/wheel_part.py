class Wheel:
    cached = {}

    def __init__(self, diameter):
        self._diameter = diameter

    def __str__(self):
        return f"Wheel(diameter = {self._diameter})"


class WheelBuilder:
    def __init__(self):
        self._cached = {}

        self._diameter = ...
        self._material = ...

    def reset(self):
        self._diameter = 24
        return self

    def set_diameter(self, diameter):
        self._diameter = diameter
        return self

    def build(self, diameter):
        if diameter in self._cached:
            wheel = self._cached.get(diameter)
        else:
            wheel = Wheel(diameter)
            self._cached[diameter] = wheel
        return wheel