# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-11 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='num',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='vote',
            name='program',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='program.program'),
        ),
    ]
