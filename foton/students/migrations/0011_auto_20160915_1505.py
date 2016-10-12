# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-15 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20160915_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sponsor_address',
            field=models.CharField(default=1, help_text='Sponsor or guardian Permanent Address', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sponsor_email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Sponsor or Guardian Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sponsor_full_name',
            field=models.CharField(default=1, help_text='Sponsor or guardian full name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sponsor_occupation',
            field=models.CharField(default=1, max_length=150, verbose_name='Occupation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sponsor_phone',
            field=models.CharField(default=1, max_length=50, verbose_name='Sponsor or Guardian Telphone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sponsor_relationship',
            field=models.CharField(default=1, help_text='Relation to Applicant', max_length=50),
            preserve_default=False,
        ),
    ]
