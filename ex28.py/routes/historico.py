from flask import Blueprint, render_template
import mysql.connector

historico = Blueprint('historico', __name__)

def salvamento(historico):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='roleta_db',
            user='root',
            password=''
        )
        cursor = connection.cursor()

        data, opcao = historico.split(' - ', 1)

        sql = "INSERT INTO historico (opcao, data) VALUES (%s, %s)"
        valores = (opcao, data)
        cursor.execute(sql, valores)

        connection.commit()
        print("Histórico salvo no banco de dados.")

    except mysql.connector.Error as erro:
        print(f"Erro ao salvar no banco: {erro}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def pegar_dados_do_banco():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='roleta_db',
            user='root',
            password=''
        )
        cursor = connection.cursor()

        sql = "SELECT opcao, data FROM historico ORDER BY data DESC"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        return resultados

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar dados do banco: {erro}")
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@historico.route("/historico")
def mostrar_historico():
    historico_dados = pegar_dados_do_banco()  
    return render_template("historico.html", historico_dados=historico_dados)

