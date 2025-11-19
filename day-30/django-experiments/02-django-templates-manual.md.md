# Django Templates Tutorial (Part 1, Part 2, Part 3)

## Part 1 --- Basics

### Variables

``` html
<p>Hello, {{ name }}</p>
```

### If-Else

``` html
{% if age >= 18 %}
<p>Adult</p>
{% else %}
<p>Minor</p>
{% endif %}
```

### Loops

``` html
<ul>
{% for item in items %}
<li>{{ item }}</li>
{% endfor %}
</ul>
```

------------------------------------------------------------------------

## Part 2 --- Intermediate Topics

### Static Files

``` html
{% load static %}
<link rel="stylesheet" href="{% static 'styles.css' %}">
```

### URL Tag

``` html
<a href="{% url 'hello-url' %}">Go</a>
```

### Custom Filters

``` python
@register.filter
def double(value):
    return value * 2
```

Usage:

``` html
{{ number|double }}
```

### Forms

``` html
<form method="POST">
{% csrf_token %}
{{ form }}
</form>
```

### ORM + Templates

``` html
{% for book in books %}
{{ book.title }} - {{ book.price }}
{% endfor %}
```

------------------------------------------------------------------------

## Part 3 --- Professional Concepts

### Context Processors

``` python
def global_settings(req):
    return {"company": "Mindful AI"}
```

### Base Templates (Modular)

``` html
{% extends "base.html" %}
{% block content %}
Hello
{% endblock %}
```

### JSON Rendering

``` html
{{ data|json_script:"chartdata" }}
```

### Using Jinja2 with Django

Configured through a separate Jinja environment in settings.

### Debugging Templates

Use:

    {% debug %}

Check missing variables and unmatched tags.
