from django.forms import Form, CharField, FloatField

class formulariobusqueda(Form):
    nombre_producto = CharField(max_length=150)   


class formularioZapatillas(Form):
    nombre = CharField(max_length=150)
    marca = CharField(max_length=150)
    precio = FloatField()

class formularioPantalones(Form):
    nombre = CharField(max_length=150)
    marca = CharField(max_length=150)
    precio = FloatField()

class formularioCamisetas(Form):
    nombre = CharField(max_length=150)
    marca = CharField(max_length=150)
    precio = FloatField()