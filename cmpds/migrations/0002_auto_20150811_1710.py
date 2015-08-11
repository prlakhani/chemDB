# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmpds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compound',
            name='CSID',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compound',
            name='libraryCode',
            field=models.CharField(default=b'UC', max_length=2, choices=[(b'UC', b'UC')]),
        ),
    ]
