# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('C_app', '0002_auto_20161214_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
