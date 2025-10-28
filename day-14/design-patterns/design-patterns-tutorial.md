# 🧩 Design Patterns Tutorial

## 📘 What Are Design Patterns?

**Design patterns** are *proven solutions to common problems* that occur during software design and development.  
They aren’t complete code — rather, they are **templates or blueprints** that help you structure your code in a clean, efficient, and maintainable way.

In short:
> A Design Pattern = A general reusable solution to a recurring problem in software design.

---

## 💡 Why Do We Need Design Patterns?

| Reason | Explanation |
|--------|--------------|
| **1. Reusability** | Common patterns save time by providing pre-tested, proven development paradigms. |
| **2. Maintainability** | Code becomes easier to understand, modify, and debug. |
| **3. Scalability** | Patterns help create flexible systems that can grow and change easily. |
| **4. Team Communication** | Developers can discuss solutions using common vocabulary — e.g., “Use a Singleton here.” |
| **5. Reduces Complexity** | Patterns help manage complex system structures by defining clear responsibilities. |

> Think of patterns as the “best practices” for organizing your code.

---

## 🧱 Types of Design Patterns

| Type | Description | Example Patterns |
|------|--------------|------------------|
| **Creational** | Deal with object creation mechanisms, trying to create objects in a suitable way. | Singleton, Factory Method, Builder |
| **Structural** | Deal with object composition — how classes and objects combine to form larger structures. | Adapter, Decorator, Facade |
| **Behavioral** | Deal with communication between objects, improving flexibility. | Observer, Strategy, Command |

---

## 🏗️ 1. Creational Patterns Example — **Singleton Pattern**

### Problem:
You want to ensure that a class has **only one instance** (e.g., for a database connection or configuration manager).

### Python Example:
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Test
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True → Both refer to the same instance
```

### Real-life Use Case:
- Database connection pool
- Logging systems
- Configuration manager in applications

---

## ⚙️ 2. Structural Patterns Example — **Adapter Pattern**

### Problem:
Two classes are incompatible but need to work together.

### Example:
Suppose you have an existing API returning temperature in Celsius, but your new system expects Fahrenheit.

```python
class CelsiusTemperature:
    def get_temp_celsius(self):
        return 25

class FahrenheitAdapter:
    def __init__(self, celsius_obj):
        self.celsius_obj = celsius_obj

    def get_temp_fahrenheit(self):
        return (self.celsius_obj.get_temp_celsius() * 9/5) + 32

# Usage
celsius = CelsiusTemperature()
adapter = FahrenheitAdapter(celsius)
print(adapter.get_temp_fahrenheit())  # 77.0°F
```

### Real-life Use Case:
- Integrating legacy systems
- Plug-in architectures (e.g., adapting external APIs)

---

## 🔄 3. Behavioral Patterns Example — **Observer Pattern**

### Problem:
You have multiple objects that need to stay in sync when one changes.

### Example:
When a subject (like stock data) changes, all observers (like user dashboards) should be updated automatically.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received: {message}")

# Usage
subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.attach(observer1)
subject.attach(observer2)
subject.notify("Stock prices updated!")
```

### Real-life Use Case:
- Event-driven systems (e.g., GUI listeners)
- Notification systems (e.g., push updates)

---

## 🧠 Summary

| Category | Focus | Example |
|-----------|--------|----------|
| Creational | Object creation | Singleton, Factory |
| Structural | Object composition | Adapter, Decorator |
| Behavioral | Object interaction | Observer, Strategy |

---

## 🧰 When to Use Design Patterns

✅ When you face **repeated architectural or design problems**  
✅ When your code becomes **hard to extend or maintain**  
✅ When your system **needs flexibility** and **reusability**  
✅ When you want to **improve communication** between developers  

---

## 🪄 Real-world Analogy

- **Factory Pattern** → Like a restaurant kitchen producing different dishes (objects) based on order (input).  
- **Singleton Pattern** → Like a single government issuing passports — only one instance allowed.  
- **Observer Pattern** → Like YouTube subscriptions: users (observers) are notified when a new video (subject) is uploaded.

---

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
