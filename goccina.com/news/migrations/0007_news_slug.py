# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-23 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20160924_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Slug'),
        ),
    ]
