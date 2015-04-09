# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0015_auto_20150402_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='tournament',
            field=models.ForeignKey(default=0, to='seeding.Tournament'),
            preserve_default=False,
        ),
    ]
