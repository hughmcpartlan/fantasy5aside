# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Striker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('team_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
            ],
        ),
    ]
