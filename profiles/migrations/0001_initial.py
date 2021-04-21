# Generated by Django 3.2 on 2021-04-20 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Last Name')),
                ('employee_number', models.IntegerField(blank=True, null=True, verbose_name='Employee Number')),
                ('division', models.IntegerField(choices=[(0, '00-Corp'), (1, '01-Tuc'), (2, '02-Phx'), (3, '03-Hes'), (4, '04-Cor'), (5, '05-Vgs'), (6, '06-Pip'), (7, '07-Reno'), (8, '08-Car'), (9, '09-Pac'), (10, '10-Bhc'), (98, 'None'), (99, 'All')], default=98, verbose_name='Division')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Phone')),
                ('extension', models.IntegerField(blank=True, null=True, verbose_name='Extension')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]