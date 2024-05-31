from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class BookReview(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    review = models.TextField()
    image_url = models.URLField()
    rating = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)  # Assuming phone numbers are strings
    address = models.CharField(max_length=100)  # Assuming addresses are strings

    def __str__(self):
        return f"Phone: {self.phone_number}, Address: {self.address}"


from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


    

