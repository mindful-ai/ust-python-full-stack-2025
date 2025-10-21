'''
Here, multiple inheritance is combined with multilevel inheritance —
a child inherits from a parent, which itself inherits from multiple parents.

'''

class Person:
    def get_personal_info(self):
        return "Name, Age, Address"

class Employee:
    def get_employee_info(self):
        return "Employee ID, Department"

class SoftwareEngineer(Person, Employee):
    def get_skillset(self):
        return "Python, SQL, ML"

class TeamLead(SoftwareEngineer):
    def get_role(self):
        return "Managing software team"

lead = TeamLead()
print(lead.get_personal_info())  # From Person
print(lead.get_employee_info())  # From Employee
print(lead.get_skillset())       # From SoftwareEngineer
print(lead.get_role())           # From TeamLead
