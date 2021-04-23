# Generated by Django 3.2 on 2021-04-23 04:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_auto_20210422_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='subcategory',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='tickets.subcategory', verbose_name='Sub Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 23, 4, 20, 10, 14397, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 23, 4, 20, 10, 11394, tzinfo=utc), verbose_name='Created'),
        ),
    ]
