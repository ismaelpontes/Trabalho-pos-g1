# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 00:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0019_auto_20170925_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(max_length=50)),
                ('compromissos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Compromisso')),
                ('convidado', models.ManyToManyField(null=True, related_name='convidados', to=settings.AUTH_USER_MODEL)),
                ('dono_evento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Compartilhamento',
            new_name='AgendaUsuario',
        ),
        migrations.RemoveField(
            model_name='convite',
            name='compromissos',
        ),
        migrations.RemoveField(
            model_name='convite',
            name='convidado',
        ),
        migrations.AlterField(
            model_name='agenda',
            name='institucional',
            field=models.BooleanField(verbose_name='Institucional'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='visivel',
            field=models.BooleanField(verbose_name='Público'),
        ),
        migrations.DeleteModel(
            name='Convite',
        ),
    ]