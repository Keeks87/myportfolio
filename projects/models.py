# projects/models.py

# Import models
from django.db import models


class Project(models.Model):
    """Model representing a project."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
