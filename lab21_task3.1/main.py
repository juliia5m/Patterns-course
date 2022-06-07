from customer import Customer
from bank import BankPayment
from paypal import PayPalPayment
from applepay import ApplePayPayment
from googlepay import GooglePayPayment


def main():
    customer = Customer()

    customer.pay_method(ApplePayPayment())
    customer.make_payment(500)

    customer.pay_method(GooglePayPayment())
    customer.make_payment(500)

    customer.pay_method(PayPalPayment())
    customer.make_payment(500)

    customer.pay_method(BankPayment())
    customer.make_payment(500)


if __name__ == '__main__':
    main()
