from pay import PaymentMethod


class GooglePayPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f'${amount} payment from GooglePlay account.')