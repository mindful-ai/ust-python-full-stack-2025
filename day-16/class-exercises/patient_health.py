# ==============================
# PATIENT HEALTH TRACKER SYSTEM
# ==============================

# ---- Memento Pattern ----
class HealthMemento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Patient:
    def __init__(self, name):
        self.name = name
        self.heart_rate = 0
        self.bp = 0
        self.temperature = 0
        self.observers = []
        self.history = []

    # Observer pattern
    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for obs in self.observers:
            obs.update(self)

    # Set vitals and trigger observer updates
    def set_vitals(self, heart_rate, bp, temperature):
        self.heart_rate = heart_rate
        self.bp = bp
        self.temperature = temperature
        print(f"\n🩺 Updated vitals for {self.name}: HR={heart_rate}, BP={bp}, Temp={temperature}")
        self.notify()

    # Memento pattern
    def save_state(self):
        memento = HealthMemento((self.heart_rate, self.bp, self.temperature))
        self.history.append(memento)
        print("💾 State saved.")

    def restore_state(self, memento):
        self.heart_rate, self.bp, self.temperature = memento.get_state()
        print(f"🔄 Restored vitals: HR={self.heart_rate}, BP={self.bp}, Temp={self.temperature}")

    # Visitor accept method
    def accept(self, visitor):
        visitor.visit(self)


# ---- Observer Pattern ----
class Observer:
    def update(self, patient):
        pass


class Doctor(Observer):
    def update(self, patient):
        if patient.heart_rate > 120 or patient.temperature > 102:
            print(f"🚨 Doctor Alert: {patient.name} has critical vitals!")


class Nurse(Observer):
    def update(self, patient):
        if patient.bp > 140:
            print(f"⚠️ Nurse Alert: {patient.name} has high BP!")


# ---- Visitor Pattern ----
class Visitor:
    def visit(self, patient):
        pass


class ReportGenerator(Visitor):
    def __init__(self):
        self.records = []

    def visit(self, patient):
        data = (patient.name, patient.heart_rate, patient.bp, patient.temperature)
        self.records.append(data)

    def generate_report(self):
        print("\n📊 Health Report Summary:")
        for name, hr, bp, temp in self.records:
            print(f"- {name}: HR={hr}, BP={bp}, Temp={temp}")


# ---- Demonstration ----
if __name__ == "__main__":
    # Create patient
    p1 = Patient("Anil Kumar")

    # Attach observers
    doctor = Doctor()
    nurse = Nurse()
    p1.attach(doctor)
    p1.attach(nurse)

    # Set vitals and save state
    p1.set_vitals(90, 120, 98.6)
    p1.save_state()

    # New vitals (critical)
    p1.set_vitals(130, 150, 103)

    # Restore to safe state
    if p1.history:
        p1.restore_state(p1.history[-1])

    # Visitor pattern - reporting
    report = ReportGenerator()
    p1.accept(report)
    report.generate_report()
