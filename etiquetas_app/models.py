from django.db import models

# Create your models here.

class Etiqueta(models.Model):
    from productos_app.models import Producto

    nombre = models.CharField(max_length=100)
    productos = models.ManyToManyField(Producto)
    
    def __str__(self):
        return self.nombre


    