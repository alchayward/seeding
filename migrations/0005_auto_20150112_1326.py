# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0004_auto_20150112_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='current_round',
        ),
        migrations.AddField(
            model_name='session',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 2, 26, 16, 240992, tzinfo=utc), verbose_name=b'date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='name',
            field=models.CharField(default='sess', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='tournament',
            field=models.ForeignKey(default=None, to='seeding.Tournament'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='slug',
            field=models.SlugField(max_length=160, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
