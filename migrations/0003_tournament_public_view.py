# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0002_auto_20150102_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='public_view',
            field=models.BooleanField(default=b'True'),
            preserve_default=True,
        ),
    ]
