from students import Student
import csv
from operator import methodcaller, attrgetter


# Read the contents 


student_data = []

with open("students.csv", "r") as csvdata:  # context manager
    pass
    

# Create a list of student objects
students = []
for data in student_data:
    temp = Student(data['name'], data['regid'], data['age'])
    temp.set_marks(phy=data['phy'], chem=data['chem'], bio=data['bio'], math=data['math'])
    students.append(temp)

print(type(students[0])) # output if __repr__ not defined-> <class 'students.Student'>
print(students[0]) # output if __str__ not defined -> <students.Student object at 0x000002076AE82F30>

# Calculate average and rank

# Use methodcaller, attrgetter to calculate averages
# Use comprehensions for the sake of practicing

print(avgs, ranks)


# Write data to the report

with open('studentreport-oop.csv', 'w', newline='') as csvfile:
    pass
    