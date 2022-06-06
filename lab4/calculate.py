from abc import ABC, abstractmethod


class V_Calculator(ABC):
    @abstractmethod
    def set_vehicle(self, vehicle):
        pass

    @abstractmethod
    def calculate_price(self):
        pass


class T_Calculator(V_Calculator):
    _average_price = 6000

    def set_vehicle(self, vehicle):
        self._vehicle = vehicle

    def calculate_price(self):

        assert self._vehicle is not None, "Define you vehicle"

        if self.average_price - self._vehicle.age * 100 - self._vehicle.kilometrage / 100 > 0:
            price = self.average_price - self._vehicle.age * 100 - self._vehicle.kilometrage / 100
            return f"{price}_USD"
        else:
            price = 0
            return f"{price}_USD"

    @property
    def average_price(self):
        return self._average_price


class C_Calculator(V_Calculator):
    _average_price = 6000

    def set_vehicle(self, vehicle):
        self._vehicle = vehicle

    def _get_retail_price(self):
        assert self._vehicle is not None, "Define you vehicle"

        if self._vehicle.model == "Ford":
            return 3000
        elif self._vehicle.model == "Audi":
            return 5000
        elif self._vehicle.model == "BMW":
            return 7000
        elif self._vehicle.model == "Tesla":
            return 10000
        else:
            return self._average_price

    def calculate_price(self):
        global price
        assert self._vehicle is not None, "Define you vehicle"

        if (1 - self._vehicle.damage) * max(self._get_retail_price() - (self._vehicle.age * 100), 0) > 0:
            price = int((1 - self._vehicle.damage) * max(self._get_retail_price() - (self._vehicle.age * 100), 0))
            return f"{price}_USD"
        else:
            price = 0
            return f"{price}_USD"

    @property
    def average_price(self):
        return self._average_price
