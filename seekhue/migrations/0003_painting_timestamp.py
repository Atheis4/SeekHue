# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 17:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekhue', '0002_auto_20160602_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 6, 2, 17, 13, 42, 532993)),
        ),
    ]