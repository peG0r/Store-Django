from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductoListView.as_view(), name='producto_list'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
    path('productos/crear/', views.producto_create, name='producto_create'),
    path('productos/<int:pk>/editar/', views.producto_edit, name='producto_edit'),
    path('productos/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
]