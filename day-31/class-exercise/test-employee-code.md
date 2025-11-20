### Tasks 

-   Create the three models.

-   Run migrations.

-   Add at least:

    -   2 departments
    -   3 skills
    -   2 employees
    -   Assign skills to employees.

-   Write test cases to verify:

    -   Employees are created correctly
    -   Department relationship works
    -   Skills Many-To-Many relationship works
    -   __str__() method returns readable strings
    -   Filtering employees by department
    -   Filtering employees by skill

```python

from django.test import TestCase
from .models import Department, Skill, Employee


class EmployeeModelTests(TestCase):

    def setUp(self):
        # Departments
        self.dep_it = Department.objects.create(name="IT")
        self.dep_hr = Department.objects.create(name="HR")

        # Skills
        self.skill_python = Skill.objects.create(name="Python")
        self.skill_django = Skill.objects.create(name="Django")
        self.skill_excel = Skill.objects.create(name="Excel")

        # Employees
        self.emp_1 = Employee.objects.create(
            name="Alice",
            age=30,
            department=self.dep_it
        )

        self.emp_2 = Employee.objects.create(
            name="Bob",
            age=25,
            department=self.dep_hr
        )

        # Add skills
        self.emp_1.skills.add(self.skill_python, self.skill_django)
        self.emp_2.skills.add(self.skill_excel)

    # --------------------------------------------------

    def test_department_creation(self):
        self.assertEqual(self.dep_it.name, "IT")
        self.assertEqual(str(self.dep_it), "IT")

    # --------------------------------------------------

    def test_skill_creation(self):
        self.assertEqual(self.skill_python.name, "Python")
        self.assertEqual(str(self.skill_python), "Python")

    # --------------------------------------------------

    def test_employee_creation(self):
        self.assertEqual(self.emp_1.name, "Alice")
        self.assertEqual(self.emp_1.age, 30)
        self.assertEqual(self.emp_1.department.name, "IT")
        self.assertEqual(str(self.emp_1), "Alice")

    # --------------------------------------------------

    def test_employee_skills(self):
        skills = self.emp_1.skills.all()
        self.assertEqual(skills.count(), 2)
        self.assertIn(self.skill_python, skills)
        self.assertIn(self.skill_django, skills)

    # --------------------------------------------------

    def test_filter_by_department(self):
        it_employees = Employee.objects.filter(department=self.dep_it)
        self.assertEqual(it_employees.count(), 1)
        self.assertEqual(it_employees.first().name, "Alice")

    # --------------------------------------------------

    def test_filter_by_skill(self):
        python_devs = Employee.objects.filter(skills__name="Python")
        self.assertEqual(python_devs.count(), 1)
        self.assertEqual(python_devs.first().name, "Alice")


```