# Generated by Django 3.2 on 2021-04-17 00:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20210416_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 0, 3, 31, 943998, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 17, 0, 3, 31, 943998, tzinfo=utc), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='technician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='technician', to='tickets.users'),
        ),
    ]