from django.contrib import admin
from productos.models import Zapatilla, camisetas, pantalones
from authentication.models import Avatar

# Register your models here.
admin.site.register(Zapatilla)

admin.site.register(camisetas)

admin.site.register(pantalones)

admin.site.register(Avatar)


