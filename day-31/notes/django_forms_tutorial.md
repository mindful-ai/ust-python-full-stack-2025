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

### Analysing the forms request and it's body

```python

def contact_admin(request):
    if request.method == "POST":
        form = ContactAdminForm(request.POST)
        if form.is_valid():

            # Extract submitted values
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            # Print to console/log
            print("Request: ", request.POST)
            print("Body: ", form)
            print("Subject:", subject)
            print("Message:", message)
            print("Email:", email)

            return render(request, "contact_success.html", {
                "subject": subject,
                "message": message,
                "email": email
            })

    else:
        form = ContactAdminForm()

    return render(request, "contact_form.html", {"form": form})

```

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Admin</title>
</head>
<body>

<h2>Contact Admin Form</h2>

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}

    <button type="submit">Send</button>
</form>

</body>
</html>

```

You still need to:
- Create the contact_success html template
- URL update

### Navigating between pages

```html
<a href="{% url 'add_student' %}"><button>Send Another Message</button></a>
```


```html
<a href="{% url 'contact_admin' %}"><button>Contact Admin</button></a>

```

-   In add_student

```html
<a href="{% url 'calc' %}"><button>Use Calculator</button></a>
```


### Experimenting with different widgets

```python

from django.db import models

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

```

```python

from django import forms
from .models import StudentFeedback

class StudentFeedbackForm(forms.ModelForm):
    class Meta:
        model = StudentFeedback
        fields = [
            'name', 'email', 'age', 'satisfaction', 'gender',
            'enrolled', 'join_date', 'course', 'comments'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'age': forms.NumberInput(attrs={'min': 10, 'max': 100}),
            'satisfaction': forms.NumberInput(attrs={'type': 'range', 'min': 1, 'max': 10}),
            'gender': forms.RadioSelect(),
            'enrolled': forms.CheckboxInput(),
            'join_date': forms.DateInput(attrs={'type': 'date'}),
            'course': forms.TextInput(attrs={'placeholder': 'Your course name'}),
            'comments': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Any feedback…'}),
        }

```

```python

from django.shortcuts import render
from .forms import StudentFeedbackForm

def feedback_view(request):
    if request.method == "POST":
        form = StudentFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "feedback_success.html", {"data": form.cleaned_data})
    else:
        form = StudentFeedbackForm()

    return render(request, "feedback_form.html", {"form": form})

```

```html

<!DOCTYPE html>
<html>
<head>
    <title>Student Feedback Form</title>
</head>
<body>

<h2>Student Feedback Form</h2>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
    </table>

    <button type="submit">Submit Feedback</button>
</form>

</body>
</html>


```

```html

<!DOCTYPE html>
<html>
<head>
    <title>Feedback Submitted</title>
</head>
<body>

<h2>Thank you! Your feedback has been saved.</h2>

<h3>Submitted Data:</h3>
<ul>
    <li><strong>Name:</strong> {{ data.name }}</li>
    <li><strong>Email:</strong> {{ data.email }}</li>
    <li><strong>Age:</strong> {{ data.age }}</li>
    <li><strong>Satisfaction:</strong> {{ data.satisfaction }}</li>
    <li><strong>Gender:</strong> {{ data.gender }}</li>
    <li><strong>Enrolled:</strong> {{ data.enrolled }}</li>
    <li><strong>Join Date:</strong> {{ data.join_date }}</li>
    <li><strong>Course:</strong> {{ data.course }}</li>
    <li><strong>Comments:</strong> {{ data.comments }}</li>
</ul>

<a href="{% url 'feedback_form' %}">
    <button>Submit Another Response</button>
</a>

</body>
</html>

```

```python

from django.urls import path
from .views import feedback_view

urlpatterns = [
    path('feedback/', feedback_view, name='feedback_form'),
]

```

```python

from django.contrib import admin
from .models import StudentFeedback

admin.site.register(StudentFeedback)

```