from django.urls import path
from sucursales_app import views

urlpatterns = [
    path("sucursales", views.inicio_vistasSucursales, name="sucursales"),
    path("registrarSucursal/", views.registrarSucursal, name="registrarSucursal"),
    
    path("borrarSucursal/<id_sucursal>", views.borrarSucursal, name="borrarSucursal"),
    path("seleccionarSucursal/<id_sucursal>", views.seleccionarSucursal, name="seleccionarSucursal"),
    path("editarSucursal/", views.editarSucursal, name="editarSucursal")
]