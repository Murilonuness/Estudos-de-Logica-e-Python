from flask import Blueprint, render_template, request
import random
import datetime
import requests
from routes.historico import salvamento

roleta = Blueprint('roleta', __name__)

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@roleta.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        opcoes = [
            request.form.get('afazer1'),
            request.form.get('afazer2'),
            request.form.get('afazer3'),
            request.form.get('afazer4'),
            request.form.get('afazer5'),
            request.form.get('afazer6'),
        ]

        opcoes = [op for op in opcoes if op]

        if not opcoes:
            return render_template('roleta.html', mensagem='Nenhuma opção foi cadastrada.')

        escolhido = random.choice(opcoes)
        historico = f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {escolhido}'
        
        salvamento(historico)

        resultado = {"tipo": "Afazer", "nome": escolhido}

        if escolhido.lower() == "filme":
            url = "https://api.tvmaze.com/shows"
            dados = fetch_data(url)
            if dados:
                filme = random.choice(dados)
                resultado = {
                    "tipo": "Filme",
                    "nome": filme["name"],
                    "genero": ", ".join(filme["genres"]),
                    "resumo": filme["summary"].replace("<p>", "").replace("</p>", ""),
                }

        elif escolhido.lower() == "série":
            url = "https://api.tvmaze.com/shows"
            dados = fetch_data(url)
            if dados:
                serie = random.choice(dados)
                resultado = {
                    "tipo": "Série",
                    "nome": serie["name"],
                    "genero": ", ".join(serie["genres"]),
                    "resumo": serie["summary"].replace("<p>", "").replace("</p>", ""),
                }

        elif escolhido.lower() == "anime":
            url = "https://api.jikan.moe/v4/top/anime"
            dados = fetch_data(url)
            if dados and "data" in dados:
                anime = random.choice(dados["data"])
                resultado = {
                    "tipo": "Anime",
                    "nome": anime["title"],
                    "genero": ", ".join([genre["name"] for genre in anime["genres"]]),
                    "resumo": anime.get("synopsis", "Não disponível"),
                }

        elif escolhido.lower() == "música":
            url = "https://api.deezer.com/chart"
            dados = fetch_data(url)
            if dados and "tracks" in dados and "data" in dados["tracks"]:
                musica = random.choice(dados["tracks"]["data"])
                resultado = {
                    "tipo": "Música",
                    "nome": musica["title"],
                    "artista": musica["artist"]["name"],
                }

        elif escolhido.lower() == "livro":
            url = "https://openlibrary.org/subjects/science_fiction.json"
            dados = fetch_data(url)
            if dados and "works" in dados:
                livro = random.choice(dados["works"])
                resultado = {
                    "tipo": "Livro",
                    "nome": livro["title"],
                    "autor": livro.get("author_name", "Desconhecido"),
                }
        elif escolhido.lower() == "prato":
            url = "https://www.themealdb.com/api/json/v1/1/random.php"
            dados = fetch_data(url)
            if dados and "meals" in dados:
                prato = dados["meals"][0]
                resultado = {
                    "tipo": "Prato",
                    "nome": prato["strMeal"],
                    "ingredientes": [
                        prato[f"strIngredient{i}"] for i in range(1, 21) if prato[f"strIngredient{i}"]
                    ],
                    "instrucao": prato["strInstructions"],
                }

        return render_template('roleta.html', resultado=resultado)

    return render_template('roleta.html')
