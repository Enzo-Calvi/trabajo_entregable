from django.forms import Form, CharField, FloatField

class formulariobusqueda(Form):
    nombre_producto = CharField(max_length=150)   


class formulariodecreacion(Form):
    nombre = CharField(max_length=150)
    marca = CharField(max_length=150)
    precio = FloatField()