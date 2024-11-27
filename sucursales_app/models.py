from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id_sucursal = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    horario = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre