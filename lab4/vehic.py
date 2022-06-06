class Vehicle:
    def __init__(self, age = 0, model = "def", damage = 0, kilometrage = 0):
        self._age = age
        self._model = model
        self._damage = damage
        self._kilometrage = kilometrage

    @property
    def age(self):
        return self._age

    @property
    def model(self):
        return self._model

    @property
    def damage(self):
        return self._damage

    @property
    def kilometrage(self):
        return self._kilometrage


class Car(Vehicle):
    def __init__(self, age, model, damage):
        super(Car, self).__init__(age=age, model=model, damage=damage, kilometrage=0)


class Truck(Vehicle):
    def __init__(self, age, kilometrage):
        super(Truck, self).__init__(age=age, model='truck', damage=0, kilometrage=kilometrage)
