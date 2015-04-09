# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0016_game_tournament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='tournament',
            field=models.ForeignKey(default=None, to='seeding.Tournament'),
        ),
    ]
