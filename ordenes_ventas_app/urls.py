from django.urls import path
from ordenes_ventas_app import views

urlpatterns = [
    path("ordenes", views.inicio_vistasOrdenes, name="ordenes"),
    path("registrarOrden/", views.registrarOrden, name="registrarOrden"),
    
    path("borrarOrden/<id_orden>", views.borrarOrden, name="borrarOrden"),
    path("seleccionarOrden/<id_orden>", views.seleccionarOrden, name="seleccionarOrden"),
    path("editarOrden/", views.editarOrden, name="editarOrden")
]