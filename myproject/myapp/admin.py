from django.contrib import admin
from myapp.models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Solicitud)
admin.site.register(ItemCarrito)