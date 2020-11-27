from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    keycloack_id = models.CharField(max_length=100)

