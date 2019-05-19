# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-19 19:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_auto_20190519_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='shared_with',
            field=models.ManyToManyField(related_name='sharee', to=settings.AUTH_USER_MODEL),
        ),
    ]
