from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.

def inicio_vistasEmpleados(request):
    empleados = Empleado.objects.all()
    return render(request, "gestionarEmpleado.html", {"empleado": empleados})

def registrarEmpleado(request):
    id_empleado = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    puesto = request.POST["txtpuesto"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    horario = request.POST["txthorario"]
    id_sucursal = request.POST["txtidsucursal"]

    Empleado.objects.create(
        id_empleado=id_empleado,
        nombre=nombre,
        apellido=apellido,
        puesto=puesto,
        telefono=telefono,
        email=email,
        horario=horario,
        id_sucursal=id_sucursal
    )
    return redirect("empleados")

def borrarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("empleados")

def seleccionarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleado.html", {"empleado": empleado})

def editarEmpleado(request):
    id_empleado = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    puesto = request.POST["txtpuesto"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    horario = request.POST["txthorario"]
    id_sucursal = request.POST["txtidsucursal"]

    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre = nombre
    empleado.apellido = apellido
    empleado.puesto = puesto
    empleado.telefono = telefono
    empleado.email = email
    empleado.horario = horario
    empleado.id_sucursal = id_sucursal
    empleado.save()
    return redirect("empleados")
