# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0005_auto_20150112_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='slug',
            field=models.SlugField(default='def', max_length=160, editable=False, blank=True),
            preserve_default=False,
        ),
    ]
