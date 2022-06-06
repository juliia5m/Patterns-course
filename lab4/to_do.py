from abc import ABC, abstractmethod
from auto import Auto
from calculate import C_Calculator, T_Calculator
from vehic import Car, Truck


class Customs(ABC):
    @abstractmethod
    def vh_price(self, auto):
        pass

    @abstractmethod
    def tax(self, auto):
        pass


class Adapter(Customs):
    _truck_calc = T_Calculator()
    _car_calc = C_Calculator()
    _usd2hrn = 29.4
    _price_hrn: float


    def vh_price(self, auto):
        if auto.model == 'truck':
            calc = self._truck_calc
            calc.set_vehicle(Truck(age=auto.age, kilometrage=auto.kilometrage))
        else:
            calc = self._car_calc
            calc.set_vehicle(Car(age=auto.age, model=auto.model, damage=1 if auto.damaged else 0))

        price_str = calc.calculate_price()
        price_usd = float(price_str[:-4])
        self._price_hrn = price_usd * self._usd2hrn
        return self._price_hrn

    def tax(self, auto):
        const = 0.2
        return self.vh_price(auto) * const

# numbers from class work

def results():
    a1 = Auto(age=2, model='truck', damaged=False, kilometrage=10000)
    a2 = Auto(age=10, model='Ford', damaged=True, kilometrage=500000)
    a3 = Auto(age=3, model='Tesla', damaged=False, kilometrage=75000)
    autos = [a1,a2,a3]
    adapter = Adapter()
    for auto in autos:
        print("---")
        print(auto)
        pr = adapter.vh_price(auto)
        tx = adapter.tax(auto)
        print(f'Price is equal to: {pr}, tax is equal to: {tx}')
        print("---")



if __name__ == '__main__':
    results()
