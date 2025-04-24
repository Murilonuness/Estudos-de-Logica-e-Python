from django.urls import path
from .views import listar_frutas

urlpatterns = [
    path('', listar_frutas, name='lista_frutas'),
]
