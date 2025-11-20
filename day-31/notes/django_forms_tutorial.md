# Forms

### Create the student app

```sh
python manage.py startapp student
```

### Create the models

```python
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
```

### Create the form

```python
from django import forms
from .models import Student



class ContactAdminForm(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'course']

```
### Write the views

```python

from .models import Student

# Create your views here.

def add_student(request):

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Directly take the data and saves it in a model
            return redirect("student_success")
    else:
        form = StudentForm()

    return render(request, "add_student.html", {"form": form})

def student_success(request):
    return render(request, "success.html")


def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})

```

### Update the templates

```html

<!DOCTYPE html>
<html>
<head>
    <title>Add Student</title>
</head>
<body>

<h2>Add Student</h2>

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save Student</button>
</form>

</body>
</html>

```


```html
<h2>All Students</h2>

<ul>
{% for stud in students %}
    <li>{{ stud.full_name }} — {{ stud.course.name }}</li>
{% endfor %}
</ul>
```

```html

<h3>Student added successfully!</h3>
<a href="/student/add/">Add another</a>

```

### Furnish initial data in the database

```shell
In [2]: from student.models import Course

In [3]: Course.objects.create(name="Python Basics", duration_months=3)
Out[3]: <Course: Python Basics>

In [4]: Course.objects.create(name="Django Basics", duration_months=3)
Out[4]: <Course: Django Basics>

In [5]: Course.objects.create(name="Django Advanced", duration_months=3)
Out[5]: <Course: Django Advanced>

In [6]: exit
```

### Register the URLs

```python
from . import views
from django.urls import path

urlpatterns = [
    path('student/add/', views.add_student, name="add_student"),
    path("student/success", views.student_success, name="student_success"),
    path("student/list", views.student_list, name="student_list")
    
]
```

### Register URLs in the project

```python

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('firstapp.urls')),
    path('', include('student.urls')),
]

```

### Run the server

```sh
python manage.py runserver
```


NOTE: Do not forget to register the student app in INSTALLED_APPS in settings.py
