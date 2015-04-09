# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeding', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fouls',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('infraction', models.CharField(max_length=250)),
                ('time', models.TimeField()),
                ('status', models.CharField(default=b'NO', max_length=2, choices=[(b'NO', b'None'), (b'TO', b'Completed'), (b'T3', b'30 seconds time off'), (b'2M', b'2 mins time off'), (b'SO', b'Sent off all game')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('completed', models.BooleanField(default=b'FALSE')),
                ('score_1', models.IntegerField()),
                ('score_2', models.IntegerField()),
                ('duration', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assisted', models.BooleanField(default=b'FALSE')),
                ('rating', models.IntegerField(default=-1)),
                ('time', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('bio', models.TextField(default=b'')),
                ('rating', models.FloatField(default=0.0)),
                ('club', models.ForeignKey(to='seeding.Club')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'FU', max_length=2, choices=[(b'CP', b'Completed'), (b'IP', b'In Progress'), (b'FU', b'To Be Played')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoundGames',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game', models.ForeignKey(to='seeding.Game')),
                ('round', models.ForeignKey(to='seeding.Round')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_rounds', models.IntegerField()),
                ('current_round', models.ForeignKey(to='seeding.Round')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player', models.ForeignKey(to='seeding.Player')),
                ('team', models.ForeignKey(to='seeding.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='goals',
            name='assist',
            field=models.ForeignKey(related_name='goals_assist', to='seeding.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goals',
            name='player',
            field=models.ForeignKey(related_name='goals_player', to='seeding.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='ass_ref',
            field=models.ForeignKey(related_name='game_ass_ref', to='seeding.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='ref',
            field=models.ForeignKey(related_name='game_ref', to='seeding.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='team_1',
            field=models.ForeignKey(related_name='game_team1', to='seeding.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='team_2',
            field=models.ForeignKey(related_name='game_team2', to='seeding.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fouls',
            name='player',
            field=models.ForeignKey(to='seeding.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='rating',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tournament',
            name='session',
            field=models.ForeignKey(default=None, to='seeding.Session'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='member1',
            field=models.ForeignKey(related_name='team_m1', to='seeding.Player'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='member2',
            field=models.ForeignKey(related_name='team_m2', to='seeding.Player'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='member3',
            field=models.ForeignKey(related_name='team_m3', to='seeding.Player'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
            preserve_default=True,
        ),
    ]
