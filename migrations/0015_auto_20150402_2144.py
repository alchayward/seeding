# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0014_auto_20150402_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='session',
            field=models.ManyToManyField(to='seeding.Session', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='tournament',
            field=models.ManyToManyField(to='seeding.Tournament', null=True),
            preserve_default=True,
        ),
    ]
