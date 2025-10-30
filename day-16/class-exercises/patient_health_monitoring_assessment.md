
# Assessment Problem: Patient Health Monitoring System

## Objective
Design a **Patient Health Monitoring System** that demonstrates the **Memento**, **Observer**, and **Visitor** behavioral design patterns.  
The system should simulate patients' health data being updated in real-time, allow for saving and restoring health history, and generate different kinds of health reports using the Visitor pattern.

---

## Problem Description

### Context
In a hospital’s digital monitoring system, patients’ health data (such as temperature, blood pressure, and heart rate) is updated frequently.  
The system needs to:
1. **Notify** doctors and nurses when the patient’s condition changes (Observer Pattern).
2. **Save** and **restore** snapshots of the patient’s health state (Memento Pattern).
3. **Generate reports** such as a “Summary Report” and a “Detailed Report” (Visitor Pattern).

---

## Requirements

1. **Observer Pattern**  
   - Implement `Subject` and `Observer` classes.  
   - `Patient` acts as the Subject that notifies its observers (Doctor, Nurse) of any health updates.

2. **Memento Pattern**  
   - Implement a `HealthMemento` class that stores the patient’s state.  
   - Implement a `HealthHistory` caretaker class that keeps track of saved health states.  
   - The `Patient` can save and restore its health data.

3. **Visitor Pattern**  
   - Implement a `HealthReportVisitor` interface.  
   - Implement two concrete visitors:
     - `SummaryReportVisitor`
     - `DetailedReportVisitor`  
   - The `Patient` class accepts visitors that generate reports from the health data.

---

## Skeleton Code

```python
# ==================== Observer Pattern ====================
class Observer:
    def update(self, patient):
        pass

class Patient:
    def __init__(self, name):
        self.name = name
        self.health_data = {}
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for obs in self.observers:
            obs.update(self)

    def set_health_data(self, data):
        self.health_data = data
        self.notify()

# ==================== Memento Pattern ====================
class HealthMemento:
    def __init__(self, health_data):
        self.health_data = health_data.copy()

class HealthHistory:
    def __init__(self):
        self._history = []

    def save(self, memento):
        self._history.append(memento)

    def restore(self, index):
        return self._history[index]

# ==================== Visitor Pattern ====================
class HealthReportVisitor:
    def visit(self, patient):
        pass

# ==================== Integration ====================
def main():
    patient = Patient("Anil Kumar")
    doctor = Doctor()
    nurse = Nurse()

    patient.attach(doctor)
    patient.attach(nurse)

    history = HealthHistory()

    # Initial health data
    patient.set_health_data({"temperature": 98.6, "heart_rate": 72, "bp": "120/80"})
    history.save(patient.save_state())

    # Updated health data
    patient.set_health_data({"temperature": 101.2, "heart_rate": 90, "bp": "130/85"})
    history.save(patient.save_state())

    # Generate reports
    summary = SummaryReportVisitor()
    detailed = DetailedReportVisitor()

    patient.accept(summary)
    patient.accept(detailed)

    # Restore previous state
    print("\nRestoring previous health state...")
    patient.restore_state(history.restore(0))
    patient.accept(detailed)


if __name__ == "__main__":
    main()
```

---

