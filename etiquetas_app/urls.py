from . import views
from django.urls import path


urlpatterns = [

    # URLs para vistas de etiquetas
    path('etiquetas/', views.EtiquetaListView.as_view(), name='etiqueta_list'),
    path('etiquetas/<int:pk>/', views.EtiquetaDetailView.as_view(), name='etiqueta_detalle'),
    path('etiquetas/crear/', views.etiqueta_crear, name='etiqueta_crear'),
    path('etiquetas/<int:pk>/editar/', views.etiqueta_editar, name='etiqueta_editar'),

]
