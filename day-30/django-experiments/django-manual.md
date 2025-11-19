# Django Project Setup

### Installation

pip install Django==5.2.8

### Check Installation

django-admin --version

### Creating a project

```bash
mkdir webprojects
cd webprojects
django-admin startproject firstproject
```

### Create an app

Django project consists of various apps focusses on providing specific features

Be inside the project folder and give the following command:
Note manage.py should be visible when you list the folder

python manage.py startapp firstapp

###  Register the app into the project

Edit webprojects\firstproject\firstproject\settings.py

Add "firstapp" into INSTALLED_APPS

### Create a simple view

Update the webprojects\firstproject\firstapp\views.py

```python
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
```

### Map the URLS (app)

webprojects\firstproject\firstapp\urls.py

```python
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('greet/<str:name>/', views.greet, name="greet"),
    path('info/', views.info_json, name="info_json")
]
```

### Add the app URLs to the project URLs

webprojects\firstproject\firstproject\urls.py

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('firstapp.urls'))
]
```

### Run the server

python manage.py runserver

----

# Static and HTML files

### Create a static/ in firstapp

C:\mindful-ai\ust-global-python-fs\webprojects\firstproject\firstapp\static

Add a styles.css

```css
.test{
    background-color: aquamarine;
    color:brown;
}
```

### Update settings.py

webprojects\firstproject\firstproject\settings.py

```python

import os.path

...

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "firstapp/static")
]

```

### Creating HTML content for an app

Create a folder called templates in your app
webprojects\firstproject\firstapp\templates

Add some content into it:

```html
 <h1 class="test">Welcome to Django App!</h1>
```

Add: 

```html
<link rel="stylesheet" href="../static/styles.css"> 
```

Django automatically loads templates/ inside each app.

### Serve the HTML content

Inside: webprojects\firstproject\firstapp

Write the view in views.py
```python
def index(request):
    return render(request, "index.html")
```

Update paths in urls.py
```python
path('page/', views.index, name="index")
```

The page should be available on: 
```sh
http://127.0.0.1:8000/page/
```

# Workflow

To add a HTML file

-   Add a html file to templates/
-   Update views.py

-   Update urls.py
