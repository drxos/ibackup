# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-15 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0020_auto_20170315_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Birth Date (required)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_venue',
            field=models.CharField(max_length=100, verbose_name='Place of Birth (required)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.IntegerField(choices=[('', 'Choose your gender'), (0, 'Female'), (1, 'Male')], verbose_name='Gender (required) '),
        ),
        migrations.AlterField(
            model_name='student',
            name='marital_status',
            field=models.IntegerField(choices=[('', 'Choose your marital status'), (0, 'Single'), (1, 'Maried')], default=0, null=True, verbose_name='Marital Status (required)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='national_Id',
            field=models.CharField(blank=True, max_length=50, verbose_name='National ID (optional)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='origin',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='Nationality (required)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsor_address',
            field=models.CharField(blank=True, help_text='Sponsor or Guardian Permanent Address', max_length=50, verbose_name='Sponsor or Guardian Address (required)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsor_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Sponsor or Guardian Email (required)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsor_full_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Sponsor or guardian full name (required)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsor_occupation',
            field=models.CharField(blank=True, max_length=150, verbose_name='Occupation (required)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsor_phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Sponsor or Guardian Telphone (required)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsor_relationship',
            field=models.CharField(blank=True, help_text='Relation to Applicant', max_length=50, verbose_name='Relationship with Sponsor or Guardian (required)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_type',
            field=models.IntegerField(choices=[('', 'Choose your type'), (0, 'Regular Student'), (1, 'Allianza Student')], default=1, verbose_name='Type (required)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Year', verbose_name='Academic Year (required)'),
        ),
    ]
