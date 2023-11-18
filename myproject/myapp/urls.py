from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio/', RedirectView.as_view(url='/')),
    path('add/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('res/<int:producto_id>/', sacar_del_carrito, name='sacar_del_carrito'),
    path('solicitudes/', solicitudes, name='ver_solicitudes'),
    path('addSoli/', addSolicitud, name='addSoli'),
]
