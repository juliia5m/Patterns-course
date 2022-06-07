from pay import PaymentMethod


class PayPalPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f'${amount} payment from PayPal.')