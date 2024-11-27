from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

def inicio_vistasClientes(request):
    clientes = Cliente.objects.all()
    return render(request, "gestionarCliente.html", {"cliente": clientes})

def registrarCliente(request):
    id_cliente = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]

    Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        apellido=apellido,
        direccion=direccion,
        telefono=telefono
    )
    return redirect("clientes")

def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("clientes")

def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarCliente.html", {"cliente": cliente})

def editarCliente(request):
    id_cliente = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.apellido = apellido
    cliente.direccion = direccion
    cliente.telefono = telefono
    cliente.save()
    return redirect("clientes")
