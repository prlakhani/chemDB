# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chemName', models.CharField(max_length=100)),
                ('SMILES', models.CharField(max_length=500)),
                ('InCHI', models.CharField(max_length=500)),
                ('box', models.PositiveSmallIntegerField()),
                ('row', models.CharField(max_length=1)),
                ('column', models.PositiveSmallIntegerField()),
                ('vendor', models.CharField(max_length=20, null=True, blank=True)),
                ('vendorCatNo', models.CharField(max_length=20, null=True, blank=True)),
                ('solvent', models.CharField(default=b'DMSO', max_length=10, choices=[(b'DMSO', b'DMSO'), (b'Ethanol', b'Ethanol'), (b'PEG', b'PEG'), (b'H2O', b'H2O')])),
                ('solventNote', models.TextField(null=True, blank=True)),
                ('molecularWeight', models.DecimalField(max_digits=6, decimal_places=3)),
                ('concmM', models.DecimalField(max_digits=6, decimal_places=3)),
                ('reasonOrdered', models.TextField(null=True, blank=True)),
                ('personOrdered', models.CharField(max_length=20, choices=[(b'Dave Kokel', b'Dave Kokel'), (b'Matt McCarroll', b'Matt McCarroll'), (b'Parth Lakhani', b'Parth Lakhani'), (b'Ethan Fertsch', b'Ethan Fertsch')])),
                ('powderLocation', models.CharField(max_length=50, null=True, blank=True)),
                ('mechanismTargetNotes', models.TextField(null=True, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('rothID', models.PositiveIntegerField(null=True, blank=True)),
                ('kokelLabID', models.CharField(max_length=10)),
                ('dateOrdered', models.DateField(default=django.utils.timezone.now)),
                ('libraryCode', models.CharField(max_length=2, choices=[(b'UC', b'UC')])),
            ],
        ),
    ]
