from abc import ABC, abstractmethod

# --- SRP: Separate classes for distinct responsibilities ---
class InvoiceGenerator:
    def generate_invoice(self, amount):
        print(f"[Invoice] Generated for ₹{amount}")

# --- OCP: Abstract base class for extension ---
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# --- LSP: Subclasses can replace the base class ---
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"[Payment] ₹{amount} paid using Credit Card.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"[Payment] ₹{amount} paid via PayPal.")

# --- ISP: Separate interfaces for online/offline payments ---
class OnlinePayment(Payment):
    @abstractmethod
    def authenticate(self):
        pass

class UpiPayment(OnlinePayment):
    def authenticate(self):
        print("[Auth] UPI authentication successful.")
    def pay(self, amount):
        self.authenticate()
        print(f"[Payment] ₹{amount} paid using UPI.")

# --- DIP: Depend on abstraction, not concretion ---
class PaymentService:
    def __init__(self, payment: Payment, invoice: InvoiceGenerator):
        self.payment = payment
        self.invoice = invoice
    
    def make_payment(self, amount):
        self.payment.pay(amount)
        self.invoice.generate_invoice(amount)

# --- Client code ---
if __name__ == "__main__":
    service = PaymentService(UpiPayment(), InvoiceGenerator())
    service.make_payment(1000)

    service2 = PaymentService(PayPalPayment(), InvoiceGenerator())
    service2.make_payment(500)
