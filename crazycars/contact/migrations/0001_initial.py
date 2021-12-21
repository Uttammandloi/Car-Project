# Generated by Django 3.2.9 on 2021-12-17 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('car_id', models.IntegerField()),
                ('customer_need', models.CharField(max_length=300)),
                ('car_title', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('messege', models.TextField(blank=True)),
                ('user_id', models.CharField(blank=True, max_length=300)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]