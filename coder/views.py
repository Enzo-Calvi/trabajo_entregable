from django.shortcuts import render
from django.http import HttpResponse
from coder.models import registro_familiar

# Create your views here.

def registro_familiar(request):

    familiares = registro_familiar.objects.all()

    lista_familiares_nombres = []

    for registro_familiar in familiares:
        lista_familiares_nombres.append(registro_familiar.nombre)
        
    return HttpResponse(familiares.nombre)
