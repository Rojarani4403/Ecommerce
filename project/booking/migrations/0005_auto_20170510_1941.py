# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-10 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20170510_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]