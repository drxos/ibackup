# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-21 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cicanon', '0004_auto_20160916_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_fr',
            field=models.CharField(max_length=250, null=True, verbose_name='Title'),
        ),
    ]
