# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171104_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='branch',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='api',
            name='year',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='choices',
            field=models.CharField(choices=[('Official', 'Official'), ('Class', 'Class'), ('All', 'All')], default='All', max_length=1, null=True),
        ),
    ]
