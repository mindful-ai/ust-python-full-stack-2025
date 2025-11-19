from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello! Welcome to the Django App")

def greet(request, name):
    return HttpResponse(f"<h3>Hello {name}, Nice to meet you</h3>")

def info_json(request):
    data = { "name": "Purushotham", "age": 40, "status": "Working" }
    return JsonResponse(data)

def index(request):
    return render(request, "child.html")

def calc(request):
    return render(request, "calculator.html")

def show_values(request):
    context = {
        "name": "Rahul", 
        "age": 25,
        "status": False,
        "fruits": ["Apple", "Banana", "Mango", "Orange"],
        "students": ["Anil", "Sunil", "Asha", "Usha"],
        "emp": {
            "name": "Manoj", "dept": "IT", "salary": 50000
        }
    }
    return render(request, "templates.html", context=context)

