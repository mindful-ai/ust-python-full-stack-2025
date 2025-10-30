
# 🚗 Smart Auto Manufacturing and Monitoring System (SAMMS)

## 🎯 Objective
Design a simulation system for a **Smart Automobile Manufacturing and Monitoring System (SAMMS)** that models the design, production, configuration, and monitoring of cars using multiple design patterns.  
Students will explore how different design patterns interact to form a scalable, maintainable, and extendable software architecture.

---

## 🏭 System Overview
The SAMMS system aims to:
1. Build cars of different models and configurations.
2. Manage parts and their reuse efficiently.
3. Support dynamic addition of sensors and behavior tracking.
4. Allow for undo operations in design.
5. Support flexible chain-based quality checks.
6. Enable runtime notifications for monitoring changes.

---

## ⚙️ Design Patterns Used

| Module | Design Pattern | Purpose |
|---------|----------------|----------|
| Car Builder | **Builder** | Construct cars with varying specifications (engine type, body style, color, etc.) step by step. |
| Car Factory | **Factory Method / Abstract Factory** | Create different families of cars (Electric, Petrol, Hybrid). |
| Configuration Manager | **Singleton** | Manage global configurations like production capacity, default colors, etc. |
| Sensor Integration | **Adapter** | Make third-party or legacy sensors compatible with the internal system. |
| Shared Parts | **Flyweight** | Efficiently manage repeated use of identical components like tires, seats, or mirrors. |
| Car Hierarchy | **Composite** | Represent cars as compositions of parts and sub-parts (Car → Engine → Components). |
| Quality Check Chain | **Chain of Responsibility** | Pass each car through a sequence of quality checks (paint, electronics, safety). |
| Car Design History | **Memento** | Store and restore previous car configurations (undo/redo). |
| Diagnostic and Reporting | **Visitor** | Perform operations like performance reporting or cost calculation without modifying car classes. |
| Monitoring System | **Observer** | Notify monitoring dashboards whenever car or sensor states change. |

---

## 🧩 High-Level Architecture

```
             ┌──────────────────────────────┐
             │  Singleton: ConfigManager     │
             └────────────┬─────────────────┘
                          │
                          ▼
        ┌──────────────────────────────────────────────┐
        │ Factory + Builder: CarFactory & CarBuilder   │
        └──────────────────────────────────────────────┘
                          │
                          ▼
        ┌──────────────────────────────────────────────┐
        │ Composite: Car → Subsystems → Components     │
        └──────────────────────────────────────────────┘
           │              │                │
           ▼              ▼                ▼
   (Flyweight)      (Adapter)        (Observer)
   Shared Parts   Third-party Sensor   Monitor
           │              │                │
           └──────────────┴────────────────┘
                          │
                    Chain of Responsibility
                          │
                          ▼
                       Memento
                          │
                          ▼
                       Visitor
```

---

## 🧠 Detailed Python Implementation

### 1️⃣ Singleton — `ConfigManager`
```python
class ConfigManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.default_color = "White"
            cls.__instance.max_cars = 100
            print("[ConfigManager] Initialized global configuration.")
        return cls.__instance
```

### 2️⃣ Builder — `CarBuilder`
```python
class Car:
    def __init__(self):
        self.engine = None
        self.color = None
        self.body_style = None

    def __str__(self):
        return f"Car(engine={self.engine}, color={self.color}, body={self.body_style})"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_body_style(self, style):
        self.car.body_style = style
        return self

    def build(self):
        return self.car
```

### 3️⃣ Factory — `CarFactory`
```python
class CarFactory:
    def create_car(self, type):
        builder = CarBuilder()
        if type == "Electric":
            return builder.set_engine("EV Motor").set_color("Blue").set_body_style("Hatchback").build()
        elif type == "Petrol":
            return builder.set_engine("V8 Engine").set_color("Red").set_body_style("Sedan").build()
        elif type == "Hybrid":
            return builder.set_engine("Hybrid Engine").set_color("Silver").set_body_style("SUV").build()
        else:
            raise ValueError("Unknown car type!")
```

### 4️⃣ Flyweight — `PartFactory`
```python
class CarPart:
    def __init__(self, name):
        self.name = name


class PartFactory:
    _parts = {}

    def get_part(self, name):
        if name not in self._parts:
            print(f"[Flyweight] Creating new shared part: {name}")
            self._parts[name] = CarPart(name)
        else:
            print(f"[Flyweight] Reusing existing part: {name}")
        return self._parts[name]
```

