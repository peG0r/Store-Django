from django.db import models
from django.contrib.auth import get_user_model
from productos_app.models import Producto
from django.contrib.sessions.models import Session
import uuid

User = get_user_model()


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='carritos')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.usuario:
            return f"Carrito de {self.usuario.username}"
        else:
            return "Carrito sin usuario asociado"



class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='carrito_item')
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE, related_name='items')
    cantidad = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)