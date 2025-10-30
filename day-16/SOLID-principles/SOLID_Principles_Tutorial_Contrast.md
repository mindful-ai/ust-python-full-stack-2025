
# 🧱 SOLID Principles Tutorial — Correct vs Wrong Implementations

This tutorial explains each of the **SOLID design principles** with **wrong and corrected examples** in Python.  
Each section contains:
- A **violation example (❌ Wrong)**  
- A **corrected version (✅ Correct)**  
- A **key takeaway**

---

## 1️⃣ Single Responsibility Principle (SRP)

**Definition:** A class should have only one reason to change.

---

### ❌ Wrong Example

```python
class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        print("Generating report:", self.data)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.data)
        print("Report saved!")
```

👉 Here, the class **generates** and **saves** the report — two responsibilities.

---

### ✅ Correct Example

```python
class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report: {self.data}"


class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, 'w') as f:
            f.write(report)
        print("Report saved successfully!")
```

👉 Each class now has **one reason to change** — one for report logic, another for persistence.

---

## 2️⃣ Open/Closed Principle (OCP)

**Definition:** Software entities should be open for extension but closed for modification.

---

### ❌ Wrong Example

```python
class DiscountCalculator:
    def calculate(self, customer_type, amount):
        if customer_type == "Regular":
            return amount * 0.9
        elif customer_type == "Premium":
            return amount * 0.8
```

👉 Adding a new customer type requires modifying existing code — violating OCP.

---

### ✅ Correct Example

```python
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, amount):
        pass


class RegularDiscount(Discount):
    def apply(self, amount):
        return amount * 0.9


class PremiumDiscount(Discount):
    def apply(self, amount):
        return amount * 0.8


class SuperPremiumDiscount(Discount):
    def apply(self, amount):
        return amount * 0.7
```

👉 You can now **extend** new discount types without changing the base logic.

---

## 3️⃣ Liskov Substitution Principle (LSP)

**Definition:** Subclasses should be substitutable for their base classes.

---

### ❌ Wrong Example

```python
class Bird:
    def fly(self):
        print("I can fly!")


class Ostrich(Bird):
    def fly(self):
        raise Exception("I cannot fly!")
```

👉 `Ostrich` breaks the contract of the `Bird` class — not substitutable.

---

### ✅ Correct Example

```python
class Bird:
    def move(self):
        print("I can move!")


class FlyingBird(Bird):
    def fly(self):
        print("I can fly!")


class Ostrich(Bird):
    def walk(self):
        print("I can walk!")
```

👉 Each subclass behaves **according to expectations** — no broken contracts.

---

## 4️⃣ Interface Segregation Principle (ISP)

**Definition:** Clients should not be forced to depend on interfaces they do not use.

---

### ❌ Wrong Example

```python
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Robot(Worker):
    def work(self):
        print("Robot working...")

    def eat(self):
        raise Exception("Robots do not eat!")
```

👉 The `Robot` class is forced to implement an unnecessary method.

---

### ✅ Correct Example

```python
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Human(Workable, Eatable):
    def work(self):
        print("Human working...")

    def eat(self):
        print("Human eating...")


class Robot(Workable):
    def work(self):
        print("Robot working...")
```

👉 Interfaces are now **segregated** based on what each client actually needs.

---

## 5️⃣ Dependency Inversion Principle (DIP)

**Definition:** High-level modules should not depend on low-level modules; both should depend on abstractions.

---

### ❌ Wrong Example

```python
class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL database")


class Application:
    def __init__(self):
        self.db = MySQLDatabase()

    def start(self):
        self.db.connect()
```

👉 The high-level `Application` depends directly on a **concrete** database — not flexible.

---

### ✅ Correct Example

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL database")


class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL database")


class Application:
    def __init__(self, db: Database):
        self.db = db

    def start(self):
        self.db.connect()
```

👉 The `Application` now depends on an **abstraction** (`Database`) — easily switch databases.

---

## 🧩 Summary

| Principle | Problem Solved | Key Idea |
|------------|----------------|-----------|
| **SRP** | Too many responsibilities | One reason to change |
| **OCP** | Hard to extend | Extend, don’t modify |
| **LSP** | Broken inheritance | Respect contracts |
| **ISP** | Bloated interfaces | Split interfaces |
| **DIP** | Tight coupling | Depend on abstractions |

---

## ✅ Final Takeaway

Following **SOLID principles** leads to:
- Clean, modular, testable code  
- Easier maintenance and extension  
- Lower coupling and higher cohesion
