# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmpds', '0002_auto_20150811_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='kokelLabID',
        ),
    ]
