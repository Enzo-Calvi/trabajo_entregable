from django.urls import path
from authentication.views import login_view, register_view, logout_view
from productos.views import editar_usuario

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    
]