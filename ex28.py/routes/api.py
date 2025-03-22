from flask import Flask, render_template, request, Blueprint
import random
import requests

api = Blueprint('api', __name__)

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@api.route("/", methods=["GET", "POST"])
def roleta():
    if request.method == "POST":
        afazeres = [request.form.get(f"afazer{i}") for i in range(1, 7)]
        afazeres = [a for a in afazeres if a]

        if afazeres:
            sorteado = random.choice(afazeres)

            resultado = {"tipo": "Afazer", "nome": sorteado}

            if sorteado.lower() == "filme":
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
            elif sorteado.lower() == "série":
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
            elif sorteado.lower() == "anime":
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
            elif sorteado.lower() == "música":
                url = "https://api.deezer.com/chart"
                dados = fetch_data(url)
                if dados and "tracks" in dados and "data" in dados["tracks"]:
                    musica = random.choice(dados["tracks"]["data"])
                    resultado = {
                        "tipo": "Música",
                        "nome": musica["title"],
                        "artista": musica["artist"]["name"],
                    }
            elif sorteado.lower() == "livro":
                url = "https://openlibrary.org/subjects/science_fiction.json"
                dados = fetch_data(url)
                if dados and "works" in dados:
                    livro = random.choice(dados["works"])
                    resultado = {
                        "tipo": "Livro",
                        "nome": livro["title"],
                        "autor": livro.get("author_name", "Desconhecido"),
                    }
            elif sorteado.lower() == "prato":
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

            return render_template("roleta.html", resultado=resultado)

    return render_template("roleta.html", resultado=None)

@api.route('/dados')
def get_dados():
    return "API para dados externa"