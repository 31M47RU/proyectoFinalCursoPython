from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Sum

"""
ZONA DE RENDERS DE PAGINAS HTML
"""

def inicio(request):
    productos = Producto.objects.all()
    carrito = Carrito.objects.first()
    return render(request, "html/inicio.html", {'productos': productos, 'carrito': carrito})

def solicitudes(request):
    solicitudes = Solicitud.objects.annotate(precio_total=Sum('carrito__itemcarrito__cantidad' * 'carrito__itemcarrito__producto__precio')).all()
    return render(request, 'html/solicitudes.html', {'solicitudes': solicitudes})

"""
ACCIONES PARA MODIFICAR EL CARRITO DE COMPRA
"""

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    carrito, creado = Carrito.objects.get_or_create()
    
    item_carrito, _ = ItemCarrito.objects.get_or_create(producto=producto, carrito=carrito)
    item_carrito.cantidad += 1
    item_carrito.save()

    return redirect('/inicio')
    
def sacar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    carrito, creado = Carrito.objects.get_or_create()
    
    item_carrito, _ = ItemCarrito.objects.get_or_create(producto=producto, carrito=carrito)
    if int(item_carrito.cantidad) <= 0: pass
    else: item_carrito.cantidad = int(item_carrito.cantidad) - 1
    item_carrito.save()

    return redirect('/inicio')


"""
ACCIONES PARA LAS SOLICITUDES DE COMPRA
"""

def addSolicitud(request):
    carrito = Carrito.objects.first()
    solicitud = Solicitud.objects.create(carrito=carrito)

    productos_html = "<ul style='list-style:none;'>"
    for item_carrito in carrito.itemcarrito_set.all():
        productos_html += f"<li>{item_carrito.producto.nombre}</li>"
    productos_html += "</ul>"

    solicitud.productos = productos_html
    solicitud.save()

    carrito.itemcarrito_set.all().delete()

    return redirect('/inicio')


def confirmar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    
    productos_en_solicitud = solicitud.productos.split(',')

    for producto_nombre in productos_en_solicitud:
        producto = get_object_or_404(Producto, nombre=producto_nombre.strip())

        carrito = get_object_or_404(Carrito, producto=producto)

        producto.stock -= carrito.cantidad
        producto.save()

        carrito.delete()

    solicitud.delete()

    return redirect('ver_solicitudes')

def cancelar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    solicitud.delete()

    return redirect('ver_solicitudes')
