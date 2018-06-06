# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0035_rename_divset_constraint'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisation',
            options={'get_latest_by': 'start_date', 'ordering': ('official_name', '-start_date')},
        ),
    ]
