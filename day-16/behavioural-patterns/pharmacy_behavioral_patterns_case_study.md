# 🏥 Behavioral Design Patterns Case Study & Assessment (Pharmacy Theme)

## 📘 Case Study: SmartPharma – Intelligent Pharmacy Management System

### 🎯 Objective
This case study demonstrates the **practical integration** of multiple **Behavioral Design Patterns** — namely:
- Chain of Responsibility  
- Command  
- Mediator  
- Memento  
- Observer  
- Visitor  

within a **medical domain** project — an intelligent pharmacy system.

---

## 💡 Project Overview

SmartPharma is a digital pharmacy management system that manages:
- Prescription validation  
- Stock and ordering  
- Communication between pharmacy departments  
- Undo/Redo for orders  
- Notifications for stock changes  
- Analytical reporting

---

## 🧩 Design Patterns Used and Their Purpose

| Pattern | Purpose |
|----------|----------|
| **Chain of Responsibility** | Validate prescriptions through multiple checks (doctor signature, stock, expiry). |
| **Command** | Execute actions like place, cancel, or restock order. |
| **Mediator** | Manage communication between inventory, billing, and notifications. |
| **Memento** | Store and restore previous states of orders (undo). |
| **Observer** | Notify customers and pharmacists when stock changes. |
| **Visitor** | Generate analytical reports and visit system components. |

---

## 🧠 Case Study Code Example

```python
# ========================
# 1. Chain of Responsibility
# ========================

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, prescription):
        if self.successor:
            return self.successor.handle(prescription)


class DoctorSignatureCheck(Handler):
    def handle(self, prescription):
        if not prescription.get("doctor_signed", False):
            print("❌ Prescription rejected: Doctor signature missing.")
            return False
        print("✅ Doctor signature verified.")
        return super().handle(prescription)


class StockCheck(Handler):
    def __init__(self, stock, successor=None):
        super().__init__(successor)
        self.stock = stock

    def handle(self, prescription):
        if prescription["medicine"] not in self.stock:
            print("❌ Medicine not available.")
            return False
        print("✅ Medicine available in stock.")
        return super().handle(prescription)


class ExpiryCheck(Handler):
    def handle(self, prescription):
        print("✅ Expiry date verified.")
        return True


# ========================
# 2. Command Pattern
# ========================

class Command:
    def execute(self):
        pass


class PlaceOrderCommand(Command):
    def __init__(self, receiver, medicine):
        self.receiver = receiver
        self.medicine = medicine

    def execute(self):
        self.receiver.place_order(self.medicine)


class CancelOrderCommand(Command):
    def __init__(self, receiver, medicine):
        self.receiver = receiver
        self.medicine = medicine

    def execute(self):
        self.receiver.cancel_order(self.medicine)


# ========================
# 3. Mediator Pattern
# ========================

class Mediator:
    def notify(self, sender, event):
        pass


class PharmacyMediator(Mediator):
    def __init__(self):
        self.inventory = None
        self.billing = None
        self.notification = None

    def notify(self, sender, event):
        if event == "order_placed":
            self.billing.generate_bill(sender)
            self.notification.send_notification("Order placed successfully!")
        elif event == "out_of_stock":
            self.notification.send_notification("Medicine out of stock!")


# ========================
# 4. Memento Pattern
# ========================

class OrderMemento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class OrderHistory:
    def __init__(self):
        self._history = []

    def save(self, state):
        self._history.append(OrderMemento(state))

    def undo(self):
        if self._history:
            return self._history.pop().get_state()


# ========================
# 5. Observer Pattern
# ========================

class Observer:
    def update(self, message):
        pass


class Customer(Observer):
    def update(self, message):
        print(f"Customer received: {message}")


class Pharmacist(Observer):
    def update(self, message):
        print(f"Pharmacist alert: {message}")


class Inventory:
    def __init__(self):
        self.observers = []
        self.stock = {"Paracetamol": 10}

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)

    def restock(self, item, qty):
        self.stock[item] = self.stock.get(item, 0) + qty
        self.notify(f"{item} restocked with {qty} units.")


# ========================
# 6. Visitor Pattern
# ========================

class Visitor:
    def visit(self, element):
        pass


class SalesReportVisitor(Visitor):
    def visit(self, element):
        print(f"Generating report for {element.__class__.__name__}...")


# ========================
# Main Demonstration
# ========================

if __name__ == "__main__":
    # Chain of Responsibility
    stock = {"Paracetamol": 10, "Amoxicillin": 5}
    chain = DoctorSignatureCheck(StockCheck(stock, ExpiryCheck()))

    prescription = {"doctor_signed": True, "medicine": "Paracetamol"}
    chain.handle(prescription)

    # Command
    class OrderReceiver:
        def place_order(self, med): print(f"Order placed for {med}")
        def cancel_order(self, med): print(f"Order cancelled for {med}")

    receiver = OrderReceiver()
    place_order = PlaceOrderCommand(receiver, "Paracetamol")
    place_order.execute()

    # Observer
    inventory = Inventory()
    c1, p1 = Customer(), Pharmacist()
    inventory.attach(c1)
    inventory.attach(p1)
    inventory.restock("Amoxicillin", 20)
```

---

