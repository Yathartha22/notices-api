# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-24 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20171123_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='notice_file',
            field=models.FileField(blank=True, null=True, upload_to='uploaded_files/notice_files/'),
        ),
    ]
