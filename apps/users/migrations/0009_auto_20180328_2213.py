# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-28 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180328_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='version',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
