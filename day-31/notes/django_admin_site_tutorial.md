### Creating the superuser

```sh
python manage.py createsuperuser
```

### Register the models in the admin site

student/admin.py

```python

from django.contrib import admin
from .models import Student, Course

# Register your models here.

admin.site.register(Student)
admin.site.register(Course)

```

### Open the admin panel


```sh
python manage.py runserver
```

```sh
http://127.0.0.1:8000/admin
```

### Modify the models

-   Courses
-   Students