# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=b'TRUE')),
                ('name', models.CharField(max_length=250)),
                ('member1', models.DateTimeField(verbose_name=b'date')),
                ('member2', models.DateTimeField(verbose_name=b'date')),
                ('member3', models.DateTimeField(verbose_name=b'date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=b'TRUE')),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateTimeField(verbose_name=b'date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
