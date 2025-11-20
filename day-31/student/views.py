from django.shortcuts import render, redirect
from .forms import StudentForm, ContactAdminForm
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
