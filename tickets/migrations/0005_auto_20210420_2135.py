# Generated by Django 3.2 on 2021-04-21 04:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20210420_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='division',
            field=models.CharField(default='None', max_length=100, verbose_name='Division'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 4, 35, 1, 263196, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 21, 4, 35, 1, 263196, tzinfo=utc), verbose_name='Created'),
        ),
    ]
