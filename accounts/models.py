
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('renter', 'Renter'),
        ('owner', 'House Owner'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
