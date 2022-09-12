from django.urls import path
from productos.views import *

urlpatterns = [ 
    path("", index, name="productos_inicio"),
    path("zapatillas/", zapatillas, name="zapatillas"),
    path("camisetas/", camiseta, name="camisetas"),
    path("pantalones/", pantalon, name="pantalones"),
    path("zapatillas/", leerZapatillas, name="LeerZapatillas"),
    path("camisetas/", leerCamisetas, name="LeerCamisetas"),
    path("pantalones/", leerPantalones, name="LeerPantalones")
]