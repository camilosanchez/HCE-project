# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20141123_1937'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActivityRegist',
            new_name='ActivityAssist',
        ),
    ]
