from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.PositiveSmallIntegerField(primary_key=True)
    id_prod = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    disponible = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre