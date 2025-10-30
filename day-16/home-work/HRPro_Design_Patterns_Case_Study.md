# 🧩 Case Study Project: HRPro+ — Intelligent Employee Management Platform

## 🎯 Goal
To design and develop an **Employee Management System (EMS)** that handles employee creation, payroll processing, performance reviews, leave approvals, notifications, and report generation — using **multiple design patterns cohesively** to produce a scalable, maintainable, and extensible system.

---

## 🏢 Context & Usefulness

Modern HR departments handle diverse processes:
- Employee onboarding/offboarding  
- Salary and benefits computation  
- Performance tracking and appraisals  
- Leave and attendance approvals  
- Notifications and analytics reports  

**HRPro+** aims to be a **modular HR system** that automates and unifies these workflows with clean design and extensibility — ideal for both educational and practical enterprise use.

---

## 🧠 Patterns Involved and Their Purpose

| Pattern | Purpose in the System | Example Use |
|----------|----------------------|--------------|
| **Builder** | Create complex `Employee` objects step-by-step | Build employee profile with optional details (address, department, salary plan, etc.) |
| **Factory Method / Abstract Factory** | Centralized creation of different employee types | Create `FullTimeEmployee`, `PartTimeEmployee`, `Intern`, etc. |
| **Singleton** | Maintain one shared system configuration or database connection | Singleton `HRDatabase` or `ConfigManager` |
| **Adapter** | Integrate third-party payroll or notification services | Adapts `ExternalPayrollAPI` or `SlackNotifier` |
| **Flyweight** | Optimize memory for shared intrinsic data | Share role metadata or department details across many employees |
| **Composite** | Represent organizational hierarchy | A `Department` containing `Employees` and sub-departments |
| **Chain of Responsibility** | Leave or reimbursement approval flow | Request goes from Manager → HR → Director until approved |
| **Memento** | Save and restore employee state | Snapshot of employee record before salary revision |
| **Visitor** | Add operations without modifying structures | Generate reports or analytics across employee tree |
| **Observer** | Notify modules of important events | Notify Payroll/Analytics when a new employee is added |

---

## 🧩 High-Level Architecture

```
┌──────────────────────────┐
│       HRPro+ System      │
├──────────────────────────┤
│ - EmployeeBuilder        │ ← Builder
│ - EmployeeFactory        │ ← Factory
│ - HRDatabase (Singleton) │ ← Singleton
│ - PayrollAdapter         │ ← Adapter
│ - RoleFlyweightFactory   │ ← Flyweight
│ - Department (Composite) │ ← Composite
│ - LeaveApprovalChain     │ ← Chain of Responsibility
│ - EmployeeMemento        │ ← Memento
│ - ReportVisitor          │ ← Visitor
│ - EventNotifier          │ ← Observer
└──────────────────────────┘
```

---

## 🧱 Core Classes and Pattern Implementation Summary

### 1. **Employee Creation (Builder + Factory)**

```python
class EmployeeBuilder:
    def __init__(self):
        self.emp = Employee()

    def set_name(self, name):
        self.emp.name = name
        return self

    def set_role(self, role):
        self.emp.role = role
        return self

    def set_salary(self, salary):
        self.emp.salary = salary
        return self

    def build(self):
        return self.emp


class EmployeeFactory:
    @staticmethod
    def create_employee(emp_type, name):
        builder = EmployeeBuilder().set_name(name)
        if emp_type == "fulltime":
            return builder.set_role("Full-Time").set_salary(50000).build()
        elif emp_type == "intern":
            return builder.set_role("Intern").set_salary(10000).build()
        else:
            return builder.set_role("Contract").set_salary(30000).build()
```

---

### 2. **System Configuration (Singleton)**

```python
class ConfigManager:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.settings = {"currency": "INR", "timezone": "IST"}
        return cls._instance
```

---

### 3. **External Integration (Adapter)**

