# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-14 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='abcd@gmail.com', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.TextField(default='user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.TextField(blank=True),
        ),
    ]