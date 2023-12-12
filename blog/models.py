# blog/models.py

from django.db import models

class Post(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
