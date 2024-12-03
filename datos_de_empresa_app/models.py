from django.db import models

# Create your models here.
class Datos(models.Model):
    id_empresa = models.PositiveSmallIntegerField(primary_key=True)
    id_sucursal = models.PositiveSmallIntegerField()
    nombre_empresa = models.CharField(max_length=50)
    ubicacion_empresa = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre_empresa