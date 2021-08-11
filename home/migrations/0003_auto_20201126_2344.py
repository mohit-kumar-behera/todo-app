# Generated by Django 3.0.7 on 2020-11-26 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_taskcreate_tasktitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcontent',
            name='task_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskcreate',
            name='dateCreated',
            field=models.DateField(auto_now_add=True),
        ),
    ]
