# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-29 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20160929_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='adı'),
        ),
        migrations.AddField(
            model_name='teams',
            name='name_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='adı'),
        ),
        migrations.AddField(
            model_name='teams',
            name='name_tr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='adı'),
        ),
        migrations.AddField(
            model_name='teams',
            name='text_en',
            field=models.TextField(blank=True, null=True, verbose_name='alıntı'),
        ),
        migrations.AddField(
            model_name='teams',
            name='text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='alıntı'),
        ),
        migrations.AddField(
            model_name='teams',
            name='text_tr',
            field=models.TextField(blank=True, null=True, verbose_name='alıntı'),
        ),
    ]