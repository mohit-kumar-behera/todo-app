# Generated by Django 3.0.7 on 2020-11-27 18:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201128_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='taskTime',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 11, 27, 18, 47, 9, 58177, tzinfo=utc)),
        ),
    ]
