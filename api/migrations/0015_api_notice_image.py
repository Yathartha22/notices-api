# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20171109_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='notice_image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/notcie_images/'),
        ),
    ]
