# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import seekhue.models


class Migration(migrations.Migration):

    dependencies = [
        ('seekhue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='seekhue_sort',
            field=models.ImageField(upload_to=seekhue.models.unique_file_name),
        ),
        migrations.AlterField(
            model_name='painting',
            name='source',
            field=models.ImageField(upload_to=seekhue.models.unique_file_name),
        ),
    ]
