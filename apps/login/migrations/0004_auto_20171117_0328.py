# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-17 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=128),
        ),
    ]