
from multiprocessing import context
from django.shortcuts import render, redirect
from productos.models import Zapatilla, camisetas, pantalones
from productos.forms import formularioCamisetas, formularioPantalones, formularioZapatillas, formulariobusqueda
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authentication.models import Avatar
from authentication.forms import UserEditForm, AvatarForm
from django.contrib.auth.models import User


# Create your views here.


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

@login_required
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

        formulario = formularioZapatillas()
        context = {
            "zapatillas": zapatillas,
            "formulario": formulario
        }

        return render(request, "productos/zapatillas.html", context)

@login_required
def Camisetas(request):

    Camisetas = camisetas.objects.all()

    if request.method == "GET":
        formulario = formularioCamisetas


        context = {
            "camiseta": Camisetas,
            "formulario": formulario,
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

        formulario = formularioCamisetas()
        context = {
            "camiseta": Camisetas,
            "formulario": formulario
        }

        return render(request, "productos/camisetas.html", context)

@login_required
def Pantalones(request):

    Pantalones = pantalones.objects.all()

    if request.method == "GET":
        formulario = formularioPantalones


        context = {
            "pantalon": Pantalones,
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

        formulario = formularioPantalones()
        context = {
            "pantalon": Pantalones,
            "formulario": formulario
        }

        return render(request, "productos/pantalones.html", context)

def leerZapatillas(request):

    zapatillas = Zapatilla.objects.all()

    contexto = {"zapatillas": zapatillas}

    return render (request, "productos/zapatillas.html", contexto)

def leerCamisetas(request):

    camiseta = camisetas.objects.all()

    contexto = {"camiseta": camiseta}

    return render (request, "productos/camisetas.html", contexto)

def leerPantalones(request):

    pantalon = pantalones.objects.all()

    contexto = {"pantalon": pantalon}

    return render (request, "productos/pantalones.html", contexto)

def eliminarZapatillas(request, id_zapatilla):

    try:
        zapatilla = Zapatilla.objects.get(id=id_zapatilla)
        
        zapatilla.delete()

        return redirect("zapatillas")
    except:
        return redirect("zapatillas")

def eliminarCamisetas(request, id_camiseta):

    try:
        camiseta = camisetas.objects.get(id=id_camiseta)
        
        camiseta.delete()

        return redirect("camisetas")
    except:
        return redirect("camisetas")

def eliminarPantalones(request, id_pantalon):

    try:
        pantalon = pantalones.objects.get(id=id_pantalon)
        
        pantalon.delete()

        return redirect("pantalones")
    except:
        return redirect("pantalones")

def actualizarZapatillas(request, id_zapatilla):

    if request.method == "GET":
        formulario = formularioZapatillas()
        contexto = {
            "formulario": formulario
        }
    
        return render(request, "productos/zapatillas.html", contexto)

    else: 
        formulario = formularioZapatillas(request.POST)

        if formulario.is_valid(): 
            data = formulario.cleaned_data
            
            try:
                zapatilla = Zapatilla.objects.get(id=id_zapatilla)

                zapatilla.nombre = data.get("nombre")
                zapatilla.marca = data.get("marca")
                zapatilla.precio = data.get("precio")
                zapatilla.save()

            except:
                return HttpResponse("Error en la Actualizacion")

        return redirect("zapatillas")

def actualizarCamisetas(request, id_camisetas):

    if request.method == "GET":
        formulario = formularioCamisetas()
        contexto = {
            "formulario": formulario
        }
    
        return render(request, "productos/camisetas.html", contexto)

    else: 
        formulario = formularioCamisetas(request.POST)

        if formulario.is_valid(): 
            data = formulario.cleaned_data
            
            try:
                camiseta = camisetas.objects.get(id=id_camisetas)

                camiseta.nombre = data.get("nombre")
                camiseta.marca = data.get("marca")
                camiseta.precio = data.get("precio")
                camiseta.save()

            except:
                return HttpResponse("Error en la Actualizacion")

        return redirect("camisetas")

def actualizarPantalones(request, id_pantalones):

    if request.method == "GET":
        formulario = formularioPantalones()
        contexto = {
            "formulario": formulario
        }
    
        return render(request, "productos/pantalones.html", contexto)

    else: 
        formulario = formularioPantalones(request.POST)

        if formulario.is_valid(): 
            data = formulario.cleaned_data
            
            try:
                pantalon = pantalones.objects.get(id=id_pantalones)

                pantalon.nombre = data.get("nombre")
                pantalon.marca = data.get("marca")
                pantalon.precio = data.get("precio")
                pantalon.save()

            except:
                return HttpResponse("Error en la Actualizacion")

        return redirect("pantalones")

@login_required
def editar_usuario(request):

    if request.method == "GET":
        form = UserEditForm(initial={"email": request.user.email, "username": request.user.username, "password1":"", "password2":""})
        return render(request, "productos/cambio_usuario.html", {"form": form})
    else:
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = request.user
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()
            return redirect("productos_inicio")
        else:
            return render(request, "productos/cambio_usuario.html", {"form": form})

@login_required
def inicio(request):

    avatar = Avatar.objects.filter(usuario=request.user).first()

    context = {
        "imagen": avatar.imagen.url
    }
    
    return render(request, "productos/productos.html",context)

def agregar_avatar(request):

    if request.method == "GET":
        form = AvatarForm()
        contexto = {"form":form}
        return render(request, "productos/agregar_avatar.html", contexto)
    else:
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            usuario = User.objects.filter(username = request.user.username).first()
            avatar = Avatar(usuario = usuario, imagen = data["imagen"])

            avatar.save()

            return redirect("productos_inicio",)