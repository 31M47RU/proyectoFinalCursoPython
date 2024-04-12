from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="static/img/")

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    productos = models.ManyToManyField(Producto, through='ItemCarrito')

    def __str__(self):
        return f"Carrito {self.id}"

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.carrito} - {self.producto} - Cantidad: {self.cantidad}"

    
class Solicitud(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ItemSolicitud')

    def obtener_productos(self):
        return self.productos.all()

    def calcular_precio_total(self):
        return sum(item.cantidad * item.producto.precio for item in self.itemsolicitud_set.all())

    def __str__(self):
        return f"Solicitud {self.id}"


class ItemSolicitud(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.solicitud} - {self.producto} - Cantidad: {self.cantidad}"

