# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 23:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0013_auto_20170925_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compartilhamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='usuario',
        ),
        migrations.AddField(
            model_name='compartilhamento',
            name='agenda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Agenda'),
        ),
        migrations.AddField(
            model_name='compartilhamento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]