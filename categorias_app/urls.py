from django.urls import path
from categorias_app import views

urlpatterns = [
    path("categoria", views.inicio_vistasCategorias, name="categoria"),
    path("registrarCategoria/", views.registrarCategoria, name="registrarCategoria"),
    
    path("borrarCategoria/<id_categoria>", views.borrarCategoria, name="borrarCategoria"),
    path("seleccionarCategoria/<id_categoria>", views.seleccionarCategoria, name="seleccionarCategoria"),
    path("editarCategoria/", views.editarCategoria, name="editarCategoria")
]