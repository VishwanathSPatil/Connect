# Generated by Django 3.1.2 on 2020-11-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_auto_20201103_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='gender',
            field=models.CharField(default='M', max_length=1),
        ),
    ]
