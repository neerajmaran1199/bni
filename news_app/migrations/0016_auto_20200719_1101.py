# Generated by Django 2.2.2 on 2020-07-19 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0015_auto_20200719_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 19, 11, 1, 50, 393029)),
        ),
    ]