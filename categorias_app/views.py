from django.shortcuts import render, redirect
from .models import Categoria

# Create your views here.

def inicio_vistasCategorias (request):
    cat = Categoria.objects.all()

    return render(request, "gestionarCategoria.html",{"miscat": cat})

def registrarCategoria (request):
    id_categoria = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    id_prod = request.POST["txtidprod"]
    desc = request.POST["txtdes"]
    disponible = request.POST["txtdis"]

    guardar= Categoria.objects.create(id_categoria=id_categoria, nombre=nombre, id_prod=id_prod, desc=desc, disponible=disponible)

    return redirect("categoria")

def borrarCategoria (request, id_categoria):
    cat = Categoria.objects.get(id_categoria=id_categoria)
    cat.delete()

    return redirect("categoria")

def seleccionarCategoria(request, id_categoria):
    cat = Categoria.objects.get(id_categoria= id_categoria)
    
    return render (request, "editarCategoria.html", {"miscat":cat})

def editarCategoria(request):
    id_categoria = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    id_prod = request.POST["txtidprod"]
    desc = request.POST["txtdes"]
    disponible = request.POST["txtdis"]
    
    cat = Categoria.objects.get(id_categoria=id_categoria)

    cat.nombre= nombre
    cat.id_prod = id_prod
    cat.desc = desc
    cat.disponible = disponible
    cat.save()
    return redirect("categoria")