"""trabajo_entregable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trabajo_entregable.views import hello, hora_actual, hello_name, calcular_nacimiento, inicio
from coder.views import lista_familiares 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello),
    path("hora/", hora_actual),
    path("hello/<name>/<apellido>", hello_name),
    path("calcular_edad/<int:edad>/", calcular_nacimiento),
    path("familiares/", lista_familiares),
    path("inicio/", inicio),
    
]
