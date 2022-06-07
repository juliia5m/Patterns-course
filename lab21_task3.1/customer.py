

class Customer:
    def __init__(self):
        self._payment_method = None

    def pay_method(self, payment_method):
        self._payment_method = payment_method

    def make_payment(self, amount):
        # assert self._payment_method is not None, "error; set a payment method"

        if self._payment_method is not None:
            self._payment_method.make_payment(amount)
        else:
            print("error; set a payment method")