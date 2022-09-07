from django.urls import path
from productos.views import *

urlpatterns = [ 
    path("", index, name="productos_inicio"),
    path("zapatillas/", zapatillas, name="zapatillas"),
    path("camisetas/", camiseta, name="camisetas"),
    path("pantalones/", pantalon, name="pantalones")
]