from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_adicionar_frutas, name='listar_frutas'),
]
