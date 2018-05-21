# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0007_user_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('story_id', models.AutoField(primary_key=True, serialize=False)),
                ('story_title', models.CharField(max_length=100, unique=True)),
                ('age_group', models.CharField(default='3-8', max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('album_image', models.TextField()),
            ],
            options={
                'db_table': 'story',
            },
        ),
    ]
