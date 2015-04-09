# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0003_tournament_public_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='session',
        ),
        migrations.AddField(
            model_name='tournament',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
