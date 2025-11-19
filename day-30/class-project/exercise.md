Django Templating – Assessment Problem

Overview

This assessment focuses on practicing basic Django templating features:

Variables
if / else conditions
for loops
Template inheritance (extends)

You will create a simple student dashboard using these features.

Context

You are developing a small student dashboard page for a college website

The dashboard should display:

    Student information
    Their enrollment status
    List of their enrolled courses

The page must be rendered using Django templates with inheritance.

Task Description

1️⃣ Create a Django App

    Create a new Django app named:

    studentdash

2️⃣ Pass Data From the View

    In views.py, pass the following student dictionary as context:

    {
    "name": "Rahul Sharma",
    "active": True,
    "courses": ["Mathematics", "Physics", "Computer Science"]
    }

3️⃣ Create Templates

    a. base.html

    Create a base template that contains:
    A main heading (e.g., College Dashboard)

    A block named:
    {% block content %}{% endblock %}

    This block will be filled by other templates.

    b. dashboard.html

    This template must:
    Extend base.html
    Display the student’s name using a variable
    Use an if/else block to show the student’s status:

    If active is True → "Status: Active Student"
    Otherwise → "Status: Inactive Student"

    Use a for loop to display each course in an unordered list

4️⃣ Expected Output

    College Dashboard
    -----------------

    Student Name: Rahul Sharma
    Status: Active Student

    Enrolled Courses:
    • Mathematics
    • Physics
    • Computer Science

