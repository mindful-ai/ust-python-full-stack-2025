from django.shortcuts import render, redirect
from .forms import StudentForm, ContactAdminForm, StudentFeedbackForm
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

def feedback_view(request):
    if request.method == "POST":
        form = StudentFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "feedback_success.html", {"data": form.cleaned_data})
    else:
        form = StudentFeedbackForm()

    return render(request, "feedback_form.html", {"form": form})