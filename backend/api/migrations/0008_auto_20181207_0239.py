# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-07 02:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20181129_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone_number',
            new_name='phonenumber',
        ),
        migrations.AlterField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='api.Profile'),
        ),
    ]
