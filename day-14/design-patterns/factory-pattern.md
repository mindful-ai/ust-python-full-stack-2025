# 🏭 Factory Design Pattern — Real-Life Example

## 📘 Concept Recap

**Factory Pattern** is a *Creational Design Pattern* that provides a way to **create objects without exposing the object creation logic to the client**.

Instead of creating objects directly with `ClassName()`, you delegate that job to a **Factory** which decides which subclass or object type to instantiate based on some input.

---

## 🎯 Real-Life Problem Statement

### Scenario:
You are building a **Payment Processing System** that supports multiple payment methods:
- Credit Card  
- PayPal  
- UPI  

Each payment type requires a different implementation for the `process_payment()` method.  

### Problem:
If you use multiple `if-else` statements to decide which payment class to use, your code becomes hard to maintain and extend — especially if you later add more payment options (e.g., Crypto, Net Banking).

We need a **clean, scalable way** to create the appropriate payment processor without changing client code.

---

## 🧩 Factory Pattern Solution

We’ll create:
1. **An interface (base class)** → `PaymentMethod`
2. **Concrete subclasses** → `CreditCardPayment`, `PayPalPayment`, `UPIPayment`
3. **A Factory class** → `PaymentFactory` that decides which object to instantiate.

---

### ✅ Implementation in Python

```python
from abc import ABC, abstractmethod

# Step 1: Abstract Base Class
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Step 2: Concrete Implementations
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing credit card payment of ₹{amount}."


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ₹{amount}."


class UPIPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing UPI payment of ₹{amount}."


# Step 3: Factory Class
class PaymentFactory:
    @staticmethod
    def get_payment_method(method_type):
        if method_type == "creditcard":
            return CreditCardPayment()
        elif method_type == "paypal":
            return PayPalPayment()
        elif method_type == "upi":
            return UPIPayment()
        else:
            raise ValueError(f"Unknown payment method: {method_type}")


# Step 4: Client Code (using the Factory)
def main():
    for method in ["creditcard", "paypal", "upi"]:
        payment_processor = PaymentFactory.get_payment_method(method)
        print(payment_processor.process_payment(1500))


if __name__ == "__main__":
    main()
```

---

### 🧠 Output

```
Processing credit card payment of ₹1500.
Processing PayPal payment of ₹1500.
Processing UPI payment of ₹1500.
```

---

## 💬 Explanation

| Step | What Happens | Why It’s Important |
|------|---------------|--------------------|
| **1. Define Base Class** | `PaymentMethod` ensures all payment types follow a common interface. | Promotes consistency |
| **2. Implement Subclasses** | Each class handles its own logic for processing payment. | Enables flexibility |
| **3. Factory Handles Creation** | `PaymentFactory` decides which payment class to instantiate. | Avoids `if-else` logic in client code |
| **4. Client Just Uses Factory** | The client doesn’t know or care about which class is used internally. | Easy to add new payment types |

---

## ⚡ Advantages

✅ **Encapsulation of Object Creation** — Client code doesn’t need to know how objects are created.  
✅ **Open/Closed Principle** — You can add new payment types without modifying client code.  
✅ **Improved Maintainability** — Centralized object creation logic.  
✅ **Easier Testing** — Factory methods can easily be mocked.

---

## 🧠 Real-World Use Cases of Factory Pattern

| Domain | Example |
|--------|----------|
| Web Development | Creating different database connectors (MySQL, PostgreSQL, MongoDB) |
| Payment Systems | Supporting different gateways like Razorpay, PayPal, Stripe |
| UI Development | Creating platform-specific buttons (Android, iOS) |
| Game Engines | Creating different character or weapon types dynamically |

---
