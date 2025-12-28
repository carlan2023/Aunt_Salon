from django.db import models
# from django.contrib.auth.models import User  # Using Django's built-in User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES=(
        ('client', 'Client')
        ('hairdresser', 'Hairdresser')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    