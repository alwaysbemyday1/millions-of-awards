from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True
   
    def create_user(self, nickname, password, **extra_fields):
        if not nickname:
            raise ValueError('nickname does not exist')
        if not password:
            raise ValueError('password does not exist')
        
        email = self.normalize_email(email)
        user = self.model(nickname=nickname ,email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email = self.normalize_email(email), password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
   objects = UserManager()
   
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