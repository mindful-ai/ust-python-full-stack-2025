'''
When two parent classes inherit from the same grandparent class, 
and a child inherits from both of those parents — we get a diamond shape of inheritance.
This raises ambiguity/race conditions -> which is later resolved by python using MRO
'''

class Person:
    def __init__(self):
        print("Person initialized")

class Mother(Person):
    def __init__(self):
        super().__init__()
        print("Mother initialized")

class Father(Person):
    def __init__(self):
        super().__init__()
        print("Father initialized")

class Child(Mother, Father):
    def __init__(self):
        super().__init__()
        print("Child initialized")

child = Child()
