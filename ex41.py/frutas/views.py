from django.shortcuts import render, redirect, get_object_or_404
from .models import Fruta

def listar_adicionar_frutas(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        qtd = int(request.POST['qtd'])

        fruta, criada = Fruta.objects.get_or_create(nome=nome)
        if criada:
            fruta.qtd = qtd
        else:
            fruta.qtd += qtd
        fruta.save()
        return redirect('listar_frutas')

    frutas = Fruta.objects.all()
    return render(request, 'frutas/lista.html', {'frutas': frutas})

def excluir_fruta(request, fruta_id):
    fruta = get_object_or_404(Fruta, id=fruta_id)

    if fruta.qtd > 1:
        fruta.qtd -= 1
        fruta.save()
    else:
        fruta.delete()

    return redirect('listar_frutas')

def deletar_fruta(request, fruta_id):
    fruta = get_object_or_404(Fruta, id=fruta_id)
    fruta.delete()
    return redirect('listar_frutas')