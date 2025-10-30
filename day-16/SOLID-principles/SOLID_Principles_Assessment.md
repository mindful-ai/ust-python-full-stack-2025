
# 🧩 SOLID Principles Assessment

## Problem Statement

You are asked to design a simple **E-Commerce Order Processing System** following the **SOLID design principles**.

### Requirements

1. **Single Responsibility Principle (SRP)**  
   - Create separate classes for managing orders and generating invoices.

2. **Open/Closed Principle (OCP)**  
   - The payment method should be extendable (e.g., CreditCard, PayPal, UPI) without modifying the existing code.

3. **Liskov Substitution Principle (LSP)**  
   - Derived payment methods should be substitutable for the base payment method.

4. **Interface Segregation Principle (ISP)**  
   - The interface for notification should separate Email and SMS functionality.

5. **Dependency Inversion Principle (DIP)**  
   - The Order class should depend on abstractions (interfaces), not concrete implementations.

---

## Skeleton Code

```python
from abc import ABC, abstractmethod

# SRP: Separate order management and invoice generation
class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        pass


class InvoiceGenerator:
    def generate_invoice(self, order):
        pass


# OCP + LSP: Payment interface and implementations
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentProcessor):
    def pay(self, amount):
        pass


class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        pass


# ISP: Separate notification interfaces
class EmailNotifier(ABC):
    @abstractmethod
    def send_email(self, message):
        pass


class SMSNotifier(ABC):
    @abstractmethod
    def send_sms(self, message):
        pass


# DIP: Order depends on abstractions
class Checkout:
    def __init__(self, payment_processor: PaymentProcessor, notifier: EmailNotifier):
        self.payment_processor = payment_processor
        self.notifier = notifier

    def process_order(self, order: Order):
        pass


if __name__ == "__main__":
    # Example: Fill in the implementation details and demonstrate SOLID principles
    pass
```

---

## ✅ Solution Reference

```python
from abc import ABC, abstractmethod

# SRP
class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item['price'] for item in self.items)


class InvoiceGenerator:
    def generate_invoice(self, order):
        print(f"Invoice total: ₹{order.calculate_total()}")


# OCP + LSP
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ₹{amount} via Credit Card")


class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ₹{amount} via PayPal")


class UPIPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI")


# ISP
class EmailNotifier(ABC):
    @abstractmethod
    def send_email(self, message):
        pass


class SMSNotifier(ABC):
    @abstractmethod
    def send_sms(self, message):
        pass


class EmailService(EmailNotifier):
    def send_email(self, message):
        print(f"Email sent: {message}")


class SMSService(SMSNotifier):
    def send_sms(self, message):
        print(f"SMS sent: {message}")


# DIP
class Checkout:
    def __init__(self, payment_processor: PaymentProcessor, notifier: EmailNotifier):
        self.payment_processor = payment_processor
        self.notifier = notifier

    def process_order(self, order: Order):
        amount = order.calculate_total()
        self.payment_processor.pay(amount)
        self.notifier.send_email(f"Your order for ₹{amount} has been processed!")


if __name__ == "__main__":
    order = Order([{'item': 'Laptop', 'price': 60000}, {'item': 'Mouse', 'price': 1000}])
    invoice = InvoiceGenerator()
    invoice.generate_invoice(order)

    payment = UPIPayment()
    notifier = EmailService()

    checkout = Checkout(payment, notifier)
    checkout.process_order(order)
```

---

## 💡 Key Takeaways

- **SRP** → Each class has one reason to change.  
- **OCP** → Easily extend payment methods.  
- **LSP** → Derived classes behave as expected.  
- **ISP** → Clients only depend on what they use.  
- **DIP** → High-level modules depend on abstractions.
