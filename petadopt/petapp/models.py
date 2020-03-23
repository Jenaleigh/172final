from django.db import models

# Create your models here.

class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    petName = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    submission_date = models.DateTimeField()
    petSpecies = models.CharField(max_length=30)
    petBreed = models.CharField(max_length=30, blank=True)
    petDescription = models.TextField()
    petSex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    petAge = models.IntegerField(null=True)
    petVaccinations = models.ManyToManyField('Vaccine', blank=True)

    def __str__(self):
        return self.petName
    
    class Meta:
        db_table='pet'
        verbose_name_plural='pets'


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='vaccine'
        verbose_name_plural='vaccines'
