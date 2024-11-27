from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    horario = models.CharField(max_length=50)
    id_sucursal = models.PositiveSmallIntegerField()