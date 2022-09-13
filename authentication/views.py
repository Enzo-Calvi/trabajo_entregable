from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Formularios para crear sesion o crear usuarios.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authentication.forms import UserRegister

# Funciones para autenticar e iniciar sesion.
from django.contrib.auth import login, authenticate, logout


def login_view(request):

    if request.method == "GET":
        formulario = AuthenticationForm()
        return render(request, "authentication/login.html", {"form": formulario})
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("productos_inicio")

        return HttpResponse("Formulario No Valido")

def register_view(request):
    if request.method == "GET":
        formulario = UserRegister()
        return render(request, "authentication/register.html", {"form": formulario})
    
    else:
        formulario = UserRegister(request.POST)

        if formulario.is_valid():
            formulario.save()
        
        return redirect("productos_inicio")

def logout_view(request):

    logout(request)
    return redirect("productos_inicio")