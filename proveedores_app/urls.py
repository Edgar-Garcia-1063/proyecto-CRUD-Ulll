from django.urls import path
from proveedores_app import views

urlpatterns = [
    path("proveedores", views.inicio_vistasProveedores, name="proveedores"),
    path("registrarProveedor/", views.registrarProveedor, name="registrarProveedor"),
    
    path("borrarProveedor/<id_proveedor>", views.borrarProveedor, name="borrarProveedor"),
    path("seleccionarProveedor/<id_proveedor>", views.seleccionarProveedor, name="seleccionarProveedor"),
    path("editarProveedor/", views.editarProveedor, name="editarProveedor")
]