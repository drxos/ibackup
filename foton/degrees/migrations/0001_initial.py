# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-08 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('pdf', models.FileField(upload_to='pdf/')),
                ('pdf_fr', models.FileField(null=True, upload_to='pdf/')),
                ('pdf_en', models.FileField(null=True, upload_to='pdf/')),
            ],
            options={
                'verbose_name_plural': 'Programs',
                'verbose_name': 'Program',
            },
        ),
        migrations.CreateModel(
            name='Bachelor',
            fields=[
                ('program_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='degrees.Program')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.Option')),
                ('option_en', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.Option')),
                ('option_fr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.Option')),
            ],
            options={
                'verbose_name_plural': 'Bachelors',
                'verbose_name': 'Bachelor',
            },
            bases=('degrees.program',),
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('program_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='degrees.Program')),
                ('speciality', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='programs.Speciality')),
                ('speciality_en', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.Speciality')),
                ('speciality_fr', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.Speciality')),
            ],
            options={
                'verbose_name_plural': 'Masters',
                'verbose_name': 'Master',
            },
            bases=('degrees.program',),
        ),
    ]
