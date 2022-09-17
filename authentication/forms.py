from dataclasses import fields
import email
from django.forms import Form, CharField, FloatField, EmailField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegister(UserCreationForm):

    email = EmailField()
    password1 = CharField(label="Contraseña", widget= PasswordInput)
    password2 = CharField(label="Confirmar Contraseña", widget= PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {"username":"", "email":"", "password1":"", "password2":""}

class UserEditForm(UserCreationForm):

    email = EmailField(label="Modificar E-Mail")
    password1 = CharField(label="Nueva Contraseña", widget= PasswordInput)
    password2 = CharField(label="Confirmar Nueva Contraseña", widget= PasswordInput)
    first_name = CharField(label="Nombre")
    last_name = CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {"username":"", "email":"", "password1":"", "password2":""}

class AvatarForm(Form):

    imagen = ImageField()
    
