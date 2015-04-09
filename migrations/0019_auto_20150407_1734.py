# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0018_auto_20150407_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='rating',
            new_name='score',
        ),
        migrations.AddField(
            model_name='team',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
