from django.urls import path
from productos_app import views

urlpatterns = [
    path("productos", views.inicio_vistasProductos, name="productos"),
    path("registrarProducto/", views.registrarProducto, name="registrarProducto"),
    
    path("borrarProducto/<id_producto>", views.borrarProducto, name="borrarProducto"),
    path("seleccionarProducto/<id_producto>", views.seleccionarProducto, name="seleccionarProducto"),
    path("editarProducto/", views.editarProducto, name="editarProducto")
]