# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0013_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fouls',
            name='player',
        ),
        migrations.DeleteModel(
            name='Fouls',
        ),
        migrations.RemoveField(
            model_name='goals',
            name='assist',
        ),
        migrations.RemoveField(
            model_name='goals',
            name='player',
        ),
        migrations.DeleteModel(
            name='Goals',
        ),
        migrations.RemoveField(
            model_name='player',
            name='club',
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.RemoveField(
            model_name='teammembers',
            name='player',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.RemoveField(
            model_name='teammembers',
            name='team',
        ),
        migrations.DeleteModel(
            name='TeamMembers',
        ),
        migrations.RemoveField(
            model_name='tournamentgames',
            name='session',
        ),
        migrations.RemoveField(
            model_name='tournamentgames',
            name='tournament',
        ),
        migrations.DeleteModel(
            name='TournamentGames',
        ),
        migrations.RemoveField(
            model_name='tournamentteam',
            name='session',
        ),
        migrations.RemoveField(
            model_name='tournamentteam',
            name='team',
        ),
        migrations.RemoveField(
            model_name='tournamentteam',
            name='tournament',
        ),
        migrations.DeleteModel(
            name='TournamentTeam',
        ),
        migrations.AddField(
            model_name='team',
            name='session',
            field=models.ManyToManyField(to='seeding.Session'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='tournament',
            field=models.ManyToManyField(to='seeding.Tournament'),
            preserve_default=True,
        ),
    ]
