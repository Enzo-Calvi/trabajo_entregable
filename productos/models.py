from django.db import models

# Create your models here.

class producto(models.Model):

    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    precio = models.FloatField()

def __str__(self):
    return f"{self.nombre} - {self.marca}"