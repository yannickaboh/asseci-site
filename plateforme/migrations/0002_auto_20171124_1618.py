# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plateforme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='dateCreation',
            field=models.DateTimeField(verbose_name="Date de l'evenement"),
        ),
    ]
