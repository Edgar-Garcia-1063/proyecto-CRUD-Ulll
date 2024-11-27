from django.db import models

# Create your models here.
class Inventario(models.Model):
    id_inventario = models.PositiveSmallIntegerField(primary_key=True)
    id_producto = models.PositiveSmallIntegerField()
    id_proveedor = models.PositiveSmallIntegerField()
    estatus = models.CharField(max_length=50)
    disponible = models.CharField(max_length=10)
    id_sucursal = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.id_inventario