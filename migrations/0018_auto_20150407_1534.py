# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0017_auto_20150407_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='tournament',
            field=models.ForeignKey(default=0, to='seeding.Tournament'),
        ),
    ]
