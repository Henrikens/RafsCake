from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
