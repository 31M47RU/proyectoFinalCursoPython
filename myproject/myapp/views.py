from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *

def inicio(request):
    producto = Producto.objects.all()
    return render(request, "html/inicio.html", {'producto': producto})

def carrito(request):
    carrito = Carrito.objects.all()
    return render(request, "html/carrito.html", {'carrito': carrito})