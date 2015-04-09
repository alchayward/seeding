# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0009_auto_20150112_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tournamentteam',
            old_name='inital_seeding',
            new_name='inital_rank',
        ),
    ]
