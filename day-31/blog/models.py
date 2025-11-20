
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    

'''

>python manage.py shell
9 objects imported automatically (use -v 2 for details).

Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.28.0 -- An enhanced Interactive Python. Type '?' for help.
Ctrl click to launch VS Code Native REPL

In [1]: from blog.models import Post, Tag, Author

In [2]: a1 = Author.objects.create(name="Anil Kumar")

In [3]: a2 = Author.objects.create(name="Sunil Kumar")

In [4]: t1 = Tag.objects.create(name="Django")

In [5]: t2 = Tag.objects.create(name="Python")

In [6]: t3 = Tag.objects.create(name="Webdev")

In [7]: Author.objects.all()
Out[7]: <QuerySet [<Author: Anil Kumar>, <Author: Sunil Kumar>]>

In [8]: Tag.objects.all()
Out[8]: <QuerySet [<Tag: Django>, <Tag: Python>, <Tag: Webdev>]>

In [9]: p1 = Post.objects.create(author=a1, title="Setting up the Django project", content="Beginner Django project")

In [10]: p1.tags.add(t1, t2, t3)

In [11]: Post.objects.all()
Out[11]: <QuerySet [<Post: First Post - Revised>, <Post: Setting up the Django project>]>

In [12]: Post.objects.filter(tags=t1)
Out[12]: <QuerySet [<Post: Setting up the Django project>]>

In [13]: exit


'''