```python
class ExternalPayrollAPI:
    def make_payment(self, emp_id, amount):
        print(f"Paid {amount} to employee #{emp_id} via ExternalPayrollAPI")

class PayrollAdapter:
    def __init__(self, external_api):
        self.external_api = external_api

    def process_salary(self, employee):
        self.external_api.make_payment(employee.id, employee.salary)
```

---

### 4. **Memory Optimization (Flyweight)**

```python
class RoleFlyweight:
    def __init__(self, title, benefits):
        self.title = title
        self.benefits = benefits

class RoleFactory:
    _roles = {}

    @staticmethod
    def get_role(title, benefits):
        key = (title, tuple(benefits))
        if key not in RoleFactory._roles:
            RoleFactory._roles[key] = RoleFlyweight(title, benefits)
        return RoleFactory._roles[key]
```

---

### 5. **Organization Hierarchy (Composite)**

```python
class OrgComponent:
    def show_details(self):
        pass

class EmployeeLeaf(OrgComponent):
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def show_details(self):
        print(f"{self.name} - {self.role}")

class DepartmentComposite(OrgComponent):
    def __init__(self, name):
        self.name = name
        self.children = []
    def add(self, component):
        self.children.append(component)
    def show_details(self):
        print(f"Department: {self.name}")
        for child in self.children:
            child.show_details()
```

---

### 6. **Approval Flow (Chain of Responsibility)**

```python
class Approver:
    def __init__(self, next_approver=None):
        self.next = next_approver
    def approve(self, request):
        pass

class Manager(Approver):
    def approve(self, request):
        if request.amount < 10000:
            print("Manager approved the request")
        elif self.next:
            self.next.approve(request)

class HRHead(Approver):
    def approve(self, request):
        if request.amount < 50000:
            print("HR Head approved the request")
        elif self.next:
            self.next.approve(request)
```

---

### 7. **State Backup (Memento)**

```python
class EmployeeMemento:
    def __init__(self, state):
        self.state = state

class Employee:
    def __init__(self):
        self.name = ""
        self.salary = 0
        self.role = ""

    def save(self):
        return EmployeeMemento(self.__dict__.copy())

    def restore(self, memento):
        self.__dict__ = memento.state
```

---

### 8. **Report Generation (Visitor)**

```python
class ReportVisitor:
    def visit_employee(self, employee):
        print(f"Employee Report: {employee.name}, {employee.role}")

    def visit_department(self, department):
        print(f"Department Report: {department.name}")
```

---

### 9. **Event Notification (Observer)**

```python
class EventNotifier:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, observer):
        self.subscribers.append(observer)
    def notify(self, event):
        for obs in self.subscribers:
            obs.update(event)

class PayrollSystem:
    def update(self, event):
        print(f"PayrollSystem received event: {event}")
```

---

## 🧪 Client Code (Integration Example)

```python
if __name__ == "__main__":
    config = ConfigManager()
    print(config.settings)

    emp1 = EmployeeFactory.create_employee("fulltime", "Alice")
    emp2 = EmployeeFactory.create_employee("intern", "Bob")

    notifier = EventNotifier()
    notifier.subscribe(PayrollSystem())
    notifier.notify(f"New employee added: {emp1.name}")

    payroll = PayrollAdapter(ExternalPayrollAPI())
    payroll.process_salary(emp1)

    dev_dept = DepartmentComposite("Development")
    dev_dept.add(EmployeeLeaf(emp1.name, emp1.role))
    dev_dept.add(EmployeeLeaf(emp2.name, emp2.role))
    dev_dept.show_details()

    approval_chain = Manager(HRHead())
    class Request: amount = 20000
    approval_chain.approve(Request())

    snapshot = emp1.save()
    emp1.salary = 70000
    emp1.restore(snapshot)

    visitor = ReportVisitor()
    visitor.visit_employee(emp1)
    visitor.visit_department(dev_dept)
```

---

## 🧾 Outcome
✅ Teaches **10 design patterns in one cohesive real application**  
✅ Realistic HR domain: meaningful for business use  
✅ Reusable and extendable architecture  
✅ Students can visualize why each pattern exists  
✅ Easy to expand with GUI, database, or web layer
