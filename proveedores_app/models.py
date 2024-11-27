from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre