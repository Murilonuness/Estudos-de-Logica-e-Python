import mysql.connector
import random
import string
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class User:
    def __init__(self, db_name):
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': db_name
        }
        try:
            self.conn = mysql.connector.connect(**self.db_config)
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")

    def create_user(self, nome, telefone, cidade, sexo, segundo_nome, email, senha):
        print(f"Tentando criar usuário: {nome}, {telefone}, {cidade}, {sexo}, {segundo_nome}, {email}")

        if not self.validar_inputs(nome, telefone, cidade, sexo, segundo_nome, email, senha):
            return

        if self.email_exists(email):
            print("Erro: Este e-mail já está cadastrado.")
            return

        if self.telefone_exists(telefone):
            print("Erro: Este telefone já está cadastrado.")
            return

        senha_hash = generate_password_hash(senha)

        sql = """
        INSERT INTO users (nome, telefone, cidade, sexo, segundoNome, email, senha)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(sql, (nome, telefone, cidade, sexo, segundo_nome, email, senha_hash))
            self.conn.commit()
            print("Usuário cadastrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao inserir usuário: {err}")

    def read_users(self):
        self.cursor.execute("SELECT id, nome, telefone, cidade, sexo, segundoNome, email FROM users")
        return self.cursor.fetchall()

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return self.cursor.fetchone()

    def update_user(self, user_id, nome=None, telefone=None, cidade=None, sexo=None, segundo_nome=None, email=None, senha=None):
        sql = "UPDATE users SET "
        values = []

        if nome:
            sql += "nome = %s, "
            values.append(nome)
        if telefone:
            if self.telefone_exists(telefone):
                print("Erro: Este telefone já está cadastrado para outro usuário.")
                return
            sql += "telefone = %s, "
            values.append(telefone)
        if cidade:
            sql += "cidade = %s, "
            values.append(cidade)
        if sexo:
            sql += "sexo = %s, "
            values.append(sexo)
        if segundo_nome:
            sql += "segundoNome = %s, "
            values.append(segundo_nome)
        if email:
            if self.email_exists(email):
                print("Erro: Este e-mail já está cadastrado para outro usuário.")
                return
            sql += "email = %s, "
            values.append(email)
        if senha:
            senha_hash = generate_password_hash(senha)
            sql += "senha = %s, "
            values.append(senha_hash)

        if values:
            sql = sql.rstrip(", ") + " WHERE id = %s"
            values.append(user_id)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Usuário atualizado com sucesso!")

    def delete_user(self, user_id):
        try:
            self.cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            self.conn.commit()
            print("Usuário deletado!")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar usuário: {err}")

    def email_exists(self, email):
        self.cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        return self.cursor.fetchone() is not None

    def telefone_exists(self, telefone):
        self.cursor.execute("SELECT id FROM users WHERE telefone = %s", (telefone,))
        return self.cursor.fetchone() is not None
    
    def alterar_senha(self, email, nova_senha):
        if not self.email_exists(email):
            print("Erro: E-mail não encontrado.")
            return

        if len(nova_senha) < 6:
            print("Erro: A nova senha deve ter pelo menos 6 caracteres.")
            return

        try:
            senha_hash = generate_password_hash(nova_senha)
            self.cursor.execute("UPDATE users SET senha = %s WHERE email = %s", (senha_hash, email))
            self.conn.commit()
            print("Senha alterada com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao alterar senha: {err}")

    def resetar_senha(self, email):
        usuarios = self.read_users()
        for usuario in usuarios:
            if usuario[6] == email:
                nova_senha = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                senha_hash = generate_password_hash(nova_senha)
                self.cursor.execute("UPDATE users SET senha = %s WHERE email = %s", (senha_hash, email))
                self.conn.commit()
                print(f"Senha resetada com sucesso. Nova senha: {nova_senha}")
                return
        print("Usuário não encontrado.")

    def login(self, email, senha):
        self.cursor.execute("SELECT id, nome, senha FROM users WHERE email = %s", (email,))
        user = self.cursor.fetchone()
        if user:
            user_id, nome, senha_hash = user
            if check_password_hash(senha_hash, senha):
                print(f"Bem-vindo, {nome}!")
                return (user_id, nome)
            else:
                print("Senha incorreta.")
        else:
            print("E-mail não encontrado.")
        return None

    def search_by_name(self, nome):
        self.cursor.execute("SELECT id, nome, telefone, cidade, email FROM users WHERE nome LIKE %s", (f"%{nome}%",))
        return self.cursor.fetchall()

    def validar_inputs(self, nome, telefone, cidade, sexo, segundo_nome, email, senha):
        if not isinstance(nome, str) or len(nome) < 2:
            print("Erro: Nome deve ser um texto com pelo menos 2 caracteres.")
            return False
        if not telefone.isdigit() or len(telefone) < 9:
            print("Erro: Telefone deve conter apenas números e ter pelo menos 9 dígitos.")
            return False
        if not isinstance(cidade, str) or len(cidade) < 2:
            print("Erro: Cidade deve ser um texto válido.")
            return False
        if sexo not in ["M", "F", "Outro"]:
            print("Erro: Sexo deve ser 'M', 'F' ou 'Outro'.")
            return False
        if not isinstance(segundo_nome, str) or len(segundo_nome) < 2:
            print("Erro: Segundo nome deve ser um texto com pelo menos 2 caracteres.")
            return False
        if "@" not in email or "." not in email:
            print("Erro: Email inválido.")
            return False
        if len(senha) < 6:
            print("Erro: A senha deve ter pelo menos 6 caracteres.")
            return False
        return True

    def consultar_compras_do_usuario(self, usuario_id):
        cursor = self.conn.cursor(dictionary=True)
        try:
            query = """
                SELECT 
                    compras.id_compra,
                    estoque.produto AS nome_produto,
                    compras.quantidade,
                    compras.preco_total,
                    compras.data_compra
                FROM compras
                JOIN estoque ON compras.produto_id = estoque.id
                WHERE compras.usuario_id = %s
                ORDER BY compras.data_compra DESC
            """
            cursor.execute(query, (usuario_id,))
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao consultar compras do usuário: {e}")
            return []
        finally:
            cursor.close()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def __del__(self):
        self.close_connection()