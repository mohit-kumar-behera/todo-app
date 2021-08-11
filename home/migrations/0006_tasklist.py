# Generated by Django 3.0.7 on 2020-11-27 18:37

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_taskcreate'),
    ]

    operations = [
        migrations.CreateModel(
            name='taskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskDescription', models.TextField()),
                ('taskTime', models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 27, 18, 37, 59, 600038, tzinfo=utc))),
                ('isComplete', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.taskCreate')),
            ],
        ),
    ]
