# Generated by Django 3.0.8 on 2020-07-05 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_auto_20200706_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 1, 50, 55, 660987)),
        ),
        migrations.AlterField(
            model_name='country',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 1, 50, 55, 657996)),
        ),
        migrations.AlterField(
            model_name='entertainment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 1, 50, 55, 659990)),
        ),
        migrations.AlterField(
            model_name='foreign',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 1, 50, 55, 658996)),
        ),
        migrations.AlterField(
            model_name='politics',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 1, 50, 55, 662982)),
        ),
        migrations.AlterField(
            model_name='startup',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 1, 50, 55, 661987)),
        ),
        migrations.AlterField(
            model_name='tech',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 1, 50, 55, 659990)),
        ),
    ]