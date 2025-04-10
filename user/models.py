from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('is_admin', default=False)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)