# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-12 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pin',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]