from django.shortcuts import render
from productos.models import producto
from productos.forms import formulariobusqueda
from productos.forms import formulariodecreacion

# Create your views here.

def index(request):
    
    listado_productos = producto.objects.all()

    if request.GET.get("nombre_producto"):

        formulario = formulariobusqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos = listado_productos.filter(nombre__icontains = data["nombre_producto"])

        return render(request, "productos/index.html", {"productos": listado_productos})

    else:
        formulario = formulariobusqueda()
        return render(request, "productos/index.html", {"productos": listado_productos, "formulario": formulario})

def productos(request):

    if request.method == "POST":

        prendas = formulariodecreacion(request.POST)

        print(prendas)

        if prendas.is_valid():
            informacion = prendas.cleaned_data

            camiseta = formulariodecreacion (nombre=informacion["nombre"], marca=informacion["marca"], precio=informacion["precio"])

            camiseta.save()

            return render(request, "productos/index.html")

    else:
        camiseta = formulariodecreacion()
        return render(request, "productos/productos.html", {"prendas": camiseta})
    return render(request, "productos/productos.html", {"prendas": prendas})
