from flask import Flask
from routes.roleta import roleta
from routes.historico import historico
from routes.erro import erro
from routes.api import api

app = Flask(__name__)

app.register_blueprint(roleta)
app.register_blueprint(historico)
app.register_blueprint(erro)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)
