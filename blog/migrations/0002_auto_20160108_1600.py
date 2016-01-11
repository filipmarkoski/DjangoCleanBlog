# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 15:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 8, 16, 0, 37, 691499)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]