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
from abc import ABC, abstractmethod

# ==================== Chain of Responsibility ====================
class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, prescription):
        pass

class PharmacistHandler(Handler):
    def handle_request(self, prescription):
        if prescription["type"] == "common":
            print(f"Pharmacist handled prescription for {prescription['medicine']}")
        elif self.successor:
            self.successor.handle_request(prescription)

class DoctorHandler(Handler):
    def handle_request(self, prescription):
        if prescription["type"] == "critical":
            print(f"Doctor approved prescription for {prescription['medicine']}")
        elif self.successor:
            self.successor.handle_request(prescription)

class SpecialistHandler(Handler):
    def handle_request(self, prescription):
        if prescription["type"] == "special":
            print(f"Specialist approved prescription for {prescription['medicine']}")
        else:
            print("No handler available for this prescription type.")

# ==================== Command Pattern ====================
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class PlaceOrderCommand(Command):
    def __init__(self, pharmacy, medicine):
        self.pharmacy = pharmacy
        self.medicine = medicine

    def execute(self):
        self.pharmacy.place_order(self.medicine)

class RefillStockCommand(Command):
    def __init__(self, pharmacy, medicine, qty):
        self.pharmacy = pharmacy
        self.medicine = medicine
        self.qty = qty

    def execute(self):
        self.pharmacy.refill_stock(self.medicine, self.qty)

# ==================== Mediator Pattern ====================
class PharmacyMediator:
    def __init__(self):
        self.pharmacist = None
        self.inventory_manager = None
        self.payment_processor = None
        self.notification_service = None

    def register_components(self, pharmacist, inventory_manager, payment_processor, notification_service):
        self.pharmacist = pharmacist
        self.inventory_manager = inventory_manager
        self.payment_processor = payment_processor
        self.notification_service = notification_service

    def notify(self, sender, event, data=None):
        if event == "prescription_processed":
            print("[Mediator] Pharmacist processed a prescription. Checking inventory...")
            self.inventory_manager.check_stock(data)
        elif event == "stock_checked":
            print("[Mediator] Inventory checked. Proceeding to payment...")
            self.payment_processor.process_payment(data)
        elif event == "payment_successful":
            print("[Mediator] Payment done. Sending notification...")
            self.notification_service.send_notification(data)
        else:
            print("[Mediator] No handler for event:", event)

# ==================== Colleague Classes ====================
class Pharmacist:
    def __init__(self, mediator):
        self.mediator = mediator

    def process_prescription(self, prescription):
        print(f"Pharmacist processing {prescription['medicine']}")
        self.mediator.notify(self, "prescription_processed", prescription)

class InventoryManager:
    def __init__(self, mediator):
        self.mediator = mediator
        self.stock = {"Paracetamol": 10, "Antibiotic": 5}

    def check_stock(self, prescription):
        med = prescription["medicine"]
        if self.stock.get(med, 0) > 0:
            print(f"InventoryManager: {med} is in stock.")
            self.stock[med] -= 1
            self.mediator.notify(self, "stock_checked", prescription)
        else:
            print(f"InventoryManager: {med} out of stock!")

class PaymentProcessor:
    def __init__(self, mediator):
        self.mediator = mediator

    def process_payment(self, prescription):
        print(f"PaymentProcessor: Processing payment for {prescription['medicine']}...")
        self.mediator.notify(self, "payment_successful", prescription)

class NotificationService:
    def __init__(self, mediator):
        self.mediator = mediator

    def send_notification(self, prescription):
        print(f"NotificationService: Message sent to patient about {prescription['medicine']}")

# ==================== Memento Pattern ====================
class PharmacyMemento:
    def __init__(self, state):
        self.state = state.copy()

class PharmacyHistory:
    def __init__(self):
        self.history = []

    def save(self, memento):
        self.history.append(memento)

    def restore(self, index):
        return self.history[index]

# ==================== Visitor Pattern ====================
class ReportVisitor(ABC):
    @abstractmethod
    def visit(self, pharmacy):
        pass

class SalesReportVisitor(ReportVisitor):
    def visit(self, pharmacy):
        print(f"Sales Report: Total medicines sold = {pharmacy.medicines_sold}")

# ==================== Pharmacy Core ====================
class Pharmacy:
    def __init__(self):
        self.stock = {"Paracetamol": 10, "Antibiotic": 5}
        self.medicines_sold = 0

    def place_order(self, medicine):
        if self.stock.get(medicine, 0) > 0:
            self.stock[medicine] -= 1
            self.medicines_sold += 1
            print(f"Order placed for {medicine}")
        else:
            print(f"{medicine} is out of stock")

    def refill_stock(self, medicine, qty):
        self.stock[medicine] = self.stock.get(medicine, 0) + qty
        print(f"Stock refilled: {medicine} -> {self.stock[medicine]} units")

    def accept(self, visitor):
        visitor.visit(self)

# ==================== Client Code ====================
def main():
    print("\n=== SmartPharma System (with Mediator) ===")

    # Mediator setup
    mediator = PharmacyMediator()
    pharmacist = Pharmacist(mediator)
    inventory_manager = InventoryManager(mediator)
    payment_processor = PaymentProcessor(mediator)
    notification_service = NotificationService(mediator)

    mediator.register_components(pharmacist, inventory_manager, payment_processor, notification_service)

    # Chain of Responsibility setup
    handler_chain = PharmacistHandler(DoctorHandler(SpecialistHandler()))

    # Create pharmacy system
    pharmacy = Pharmacy()

    # History and visitor
    history = PharmacyHistory()
    visitor = SalesReportVisitor()

    # Prescription handling via Chain
    prescriptions = [
        {"medicine": "Paracetamol", "type": "common"},
        {"medicine": "Antibiotic", "type": "critical"}
    ]

    for p in prescriptions:
        handler_chain.handle_request(p)
        pharmacist.process_prescription(p)

    # Commands
    order = PlaceOrderCommand(pharmacy, "Paracetamol")
    refill = RefillStockCommand(pharmacy, "Antibiotic", 10)

    order.execute()
    refill.execute()

    # Save system state
    history.save(PharmacyMemento(pharmacy.stock))

    # Visitor
    pharmacy.accept(visitor)

if __name__ == "__main__":
    main()

```

---

