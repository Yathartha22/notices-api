# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-11 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_api_notice_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='notice_image',
        ),
        migrations.AddField(
            model_name='api',
            name='notice_file',
            field=models.FileField(blank=True, null=True, upload_to='accounts/notcie_images/'),
        ),
    ]
