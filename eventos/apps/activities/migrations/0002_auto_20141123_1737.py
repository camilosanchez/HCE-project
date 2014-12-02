# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventactivity',
            name='activity_registration',
        ),
        migrations.RemoveField(
            model_name='eventactivity',
            name='going',
        ),
        migrations.AddField(
            model_name='activityregist',
            name='activity_registration',
            field=models.ForeignKey(blank=True, to='activities.EventActivity', null=True),
            preserve_default=True,
        ),
    ]
