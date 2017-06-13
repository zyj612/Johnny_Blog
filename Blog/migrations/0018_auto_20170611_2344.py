# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0017_auto_20170611_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='is_recommend',
        ),
        migrations.AddField(
            model_name='article',
            name='pra',
            field=models.BooleanField(default=False, verbose_name='点赞总数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='click_count',
            field=models.IntegerField(default=0, verbose_name='阅读次数'),
        ),
    ]