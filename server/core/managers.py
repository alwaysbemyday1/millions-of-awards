from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True
   
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('username does not exist')
        if not password:
            raise ValueError('password does not exist')
        
        user = self.model(username=username , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
