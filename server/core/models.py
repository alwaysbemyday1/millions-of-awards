from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=25, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin