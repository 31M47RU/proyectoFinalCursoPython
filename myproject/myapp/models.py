from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="static/img/")

    def getNombre(self):
        return self.nombre

    def getDescripcion(self):
        return self.descripcion

    def getPrecio(self):
        return self.precio
    
    def getStock(self):
        return self.stock

    def __str__(self):
        return self.nombre
