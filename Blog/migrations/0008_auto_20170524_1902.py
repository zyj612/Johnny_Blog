# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 11:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20170524_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentreply',
            old_name='reply_to',
            new_name='reply_to_nickname',
        ),
        migrations.AddField(
            model_name='commentreply',
            name='reply_to_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_replied', to=settings.AUTH_USER_MODEL),
        ),
    ]
