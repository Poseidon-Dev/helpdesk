from django.db import models

from core.const import DIVISION_CHOICES
from users.models import User

class Profile(models.Model):
    
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=256,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=256,
        null=True,
        blank=True,
    )
    employee_number = models.IntegerField(
        verbose_name='Employee Number',
        null=True,
        blank=True,
    )
    division = models.IntegerField(
        verbose_name='Division',
        null=False,
        blank=False,
        choices=DIVISION_CHOICES,
        default=98,
    )
    phone = models.CharField(
        verbose_name='Phone',
        max_length=30,
        null=True,
        blank=True,
    )
    extension = models.IntegerField(
        verbose_name='Extension',
        null=True,
        blank=True,
    )

    def get_full_name(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    def get_short_name(self):
        last_as_string = str(self.last_name).capitalize()
        return f'{self.first_name.capitalize()} {last_as_string[:1].capitalize()}'

    def __str__(self):
        return self.get_full_name()