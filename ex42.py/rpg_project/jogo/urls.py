from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_personagens, name='listar_personagens'),
    path('criar/', views.criar_personagem, name='criar_personagem'),
    path('desafio/', views.desafio, name='desafio'),
    path('personagem/editar/<int:pk>/', views.editar_personagem, name='editar_personagem'),
]
