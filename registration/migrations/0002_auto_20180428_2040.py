# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-29 00:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='RegistrationProfile',
        ),
    ]
