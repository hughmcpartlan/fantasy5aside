# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='team_name',
            new_name='name',
        ),
    ]