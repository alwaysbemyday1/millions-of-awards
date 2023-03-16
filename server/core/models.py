from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
#    objects = UserManager()
   
   nickname = models.CharField(max_length=25, unique=True)
   email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
   is_active = models.BooleanField(default=True)
   is_admin = models.BooleanField(default=False)

   USERNAME_FIELD = 'nickname'

   def __str__(self):
       return self.nickname

   @property
   def is_staff(self):
       return self.is_admin