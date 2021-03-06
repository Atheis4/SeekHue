# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ImageField(upload_to='')),
                ('seekhue_sort', models.ImageField(upload_to='')),
                ('artist', models.CharField(default='', max_length=80)),
                ('title', models.CharField(default='', max_length=80)),
                ('year', models.CharField(default='', max_length=4)),
                ('data', models.TextField(default='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
