# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-16 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cicanon', '0003_auto_20160916_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug_en',
            field=models.SlugField(null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug_fr',
            field=models.SlugField(null=True, unique=True, verbose_name='Slug'),
        ),
    ]
