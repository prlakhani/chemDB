# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmpds', '0003_remove_compound_kokellabid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compound',
            name='dateOrdered',
            field=models.CharField(default=b'2015-08-12', max_length=10),
        ),
    ]
