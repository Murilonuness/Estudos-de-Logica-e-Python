from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_personagens, name='listar_personagens'),
    path('criar/', views.criar_personagem, name='criar_personagem'),
    path('desafio/', views.desafio, name='desafio'),
    path('acao-mestre/', views.acao_mestre, name='acao_mestre'),
    path('personagem/editar/<int:pk>/', views.editar_personagem, name='editar_personagem'),
    path('personagens/resetar_xp/', views.resetar_xp, name='resetar_xp'),
    path('personagem/resetar_xp/<int:pk>/', views.resetar_xp_personagem, name='resetar_xp_personagem'),
]
