# Generated by Django 3.1.2 on 2020-11-27 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20201127_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='time',
        ),
        migrations.AlterField(
            model_name='activity',
            name='Date_of_event',
            field=models.DateTimeField(),
        ),
    ]
