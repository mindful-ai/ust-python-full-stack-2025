from . import views
from django.urls import path

urlpatterns = [
    path('student/add/', views.add_student, name="add_student"),
    path("student/success", views.student_success, name="student_success"),
    path("student/list", views.student_list, name="student_list")
    
]