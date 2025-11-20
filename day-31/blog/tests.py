from django.test import TestCase
from blog.models import Post, Tag, Author

# Create your tests here.

class BlogModelTests(TestCase):

    def setUp(self):
        # Create Authors
        self.author1 = Author.objects.create(name="John Doe")
        self.author2 = Author.objects.create(name="Mary Smith")

        # Create Tags
        self.tag1 = Tag.objects.create(name="django")
        self.tag2 = Tag.objects.create(name="python")

        # Create Posts
        self.post1 = Post.objects.create(
            author=self.author1,
            title="My First Django Post",
            content="Learning Django testing."
        )

        self.post2 = Post.objects.create(
            author=self.author2,
            title="Advanced Python Tricks",
            content="Generators, decorators, metaclasses."
        )

        # Add tags to posts (M2M)
        self.post1.tags.add(self.tag1, self.tag2)
        self.post2.tags.add(self.tag2)

    # -----------------------------------------------------

    def test_author_creation(self):
        self.assertEqual(self.author1.name, "John Doe")
        self.assertEqual(str(self.author1), "John Doe")

    # -----------------------------------------------------

    def test_tag_creation(self):
        self.assertEqual(self.tag1.name, "django")
        self.assertEqual(str(self.tag1), "django")

    # -----------------------------------------------------

    def test_post_creation(self):
        self.assertEqual(self.post1.title, "My First Django Post")
        self.assertEqual(str(self.post1), "My First Django Post")
        self.assertEqual(self.post1.author.name, "John Doe")

    # -----------------------------------------------------

    def test_post_tags(self):
        tags = self.post1.tags.all()
        self.assertEqual(tags.count(), 2)
        self.assertIn(self.tag1, tags)
        self.assertIn(self.tag2, tags)

    # -----------------------------------------------------

    def test_filter_posts_by_author(self):
        posts = Post.objects.filter(author=self.author1)
        self.assertEqual(posts.count(), 1)
        self.assertEqual(posts.first().title, "My First Django Post")

    # -----------------------------------------------------

    def test_filter_posts_by_tag(self):
        django_posts = Post.objects.filter(tags__name="django")
        python_posts = Post.objects.filter(tags__name="python")

        self.assertEqual(django_posts.count(), 1)
        self.assertEqual(python_posts.count(), 2)