# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-06 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='adresi'),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='adresi'),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_tr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='adresi'),
        ),
    ]
