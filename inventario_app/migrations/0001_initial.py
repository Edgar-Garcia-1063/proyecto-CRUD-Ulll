# Generated by Django 5.1.2 on 2024-11-27 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('id_producto', models.PositiveSmallIntegerField()),
                ('id_proveedor', models.PositiveSmallIntegerField()),
                ('estatus', models.CharField(max_length=50)),
                ('disponible', models.CharField(max_length=10)),
                ('id_sucursal', models.PositiveSmallIntegerField()),
            ],
        ),
    ]