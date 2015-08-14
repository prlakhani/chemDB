# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmpds', '0004_auto_20150812_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compound',
            name='dateOrdered',
            field=models.CharField(default=b'2015-08-13', max_length=10),
        ),
        migrations.AlterField(
            model_name='compound',
            name='rothID',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
    ]
