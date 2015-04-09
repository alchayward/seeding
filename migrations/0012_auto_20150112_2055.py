# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0011_session_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roundgames',
            name='game',
        ),
        migrations.RemoveField(
            model_name='roundgames',
            name='round',
        ),
        migrations.DeleteModel(
            name='RoundGames',
        ),
        migrations.AddField(
            model_name='game',
            name='round',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='session',
            field=models.ForeignKey(default=None, to='seeding.Session'),
            preserve_default=True,
        ),
    ]
