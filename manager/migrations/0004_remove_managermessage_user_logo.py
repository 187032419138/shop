# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-04-27 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_managermessage_user_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managermessage',
            name='user_logo',
        ),
    ]
