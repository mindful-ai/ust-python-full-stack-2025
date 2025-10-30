# SOLID Principles in Python

## 🧩 Overview

**SOLID** is an acronym for five key principles of object-oriented software design:

| Principle | Meaning | Key Idea |
|------------|----------|-----------|
| **S** | **Single Responsibility Principle (SRP)** | A class should have only one reason to change. |
| **O** | **Open/Closed Principle (OCP)** | Classes should be open for extension, but closed for modification. |
| **L** | **Liskov Substitution Principle (LSP)** | Subclasses should be substitutable for their base classes without breaking functionality. |
| **I** | **Interface Segregation Principle (ISP)** | Clients should not be forced to depend on interfaces they do not use. |
| **D** | **Dependency Inversion Principle (DIP)** | High-level modules should depend on abstractions, not concrete implementations. |

---

## 🧠 Example: Payment Processing System

We’ll design a simple **Payment System** to demonstrate all five SOLID principles.

---

### 1️⃣ Single Responsibility Principle (SRP)

> Each class should have **only one reason to change** — i.e., one responsibility.

```python
class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of ₹{amount}")

class InvoiceGenerator:
    def generate_invoice(self, amount):
        print(f"Invoice generated for ₹{amount}")
```
Now, changes in invoicing won’t affect payment logic.

---

### 2️⃣ Open/Closed Principle (OCP)

> Classes should be **open for extension** but **closed for modification**.

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")
```

Adding a new payment type like `UPIPayment` doesn’t require changing existing code.

---

### 3️⃣ Liskov Substitution Principle (LSP)

> Subclasses should be **substitutable** for their parent class.

```python
def complete_payment(payment_method: Payment, amount):
    payment_method.pay(amount)

complete_payment(CreditCardPayment(), 500)
complete_payment(PayPalPayment(), 750)
```

All subclasses behave consistently with the base class interface.

---

### 4️⃣ Interface Segregation Principle (ISP)

> Clients should not depend on methods they do not use.

```python
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class OnlinePayment(Payment):
    @abstractmethod
    def authenticate(self):
        pass

class UpiPayment(OnlinePayment):
    def authenticate(self):
        print("UPI authenticated.")
    
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI.")
```

Each class implements only what it needs.

---

### 5️⃣ Dependency Inversion Principle (DIP)

> High-level modules should depend on **abstractions**, not on **concrete implementations**.

```python
class PaymentService:
    def __init__(self, payment: Payment):
        self.payment = payment  # depends on abstraction
    
    def make_payment(self, amount):
        self.payment.pay(amount)

service = PaymentService(PayPalPayment())
service.make_payment(1200)
```

We can switch payment types easily without modifying `PaymentService`.

---

## 🧩 Full Working Example (Combining All SOLID Principles)

```python
from abc import ABC, abstractmethod

# --- SRP ---
class InvoiceGenerator:
    def generate_invoice(self, amount):
        print(f"[Invoice] Generated for ₹{amount}")

# --- OCP ---
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# --- LSP ---
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"[Payment] ₹{amount} paid using Credit Card.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"[Payment] ₹{amount} paid via PayPal.")

# --- ISP ---
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

# --- DIP ---
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
```

**Output:**
```
[Auth] UPI authentication successful.
[Payment] ₹1000 paid using UPI.
[Invoice] Generated for ₹1000
[Payment] ₹500 paid via PayPal.
[Invoice] Generated for ₹500
```

---

## 🏁 Summary

| Principle | Example in Code | Benefit |
|------------|----------------|----------|
| SRP | `PaymentProcessor` vs `InvoiceGenerator` | Simplifies maintenance |
| OCP | Abstract class `Payment` | Add new types without modifying code |
| LSP | `CreditCardPayment`, `PayPalPayment` | Interchangeable subclasses |
| ISP | `OnlinePayment` separates authentication | Avoids forcing unused methods |
| DIP | `PaymentService` depends on `Payment` interface | Increases flexibility and testability |
