# Generated by Django 3.0.8 on 2020-07-05 21:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0005_auto_20200706_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 2, 52, 34, 699535)),
        ),
        migrations.AlterField(
            model_name='country',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 2, 52, 34, 696542)),
        ),
        migrations.AlterField(
            model_name='country',
            name='image',
            field=models.ImageField(null=True, upload_to='pics_country'),
        ),
        migrations.AlterField(
            model_name='entertainment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 2, 52, 34, 698538)),
        ),
        migrations.AlterField(
            model_name='foreign',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 2, 52, 34, 697540)),
        ),
        migrations.AlterField(
            model_name='politics',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 2, 52, 34, 701530)),
        ),
        migrations.AlterField(
            model_name='startup',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 2, 52, 34, 700531)),
        ),
        migrations.AlterField(
            model_name='tech',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 6, 2, 52, 34, 698538)),
        ),
    ]
