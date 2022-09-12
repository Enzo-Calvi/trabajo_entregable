from multiprocessing import context
from django.shortcuts import render
from productos.models import Zapatilla, camisetas, pantalones
from productos.forms import formularioCamisetas, formularioPantalones, formularioZapatillas, formulariobusqueda
from django.http import HttpResponse

# Create your views here.

# def camiseta(request):
#     camisetas = camisetas(nombre="Air Jordan", marca="Nike", precio="0000")
#     camisetas.save()

#     return HttpResponse("Camiseta Agregada")

# def zapatillas(request):
#     zapatillas = zapatillas(nombre="Air Jordan", marca="Nike", precio="0000")
#     zapatillas.save()

#     return HttpResponse("Camiseta Agregada")

# def pantalon(request):
#     pantalones = pantalones(nombre="Air Jordan", marca="Nike", precio="0000")
#     pantalones.save()

#     return HttpResponse("Pantalon Agregado")


def index(request):
    
    listado_productos = Zapatilla.objects.all()

    if request.GET.get("nombre_producto"):

        formulario = formulariobusqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos = listado_productos.filter(nombre__icontains = data["nombre_producto"])

        return render(request, "productos/index.html", {"productos": listado_productos})

    else:
        formulario = formulariobusqueda()
        return render(request, "productos/index.html", {"productos": listado_productos, "formulario": formulario})

def lista_camisetas(request):
    
    listado_camisetas = camisetas.objects.all()

    if request.GET.get("nombre_producto"):

        formulario = formulariobusqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_camisetas = listado_camisetas.filter(nombre__icontains = data["nombre_producto"])

        return render(request, "productos/index.html", {"productos": listado_camisetas})

    else:
        formulario = formulariobusqueda()
        return render(request, "productos/index.html", {"productos": listado_camisetas, "formulario": formulario})

def zapatillas(request):

    zapatillas = Zapatilla.objects.all()

    if request.method == "GET":
        formulario = formularioZapatillas


        context = {
            "zapatillas": zapatillas,
            "formulario": formulario
        }

        return render(request, "productos/zapatillas.html", context)

    else:
        formulario = formularioZapatillas(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre = data.get("nombre")
            marca = data.get("marca")
            precio = data.get("precio")
            zapatilla = Zapatilla(nombre=nombre, marca=marca, precio=precio)

            zapatilla.save()

        context = {
            "zapatillas": zapatillas,
            "formulario": formulario
        }

        return render(request, "productos/zapatillas.html", context)

def camiseta(request):

    camiseta = camisetas.objects.all()

    if request.method == "GET":
        formulario = formularioCamisetas


        context = {
            "camiseta": camiseta,
            "formulario": formulario,
            "Camiseta": camiseta
        }

        return render(request, "productos/camisetas.html", context)

    else:
        formulario = formularioCamisetas(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre = data.get("nombre")
            marca = data.get("marca")
            precio = data.get("precio")
            camiseta = camisetas(nombre=nombre, marca=marca, precio=precio)

            camiseta.save()

        context = {
            "camiseta": camiseta,
            "formulario": formulario
        }

        return render(request, "productos/camisetas.html", context)

def pantalon(request):

    pantalon = pantalones.objects.all()

    if request.method == "GET":
        formulario = formularioPantalones


        context = {
            "pantalon": pantalon,
            "formulario": formulario
        }

        return render(request, "productos/pantalones.html", context)

    else:
        formulario = formularioPantalones(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre = data.get("nombre")
            marca = data.get("marca")
            precio = data.get("precio")
            pantalon = pantalones(nombre=nombre, marca=marca, precio=precio)

            pantalon.save()

        context = {
            "pantalon": pantalon,
            "formulario": formulario
        }

        return render(request, "productos/pantalones.html", context)