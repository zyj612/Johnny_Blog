# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_commentreply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentreply',
            options={'verbose_name': '回复评论', 'verbose_name_plural': '回复评论'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.AddField(
            model_name='comment',
            name='nickname',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='用户昵称'),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='用户昵称'),
        ),
    ]
