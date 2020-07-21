# Generated by Django 2.2.2 on 2020-07-15 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0006_auto_20200706_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics_sports')),
                ('heading', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('date_time', models.DateTimeField(default=datetime.datetime(2020, 7, 15, 22, 45, 55, 600828))),
            ],
        ),
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics_trending')),
                ('heading', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('date_time', models.DateTimeField(default=datetime.datetime(2020, 7, 15, 22, 45, 55, 600828))),
            ],
        ),
        migrations.AlterField(
            model_name='business',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 22, 45, 55, 600828)),
        ),
        migrations.AlterField(
            model_name='business',
            name='image',
            field=models.ImageField(upload_to='pics_business'),
        ),
        migrations.AlterField(
            model_name='country',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 22, 45, 55, 600828)),
        ),
        migrations.AlterField(
            model_name='entertainment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 22, 45, 55, 600828)),
        ),
        migrations.AlterField(
            model_name='entertainment',
            name='image',
            field=models.ImageField(upload_to='pics_entertainment'),
        ),
        migrations.AlterField(
            model_name='foreign',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 22, 45, 55, 600828)),
        ),
        migrations.AlterField(
            model_name='foreign',
            name='image',
            field=models.ImageField(upload_to='pics_foregn'),
        ),
        migrations.AlterField(
            model_name='politics',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 22, 45, 55, 600828)),
        ),
        migrations.AlterField(
            model_name='politics',
            name='image',
            field=models.ImageField(upload_to='pics_politics'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 22, 45, 55, 600828)),
        ),
        migrations.AlterField(
            model_name='startup',
            name='image',
            field=models.ImageField(upload_to='pics_startup'),
        ),
        migrations.AlterField(
            model_name='tech',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 22, 45, 55, 600828)),
        ),
        migrations.AlterField(
            model_name='tech',
            name='image',
            field=models.ImageField(upload_to='pics_tech'),
        ),
    ]
