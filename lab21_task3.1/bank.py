from pay import PaymentMethod


class BankPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f'${amount} payment from bank account.')