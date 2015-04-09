# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0007_auto_20150112_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentTeam',
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
            model_name='tournamentteams',
            name='session',
        ),
        migrations.RemoveField(
            model_name='tournamentteams',
            name='team',
        ),
        migrations.RemoveField(
            model_name='tournamentteams',
            name='tournament',
        ),
        migrations.DeleteModel(
            name='TournamentTeams',
        ),
    ]
