from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *

def inicio(request):
    producto = Producto.objects.all()
    return render(request, "html/inicio.html", {'producto': producto})