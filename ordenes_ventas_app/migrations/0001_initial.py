# Generated by Django 5.1.2 on 2024-11-27 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('id_cliente', models.PositiveSmallIntegerField()),
                ('fecha', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo_pago', models.CharField(max_length=50)),
            ],
        ),
    ]
