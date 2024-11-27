from django.urls import path
from inventario_app import views

urlpatterns = [
    path("inventarios", views.inicio_vistasInventarios, name="inventarios"),
    path("registrarInventario/", views.registrarInventario, name="registrarInventario"),
    
    path("borrarInventario/<id_inventario>", views.borrarInventario, name="borrarInventario"),
    path("seleccionarInventario/<id_inventario>", views.seleccionarInventario, name="seleccionarInventario"),
    path("editarInventario/", views.editarInventario, name="editarInventario")
]