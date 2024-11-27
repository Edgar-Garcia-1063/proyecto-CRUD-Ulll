from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.

def inicio_vistasProductos(request):
    productos = Producto.objects.all()
    return render(request, "gestionarProducto.html", {"producto": productos})

def registrarProducto(request):
    id_producto = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    marca = request.POST["txtmarca"]
    modelo = request.POST["txtmodelo"]
    talla = request.POST["txttalla"]
    id_proveedor = request.POST["txtidprov"]
    precio = request.POST["txtprecio"]

    Producto.objects.create(
        id_producto=id_producto,
        nombre=nombre,
        marca=marca,
        modelo=modelo,
        talla=talla,
        id_proveedor=id_proveedor,
        precio=precio
    )
    return redirect("productos")

def borrarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("productos")

def seleccionarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    return render(request, "editarProducto.html", {"producto": producto})

def editarProducto(request):
    id_producto = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    marca = request.POST["txtmarca"]
    modelo = request.POST["txtmodelo"]
    talla = request.POST["txttalla"]
    id_proveedor = request.POST["txtidprov"]
    precio = request.POST["txtprecio"]

    producto = Producto.objects.get(id_producto=id_producto)
    producto.nombre = nombre
    producto.marca = marca
    producto.modelo = modelo
    producto.talla = talla
    producto.id_proveedor = id_proveedor
    producto.precio = precio
    producto.save()
    return redirect("productos")
