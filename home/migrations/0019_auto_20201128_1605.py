# Generated by Django 3.0.7 on 2020-11-28 10:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20201128_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcreate',
            name='taskDate',
            field=models.DateField(auto_now_add=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='taskTime',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 11, 28, 10, 35, 3, 907552, tzinfo=utc)),
        ),
    ]
