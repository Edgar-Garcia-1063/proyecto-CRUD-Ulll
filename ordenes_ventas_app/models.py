from django.db import models

# Create your models here.
class Orden(models.Model):
    id_orden = models.PositiveSmallIntegerField(primary_key=True)
    id_cliente = models.PositiveSmallIntegerField()
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return self.fecha