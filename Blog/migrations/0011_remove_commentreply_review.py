# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_commentreply_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentreply',
            name='review',
        ),
    ]
