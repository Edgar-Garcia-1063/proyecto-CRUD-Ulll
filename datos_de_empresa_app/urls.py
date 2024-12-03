from django.urls import path
from datos_de_empresa_app import views

urlpatterns = [
    path("datos", views.inicio_vistasDatos, name="datos"),
    path("registrarDatos/", views.registrarDatos, name="registrarDatos"),
    path("borrarDatos/<id_empresa>", views.borrarDatos, name="borrarDatos"),
    path("seleccionarDatos/<id_empresa>", views.seleccionarDatos, name="seleccionarDatos"),
    path("editarDatos/", views.editarDatos, name="editarDatos")
]