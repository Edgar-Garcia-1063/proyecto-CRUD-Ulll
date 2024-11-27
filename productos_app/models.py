from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    talla = models.CharField(max_length=20)
    id_proveedor = models.PositiveSmallIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre