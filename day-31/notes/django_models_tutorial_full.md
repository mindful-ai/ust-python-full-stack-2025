
# Django Models & Testing — Complete Tutorial

## Table of Contents
- [Overview of Django Models](#overview-of-django-models)
- [Creating a Model](#creating-a-model)
- [Running Migrations](#running-migrations)
- [Using the ORM](#using-the-orm)
- [Model Relationships](#model-relationships)
- [Model Methods](#model-methods)
- [Testing Django Models](#testing-django-models)
- [Validation & Queryset Tests](#validation--queryset-tests)
- [Student Model System — Demonstrating Relationships](#student-model-system--demonstrating-relationships)
- [Sample Tests for Student Models](#sample-tests-for-student-models)

---

# Overview of Django Models
Django models define the structure of your data and act as the single source of truth.  
They provide:
- Automatic migration generation  
- A powerful Object-Relational Mapper (ORM)  
- Built-in validation  
- Support for complex relationships  

A model is simply a Python class that subclasses `django.db.models.Model`.

---

# Creating a Model

## 1. Create an App
```bash
python manage.py startapp blog
```

## 2. Add App to settings.py
```python
INSTALLED_APPS = [
    ...,
    'blog',
]
```

## 3. Define a Model
`blog/models.py`
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_published(self):
        return self.published
```

---

# Running Migrations

## Generate migration files
```bash
python manage.py makemigrations
```

## Apply migrations
```bash
python manage.py migrate
```

---

# Using the ORM

## Creating Objects
```python
from blog.models import Post
p1 = Post.objects.create(
    title="First Post",
    content="Welcome!",
    published=True
)
```

## Querying
```python
Post.objects.all()
Post.objects.filter(published=True)
Post.objects.get(id=1)
```

## Updating
```python
p1.title = "Updated Title"
p1.save()
```

## Deleting
```python
p1.delete()
```

---

# Model Relationships

## One-to-Many (ForeignKey)
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

## One-to-One (OneToOneField)
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
```

## Many-to-Many
```python
class Tag(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    tags = models.ManyToManyField(Tag)
```

---

# Model Methods
Model methods help you include business logic inside the model.

Example:
```python
def is_published(self):
    return self.published
```

---

# Testing Django Models

Create `tests.py` inside your app.

```python
from django.test import TestCase
from blog.models import Post

class PostModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            published=True
        )

    def test_post_created(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertTrue(self.post.published)

    def test_str_method(self):
        self.assertEqual(str(self.post), "Test Post")

    def test_is_published(self):
        self.assertTrue(self.post.is_published())
```

---

# Validation & Queryset Tests

## Testing validation
```python
def test_title_max_length(self):
    post = Post(title='A' * 300)
    with self.assertRaises(Exception):
        post.full_clean()
```

## Testing querysets
```python
def test_published_filter(self):
    Post.objects.create(title="Draft", content="abc", published=False)
    p = Post.objects.filter(published=True)
    self.assertEqual(p.count(), 1)
```

---

# Student Model System — Demonstrating Relationships

A complete Student system with:
- One-to-One (Student ↔ Profile)
- One-to-Many (Department → Students)
- Many-to-Many (Student ↔ Course)

---

# Department Model (One-to-Many)
```python
class Department(models.Model):
    name = models.CharField(max_length=100)
    building = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
```

---

# Student Model (Central Entity)
```python
class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return f"{self.roll_no} - {self.name}"
```

---

# Profile Model (One-to-One)
```python
class Profile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"Profile of {self.student.name}"
```

---

# Course Model (Many-to-Many)
```python
class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(
        Student,
        related_name='courses',
        blank=True
    )

    def __str__(self):
        return f"{self.code} - {self.title}"
```

---

# Sample Tests for Student Models

```python
from django.test import TestCase
from .models import Student, Profile, Course, Department

class StudentRelationshipsTest(TestCase):

    def setUp(self):
        self.dept = Department.objects.create(name="Computer Science")

        self.student = Student.objects.create(
            roll_no="CS101",
            name="Alice",
            age=20,
            department=self.dept
        )

        self.profile = Profile.objects.create(
            student=self.student,
            address="123 Street",
            phone="9876543210"
        )

        self.course = Course.objects.create(code="CS50", title="Intro to CS")
        self.course.students.add(self.student)

    def test_department_relationship(self):
        self.assertEqual(self.student.department.name, "Computer Science")
        self.assertIn(self.student, self.dept.students.all())

    def test_profile_relationship(self):
        self.assertEqual(self.student.profile.phone, "9876543210")

    def test_course_relationship(self):
        self.assertIn(self.student, self.course.students.all())
        self.assertIn(self.course, self.student.courses.all())
```

---

# End of Document
