from abc import ABC, abstractmethod


class Beverage(ABC):

    def __init__(self, ingredients_cost, sell_price):
        self.ingredients_cost = ingredients_cost
        self.sell_price = sell_price

    def get_ingredients_cost(self):
        return self.ingredients_cost

    def get_sell_price(self):
        return self.sell_price

    @abstractmethod
    def taste(self):
        pass
