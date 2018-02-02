# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-02 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('url', models.URLField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'URL Entries',
                'verbose_name': 'URL Entry',
            },
        ),
    ]