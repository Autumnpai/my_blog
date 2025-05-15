from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """Represent the overall blog."""
    text = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Post(models.Model):
    """An individual blog post."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a simple string representing the post."""
        return f"{self.text[:50]}..."