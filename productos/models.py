from django.db import models

# Create your models here.

class Zapatilla(models.Model):

    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    precio = models.FloatField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Marca: {self.marca} - Precio: {self.precio}"

class camisetas(models.Model):

    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    precio = models.FloatField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Marca: {self.marca} - Precio: {self.precio}"

class pantalones(models.Model):

    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    precio = models.FloatField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Marca: {self.marca} - Precio: {self.precio}"