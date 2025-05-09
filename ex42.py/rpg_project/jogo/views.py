import random
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonagemForm
from .models import Personagem, DesafioCenario
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
    acoes_disponiveis = {
        'força': {'atributo': 'forca'},
        'inteligência': {'atributo': 'inteligencia'},
        'carisma': {'atributo': 'carisma'},
        'destreza': {'atributo': 'destreza'},
    }

    resultado = None


    if request.method == 'POST':
        if 'descricao' in request.POST and 'acao' in request.POST and 'dificuldade' in request.POST:
            descricao = request.POST.get('descricao')
            acao = request.POST.get('acao')
            dificuldade = int(request.POST.get('dificuldade'))

            DesafioCenario.objects.create(
                descricao=descricao,
                acao=acao,
                dificuldade=dificuldade
            )
            return redirect('desafio')

        elif 'personagem' in request.POST and 'desafio_id' in request.POST:
            personagem_id = int(request.POST['personagem'])
            desafio_id = int(request.POST['desafio_id'])

            desafio_obj = DesafioCenario.objects.get(id=desafio_id)
            personagem = Personagem.objects.get(id=personagem_id)

            acao = desafio_obj.acao.lower()
            atributo_nome = acoes_disponiveis.get(acao, {}).get('atributo')
            atributo = getattr(personagem, atributo_nome, 0)

            dado = random.randint(1, 20)
            total = dado + atributo
            sucesso = total >= desafio_obj.dificuldade

            if sucesso:
                personagem.ganhar_xp(50)

            desafio_obj.resolvido = True
            desafio_obj.personagem_resolveu = personagem
            desafio_obj.sucesso = sucesso
            desafio_obj.dado = dado
            desafio_obj.total = total
            desafio_obj.save()

            resultado = {
                'personagem': personagem,
                'acao': acao,
                'dado': dado,
                'atributo': atributo,
                'total': total,
                'sucesso': sucesso,
                'descricao': desafio_obj.descricao,
                'dificuldade': desafio_obj.dificuldade
            }

    personagens = Personagem.objects.all()
    desafios = DesafioCenario.objects.filter(resolvido=False)

    return render(request, 'jogo/desafio.html', {
        'personagens': personagens,
        'desafios': desafios,
        'resultado': resultado
    })

def acao_mestre(request):
    resultado = None

    acoes_disponiveis = {
        'persuadir': {'atributo': 'carisma', 'nome': 'Persuadir'},
        'atacar': {'atributo': 'forca', 'nome': 'Atacar'},
        'resolver': {'atributo': 'inteligencia', 'nome': 'Resolver Enigma'},
        'esquivar': {'atributo': 'destreza', 'nome': 'Esquivar'},
        'furtar': {'atributo': 'destreza', 'nome': 'Furtar'},
        'perceber': {'atributo': 'sabedoria', 'nome': 'Perceber'},
        'resistir': {'atributo': 'sabedoria', 'nome': 'Resistir'},
        'suportar': {'atributo': 'constituicao', 'nome': 'Suportar Dor'},
        'intimidar': {'atributo': 'carisma', 'nome': 'Intimidar'},
        'investigar': {'atributo': 'inteligencia', 'nome': 'Investigar'},
        'esmagar': {'atributo': 'forca', 'nome': 'Esmagar'}
    }

    if request.method == 'POST':
        personagem_id = int(request.POST['personagem'])
        acao = request.POST['acao']
        dificuldade = int(request.POST.get('dificuldade', 15))

        personagem = get_object_or_404(Personagem, pk=personagem_id)
        atributo_nome = acoes_disponiveis.get(acao, {}).get('atributo')
        atributo = getattr(personagem, atributo_nome, 0) if atributo_nome else 0

        dado = random.randint(1, 20)
        total = dado + atributo
        sucesso = total >= dificuldade

        if sucesso:
            personagem.ganhar_xp(50)

        resultado = {
            'personagem': personagem,
            'acao': acao,
            'nome_acao': acoes_disponiveis.get(acao, {}).get('nome', 'Ação'),
            'dificuldade': dificuldade,
            'dado': dado,
            'atributo': atributo,
            'total': total,
            'sucesso': sucesso
        }

    personagens = Personagem.objects.all()
    return render(request, 'jogo/acao_mestre.html', {
        'personagens': personagens,
        'acoes_disponiveis': acoes_disponiveis,
        'resultado': resultado
    })

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