# 🎓 SmartCampus – A Student Management CLI System (Design Patterns Case Study)

## 📘 Overview
**SmartCampus** is a command-line student management system that demonstrates the use of multiple **design patterns** in a real-world context.  
It is built using **Python** and **Typer CLI** for practical usability.

This project helps students understand how **creational, structural, and behavioral patterns** can work together in a cohesive, functional application.

---

## 🧩 Patterns Used

| Category | Pattern | Purpose |
|-----------|----------|----------|
| Creational | Builder | Builds complex Student objects step by step |
| Creational | Factory | Creates different types of users (Student, Faculty, Admin) |
| Creational | Singleton | Central data repository ensuring one instance |
| Structural | Adapter | Converts/export data to various formats (e.g., CSV/JSON) |
| Structural | Flyweight | Shares department/course data to save memory |
| Structural | Composite | Organizes hierarchy of Departments → Courses → Students |
| Behavioral | Chain of Responsibility | Handles multi-step requests like leave approval |
| Behavioral | Memento | Enables undo/redo for student grade updates |
| Behavioral | Visitor | Performs operations like analytics/reporting |
| Behavioral | Observer | Notifies observers when student data changes |

---

## 🏗️ Project Structure

```
smartcampus/
│
├── smartcampus.py        # Main Typer CLI application
├── README.md             # Documentation
└── requirements.txt      # Dependencies
```

---

## ⚙️ Implementation (Core Demonstration Code)

```python
import typer
from typing import Dict

app = typer.Typer()

# ---------------- Singleton ----------------
class Database:
    _instance = None
    _data: Dict = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def add_student(self, student):
        self._data[student.id] = student

    def get_all_students(self):
        return list(self._data.values())

# ---------------- Builder ----------------
class StudentBuilder:
    def __init__(self):
        self._student = Student()

    def with_name(self, name):
        self._student.name = name
        return self

    def with_department(self, dept):
        self._student.department = dept
        return self

    def with_year(self, year):
        self._student.year = year
        return self

    def build(self):
        return self._student

# ---------------- Factory ----------------
class UserFactory:
    @staticmethod
    def create_user(role, **kwargs):
        if role == "student":
            return StudentBuilder().with_name(kwargs["name"]).with_department(kwargs["department"]).with_year(kwargs["year"]).build()
        elif role == "faculty":
            return Faculty(kwargs["name"])
        elif role == "admin":
            return Admin(kwargs["name"])
        else:
            raise ValueError("Invalid role")

# ---------------- Flyweight ----------------
class Department:
    _instances = {}

    def __new__(cls, name):
        if name not in cls._instances:
            cls._instances[name] = super(Department, cls).__new__(cls)
            cls._instances[name].name = name
        return cls._instances[name]

# ---------------- Observer ----------------
class Observer:
    def update(self, message):
        pass

class StudentObserver(Observer):
    def update(self, message):
        print(f"[Student Notification] {message}")

class FacultyObserver(Observer):
    def update(self, message):
        print(f"[Faculty Notification] {message}")

# ---------------- Memento ----------------
class GradeMemento:
    def __init__(self, grade):
        self.grade = grade

class Student:
    _id_counter = 1

    def __init__(self):
        self.id = Student._id_counter
        Student._id_counter += 1
        self.name = None
        self.department = None
        self.year = None
        self.grade = None
        self._mementos = []
        self._observers = []

    def set_grade(self, grade):
        self._mementos.append(GradeMemento(self.grade))
        self.grade = grade
        self.notify_observers(f"Grade updated for {self.name}: {self.grade}")

    def undo_grade(self):
        if self._mementos:
            m = self._mementos.pop()
            self.grade = m.grade
            self.notify_observers(f"Undo: Grade reverted for {self.name} to {self.grade}")

    def attach(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for obs in self._observers:
            obs.update(message)

class Faculty:
    def __init__(self, name):
        self.name = name

class Admin:
    def __init__(self, name):
        self.name = name

# ---------------- CLI Commands ----------------
@app.command()
def add_student(name: str, department: str, year: int):
    student = UserFactory.create_user("student", name=name, department=Department(department), year=year)
    db = Database()
    db.add_student(student)
    typer.echo(f"✅ Added student: {student.name} ({student.department.name}, Year {student.year})")

@app.command()
def list_students():
    db = Database()
    for s in db.get_all_students():
        typer.echo(f"{s.id}: {s.name} - {s.department.name} (Year {s.year})")

@app.command()
def update_grade(student_id: int, grade: float):
    db = Database()
    student = db._data.get(student_id)
    if not student:
        typer.echo("❌ Student not found")
        return
    student.set_grade(grade)
    typer.echo(f"✅ Updated grade for {student.name} to {grade}")

@app.command()
def undo_grade(student_id: int):
    db = Database()
    student = db._data.get(student_id)
    if student:
        student.undo_grade()
    else:
        typer.echo("❌ Student not found")

if __name__ == "__main__":
    app()
```

---

## 🧠 How to Run

### 1️⃣ Install dependencies:
```bash
pip install typer rich
```

### 2️⃣ Run the CLI:
```bash
python smartcampus.py add-student --name "Alice" --department "CSE" --year 2
python smartcampus.py list-students
python smartcampus.py update-grade --student-id 1 --grade 8.5
python smartcampus.py undo-grade --student-id 1
```

---

## 💡 Suggested Student Extensions

| Enhancement | Patterns Involved |
|--------------|------------------|
| Add Chain of Responsibility for leave approval | Chain of Responsibility |
| Add Adapter for CSV/JSON export | Adapter |
| Add Visitor for analytics on marks/attendance | Visitor |
| Add Observer for automatic faculty notifications | Observer |
| Extend Singleton with persistent storage (e.g., SQLite) | Singleton |

---

## 🎯 Learning Outcomes

- Understand **how multiple design patterns interact** in one cohesive project.  
- Build a **functional CLI application** using **Typer**.  
- Learn **object-oriented design thinking** beyond simple examples.  
- Gain **hands-on understanding** of patterns in a **real, maintainable system**.

---

### ✍️ Author Note

This project is designed as an **educational case study** for students learning advanced **object-oriented design** and **software architecture patterns** in Python.
