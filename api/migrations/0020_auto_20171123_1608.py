# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-23 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20171112_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='notice_file',
            field=models.FileField(blank=True, null=True, upload_to='static/notice_files/'),
        ),
    ]