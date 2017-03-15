# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-15 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0019_auto_20170315_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='marital_status',
            field=models.IntegerField(choices=[('', 'Choose your marital status'), (0, 'Single'), (1, 'Maried')], default=0, null=True, verbose_name='Marital Status'),
        ),
    ]
