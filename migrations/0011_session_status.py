# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0010_auto_20150112_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='status',
            field=models.CharField(default=b'RD', max_length=2, choices=[(b'UP', b'Updating'), (b'RD', b'Ready')]),
            preserve_default=True,
        ),
    ]
