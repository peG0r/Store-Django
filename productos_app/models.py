from django.db import models
from django.utils import timezone
from categoria_app.models import Categoria



class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    descripcion = models.TextField(default='Sin descripción.')
    stock = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(default=timezone.now) 
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    @property
    def imagen_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        return '/static/img/producto_default.png'
