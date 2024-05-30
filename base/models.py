from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)  # Assuming phone numbers are strings
    address = models.CharField(max_length=100)  # Assuming addresses are strings

    def __str__(self):
        return f"Phone: {self.phone_number}, Address: {self.address}"


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, default="default_username")
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('agent', 'Agent'),
        ('guest', 'Guest'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=15, null=True)  # Assuming phone numbers are strings
    address = models.CharField(max_length=100, null=True)  # Assuming addresses are strings
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='permissions',
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
    )

from django.db import models

    

