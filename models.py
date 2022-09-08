from django.db import models

# Create your models here.
from django.db import models

"""
Estudiantes (nombre, apellido, email)
Profesor (nombre, apellido, email, profesión)
Entregable (nombre, fechaDeEntrega,entregado)
Curso (nombre, comisión)
"""

class Pantalones(models.Model):
    color = models.CharField(max_length=128)
    talle = models.CharField(max_length=128)
    modelo = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Calzado(models.Model):
    color = models.CharField(max_length=128)
    talle = models.CharField(max_length=128)
    modelo = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Inicio(models.Model):
    redes_sociales = models.CharField(max_length=128)
    direccion = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.nombre} - {self.comision}'

class Remeras(models.Model):
    color = models.CharField(max_length=128)
    talle = models.CharField(max_length=128)
    modelo = models.CharField(max_length=128)

    def __str__(self):
        return f'Se ve como dice el metodo __str__'
