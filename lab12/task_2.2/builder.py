from car import Car
from enums import Model, Color, FuelType
from engine_part import Engine
from wheel_part import Wheel


class CarBuilder:
    wheels = {}
    engines = {}

    def __init__(self):
        self._model = ...
        self._color = ...
        self._engine = ...
        self._wheel = ...

        self.reset()

    def reset(self):
        self._model = Model.RangeRower
        self._color = Color.Red
        self._engine = Engine(133, FuelType.Petrol)
        self._wheel = Wheel(21)
        return self

    def set_model(self, model):
        self._model = model
        return self

    def set_color(self, color):
        self._color = color
        return self

    def set_engine(self, engine):
        self._engine = engine
        return self

    def set_wheel(self, wheel):
        self._wheel = wheel
        return self

    def build(self):
        return Car(
            model=self._model,
            color=self._color,
            engine=self._engine,
            wheel=self._wheel,
        )