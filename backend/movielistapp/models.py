from django.db import models


class Movie(models.Model):
    """
    Model to store movie data
    """
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    likes = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
