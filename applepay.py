from pay import PaymentMethod


class ApplePayPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f'${amount} payment from ApplePay.')