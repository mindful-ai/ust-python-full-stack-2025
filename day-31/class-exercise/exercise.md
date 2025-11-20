🎯 Problem Statement

Create three Django models:

1. Department 
    name — CharField(max_length=100)

2. Skill 
    name — CharField(max_length=100)

3. Employee 
    name — CharField(max_length=200)
    age — IntegerField
    department — ForeignKey(Department, on_delete=models.CASCADE)
    skills — ManyToManyField(Skill)

Implement __str__() for all models