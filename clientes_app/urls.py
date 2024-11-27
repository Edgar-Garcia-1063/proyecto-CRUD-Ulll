from django.urls import path
from clientes_app import views

urlpatterns = [
    path("clientes", views.inicio_vistasClientes, name="clientes"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente"),
    
    path("borrarCliente/<id_cliente>", views.borrarCliente, name="borrarCliente"),
    path("seleccionarCliente/<id_cliente>", views.seleccionarCliente, name="seleccionarCliente"),
    path("editarCliente/", views.editarCliente, name="editarCliente")
]