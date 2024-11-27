from django.shortcuts import render, redirect
from .models import Proveedor

# Create your views here.

def inicio_vistasProveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "gestionarProveedor.html", {"proveedor": proveedores})

def registrarProveedor(request):
    id_proveedor = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    contacto = request.POST["txtcontacto"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    direccion = request.POST["txtdireccion"]

    Proveedor.objects.create(
        id_proveedor=id_proveedor,
        nombre=nombre,
        contacto=contacto,
        telefono=telefono,
        email=email,
        direccion=direccion
    )
    return redirect("proveedores")

def borrarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()
    return redirect("proveedores")

def seleccionarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request, "editarProveedor.html", {"proveedor": proveedor})

def editarProveedor(request):
    id_proveedor = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    contacto = request.POST["txtcontacto"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    direccion = request.POST["txtdireccion"]

    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre = nombre
    proveedor.contacto = contacto
    proveedor.telefono = telefono
    proveedor.email = email
    proveedor.direccion = direccion
    proveedor.save()
    return redirect("proveedores")
