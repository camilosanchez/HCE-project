# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20141123_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityregist',
            name='activity_registration',
        ),
        migrations.AddField(
            model_name='eventactivity',
            name='activity_registration',
            field=models.ForeignKey(blank=True, to='activities.ActivityRegist', null=True),
            preserve_default=True,
        ),
    ]
