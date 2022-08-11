from django.forms import Form, CharField

class formulariobusqueda(Form):
    nombre_producto = CharField(max_length=150)   