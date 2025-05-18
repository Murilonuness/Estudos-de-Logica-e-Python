from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start_timer, name='start'),
    path('pause/', views.pause_timer, name='pause'),
    path('edit/', views.edit_timer, name='edit'),
    path('fullscreen/', views.fullscreen_view, name='fullscreen'),
]
