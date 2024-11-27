from django.shortcuts import render, redirect
from .models import Inventario

# Create your views here.

def inicio_vistasInventarios(request):
    inventarios = Inventario.objects.all()
    return render(request, "gestionarInventario.html", {"inventarios": inventarios})

def registrarInventario(request):
    id_inventario = request.POST["txtid"]
    id_producto = request.POST["txtidproducto"]
    id_proveedor = request.POST["txtidproveedor"]
    estatus = request.POST["txtestatus"]
    disponible = request.POST["txtdisponible"]
    id_sucursal = request.POST["txtidsucursal"]

    Inventario.objects.create(
        id_inventario=id_inventario,
        id_producto=id_producto,
        id_proveedor=id_proveedor,
        estatus=estatus,
        disponible=disponible,
        id_sucursal=id_sucursal
    )
    return redirect("inventarios")

def borrarInventario(request, id_inventario):
    inventario = Inventario.objects.get(id_inventario=id_inventario)
    inventario.delete()
    return redirect("inventarios")

def seleccionarInventario(request, id_inventario):
    inventario = Inventario.objects.get(id_inventario=id_inventario)
    return render(request, "editarInventario.html", {"inventario": inventario})

def editarInventario(request):
    id_inventario = request.POST["txtid"]
    id_producto = request.POST["txtidproducto"]
    id_proveedor = request.POST["txtidproveedor"]
    estatus = request.POST["txtestatus"]
    disponible = request.POST["txtdisponible"]
    id_sucursal = request.POST["txtidsucursal"]

    inventario = Inventario.objects.get(id_inventario=id_inventario)
    inventario.id_producto = id_producto
    inventario.id_proveedor = id_proveedor
    inventario.estatus = estatus
    inventario.disponible = disponible
    inventario.id_sucursal = id_sucursal
    inventario.save()
    return redirect("inventarios")
