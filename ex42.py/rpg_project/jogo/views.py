import random
from django.shortcuts import render, redirect
from .forms import PersonagemForm
from .models import Personagem

def criar_personagem(request):
    if request.method == 'POST':
        form = PersonagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_personagens')
    else:
        form = PersonagemForm()
    return render(request, 'jogo/criar_personagem.html', {'form': form})

def listar_personagens(request):
    personagens = Personagem.objects.all()
    return render(request, 'jogo/listar_personagens.html', {'personagens': personagens})

def desafio(request):
    resultado = None
    if request.method == 'POST':
        personagem_id = int(request.POST['personagem'])
        acao = request.POST['acao']

        personagem = Personagem.objects.get(id=personagem_id)

        if acao == 'persuadir':
            atributo = personagem.carisma
        elif acao == 'atacar':
            atributo = personagem.forca
        elif acao == 'resolver':
            atributo = personagem.inteligencia
        else:
            atributo = 0

        dado = random.randint(1, 20)
        total = dado + atributo

        sucesso = total >= 15
        resultado = {
            'personagem': personagem,
            'acao': acao,
            'dado': dado,
            'atributo': atributo,
            'total': total,
            'sucesso': sucesso
        }

    personagens = Personagem.objects.all()
    return render(request, 'jogo/desafio.html', {'personagens': personagens, 'resultado': resultado})