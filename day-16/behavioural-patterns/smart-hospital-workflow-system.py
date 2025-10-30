# ------------------------------
# 1. Chain of Responsibility - Patient routing
# ------------------------------
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, patient):
        if self._successor:
            self._successor.handle(patient)


class TriageHandler(Handler):
    def handle(self, patient):
        if patient["severity"] < 5:
            print(f"Triage: {patient['name']} sent to General Physician.")
        else:
            print(f"Triage: {patient['name']} needs specialist.")
            super().handle(patient)


class DoctorHandler(Handler):
    def handle(self, patient):
        if patient["condition"] == "heart":
            print(f"Doctor: {patient['name']} sent to Cardiologist.")
        elif patient["condition"] == "bone":
            print(f"Doctor: {patient['name']} sent to Orthopedic.")
        else:
            print(f"Doctor: {patient['name']} under observation.")

# ------------------------------
# 2. Command + Memento - Medical actions
# ------------------------------
class Memento:
    def __init__(self, state):
        self.state = state


class PatientRecord:
    def __init__(self, name):
        self.name = name
        self.history = []

    def set_diagnosis(self, diagnosis):
        self.history.append(diagnosis)

    def save(self):
        return Memento(self.history.copy())

    def restore(self, memento):
        self.history = memento.state


class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class PrescribeMedicineCommand(Command):
    def __init__(self, record, medicine):
        self.record = record
        self.medicine = medicine

    def execute(self):
        self.record.set_diagnosis(f"Prescribed {self.medicine}")
        print(f"Medicine prescribed: {self.medicine}")

    def undo(self):
        if self.record.history:
            print(f"Undoing last prescription: {self.medicine}")
            self.record.history.pop()

# ------------------------------
# 3. Mediator - Department Coordination
# ------------------------------
class Mediator:
    def notify(self, sender, event):
        pass


class HospitalMediator(Mediator):
    def __init__(self):
        self.doctor = None
        self.pharmacy = None
        self.billing = None

    def notify(self, sender, event):
        if event == "prescription_ready":
            print("Mediator: Informing Pharmacy and Billing...")
            self.pharmacy.receive_prescription(sender)
            self.billing.generate_bill(sender)


class Doctor:
    def __init__(self, mediator):
        self.mediator = mediator

    def prescribe(self, patient):
        print(f"Doctor prescribing medicine to {patient['name']}")
        self.mediator.notify(self, "prescription_ready")


class Pharmacy:
    def receive_prescription(self, doctor):
        print("Pharmacy: Prescription received.")


class Billing:
    def generate_bill(self, doctor):
        print("Billing: Bill generated.")

# ------------------------------
# 4. Observer - Notification System
# ------------------------------
class Observer:
    def update(self, patient_status):
        pass


class Relative(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, patient_status):
        print(f"Relative {self.name} notified: Patient status - {patient_status}")


class PatientMonitor:
    def __init__(self):
        self.observers = []
        self.status = None

    def attach(self, obs):
        self.observers.append(obs)

    def change_status(self, status):
        self.status = status
        for obs in self.observers:
            obs.update(status)

# ------------------------------
# 5. Visitor - Reports and Analytics
# ------------------------------
class HospitalElement:
    def accept(self, visitor):
        pass


class Patient(HospitalElement):
    def __init__(self, name, bills):
        self.name = name
        self.bills = bills

    def accept(self, visitor):
        visitor.visit_patient(self)


class ReportVisitor:
    def visit_patient(self, patient):
        print(f"Generating report for {patient.name}. Total bills: {sum(patient.bills)}")
        
# ------------------------------
# 🚀 Demonstration
# ------------------------------
if __name__ == "__main__":
    print("\n--- Chain of Responsibility ---")
    chain = TriageHandler(DoctorHandler())
    chain.handle({"name": "John", "severity": 6, "condition": "heart"})

    print("\n--- Command + Memento ---")
    record = PatientRecord("John")
    cmd = PrescribeMedicineCommand(record, "Aspirin")
    cmd.execute()
    backup = record.save()
    cmd.undo()
    record.restore(backup)
    print("Restored record:", record.history)

    print("\n--- Mediator ---")
    mediator = HospitalMediator()
    doctor = Doctor(mediator)
    pharmacy = Pharmacy()
    billing = Billing()
    mediator.doctor, mediator.pharmacy, mediator.billing = doctor, pharmacy, billing
    doctor.prescribe({"name": "John"})

    print("\n--- Observer ---")
    monitor = PatientMonitor()
    monitor.attach(Relative("Alice"))
    monitor.attach(Relative("Bob"))
    monitor.change_status("Discharged")

    print("\n--- Visitor ---")
    patient = Patient("John", [1200, 800, 500])
    visitor = ReportVisitor()
    patient.accept(visitor)