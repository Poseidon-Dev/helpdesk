# Generated by Django 3.2 on 2021-04-16 22:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20210416_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 16, 22, 30, 22, 126541, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 16, 22, 30, 22, 126541, tzinfo=utc), verbose_name='Created'),
        ),
    ]