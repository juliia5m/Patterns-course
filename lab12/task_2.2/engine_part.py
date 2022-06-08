from enums import FuelType


class Engine:
    cached = {}

    def __init__(self, power, fuel):
        self._power = power
        self._fuel = fuel

    def __str__(self):
        return f"Engine(max power = {self._power}, fuel: {self._fuel})"


class EngineBuilder:
    def __init__(self):
        self._cached = {}

        self._power = ...
        self._fuel = ...

    def reset(self):
        self._power = 210
        self._fuel = FuelType.Petrol
        return self

    def set_power(self, power):
        self._power = power
        return self

    def set_fuel(self, fuel):
        self._fuel = fuel
        return self

    def build(self, power, fuel):
        if (power, fuel) in self._cached:
            engine = self._cached.get((power, fuel))
        else:
            engine = Engine(power, fuel)
            self._cached[(power, fuel)] = engine
        return engine


