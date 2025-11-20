from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    duration_months = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

class StudentFeedback(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    satisfaction = models.IntegerField()  # slider input
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    enrolled = models.BooleanField(default=False)  # checkbox
    join_date = models.DateField()
    course = models.CharField(max_length=100)
    comments = models.TextField()

    def __str__(self):
        return self.name