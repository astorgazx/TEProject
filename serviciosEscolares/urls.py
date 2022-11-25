from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('registerTramite', views.registerTramite, name='registerTramite'),
    path('showTramites', views.showTramites, name='showTramites'),
    path('editTramite/<int:id>', views.editTramite, name='editTramite'),
    path('delTramite/<int:id>', views.delTramite, name='delTramite'),
]