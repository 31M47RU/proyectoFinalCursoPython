from django.urls import path
from django.views.generic import RedirectView
from django.http import HttpResponse
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio/', RedirectView.as_view(url='/')),
    path('add/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('res/<int:producto_id>/', sacar_del_carrito, name='sacar_del_carrito'),
    path('solicitudes/', solicitudes, name='ver_solicitudes'),
    path('addSoli/', addSolicitud, name='addSoli'),
    path('conSoli/<int:solicitud_id>/', confirmar_solicitud, name='confirmar_solicitud'),
    path('canSoli/<int:solicitud_id>/', cancelar_solicitud, name='cancelar_solicitud'),
]
