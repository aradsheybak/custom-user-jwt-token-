import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """Create new user profile"""
        if not username:
            raise ValueError("Username can not be null")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(username=username, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    MALE = "Male"
    FEMALE = "Female"
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, "Female")
    ]

    first_name = models.CharField(max_length=25, default="", blank=True, null=True, )
    last_name = models.CharField(max_length=25, default="", blank=True, null=True)
    username = models.CharField(max_length=25, default="", unique=True)
    mobile = models.CharField(max_length=25, blank=True, null=True, default="")
    email = models.EmailField(max_length=254, blank=True, null=True, unique=True)
    gender = models.CharField(max_length=6, blank=True, null=True, choices=GENDER, default=MALE)
    birthday = models.DateField(default=datetime.date.today, blank=True, null=True)
    avatar = models.ImageField(upload_to='images', default='')
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
