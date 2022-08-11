from django.shortcuts import render
from django.http import HttpResponse
from coder.models import registro_familiar
from django.template import Template, Context, loader

# Create your views here.

def familiares(request):

    familiar = registro_familiar.objects.all()

    lista_familiares_nombres = []

    for resgitro_familiar in familiar:
        lista_familiares_nombres.append(registro_familiar.nombre)
        
        
    return HttpResponse(familiares)

