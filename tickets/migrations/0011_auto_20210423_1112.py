# Generated by Django 3.2 on 2021-04-23 18:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_auto_20210423_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 23, 18, 12, 42, 378428, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 23, 18, 12, 42, 374427, tzinfo=utc), verbose_name='Created'),
        ),
    ]
