from django.shortcuts import render, redirect
from .models import Orden

# Create your views here.

def inicio_vistasOrdenes(request):
    ordenes = Orden.objects.all()
    return render(request, "gestionarOrden.html", {"orden": ordenes})

def registrarOrden(request):
    id_orden = request.POST["txtid"]
    id_cliente = request.POST["txtidcliente"]
    fecha = request.POST["txtfecha"]
    total = request.POST["txttotal"]
    metodo_pago = request.POST["txtmetodo"]

    Orden.objects.create(
        id_orden=id_orden,
        id_cliente=id_cliente,
        fecha=fecha,
        total=total,
        metodo_pago=metodo_pago
    )
    return redirect("ordenes")

def borrarOrden(request, id_orden):
    orden = Orden.objects.get(id_orden=id_orden)
    orden.delete()
    return redirect("ordenes")

def seleccionarOrden(request, id_orden):
    orden = Orden.objects.get(id_orden=id_orden)
    return render(request, "editarOrden.html", {"orden": orden})

def editarOrden(request):
    id_orden = request.POST["txtid"]
    id_cliente = request.POST["txtidcliente"]
    fecha = request.POST["txtfecha"]
    total = request.POST["txttotal"]
    metodo_pago = request.POST["txtmetodo"]

    orden = Orden.objects.get(id_orden=id_orden)
    orden.id_cliente = id_cliente
    orden.fecha = fecha
    orden.total = total
    orden.metodo_pago = metodo_pago
    orden.save()
    return redirect("ordenes")
