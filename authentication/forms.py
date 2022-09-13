from dataclasses import fields
import email
from django.forms import Form, CharField, FloatField, EmailField, PasswordInput
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
