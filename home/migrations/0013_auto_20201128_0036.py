# Generated by Django 3.0.7 on 2020-11-27 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20201128_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='taskTime',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 11, 27, 19, 6, 18, 808646, tzinfo=utc)),
        ),
    ]
