# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_api_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='choices',
            field=models.CharField(max_length=20, null=True),
        ),
    ]