# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-18 07:03
from __future__ import unicode_literals

import User.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=255, verbose_name='Nickname')),
                ('sign', models.CharField(default='', max_length=255, verbose_name='Personal Signature')),
                ('avatar', models.ImageField(default='avatars/default.jpg', upload_to=User.models.upload_avatar)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
