# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-11 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20181207_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='discordchatid',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
