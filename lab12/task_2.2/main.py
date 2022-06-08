from random import randint, choice
from enums import FuelType, Color, Model
from builder import CarBuilder
from engine_part import EngineBuilder
from wheel_part import WheelBuilder


def create(car_builder, engine_builder, wheel_builder, vehicles):

    engine = engine_builder.build(power=randint(100, 240) , fuel=choice(list(FuelType)))
    wheel = wheel_builder.build(diameter=randint(17, 35))

    car = car_builder.reset().set_color(choice(list(Color))).set_model(choice(list(Model))).set_engine(engine).set_wheel(wheel).build()

    car.info()

    vehicles.append(car)


def main():
    car_builder = CarBuilder()
    engine_builder = EngineBuilder()
    wheel_builder = WheelBuilder()
    vehicles = []

    i = 0
    while i != 3:
        create(car_builder, engine_builder, wheel_builder, vehicles)
        i += 1


if __name__ == '__main__':
    main()
