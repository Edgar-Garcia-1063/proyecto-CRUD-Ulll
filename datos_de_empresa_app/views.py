# Create your views here.
from django.shortcuts import render, redirect
from .models import Datos

# Create your views here.

def inicio_vistasDatos (request):
    dato = Datos.objects.all()

    return render(request, "gestionarDatos.html",{"dat":dato})

def registrarDatos (request):
    id_empresa = request.POST["txtidE"]
    id_sucursal = request.POST["txtidS"]
    nombre_empresa = request.POST["txtnombre"]
    ubicacion_empresa = request.POST["txtubicacion"]

    guardar= Datos.objects.create(id_empresa=id_empresa,id_sucursal=id_sucursal,nombre_empresa=nombre_empresa, ubicacion_empresa=ubicacion_empresa)

    return redirect("datos")

def borrarDatos (request, id_empresa):
    dat = Datos.objects.get(id_empresa=id_empresa)
    dat.delete()

    return redirect("datos")

def seleccionarDatos(request, id_empresa):
    dato = Datos.objects.get(id_empresa=id_empresa)
    
    return render (request, "editarDatos.html", {"dat":dato})

def editarDatos(request):
    id_empresa = request.POST["txtidE"]
    id_sucursal = request.POST["txtidS"]
    nombre_empresa = request.POST["txtnombre"]
    ubicacion_empresa = request.POST["txtubicacion"]
    
    dat = Datos.objects.get(id_empresa=id_empresa)

    dat.id_sucursal=id_sucursal
    dat.nombre_empresa=nombre_empresa
    dat.ubicacion_empresa=ubicacion_empresa
    dat.save()
    return redirect("datos")