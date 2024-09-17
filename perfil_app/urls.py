from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('acceso_denegado', views.acceso_denegado, name='acceso_denegado'),   
    path('create_user/', views.create_user, name='create_user'),
    path('perfil_detalle/<int:user_id>/', views.perfil_detalle, name='perfil_detalle'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout_view'),   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)