# Generated by Django 3.0.7 on 2020-11-29 18:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20201128_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='taskTime',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 11, 29, 18, 38, 55, 158967, tzinfo=utc), null=True),
        ),
    ]
