# ----------------------------
# SMART AUTO MANUFACTURING AND MONITORING SYSTEM (SAMMS)
# Demonstration of multiple Design Patterns in one project
# Patterns Used: Builder, Factory, Singleton, Adapter, Flyweight,
# Composite, Chain of Responsibility, Memento, Visitor, Observer
# ----------------------------

# ====== IMPORT SECTION (from previous modules or same file) ======

# Singleton
class ConfigManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.default_color = "White"
            cls.__instance.max_cars = 100
            print("[ConfigManager] Initialized global configuration.")
        return cls.__instance


# Builder + Product
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


# Factory
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


# Flyweight
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


# Composite
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


# Adapter
class LegacySensor:
    def old_reading(self):
        return "Old temperature sensor data"


class LegacySensorAdapter:
    def __init__(self, legacy_sensor):
        self.legacy_sensor = legacy_sensor

    def get_reading(self):
        return f"Adapted: {self.legacy_sensor.old_reading()}"


# Chain of Responsibility
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


# Memento
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


# Visitor
class Visitor:
    def visit(self, component):
        pass


class CostCalculatorVisitor(Visitor):
    def visit(self, component):
        print(f"[Visitor] Calculating cost for component: {component.name}")


# Observer
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


# ---------------------------
# CLIENT CODE
# ---------------------------

if __name__ == "__main__":
    print("=== SMART AUTO MANUFACTURING AND MONITORING SYSTEM ===\n")

    # 1. Singleton - Global Config
    config = ConfigManager()
    print(f"Default Color: {config.default_color}\n")

    # 2. Factory + Builder - Create a car
    factory = CarFactory()
    car = factory.create_car("Electric")
    print(f"Car Built: {car}\n")

    # 3. Composite + Flyweight - Car Structure
    car_body = CompositeComponent("Car Body")
    part_factory = PartFactory()
    wheel = part_factory.get_part("Wheel")
    seat = part_factory.get_part("Seat")

    car_body.add(LeafComponent(wheel.name))
    car_body.add(LeafComponent(seat.name))
    car_body.add(LeafComponent("Dashboard"))
    print("\n[Composite] Car Structure:")
    car_body.display()

    # 4. Adapter - Integrate Legacy Sensor
    legacy_sensor = LegacySensor()
    adapted_sensor = LegacySensorAdapter(legacy_sensor)
    print(f"\n[Adapter] Sensor Output: {adapted_sensor.get_reading()}")

    # 5. Chain of Responsibility - Quality Checks
    qc_chain = PaintCheck(EngineCheck(SafetyCheck()))
    print("\n[Chain of Responsibility] Quality Check Process:")
    qc_chain.handle(car)

    # 6. Memento - Save and Restore Car Design
    designer = CarDesigner()
    designer.design(car)
    saved = designer.save()
    print(f"\n[Memento] Saved design: {saved.state}")
    # modify and then restore
    car.color = "Green"
    designer.design(car)
    print(f"[Memento] Modified design: {designer.state}")
    designer.restore(saved)

    # 7. Visitor - Cost Calculation
    visitor = CostCalculatorVisitor()
    print("\n[Visitor] Cost Calculation:")
    for component in car_body.children:
        visitor.visit(component)

    # 8. Observer - Monitoring System
    observable_car = ObservableCar()
    dashboard = Dashboard()
    observable_car.attach(dashboard)
    print("\n[Observer] Simulating Sensor Update:")
    observable_car.notify("Battery temperature exceeded threshold.")

    print("\n=== End of Demonstration ===")



