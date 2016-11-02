# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-01 13:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import foton.courses.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Domain',
                'verbose_name_plural': 'Domains',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moocs.Category')),
            ],
            options={
                'verbose_name': 'Discipline',
                'verbose_name_plural': 'Disciplines',
            },
        ),
        migrations.CreateModel(
            name='Mooc',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Course')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moocs.Discipline')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_mooc', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mooc',
                'verbose_name_plural': 'Moocs',
            },
            bases=('courses.course',),
        ),
        migrations.CreateModel(
            name='MoocModule',
            fields=[
                ('module_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Module')),
                ('order', foton.courses.forms.OrderField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mooc_modules', to='moocs.Mooc')),
            ],
            options={
                'verbose_name': 'Mooc Module',
                'verbose_name_plural': 'Mooc Modules',
            },
            bases=('courses.module',),
        ),
    ]