from django.shortcuts import render
from productos.models import producto, camisetas, pantalones
from productos.forms import formulariobusqueda
from productos.forms import formulariodecreacion
from django.http import HttpResponse

# Create your views here.

def camiseta(request):
    camisetas = camisetas(nombre="Air Jordan", marca="Nike", precio="0000")
    camisetas.save()

    return HttpResponse("Camiseta Agregada")

def zapatillas(request):
    zapatillas = zapatillas(nombre="Air Jordan", marca="Nike", precio="0000")
    zapatillas.save()

    return HttpResponse("Camiseta Agregada")

def pantalon(request):
    pantalones = pantalones(nombre="Air Jordan", marca="Nike", precio="0000")
    pantalones.save()

    return HttpResponse("Pantalon Agregado")


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

            return render(request, "productos/create.html")

    else:
        camiseta = formulariodecreacion()
        return render(request, "productos/create.html", {"prendas": camiseta})
    return render(request, "productos/create.html", {"prendas": prendas})
