from django.contrib import admin
from .models import Producto

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'disponible', 'fecha_creacion')
    list_filter = ('disponible', 'categoria')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('precio', 'stock', 'disponible')