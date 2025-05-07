import random
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonagemForm
from .models import Personagem
from django.contrib import messages


def criar_personagem(request):
    if request.method == 'POST':
        form = PersonagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_personagens')
    else:
        form = PersonagemForm()
    return render(request, 'jogo/criar_personagem.html', {'form': form})

def editar_personagem(request, pk):
    personagem = Personagem.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = PersonagemForm(request.POST, instance=personagem)
        if form.is_valid():
            form.save()
            return redirect('listar_personagens')
    else:
        form = PersonagemForm(instance=personagem)
    
    return render(request, 'jogo/editar_personagem.html', {'form': form})

def listar_personagens(request):
    personagens = Personagem.objects.all()
    
    personagens_info = []
    for p in personagens:
        xp_necessario = (p.nivel + 1) * 100
        progresso = (p.experiencia / xp_necessario) * 100 if xp_necessario > 0 else 0
        personagens_info.append({
            'personagem': p,
            'xp_necessario': xp_necessario,
            'progresso': round(progresso, 2)
        })

    return render(request, 'jogo/listar_personagens.html', {'personagens_info': personagens_info})

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

        if sucesso:
            personagem.ganhar_xp(50)

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


def resetar_xp(request):
    personagens = Personagem.objects.all()
    for personagem in personagens:
        personagem.experiencia = 0
        personagem.save()
    messages.success(request, "Experiência de todos os personagens foi resetada com sucesso.")
    return redirect('listar_personagens')

def resetar_xp_personagem(request, pk):
    personagem = get_object_or_404(Personagem, pk=pk)
    personagem.experiencia = 0
    personagem.save()
    messages.success(request, f"A experiência de {personagem.nome} foi resetada com sucesso.")
    return redirect('listar_personagens')