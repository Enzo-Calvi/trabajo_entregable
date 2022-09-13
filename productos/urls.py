from django.urls import path
from productos.views import *

urlpatterns = [ 
    path("", index, name="productos_inicio"),
    path("zapatillas/", zapatillas, name="zapatillas"),
    path("camisetas/", Camisetas, name="camisetas"),
    path("pantalones/", Pantalones, name="pantalones"),
    path("zapatillas/", leerZapatillas, name="LeerZapatillas"),
    path("camisetas/", leerCamisetas, name="LeerCamisetas"),
    path("pantalones/", leerPantalones, name="LeerPantalones"),
    path("zapatillas/borrar/<id_zapatilla>", eliminarZapatillas, name="EliminarZapatillas"),
    path("camisetas/borrar/<id_camiseta>", eliminarCamisetas, name="EliminarCamisetas"),
    path("pantalon/borrar/<id_pantalon>", eliminarPantalones, name="EliminarPantalones"),
    path("zapatillas/editar/<id_zapatilla>", actualizarZapatillas, name="EditarZapatillas"),
    path("camisetas/editar/<id_camisetas>", actualizarCamisetas, name="EditarCamisetas"),
    path("pantalones/editar/<id_pantalones>", actualizarPantalones, name="EditarPantalones")
    ]