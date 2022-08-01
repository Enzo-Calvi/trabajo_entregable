from datetime import datetime
from django.template import Template, Context
from django.http import HttpResponse

def hello(request):

    return HttpResponse("Hola Coders")

def hora_actual(request):
    hora_a = datetime.now()
    return HttpResponse(f"<h1>{hora_a}</h1>")

def hello_name(request, name, apellido):

    return HttpResponse(f"Hola {name} {apellido}")

def calcular_nacimiento(request, edad):

    anio_actual = 2022
    anio_nacimiento = anio_actual - edad

    return HttpResponse(f"Usted ha nacido en el anio {anio_nacimiento}")

def inicio(request):

    mi_template = open(r"C:\Users\Enzo\Documents\Curso de Python\Trabajo Entregable\trabajo_entregable\templates\index.html", "r")

    plantilla = Template(mi_template.read())

    mi_template.close()

    context = Context()

    documento_a_devolver = plantilla.render(context)

    return HttpResponse(documento_a_devolver)

