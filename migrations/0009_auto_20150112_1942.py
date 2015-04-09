# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0008_auto_20150112_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='name',
            new_name='title',
        ),
    ]
