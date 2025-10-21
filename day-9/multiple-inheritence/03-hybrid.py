''' This combines hierarchical (one parent → multiple children) and 
multiple (one child ← multiple parents) inheritance. '''

class Person:
    def info(self):
        return "General personal information"

class Teacher(Person):
    def teach(self):
        return "Teaches subjects"

class Student(Person):
    def study(self):
        return "Studies subjects"

class TeachingAssistant(Teacher, Student):
    def assist(self):
        return "Helps the teacher and students"

ta = TeachingAssistant()
print(ta.info())     # From Person
print(ta.teach())    # From Teacher
print(ta.study())    # From Student
print(ta.assist())   # From TeachingAssistant
