from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(
        verbose_name='Username',
        max_length=254,
        unique=True,
    )
    date_joined = models.DateTimeField(
        verbose_name='Date Created',
        auto_now_add=True
    )
    last_login = models.DateTimeField(
        verbose_name='Last Login',
        auto_now=True,
    )
    is_admin = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.profile.get_short_name()
