from django.db import models

# Create your models here.

class registro_familiar(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fecha_nacimiento = str(models.DateField())