''' A child class inherits attributes and methods from two or more parent classes. '''
class Teacher:
    def teach(self):
        return "Teaching students"

class Researcher:
    def research(self):
        return "Conducting research"

class Professor(Teacher, Researcher):
    def guide_students(self):
        return "Guiding students in research"

# Usage
prof = Professor()
print(prof.teach())        # Teaching students
print(prof.research())     # Conducting research
print(prof.guide_students())  # Guiding students in research
