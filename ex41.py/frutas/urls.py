from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_adicionar_frutas, name='listar_frutas'),
    path('excluir/<int:fruta_id>/', views.excluir_fruta, name='excluir_fruta'),
    path('deletar/<int:fruta_id>/', views.deletar_fruta, name='deletar_fruta'),
    path('editar/<int:fruta_id>/', views.editar_fruta, name='editar_fruta'),
]
