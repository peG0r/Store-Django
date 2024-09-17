from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static


class Perfil(models.Model):
    USUARIO_NORMAL = 'NU'
    VENDEDOR = 'VE'

    ROLES_CHOICES = [
        (USUARIO_NORMAL, 'Usuario Normal'),
        (VENDEDOR, 'Vendedor'),
        # Agrega más roles si es necesario
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    rol = models.CharField(max_length=2, choices=ROLES_CHOICES, default=USUARIO_NORMAL)
    
    def __str__(self):
        return self.usuario.username

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return '/static/img/avatar_default.png'

# Si necesitas un modelo separado para permisos específicos, puedes definirlo así:
class PermisoPerfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puede_agregar = models.BooleanField(default=False)
    puede_cambiar = models.BooleanField(default=False)
    puede_eliminar = models.BooleanField(default=False)
    puede_ver = models.BooleanField(default=True)

