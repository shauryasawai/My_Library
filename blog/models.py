from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    publisher = models.CharField(max_length=100)
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

