from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class MajorCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name_en = models.CharField(max_length=25)
    name_ko = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.name_en} / {self.name_ko}"
    
    class Meta:
        verbose_name_plural = 'MajorCategories'

class MinorCategory(models.Model):
    id = models.AutoField(primary_key=True)
    major_category = models.ForeignKey(MajorCategory, on_delete=models.CASCADE)
    name_en = models.CharField(max_length=25)
    name_ko = models.CharField(max_length=25)
    
    def __str__(self):
        return f"({self.major_category.name_ko}) {self.name_en} / {self.name_ko}"
    
    class Meta:
        verbose_name_plural = 'MinorCategories'

class Awards(models.Model):
    major_category = models.ForeignKey(MajorCategory, on_delete=models.PROTECT, related_name='awards')
    minor_category = models.ForeignKey(MinorCategory, on_delete=models.PROTECT, related_name='awards')
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=25, blank=True)
    awarded_for = models.CharField(max_length=255, blank=True)
    presented_by = models.CharField(max_length=255, blank=True)
    first_awarded = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=700, blank=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    trophy = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Awards'

class Ceremony(models.Model):
    awards = models.ForeignKey(Awards, on_delete=models.CASCADE, related_name='ceremony')
    index = models.IntegerField()
    date_started = models.DateTimeField(blank=True, null=True)
    date_finished = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)
    site = models.CharField(max_length=50, blank=True)
    hosted_by = models.CharField(max_length=50, blank=True)
    produced_by = models.CharField(max_length=50, blank=True)
    directed_by = models.CharField(max_length=50, blank=True)
    logo_image = models.ImageField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Ceremonies'

class Nominee(models.Model):
    ceremony = models.ForeignKey(Ceremony, on_delete=models.CASCADE, related_name='nominee')
    name = models.CharField(max_length=50, blank=True)
    work = models.CharField(max_length=50, blank=True)
    work_awarded = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    year_worked = models.IntegerField(blank=True, null=True)
    year_ceremony = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name_plural = 'Nominees'

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