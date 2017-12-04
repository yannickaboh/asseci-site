# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 20:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plateforme', '0006_annonce_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SujetForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(max_length=255, verbose_name='Sujet')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sujetforums', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThemeForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30, unique=True, verbose_name='Titre')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='sujetforum',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sujetforums', to='plateforme.ThemeForum'),
        ),
        migrations.AddField(
            model_name='commentaires',
            name='sujetforum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='plateforme.SujetForum'),
        ),
        migrations.AddField(
            model_name='commentaires',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
