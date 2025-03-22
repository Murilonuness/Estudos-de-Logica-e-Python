from flask import Blueprint, render_template

erro = Blueprint('erro', __name__)

@erro.app_errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template('404.html'), 404
