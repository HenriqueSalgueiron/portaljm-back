from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    country = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
