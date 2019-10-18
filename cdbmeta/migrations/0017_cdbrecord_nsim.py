# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-18 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdbmeta', '0016_attribution_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdbrecord',
            name='nsim',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number of simulations'),
        ),
    ]
