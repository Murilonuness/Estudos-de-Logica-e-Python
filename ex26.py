import random
import datetime
import requests

def buscaSerie():
    url = "https://api.tvmaze.com/shows"
    response = requests.get(url)
    dados = response.json()

    serie = random.choice(dados)
    nome = serie["name"]
    genero = ", ".join(serie["genres"])
    resumo = serie["summary"].replace("<p>", "").replace("</p>", "")

    print(f'Série: {nome}\nGênero: {genero}\nResumo: {resumo}')

def buscaFilme():
    url = "https://api.tvmaze.com/shows"
    response = requests.get(url)
    dados = response.json()

    filmes = [item for item in dados if 
              "TV Movie" in item["genres"] or (item["runtime"] is not None and item["runtime"] > 90)]

    if not filmes:
        print("Nenhum filme encontrado!")
        return

    filme = random.choice(filmes)
    nome = filme["name"]
    genero = ", ".join(filme["genres"])
    resumo = filme["summary"].replace("<p>", "").replace("</p>", "")

    print(f'Filme: {nome}\nGênero: {genero}\nResumo: {resumo}')

def buscaAnime():
    url = "https://api.jikan.moe/v4/top/anime"
    response = requests.get(url)
    dados = response.json()
    anime = dados["data"][0]["title"]
    print(f'Anime Popular: {anime}')

def buscaMusica():
    url = "https://api.deezer.com/chart"
    response = requests.get(url)
    dados = response.json()

    if "tracks" in dados and "data" in dados["tracks"]:
        musica = random.choice(dados["tracks"]["data"])
        nome = musica["title"]
        artista = musica["artist"]["name"]
        print(f'Música: {nome}\nArtista: {artista}')
    else:
        print("Erro ao buscar música!")

def buscaLivro():
    url = "https://openlibrary.org/subjects/science_fiction.json"
    response = requests.get(url)
    dados = response.json()

    if "works" in dados:
        livro = random.choice(dados["works"])
        titulo = livro["title"]
        print(f'Livro: {titulo}')
    else:
        print("Erro ao buscar livro!")

def buscaPrato():
    try:
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
        response = requests.get(url)

        dados = response.json()
        Prato = dados["meals"][0]["strMeal"]
        ingredient1 = dados["meals"][0]["strIngredient1"]
        ingredient2 = dados["meals"][0]["strIngredient2"]
        ingredient3 = dados["meals"][0]["strIngredient3"]
        ingredient4  = dados["meals"][0]["strIngredient4"]

        print(f'Prato: {Prato}')
        print(f'Ingredientes: {ingredient1}, {ingredient2}, {ingredient3}, {ingredient4}')
    except ConnectionError:
        print('Erro com a conexão de api.')

def salvamento(historico):
    try:
        with open('arquivo_ex26.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(historico + '\n')
    except FileNotFoundError:
        print('Arquivo não encontrado!')

def sorteio(opcoes):
    sorteio = input('Digite "sortear" para a roleta sortear um dos afazeres: ').lower().strip()

    if sorteio.lower().strip() == 'sortear':
        escolhido = random.choice(opcoes)
        print(f'A ROLETA SORTEOU!\nO sorteado pela roleta foi {escolhido}!\n')
        historico = f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {escolhido}'
        salvamento(historico)

        if escolhido == 'Prato':
            print('Buscando um prato..\n')
            buscaPrato()
        elif escolhido == 'Filme':
            print('Buscando um filme..\n')
            buscaFilme()
        elif escolhido == 'Série':
            print('Buscando uma série..\n')
            buscaSerie()
        elif escolhido == 'Anime':
            print('Buscando um anime..\n')
            buscaAnime()
        elif escolhido == 'Livro':
            print('Buscando um livro..\n')
            buscaLivro()
        elif escolhido == 'Musica':
            print('Buscando uma música..\n')
            buscaMusica()
        else:
            print("Opção não reconhecida!")
    else:
        print('Comando inválido.')

def roleta():
    print('-' * 30)
    print('Bem vindo a roleta!')
    print('-' * 30)
    opcoes = []
    try:
        while len(opcoes) < 6:
            afazer = input('Digite opções de afazer para hoje.\nOu digite "sair" para finalizar sua sessão.\nComando: ').strip()

            if afazer.lower() == 'sair':
                print('Finalizando sessão..')
                return
            if not afazer:
                print('Nenhuma opção foi cadastrada.')
                break

            opcoes.append(afazer)
            print(f'Opcoes cadastradas: {", ".join(opcoes)}\n')

        if opcoes:
            sorteio(opcoes)
    except:
        print('Erro no menu.')
roleta()