from django.shortcuts import render, redirect
from .models import Fruta

def listar_adicionar_frutas(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        qtd = request.POST['qtd']
        Fruta.objects.create(nome=nome, qtd=qtd)
        return redirect('listar_frutas')

    frutas = Fruta.objects.all()
    return render(request, 'frutas/lista.html', {'frutas': frutas})