from django.db import models
from django.utils import timezone

# Create your models here.


class Compound(models.Model):
    import_dict = {
        'overrides': {},
        'object_colmap': {
            'identity_fields': ['chemName'],
            'self_field_cols': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                12, 13, 14, 15, 16, 18, 19, 20],
            'simple_related_cols': [],
            'field_col_mapping': {
                0: 'chemName',
                1: 'SMILES',
                2: 'InCHI',
                3: 'CSID',
                4: 'box',
                5: 'row',
                6: 'column',
                7: 'vendor',
                8: 'vendorCatNo',
                9: 'solvent',
                10: 'solventNote',
                11: 'molecularWeight',
                12: 'concmM',
                13: 'reasonOrdered',
                14: 'personOrdered',
                15: 'powderLocation',
                16: 'mechanismTargetNotes',
                17: 'note',
                18: 'rothID',
                19: 'dateOrdered',
                20: 'libraryCode'
            },
        },
    }
    export_dict = {
        'object_export': ['chemName', 'SMILES', 'InCHI', 'CSID', 'box',
                          'row', 'column', 'vendor', 'vendorCatNo', 'solvent',
                          'solventNote', 'molecularWeight', 'concmM', 'reasonOrdered',
                          'personOrdered', 'powderLocation', 'mechanismTargetNotes',
                          'note', 'rothID', 'dateOrdered', 'libraryCode']
    }
    chemName = models.CharField(max_length=100)
    SMILES = models.CharField(max_length=500)
    InCHI = models.CharField(max_length=500)
    CSID = models.CharField(
        "ChemSpider ID", max_length=10, blank=True, null=True)
    box = models.PositiveSmallIntegerField()
    row = models.CharField(max_length=1)    # validate as A-H
    column = models.PositiveSmallIntegerField()  # validate to max value of 8
    # calculated brc field?
    vendor = models.CharField(max_length=20, blank=True, null=True)
    vendorCatNo = models.CharField(max_length=20, blank=True, null=True)
    SOLVENT_CHOICES = (
        ('DMSO', 'DMSO'),
        ('Ethanol', 'Ethanol'),
        ('PEG', 'PEG'),
        ('H2O', 'H2O'),
    )
    solvent = models.CharField(
        max_length=10, choices=SOLVENT_CHOICES, default='DMSO')
    solventNote = models.TextField(blank=True, null=True)
    molecularWeight = models.DecimalField(max_digits=6, decimal_places=3)
    concmM = models.DecimalField(max_digits=6, decimal_places=3)
    reasonOrdered = models.TextField(blank=True, null=True)
    PERSONS = (
        ('Dave Kokel', 'Dave Kokel'),
        ('Matt McCarroll', 'Matt McCarroll'),
        ('Parth Lakhani', 'Parth Lakhani'),
        ('Ethan Fertsch', 'Ethan Fertsch'),
    )
    personOrdered = models.CharField(max_length=20, choices=PERSONS)
    powderLocation = models.CharField(max_length=50, blank=True, null=True)
    mechanismTargetNotes = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    # Char not Int to use batchimport, which doesn't like blank/null fields
    rothID = models.CharField(
        "ID if sent to Roth lab for testing", max_length=6, blank=True, null=True)
    dateOrdered = models.CharField(
        default=timezone.now().strftime('%Y-%m-%d'), max_length=10)
    LIBRARIES = (
        ('UC', 'UC'),
    )
    libraryCode = models.CharField(
        max_length=2, choices=LIBRARIES, default='UC')
    # boxWellCode is calculated from box+robotized(row,Column)
