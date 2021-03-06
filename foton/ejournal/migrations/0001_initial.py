# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-08 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Magasine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('abstract', models.TextField(verbose_name='abstract')),
                ('issn', models.CharField(blank=True, max_length=50)),
                ('issue', models.CharField(max_length=50, verbose_name='issue')),
                ('shop_link', models.URLField(blank=True)),
                ('free', models.BooleanField(default=True)),
                ('file', models.FileField(upload_to='files/')),
                ('image', models.ImageField(upload_to='files/')),
            ],
            options={
                'verbose_name_plural': 'Magasines',
                'verbose_name': 'Magasine',
            },
        ),
        migrations.CreateModel(
            name='Sommary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('author', models.CharField(max_length=100, verbose_name='author')),
                ('page', models.IntegerField(verbose_name='page')),
                ('keywords', models.CharField(max_length=50, verbose_name='keywords')),
                ('magasine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejournal.Magasine')),
            ],
            options={
                'verbose_name_plural': 'Sommaries',
                'verbose_name': 'Sommary',
            },
        ),
    ]
