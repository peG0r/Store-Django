from django.urls import path
from . import views

urlpatterns = [
    path('ver_carrito//', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('actualizar/<int:carrito_producto_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('eliminar/<int:carrito_producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]
