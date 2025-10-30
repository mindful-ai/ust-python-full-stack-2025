# Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")


class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


context = PaymentContext(CreditCardPayment())
context.pay(200)

context = PaymentContext(PayPalPayment())
context.pay(350)
