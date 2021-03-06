# Generated by Django 3.2 on 2021-04-23 04:10

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20210422_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='subcategory',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 23, 4, 10, 41, 792355, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 23, 4, 10, 41, 789354, tzinfo=utc), verbose_name='Created'),
        ),
    ]