### 5️⃣ Composite — `CarComponent`
```python
class CarComponent:
    def display(self, indent=0):
        pass


class LeafComponent(CarComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(" " * indent + f"- {self.name}")


class CompositeComponent(CarComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self, indent=0):
        print(" " * indent + f"+ {self.name}")
        for child in self.children:
            child.display(indent + 2)
```

### 6️⃣ Adapter — `LegacySensorAdapter`
```python
class LegacySensor:
    def old_reading(self):
        return "Old temperature sensor data"


class LegacySensorAdapter:
    def __init__(self, legacy_sensor):
        self.legacy_sensor = legacy_sensor

    def get_reading(self):
        return f"Adapted: {self.legacy_sensor.old_reading()}"
```

### 7️⃣ Chain of Responsibility — `QualityCheckHandler`
```python
class QualityCheckHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, car):
        if self.successor:
            self.successor.handle(car)


class PaintCheck(QualityCheckHandler):
    def handle(self, car):
        print(f"[QC] Paint check passed for {car.color} car.")
        super().handle(car)


class EngineCheck(QualityCheckHandler):
    def handle(self, car):
        print(f"[QC] Engine check passed for {car.engine}.")
        super().handle(car)


class SafetyCheck(QualityCheckHandler):
    def handle(self, car):
        print(f"[QC] Safety check passed for {car.body_style}.")
        super().handle(car)
```

### 8️⃣ Memento — `CarDesigner`
```python
class CarMemento:
    def __init__(self, state):
        self.state = state


class CarDesigner:
    def __init__(self):
        self.state = None

    def design(self, car):
        self.state = str(car)

    def save(self):
        return CarMemento(self.state)

    def restore(self, memento):
        self.state = memento.state
        print(f"[Memento] Restored design: {self.state}")
```

### 9️⃣ Visitor — `CostCalculatorVisitor`
```python
class Visitor:
    def visit(self, component):
        pass


class CostCalculatorVisitor(Visitor):
    def visit(self, component):
        print(f"[Visitor] Calculating cost for component: {component.name}")
```

### 🔟 Observer — `ObservableCar`
```python
class ObservableCar:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, event):
        for o in self._observers:
            o.update(event)


class Dashboard:
    def update(self, event):
        print(f"[Observer] Dashboard notified: {event}")
```

---

## 🧪 Client Driver — `main.py`

```python
if __name__ == "__main__":
    print("=== SMART AUTO MANUFACTURING AND MONITORING SYSTEM ===\n")

    config = ConfigManager()
    print(f"Default Color: {config.default_color}\n")

    factory = CarFactory()
    car = factory.create_car("Electric")
    print(f"Car Built: {car}\n")

    car_body = CompositeComponent("Car Body")
    part_factory = PartFactory()
    wheel = part_factory.get_part("Wheel")
    seat = part_factory.get_part("Seat")

    car_body.add(LeafComponent(wheel.name))
    car_body.add(LeafComponent(seat.name))
    car_body.add(LeafComponent("Dashboard"))
    print("\n[Composite] Car Structure:")
    car_body.display()

    legacy_sensor = LegacySensor()
    adapted_sensor = LegacySensorAdapter(legacy_sensor)
    print(f"\n[Adapter] Sensor Output: {adapted_sensor.get_reading()}")

    qc_chain = PaintCheck(EngineCheck(SafetyCheck()))
    print("\n[Chain of Responsibility] Quality Check Process:")
    qc_chain.handle(car)

    designer = CarDesigner()
    designer.design(car)
    saved = designer.save()
    print(f"\n[Memento] Saved design: {saved.state}")
    car.color = "Green"
    designer.design(car)
    print(f"[Memento] Modified design: {designer.state}")
    designer.restore(saved)

    visitor = CostCalculatorVisitor()
    print("\n[Visitor] Cost Calculation:")
    for component in car_body.children:
        visitor.visit(component)

    observable_car = ObservableCar()
    dashboard = Dashboard()
    observable_car.attach(dashboard)
    print("\n[Observer] Simulating Sensor Update:")
    observable_car.notify("Battery temperature exceeded threshold.")

    print("\n=== End of Demonstration ===")
```

---

## 🧩 Learning Outcomes
Students will understand:
- How multiple design patterns can work together.
- How patterns improve maintainability and extensibility.
- Real-world application of design principles in automotive domain.
