from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUser(AbstractUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission'
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/')


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class BookReview(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    review = models.TextField()
    image_url = models.URLField()
    rating = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.title



class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    



    

