# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20171117_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='github_url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]