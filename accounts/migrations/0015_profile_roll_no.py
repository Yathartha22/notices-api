# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-26 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20171124_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='roll_no',
            field=models.IntegerField(null=True),
        ),
    ]
