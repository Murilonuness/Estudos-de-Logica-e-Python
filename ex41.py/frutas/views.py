from django.shortcuts import render
from .models import Fruta

def listar_frutas(request):
    frutas = Fruta.objects.all()
    return render(request, 'frutas/lista.html', {'frutas': frutas})