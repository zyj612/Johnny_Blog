# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0019_auto_20170611_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='praise_count',
            field=models.IntegerField(default=0, verbose_name='点赞总数'),
        ),
    ]