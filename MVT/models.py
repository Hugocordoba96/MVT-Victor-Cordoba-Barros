from django.db import models

# Create your models here.

class Familiares(models.Model):

    parentesco = models.CharField(max_length=40)
    nombreyapellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    año_nac = models.IntegerField()
