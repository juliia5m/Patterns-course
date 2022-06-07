from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

