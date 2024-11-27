from django.shortcuts import render, redirect
from .models import Sucursal

# Create your views here.

def inicio_vistasSucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursal.html", {"sucursal": sucursales})

def registrarSucursal(request):
    id_sucursal = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    ciudad = request.POST["txtciudad"]
    estado = request.POST["txtestado"]
    codigo_postal = request.POST["txtcodigopostal"]
    horario = request.POST["txthorario"]

    Sucursal.objects.create(
        id_sucursal=id_sucursal,
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        ciudad=ciudad,
        estado=estado,
        codigo_postal=codigo_postal,
        horario=horario
    )
    return redirect("sucursales")

def borrarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()
    return redirect("sucursales")

def seleccionarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request, "editarSucursal.html", {"sucursal": sucursal})

def editarSucursal(request):
    id_sucursal = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    ciudad = request.POST["txtciudad"]
    estado = request.POST["txtestado"]
    codigo_postal = request.POST["txtcodigopostal"]
    horario = request.POST["txthorario"]

    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.nombre = nombre
    sucursal.direccion = direccion
    sucursal.telefono = telefono
    sucursal.ciudad = ciudad
    sucursal.estado = estado
    sucursal.codigo_postal = codigo_postal
    sucursal.horario = horario
    sucursal.save()
    return redirect("sucursales")
