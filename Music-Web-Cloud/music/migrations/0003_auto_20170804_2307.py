# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20170804_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='genere',
            new_name='genre',
        ),
    ]
