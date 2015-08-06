from django.db import models
from django.utils import timezone

# Create your models here.
class Compound(models.Model):
	chemName = models.CharField(max_length=100)
	SMILES = models.CharField(max_length=500)
	InCHI = models.CharField(max_length=500)
	box = models.PositiveSmallIntegerField()
	row = models.CharField(max_length=1)	# validate as A-H
	column = models.PositiveSmallIntegerField()	# validate to max value of 8
	# calculated brc field?
	vendor = models.CharField(max_length=20,blank=True,null=True)
	vendorCatNo = models.CharField(max_length=20,blank=True,null=True)
	SOLVENT_CHOICES = (
		('DMSO','DMSO'),
		('Ethanol','Ethanol'),
		('PEG','PEG'),
		('H2O','H2O'),
		)
	solvent = models.CharField(max_length=10, choices=SOLVENT_CHOICES, default='DMSO')
	solventNote = models.TextField(blank=True,null=True)
	molecularWeight = models.DecimalField(max_digits=6, decimal_places=3)
	concmM = models.DecimalField(max_digits=6, decimal_places=3)
	reasonOrdered = models.TextField(blank=True,null=True)
	PERSONS = (
		('Dave Kokel','Dave Kokel'),
		('Matt McCarroll','Matt McCarroll'),
		('Parth Lakhani','Parth Lakhani'),
		('Ethan Fertsch','Ethan Fertsch'),
		)
	personOrdered = models.CharField(max_length=20, choices=PERSONS)
	powderLocation = models.CharField(max_length=50,blank=True,null=True)
	mechanismTargetNotes = models.TextField(blank=True,null=True)
	note = models.TextField(blank=True,null=True)
	rothID = models.PositiveIntegerField(blank=True,null=True)
	kokelLabID = models.CharField(max_length=10)	# figure out what this means for us. do we really need the forced pk?
	dateOrdered = models.DateField(default=timezone.now())
	LIBRARIES = (
		('UC','UC')
		)
	libraryCode = models.CharField(max_length=2,choices=LIBRARIES)
	# boxWellCode is calculated from box+robotized(row,Column)