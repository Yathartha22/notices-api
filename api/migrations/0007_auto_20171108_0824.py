# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20171105_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='branch',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='choices',
            field=models.CharField(max_length=20, null=True),
        ),
    ]