# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-29 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_slider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('-id',), 'verbose_name': 'Menu', 'verbose_name_plural': 'Menuler'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ('-id',), 'verbose_name': 'Kaydırıcı', 'verbose_name_plural': 'Kaydırıcılar'},
        ),
        migrations.AddField(
            model_name='news',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Arka plan resmi'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='status',
            field=models.BooleanField(default=True, verbose_name='durumu'),
        ),
    ]
