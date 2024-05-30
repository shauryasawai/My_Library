from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    heading = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_edited')

    def __str__(self):
        return self.title
