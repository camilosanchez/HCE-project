# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('event_name', models.CharField(max_length=50)),
                ('event_initial_date', models.DateField()),
                ('event_ending_date', models.DateField()),
                ('event_slug', models.SlugField(editable=False)),
                ('description', models.TextField()),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_address', models.CharField(max_length=100)),
                ('organizer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('book_first_name', models.CharField(max_length=50)),
                ('book_last_name', models.CharField(max_length=50)),
                ('book_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('book_email', models.EmailField(max_length=75)),
                ('book_passport', models.PositiveIntegerField()),
                ('book_nationality', models.CharField(max_length=100)),
                ('book_sex', models.CharField(max_length=1, choices=[(b'S', b'Cual es su sexo?'), (b'M', b'Hombre'), (b'F', b'Mujer')])),
                ('book_special_requirements', models.TextField()),
                ('city_of_flight_origin', models.CharField(max_length=100)),
                ('arrival_date', models.DateField()),
                ('leaving_date', models.DateField()),
                ('traveling_adult_name_1', models.CharField(max_length=100)),
                ('traveling_adult_passport_1', models.PositiveIntegerField()),
                ('traveling_adult_email_1', models.EmailField(max_length=75)),
                ('traveling_adult_name_2', models.CharField(max_length=100)),
                ('traveling_adult_passport_2', models.PositiveIntegerField()),
                ('traveling_adult_email_2', models.EmailField(max_length=75)),
                ('traveling_adult_name_3', models.CharField(max_length=100)),
                ('traveling_adult_passport_3', models.PositiveIntegerField()),
                ('traveling_adult_email_3', models.EmailField(max_length=75)),
                ('traveling_adult_name_4', models.CharField(max_length=100)),
                ('traveling_adult_passport_4', models.PositiveIntegerField()),
                ('traveling_adult_email_4', models.EmailField(max_length=75)),
                ('traveling_adult_name_5', models.CharField(max_length=100)),
                ('traveling_adult_passport_5', models.PositiveIntegerField()),
                ('traveling_adult_email_5', models.EmailField(max_length=75)),
                ('traveling_adult_name_6', models.CharField(max_length=100)),
                ('traveling_adult_passport_6', models.PositiveIntegerField()),
                ('traveling_adult_email_6', models.EmailField(max_length=75)),
                ('traveling_child_name_1', models.CharField(max_length=100)),
                ('traveling_child_passport_1', models.PositiveIntegerField()),
                ('traveling_child_age_1', models.PositiveSmallIntegerField()),
                ('traveling_child_name_2', models.CharField(max_length=100)),
                ('traveling_child_passport_2', models.PositiveIntegerField()),
                ('traveling_child_age_2', models.PositiveSmallIntegerField()),
                ('traveling_child_name_3', models.CharField(max_length=100)),
                ('traveling_child_passport_3', models.PositiveIntegerField()),
                ('traveling_child_age_3', models.PositiveSmallIntegerField()),
                ('traveling_child_name_4', models.CharField(max_length=100)),
                ('traveling_child_passport_4', models.PositiveIntegerField()),
                ('traveling_child_age_4', models.PositiveSmallIntegerField()),
                ('traveling_child_name_5', models.CharField(max_length=100)),
                ('traveling_child_passport_5', models.PositiveIntegerField()),
                ('traveling_child_age_5', models.PositiveSmallIntegerField()),
                ('traveling_child_name_6', models.CharField(max_length=100)),
                ('traveling_child_passport_6', models.PositiveIntegerField()),
                ('traveling_child_age_6', models.PositiveSmallIntegerField()),
                ('hotel_checkin_date', models.DateField()),
                ('hotel_checkout_date', models.DateField()),
                ('hotel_room_adult_name_1', models.CharField(max_length=100)),
                ('hotel_room_adult_passport_1', models.PositiveIntegerField()),
                ('hotel_room_adult_email_1', models.EmailField(max_length=75)),
                ('hotel_room_adult_name_2', models.CharField(max_length=100)),
                ('hotel_room_adult_passport_2', models.PositiveIntegerField()),
                ('hotel_room_adult_email_2', models.EmailField(max_length=75)),
                ('hotel_room_adult_name_3', models.CharField(max_length=100)),
                ('hotel_room_adult_passport_3', models.PositiveIntegerField()),
                ('hotel_room_adult_email_3', models.EmailField(max_length=75)),
                ('hotel_room_adult_name_4', models.CharField(max_length=100)),
                ('hotel_room_adult_passport_4', models.PositiveIntegerField()),
                ('hotel_room_adult_email_4', models.EmailField(max_length=75)),
                ('hotel_room_adult_name_5', models.CharField(max_length=100)),
                ('hotel_room_adult_passport_5', models.PositiveIntegerField()),
                ('hotel_room_adult_email_5', models.EmailField(max_length=75)),
                ('hotel_room_adult_name_6', models.CharField(max_length=100)),
                ('hotel_room_adult_passport_6', models.PositiveIntegerField()),
                ('hotel_room_adult_email_6', models.EmailField(max_length=75)),
                ('hotel_room_child_name_1', models.CharField(max_length=50)),
                ('hotel_room_child_passport_1', models.PositiveIntegerField()),
                ('hotel_room_child_age_1', models.PositiveSmallIntegerField()),
                ('hotel_room_child_name_2', models.CharField(max_length=50)),
                ('hotel_room_child_passport_2', models.PositiveIntegerField()),
                ('hotel_room_child_age_2', models.PositiveSmallIntegerField()),
                ('hotel_room_child_name_3', models.CharField(max_length=50)),
                ('hotel_room_child_passport_3', models.PositiveIntegerField()),
                ('hotel_room_child_age_3', models.PositiveSmallIntegerField()),
                ('hotel_room_child_name_4', models.CharField(max_length=50)),
                ('hotel_room_child_passport_4', models.PositiveIntegerField()),
                ('hotel_room_child_age_4', models.PositiveSmallIntegerField()),
                ('hotel_room_child_name_5', models.CharField(max_length=50)),
                ('hotel_room_child_passport_5', models.PositiveIntegerField()),
                ('hotel_room_child_age_5', models.PositiveSmallIntegerField()),
                ('hotel_room_child_name_6', models.CharField(max_length=50)),
                ('hotel_room_child_passport_6', models.PositiveIntegerField()),
                ('hotel_room_child_age_6', models.PositiveSmallIntegerField()),
                ('cc_number', models.PositiveIntegerField()),
                ('exp_date', models.DateField()),
                ('cvv_number', models.PositiveSmallIntegerField()),
                ('cc_address', models.CharField(max_length=50)),
                ('airport_transfer', models.ForeignKey(blank=True, to='packages.TransferPackage', null=True)),
                ('event_activities', models.ManyToManyField(to='activities.EventActivity', null=True, blank=True)),
                ('extra_activities', models.ForeignKey(blank=True, to='activities.ExtraActivity', null=True)),
                ('extra_activities_custom', models.OneToOneField(null=True, blank=True, to='activities.ExtraCustom')),
                ('hotel_package', models.ForeignKey(blank=True, to='packages.HotelPackage', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='registrations',
            field=models.ForeignKey(blank=True, to='events.Registration', null=True),
            preserve_default=True,
        ),
    ]
