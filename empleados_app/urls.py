from django.urls import path
from empleados_app import views

urlpatterns = [
    path("empleados", views.inicio_vistasEmpleados, name="empleados"),
    path("registrarEmpleado/", views.registrarEmpleado, name="registrarEmpleado"),
    
    path("borrarEmpleado/<id_empleado>", views.borrarEmpleado, name="borrarEmpleado"),
    path("seleccionarEmpleado/<id_empleado>", views.seleccionarEmpleado, name="seleccionarEmpleado"),
    path("editarEmpleado/", views.editarEmpleado, name="editarEmpleado")
]