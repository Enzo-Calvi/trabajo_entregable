from django.urls import path
from productos.views import *

urlpatterns = [ 
    path("inicio/", index, name="productos_inicio"),
    path("create/", zapatillas, name="zapatillas"),
    path("camisetas/", camiseta, name="camisetas"),
    path("pantalones/", pantalon, name="pantalones")
]