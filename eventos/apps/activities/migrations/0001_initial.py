# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityRegist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('going', models.BooleanField(default=None)),
                ('people_going_number', models.PositiveSmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_date', models.DateField()),
                ('place_name', models.CharField(max_length=100)),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                ('description', models.TextField()),
                ('transfer_rate', models.PositiveSmallIntegerField()),
                ('going', models.BooleanField(default=None)),
                ('activity_registration', models.ForeignKey(blank=True, to='activities.ActivityRegist', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExtraActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_name', models.CharField(max_length=100)),
                ('venue_location', models.CharField(max_length=100)),
                ('price_from', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('place_img', models.ImageField(upload_to=b'extra_activities')),
                ('extra_package', models.ForeignKey(to='packages.ExtraPackage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExtraCustom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('budget_from', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('budget_to', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('interests', models.TextField()),
                ('custom_adult_name_1', models.CharField(max_length=50)),
                ('custom_adult_passport_1', models.PositiveIntegerField()),
                ('custom_adult_name_2', models.CharField(max_length=50)),
                ('custom_adult_passport_2', models.PositiveIntegerField()),
                ('custom_adult_name_3', models.CharField(max_length=50)),
                ('custom_adult_passport_3', models.PositiveIntegerField()),
                ('custom_adult_name_4', models.CharField(max_length=50)),
                ('custom_adult_passport_4', models.PositiveIntegerField()),
                ('custom_adult_name_5', models.CharField(max_length=50)),
                ('custom_adult_passport_5', models.PositiveIntegerField()),
                ('custom_adult_name_6', models.CharField(max_length=50)),
                ('custom_adult_passport_6', models.PositiveIntegerField()),
                ('custom_child_name_1', models.CharField(max_length=50)),
                ('custom_child_passport_1', models.PositiveIntegerField()),
                ('custom_child_age_1', models.PositiveSmallIntegerField()),
                ('custom_child_name_2', models.CharField(max_length=50)),
                ('custom_child_passport_2', models.PositiveIntegerField()),
                ('custom_child_age_2', models.PositiveSmallIntegerField()),
                ('custom_child_name_3', models.CharField(max_length=50)),
                ('custom_child_passport_3', models.PositiveIntegerField()),
                ('custom_child_age_3', models.PositiveSmallIntegerField()),
                ('custom_child_name_4', models.CharField(max_length=50)),
                ('custom_child_passport_4', models.PositiveIntegerField()),
                ('custom_child_age_4', models.PositiveSmallIntegerField()),
                ('custom_child_name_5', models.CharField(max_length=50)),
                ('custom_child_passport_5', models.PositiveIntegerField()),
                ('custom_child_age_5', models.PositiveSmallIntegerField()),
                ('custom_child_name_6', models.CharField(max_length=50)),
                ('custom_child_passport_6', models.PositiveIntegerField()),
                ('custom_child_age_6', models.PositiveSmallIntegerField()),
                ('reserve_before_event', models.BooleanField(default=None)),
                ('reserve_after_event', models.BooleanField(default=None)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExtraRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extra_adult_name_1', models.CharField(max_length=50)),
                ('extra_adult_passport_1', models.PositiveIntegerField()),
                ('extra_adult_name_2', models.CharField(max_length=50)),
                ('extra_adult_passport_2', models.PositiveIntegerField()),
                ('extra_adult_name_3', models.CharField(max_length=50)),
                ('extra_adult_passport_3', models.PositiveIntegerField()),
                ('extra_adult_name_4', models.CharField(max_length=50)),
                ('extra_adult_passport_4', models.PositiveIntegerField()),
                ('extra_adult_name_5', models.CharField(max_length=50)),
                ('extra_adult_passport_5', models.PositiveIntegerField()),
                ('extra_adult_name_6', models.CharField(max_length=50)),
                ('extra_adult_passport_6', models.PositiveIntegerField()),
                ('extra_child_name_1', models.CharField(max_length=50)),
                ('extra_child_passport_1', models.PositiveIntegerField()),
                ('extra_child_age_1', models.PositiveSmallIntegerField()),
                ('extra_child_name_2', models.CharField(max_length=50)),
                ('extra_child_passport_2', models.PositiveIntegerField()),
                ('extra_child_age_2', models.PositiveSmallIntegerField()),
                ('extra_child_name_3', models.CharField(max_length=50)),
                ('extra_child_passport_3', models.PositiveIntegerField()),
                ('extra_child_age_3', models.PositiveSmallIntegerField()),
                ('extra_child_name_4', models.CharField(max_length=50)),
                ('extra_child_passport_4', models.PositiveIntegerField()),
                ('extra_child_age_4', models.PositiveSmallIntegerField()),
                ('extra_child_name_5', models.CharField(max_length=50)),
                ('extra_child_passport_5', models.PositiveIntegerField()),
                ('extra_child_age_5', models.PositiveSmallIntegerField()),
                ('extra_child_name_6', models.CharField(max_length=50)),
                ('extra_child_passport_6', models.PositiveIntegerField()),
                ('extra_child_age_6', models.PositiveSmallIntegerField()),
                ('reserve_before_event', models.BooleanField(default=None)),
                ('reserve_after_event', models.BooleanField(default=None)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interest_title', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='extracustom',
            name='options',
            field=models.ManyToManyField(to='activities.Interest'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extraactivity',
            name='extra_registration',
            field=models.ForeignKey(blank=True, to='activities.ExtraRegistration', null=True),
            preserve_default=True,
        ),
    ]
