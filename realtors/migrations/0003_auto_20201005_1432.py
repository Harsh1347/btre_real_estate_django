# Generated by Django 3.1.1 on 2020-10-05 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20201005_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime.now),
        ),
    ]
