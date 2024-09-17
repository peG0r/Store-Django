from django.urls import path
from . import views

urlpatterns = [    
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_lista'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detalle'),
    path('categoria_crear/', views.categoria_crear, name='categoria_crear'),
    path('categorias/<int:pk>/editar/', views.categoria_editar, name='categoria_editar'),
]

