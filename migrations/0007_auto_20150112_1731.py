# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0006_session_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentGames',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.IntegerField(default=0)),
                ('session', models.ForeignKey(default=None, to='seeding.Session')),
                ('tournament', models.ForeignKey(default=None, to='seeding.Tournament')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TournamentTeams',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inital_seeding', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
                ('session', models.ForeignKey(default=None, to='seeding.Session')),
                ('team', models.ForeignKey(default=None, to='seeding.Team')),
                ('tournament', models.ForeignKey(default=None, to='seeding.Tournament')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='game',
            name='ass_ref',
        ),
        migrations.RemoveField(
            model_name='game',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='game',
            name='ref',
        ),
        migrations.AlterField(
            model_name='team',
            name='member1',
            field=models.CharField(default=b'member 1', max_length=250),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='member2',
            field=models.CharField(default=b'member 2', max_length=250),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='member3',
            field=models.CharField(default=b'member 3', max_length=250),
            preserve_default=True,
        ),
    ]
